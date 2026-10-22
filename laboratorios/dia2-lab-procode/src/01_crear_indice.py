"""[INSTRUCTORES] Crea el índice de Azure AI Search y carga la normativa de data\\normativa.

Se ejecuta ANTES de la sesión (los participantes solo consultan el índice). También sirve como
variante para participantes con permisos: usa un índice propio con --indice normativa-<tuinicial>.

    python src\\01_crear_indice.py --dry-run                 # solo valida el corpus (sin Azure)
    python src\\01_crear_indice.py                           # índice híbrido (texto + vectores + semántico)
    python src\\01_crear_indice.py --sin-vectores            # si no hay deployment de embeddings
    python src\\01_crear_indice.py --recrear                 # borra y vuelve a crear (cambio de dimensiones)

Roles (Microsoft Entra ID): Search Service Contributor + Search Index Data Contributor en el servicio de
Search; Foundry User en el proyecto (embeddings). Requiere el ranker semántico habilitado en el servicio.
Las consultas vectorizadas por Search requieren además su identidad administrada con el rol
Cognitive Services OpenAI User sobre el recurso de embeddings.
"""
from __future__ import annotations

import argparse
import asyncio
from collections import Counter

import busqueda
from config import cargar_settings, exigir
from normativa import cargar_corpus, texto_para_embedding

LOTE = 16


def resumen(corpus: list[dict]) -> None:
    docs = {f["doc_id"] for f in corpus}
    por_nivel = Counter(f["nivel_acceso"] for f in corpus)
    print(f"Corpus: {len(docs)} documentos, {len(corpus)} fragmentos; por nivel: {dict(por_nivel)}")


async def crear(args) -> None:
    settings = cargar_settings()
    nombre = args.indice or settings.search_index
    requeridos = ["search_endpoint"] + ([] if args.sin_vectores else ["project_endpoint", "embedding_model"])
    exigir(settings, *requeridos)
    vectorizador = None if args.sin_vectores else busqueda.vectorizador_desde_settings(settings)
    corpus = cargar_corpus()
    resumen(corpus)

    from azure.search.documents.aio import SearchClient
    from azure.search.documents.indexes.aio import SearchIndexClient

    async with busqueda.credencial() as cred:
        vectores: list[list[float]] = []
        if not args.sin_vectores:
            print(f"Generando embeddings con '{settings.embedding_model}' ({len(corpus)} fragmentos)...")
            textos = [texto_para_embedding(f) for f in corpus]
            for i in range(0, len(textos), LOTE):
                vectores += await busqueda.generar_embeddings(textos[i : i + LOTE], settings, cred)
        dimensiones = len(vectores[0]) if vectores else None

        async with SearchIndexClient(settings.search_endpoint, cred) as indices:
            if args.recrear:
                try:
                    await indices.delete_index(nombre)
                    print(f"Índice '{nombre}' eliminado.")
                except Exception:  # noqa: BLE001 - si no existía, seguimos
                    pass
            await indices.create_or_update_index(busqueda.construir_indice(nombre, dimensiones, vectorizador))
            print(
                f"Índice '{nombre}' listo (vectores: {dimensiones or 'no'}; "
                f"vectorizador: {vectorizador[1] if vectorizador else 'no'}; semántico: {busqueda.NOMBRE_SEMANTICA})."
            )

        documentos = [
            {**f, **({busqueda.CAMPO_VECTOR: vectores[i]} if vectores else {})} for i, f in enumerate(corpus)
        ]
        async with SearchClient(settings.search_endpoint, nombre, cred) as cliente:
            resultado = await cliente.upload_documents(documentos)
            ok = sum(1 for r in resultado if r.succeeded)
            print(f"Cargados {ok}/{len(documentos)} fragmentos.")
            if ok != len(documentos):
                raise SystemExit("Hubo fragmentos que fallaron: revisa permisos (Search Index Data Contributor).")
    print("Listo. Espera ~1 minuto y verifica con: python src\\00_verificar_entorno.py")


def main() -> None:
    ap = argparse.ArgumentParser(description="Crea y carga el índice de normativa de Austral Bank.")
    ap.add_argument("--indice", help="nombre del índice (por defecto AZURE_SEARCH_INDEX_NAME)")
    ap.add_argument("--sin-vectores", action="store_true", help="índice solo texto + semántico")
    ap.add_argument("--recrear", action="store_true", help="elimina el índice antes de crearlo")
    ap.add_argument("--dry-run", action="store_true", help="solo valida el corpus, sin llamar a Azure")
    args = ap.parse_args()
    if args.dry_run:
        resumen(cargar_corpus())
        return
    asyncio.run(crear(args))


if __name__ == "__main__":
    main()
