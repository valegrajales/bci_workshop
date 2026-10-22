"""Pruebas de las herramientas del agente con una búsqueda falsa (sin Azure)."""
import asyncio
import json
from pathlib import Path

import pytest

pytest.importorskip("agent_framework")

import agente_lab as al  # noqa: E402
import busqueda  # noqa: E402
import normativa as n  # noqa: E402
import registro_herramientas as reg  # noqa: E402


@pytest.fixture(autouse=True)
def entorno(monkeypatch):
    monkeypatch.setattr("config.cargar_env", lambda: None)
    monkeypatch.setenv("LAB_NIVEL_USUARIO", "interno")
    reg.limpiar()
    yield
    reg.limpiar()


def test_nombres_y_descripciones_de_las_herramientas():
    assert al.buscar_normativa.name == "buscar_normativa"
    assert al.consultar_estado_solicitud.name == "consultar_estado_solicitud"
    assert "NUNCA" not in al.consultar_estado_solicitud.description
    assert "UNA solicitud" in al.consultar_estado_solicitud.description
    esquema = json.dumps(al.consultar_estado_solicitud.parameters(), ensure_ascii=False)
    assert "SOL-AAAA-NNNN" in esquema
    assert set(al.consultar_estado_solicitud.parameters()["properties"]) == {"id_solicitud"}
    # el nivel de acceso nunca es un parámetro controlado por el modelo
    assert set(al.buscar_normativa.parameters()["properties"]) == {"consulta"}


def test_las_instrucciones_nombran_ambas_herramientas_y_la_cita():
    assert "buscar_normativa" in al.INSTRUCCIONES and "consultar_estado_solicitud" in al.INSTRUCCIONES
    assert "[NOR-001-02]" in al.INSTRUCCIONES


def test_buscar_normativa_aplica_filtro_del_nivel_y_formatea(monkeypatch):
    corpus = n.cargar_corpus()
    recibido = {}

    async def falsa(consulta, filtro, top=4, settings=None):
        recibido.update(consulta=consulta, filtro=filtro)
        return [f for f in corpus if f["doc_id"] == "NOR-001"][:2]

    monkeypatch.setattr(busqueda, "buscar", falsa)
    texto = asyncio.run(al.buscar_normativa.invoke(consulta="límite tarjeta"))[0].text
    assert recibido["filtro"] == "search.in(nivel_acceso, 'publico,interno', ',')"
    assert "[NOR-001-01]" in texto
    assert reg.usadas() == ["buscar_normativa"]


def test_buscar_normativa_sin_resultados(monkeypatch):
    async def vacia(consulta, filtro, top=4, settings=None):
        return []

    monkeypatch.setattr(busqueda, "buscar", vacia)
    assert asyncio.run(al.buscar_normativa.invoke(consulta="x"))[0].text.startswith("SIN_RESULTADOS")


def test_consultar_estado_solicitud_devuelve_json_legible():
    texto = asyncio.run(al.consultar_estado_solicitud.invoke(id_solicitud="SOL-2026-0003"))[0].text
    assert "Área Legal" in texto  # sin escapes \u00c1 en la traza
    datos = json.loads(texto)
    assert datos["estado"] == "En revisión"
    assert reg.LLAMADAS[-1].ok is True


def test_consultar_estado_solicitud_id_invalido_marca_error():
    texto = asyncio.run(al.consultar_estado_solicitud.invoke(id_solicitud="3"))[0].text
    assert json.loads(texto)["error"] == "formato_invalido"
    assert reg.LLAMADAS[-1].ok is False


def test_casos_de_referencia_son_coherentes_con_el_corpus_y_la_tool():
    textos = " ".join(f["contenido"].lower() for f in n.cargar_corpus())
    assert [c["id"] for c in al.CASOS] == ["C1", "C2", "C3"]
    assert {c["tool"] for c in al.CASOS} == {"buscar_normativa", "consultar_estado_solicitud"}
    assert "2.500" in textos and "350" in textos


def test_caso_fallido_1_usa_el_nivel_equivocado_y_caso_2_describe_mal_la_tool(monkeypatch):
    import importlib.util

    ruta = Path(__file__).resolve().parent.parent / "src" / "05_caso_fallido.py"
    spec = importlib.util.spec_from_file_location("caso_fallido", ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    capturado = {}

    async def falsa(consulta, filtro, top=4, settings=None):
        capturado["filtro"] = filtro
        return []

    monkeypatch.setattr(busqueda, "buscar", falsa)
    asyncio.run(mod._buscar_v2.invoke(consulta="límite tarjeta"))
    assert capturado["filtro"] == "search.in(nivel_acceso, 'publico', ',')"  # el bug del caso 1

    assert mod._buscar_v2.name == "buscar_normativa" and mod._estado_v2.name == "consultar_estado_solicitud"
    assert "solo los dígitos" in json.dumps(mod._estado_v2.parameters(), ensure_ascii=False)  # el bug del caso 2
    texto = asyncio.run(mod._estado_v2.invoke(id_solicitud="3"))[0].text
    assert json.loads(texto)["error"] == "formato_invalido"
    assert mod.HERRAMIENTAS[1][1]["id"] == "C1" and mod.HERRAMIENTAS[2][1]["id"] == "C2"


def test_definicion_del_indice():
    pytest.importorskip("azure.search.documents")
    d = busqueda.construir_indice("prueba", 1536).as_dict()
    campos = {f["name"]: f for f in d["fields"]}
    assert set(campos) == {"id", "doc_id", "titulo", "seccion", "contenido", "area", "nivel_acceso", "vector"}
    assert campos["id"]["key"] is True and campos["nivel_acceso"]["filterable"] is True
    assert campos["contenido"]["analyzer"] == "es.microsoft"
    assert campos["vector"]["dimensions"] == 1536 and campos["vector"]["vectorSearchProfile"] == busqueda.PERFIL_VECTOR
    assert campos["vector"]["retrievable"] is False
    assert "vectorizer" not in d["vectorSearch"]["profiles"][0]
    assert d["semantic"]["configurations"][0]["name"] == busqueda.NOMBRE_SEMANTICA
    sin_vectores = busqueda.construir_indice("prueba", None).as_dict()
    assert "vector" not in {f["name"] for f in sin_vectores["fields"]} and "vectorSearch" not in sin_vectores


def test_indice_con_vectorizador_para_retrieval_agentico():
    pytest.importorskip("azure.search.documents")
    d = busqueda.construir_indice(
        "prueba", 3072, ("https://recurso.openai.azure.com", "text-embedding-3-large")
    ).as_dict()
    vec = d["vectorSearch"]["vectorizers"][0]
    assert vec["name"] == busqueda.VECTORIZADOR and vec["kind"] == "azureOpenAI"
    assert vec["azureOpenAIParameters"]["resourceUri"] == "https://recurso.openai.azure.com"
    assert vec["azureOpenAIParameters"]["deploymentId"] == "text-embedding-3-large"
    assert vec["azureOpenAIParameters"]["modelName"] == "text-embedding-3-large"
    assert d["vectorSearch"]["profiles"][0]["vectorizer"] == busqueda.VECTORIZADOR


def test_vectorizador_desde_settings():
    from config import Settings

    from dataclasses import replace

    s = Settings(
        project_endpoint="https://bci-demo.services.ai.azure.com/api/projects/p",
        model="", embedding_model="text-embedding-3-large",
        search_endpoint="", search_index="", nivel_usuario="interno",
    )
    assert busqueda.vectorizador_desde_settings(s) == (
        "https://bci-demo.openai.azure.com", "text-embedding-3-large", "text-embedding-3-large"
    )
    alias = replace(s, embedding_model="emb", embedding_model_name="text-embedding-3-large")
    vectorizador = busqueda.vectorizador_desde_settings(alias)
    assert vectorizador == ("https://bci-demo.openai.azure.com", "emb", "text-embedding-3-large")
    parametros = busqueda.construir_indice("prueba", 3072, vectorizador).as_dict()[
        "vectorSearch"
    ]["vectorizers"][0]["azureOpenAIParameters"]
    assert parametros["deploymentId"] == "emb" and parametros["modelName"] == "text-embedding-3-large"
    with pytest.raises(ValueError, match="FOUNDRY_EMBEDDING_MODEL_NAME"):
        busqueda.vectorizador_desde_settings(replace(s, embedding_model="emb"))
    with pytest.raises(ValueError, match="modelo"):
        busqueda.construir_indice("prueba", 3072, ("https://recurso.openai.azure.com", "emb"))
    assert busqueda.vectorizador_desde_settings(replace(s, embedding_model="")) is None


@pytest.mark.parametrize("sin_vectores", [True, False])
def test_creacion_del_indice_sin_azure(monkeypatch, sin_vectores):
    import importlib.util
    from types import SimpleNamespace

    from config import Settings

    ruta = Path(__file__).resolve().parent.parent / "src" / "01_crear_indice.py"
    spec = importlib.util.spec_from_file_location("crear_indice", ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    settings = Settings(
        project_endpoint="" if sin_vectores else "https://recurso.services.ai.azure.com/api/projects/p",
        model="", embedding_model="alias", embedding_model_name="" if sin_vectores else "text-embedding-3-large",
        search_endpoint="https://prueba.search.windows.net", search_index="prueba", nivel_usuario="interno",
    )
    recibido = {}

    class Contexto:
        async def __aenter__(self):
            return self

        async def __aexit__(self, *args):
            pass

    class ClienteFalso(Contexto):
        def __init__(self, *args):
            pass

        async def create_or_update_index(self, indice):
            recibido["indice"] = indice.as_dict()

        async def upload_documents(self, documentos):
            recibido["documentos"] = documentos
            return [SimpleNamespace(succeeded=True) for _ in documentos]

    async def embeddings(textos, *args):
        assert not sin_vectores, "--sin-vectores no debe invocar embeddings"
        return [[0.1, 0.2] for _ in textos]

    monkeypatch.setattr(mod, "cargar_settings", lambda: settings)
    monkeypatch.setattr(busqueda, "credencial", Contexto)
    monkeypatch.setattr(busqueda, "generar_embeddings", embeddings)
    monkeypatch.setattr("azure.search.documents.indexes.aio.SearchIndexClient", ClienteFalso)
    monkeypatch.setattr("azure.search.documents.aio.SearchClient", ClienteFalso)
    asyncio.run(mod.crear(SimpleNamespace(indice=None, sin_vectores=sin_vectores, recrear=False)))
    indice = recibido["indice"]
    assert ("vectorSearch" in indice) is (not sin_vectores)
    assert all(("vector" in d) is (not sin_vectores) for d in recibido["documentos"])
    if not sin_vectores:
        parametros = indice["vectorSearch"]["vectorizers"][0]["azureOpenAIParameters"]
        assert parametros["deploymentId"] == "alias" and parametros["modelName"] == "text-embedding-3-large"


def test_todos_los_campos_del_fragmento_existen_en_el_indice():
    pytest.importorskip("azure.search.documents")
    campos = {f["name"] for f in busqueda.construir_indice("p", 8).as_dict()["fields"]} - {"vector"}
    assert set(n.cargar_corpus()[0]) == campos
    assert set(busqueda.CAMPOS_RESULTADO) <= campos


def test_parametros_de_consulta_hibrida_y_plan_b_sin_semantico(monkeypatch):
    monkeypatch.delenv("LAB_SIN_SEMANTICO", raising=False)
    p = busqueda.parametros_consulta("límite", "search.in(nivel_acceso, 'publico,interno', ',')", top=4)
    assert p["query_type"] == "semantic" and p["semantic_configuration_name"] == busqueda.NOMBRE_SEMANTICA
    assert "vector_queries" not in p and p["top"] == 4
    p = busqueda.parametros_consulta("límite", "f", top=4, vector=[0.1, 0.2])
    assert p["vector_queries"][0].k_nearest_neighbors == 12
    monkeypatch.setenv("LAB_SIN_SEMANTICO", "true")
    p = busqueda.parametros_consulta("límite", "f")
    assert "query_type" not in p and "semantic_configuration_name" not in p


def test_trazas_configuracion_con_entra_pasa_credencial(monkeypatch):
    """Con LAB_APPINSIGHTS_ENTRA=true el exportador recibe una credencial (App Insights sin llaves)."""
    import asyncio

    import trazas

    recibido = {}

    class ClienteFalso:
        async def configure_azure_monitor(self, enable_sensitive_data=False, **kwargs):
            recibido.update(kwargs)

    monkeypatch.delenv("ENABLE_CONSOLE_EXPORTERS", raising=False)
    monkeypatch.delenv("APPLICATIONINSIGHTS_CONNECTION_STRING", raising=False)
    monkeypatch.setenv("LAB_APPINSIGHTS_ENTRA", "true")
    assert asyncio.run(trazas.configurar_trazas(ClienteFalso())) == "app-insights"
    assert "credential" in recibido
    recibido.clear()
    monkeypatch.delenv("LAB_APPINSIGHTS_ENTRA")
    asyncio.run(trazas.configurar_trazas(ClienteFalso()))
    assert recibido == {}
