r"""Verifica tu entorno antes de empezar: Python, paquetes, variables, credencial y endpoints.

Uso:
    python src\00_verificar_entorno.py              # revisa todo (incluye llamadas de solo lectura)
    python src\00_verificar_entorno.py --sin-red    # solo revisión local (sin autenticarte)
    python src\00_verificar_entorno.py --probar-modelo   # además envía 1 mensaje corto al modelo

Nunca imprime tokens, llaves ni connection strings: solo hosts, nombres y "ok / error".
"""
from __future__ import annotations

import argparse
import asyncio
import sys
from importlib import metadata

from config import cargar_settings, diagnosticar

PAQUETES = [
    "agent-framework-foundry",
    "azure-search-documents",
    "azure-identity",
    "azure-monitor-opentelemetry",
    "python-dotenv",
]
MARCA = {"ok": "✔", "error": "✘", "aviso": "!"}
fallos = 0


def mostrar(estado: str, nombre: str, detalle: str = "") -> None:
    global fallos
    fallos += estado == "error"
    print(f" {MARCA[estado]} {nombre:<34} {detalle}")


def revisar_local(settings) -> None:
    print("\n[1] Python y paquetes")
    v = sys.version_info
    mostrar("ok" if v >= (3, 10) else "error", "Python", f"{v.major}.{v.minor}.{v.micro} (se requiere 3.10+; recomendado 3.11+)")
    for paquete in PAQUETES:
        try:
            mostrar("ok", paquete, metadata.version(paquete))
        except metadata.PackageNotFoundError:
            mostrar("error", paquete, "no instalado -> pip install -r requirements.txt")
    print("\n[2] Variables de entorno (.env)")
    for nombre, estado, detalle in diagnosticar(settings):
        mostrar(estado, nombre, detalle)


async def revisar_conexion(settings, probar_modelo: bool) -> None:
    from azure.identity.aio import DefaultAzureCredential

    print("\n[3] Credencial de Microsoft Entra ID (DefaultAzureCredential)")
    async with DefaultAzureCredential() as cred:
        for etiqueta, scope in (("Foundry (ai.azure.com)", "https://ai.azure.com/.default"),
                                ("Azure AI Search", "https://search.azure.com/.default")):
            try:
                await cred.get_token(scope)  # el token no se imprime
                mostrar("ok", f"Token {etiqueta}", "obtenido")
            except Exception as e:  # noqa: BLE001 - queremos un mensaje corto, no un stack trace
                mostrar("error", f"Token {etiqueta}", f"{type(e).__name__}: ejecuta `az login`")
                return

        print("\n[4] Índice de Azure AI Search (lectura)")
        try:
            from azure.search.documents.aio import SearchClient

            async with SearchClient(settings.search_endpoint, settings.search_index, cred) as sc:
                n = await sc.get_document_count()
            mostrar("ok" if n else "aviso", f"Índice {settings.search_index}", f"{n} fragmentos")
        except Exception as e:  # noqa: BLE001
            mostrar("error", f"Índice {settings.search_index}", f"{type(e).__name__}: ¿existe? ¿tienes 'Search Index Data Reader'?")

        if probar_modelo:
            print("\n[5] Modelo de chat (1 mensaje corto)")
            try:
                from agent_framework import Agent
                from agent_framework.foundry import FoundryChatClient

                client = FoundryChatClient(
                    project_endpoint=settings.project_endpoint, model=settings.model, credential=cred
                )
                r = await Agent(client=client, instructions="Responde solo con la palabra OK.").run("Hola")
                mostrar("ok", f"Deployment {settings.model}", f"respondió: {r.text.strip()[:20]}")
            except Exception as e:  # noqa: BLE001
                mostrar("error", f"Deployment {settings.model}", f"{type(e).__name__}: revisa el nombre del deployment y el rol 'Foundry User'")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sin-red", action="store_true", help="no hace llamadas a Azure")
    ap.add_argument("--probar-modelo", action="store_true", help="envía un mensaje corto al modelo")
    args = ap.parse_args()

    try:
        settings = cargar_settings()
    except ValueError as e:
        print(f" ✘ {e}")
        return 1
    revisar_local(settings)
    if not args.sin_red and fallos == 0:
        asyncio.run(revisar_conexion(settings, args.probar_modelo))
    elif fallos:
        print("\nCorrige los errores anteriores y vuelve a ejecutar (se omiten las pruebas de red).")
    print("\n" + ("Entorno listo ✔" if fallos == 0 else f"{fallos} problema(s) por resolver ✘"))
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
