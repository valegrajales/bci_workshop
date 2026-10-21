"""Azure AI Search: definición del índice, embeddings y búsqueda híbrida.

Es la ÚNICA capa que toca Azure para la recuperación. Los imports de Azure están dentro de las
funciones, así que `import busqueda` funciona sin credenciales (y sin los SDKs instalados).
Autenticación: Microsoft Entra ID (DefaultAzureCredential), sin llaves.

Patrones tomados de (ver README > Fuentes):
- repos/publico-samples/azure-search-python-samples/Quickstart-Vector-Search (índice + consulta vectorial)
- repos/publico-samples/agent-framework/python/samples/02-agents/embeddings (FoundryEmbeddingClient)
"""
from __future__ import annotations

import os

from config import Settings, cargar_settings

NOMBRE_SEMANTICA = "normativa-semantica"
CAMPO_VECTOR = "vector"
PERFIL_VECTOR = "perfil-hnsw"
ALGORITMO_VECTOR = "algoritmo-hnsw"
CAMPOS_RESULTADO = ["id", "doc_id", "titulo", "seccion", "area", "nivel_acceso", "contenido"]


# ---------------------------------------------------------------- índice (script de instructores)
def construir_indice(nombre: str, dimensiones: int | None = None):
    """Esquema: texto (analizador español) + campo vectorial opcional + configuración semántica."""
    from azure.search.documents.indexes.models import (
        HnswAlgorithmConfiguration,
        SearchableField,
        SearchField,
        SearchFieldDataType,
        SearchIndex,
        SemanticConfiguration,
        SemanticField,
        SemanticPrioritizedFields,
        SemanticSearch,
        SimpleField,
        VectorSearch,
        VectorSearchProfile,
    )

    campos = [
        SimpleField(name="id", type=SearchFieldDataType.String, key=True, filterable=True),
        SimpleField(name="doc_id", type=SearchFieldDataType.String, filterable=True, facetable=True),
        SearchableField(name="titulo", analyzer_name="es.microsoft"),
        SearchableField(name="seccion", analyzer_name="es.microsoft"),
        SearchableField(name="contenido", analyzer_name="es.microsoft"),
        SearchableField(name="area", filterable=True, facetable=True, analyzer_name="es.microsoft"),
        # nivel_acceso es la base del security trimming: filtrable, nunca visible para el modelo
        SimpleField(name="nivel_acceso", type=SearchFieldDataType.String, filterable=True, facetable=True),
    ]
    vector_search = None
    if dimensiones:
        campos.append(
            SearchField(
                name=CAMPO_VECTOR,
                type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
                searchable=True,
                vector_search_dimensions=dimensiones,
                vector_search_profile_name=PERFIL_VECTOR,
            )
        )
        vector_search = VectorSearch(
            algorithms=[HnswAlgorithmConfiguration(name=ALGORITMO_VECTOR)],
            profiles=[VectorSearchProfile(name=PERFIL_VECTOR, algorithm_configuration_name=ALGORITMO_VECTOR)],
        )
    semantica = SemanticSearch(
        default_configuration_name=NOMBRE_SEMANTICA,
        configurations=[
            SemanticConfiguration(
                name=NOMBRE_SEMANTICA,
                prioritized_fields=SemanticPrioritizedFields(
                    title_field=SemanticField(field_name="titulo"),
                    content_fields=[SemanticField(field_name="contenido")],
                    keywords_fields=[SemanticField(field_name="area")],
                ),
            )
        ],
    )
    return SearchIndex(name=nombre, fields=campos, vector_search=vector_search, semantic_search=semantica)


def credencial():
    """Credencial asíncrona de Entra ID: usa tu `az login` en local."""
    from azure.identity.aio import DefaultAzureCredential

    return DefaultAzureCredential()


async def generar_embeddings(textos: list[str], settings: Settings, cred) -> list[list[float]]:
    """Vectoriza textos con el deployment de embeddings del proyecto de Foundry."""
    from agent_framework.foundry import FoundryEmbeddingClient

    async with FoundryEmbeddingClient(
        project_endpoint=settings.project_endpoint, model=settings.embedding_model, credential=cred
    ) as cliente:
        resultado = await cliente.get_embeddings(textos)
    return [list(e.vector) for e in resultado]


# ---------------------------------------------------------------- consulta (agente)
class _Estado:
    """Clientes reutilizables (credencial + SearchClient) para todo el proceso."""

    def __init__(self, settings: Settings):
        from azure.search.documents.aio import SearchClient

        self.settings = settings
        self.cred = credencial()
        self.search = SearchClient(settings.search_endpoint, settings.search_index, self.cred)


_estado: _Estado | None = None


async def _obtener_estado(settings: Settings | None) -> _Estado:
    global _estado
    if _estado is None:
        _estado = _Estado(settings or cargar_settings())
    return _estado


async def cerrar() -> None:
    """Cierra clientes. Llámalo al terminar el script (bloque finally)."""
    global _estado
    if _estado is not None:
        await _estado.search.close()
        await _estado.cred.close()
        _estado = None


def parametros_consulta(consulta: str, filtro: str, top: int = 4, vector: list[float] | None = None) -> dict:
    """Argumentos de SearchClient.search: texto + (vector opcional) + reranking semántico + filtro.

    LAB_SIN_SEMANTICO=true desactiva el reranker semántico (plan B si el servicio no lo tiene habilitado).
    """
    parametros: dict = {"search_text": consulta, "filter": filtro, "select": CAMPOS_RESULTADO, "top": top}
    if os.environ.get("LAB_SIN_SEMANTICO", "").strip().lower() != "true":
        parametros["query_type"] = "semantic"
        parametros["semantic_configuration_name"] = NOMBRE_SEMANTICA
    if vector is not None:
        from azure.search.documents.models import VectorizedQuery

        parametros["vector_queries"] = [
            VectorizedQuery(vector=vector, k_nearest_neighbors=top * 3, fields=CAMPO_VECTOR)
        ]
    return parametros


async def buscar(    consulta: str, filtro: str, top: int = 4, settings: Settings | None = None
) -> list[dict]:
    """Búsqueda híbrida (BM25 + vectores) con reranking semántico y filtro OData.

    `filtro` lo construye el código (normativa.construir_filtro_acceso), nunca el modelo.
    Si no hay deployment de embeddings, cae a texto + semántico.
    """
    estado = await _obtener_estado(settings)
    vector = None
    if estado.settings.usa_vectores:
        vector = (await generar_embeddings([consulta], estado.settings, estado.cred))[0]
    resultados = await estado.search.search(**parametros_consulta(consulta, filtro, top, vector))
    return [dict(r) async for r in resultados]
