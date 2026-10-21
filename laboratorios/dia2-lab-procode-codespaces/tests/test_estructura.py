"""Pruebas de estructura: todo compila, los starters tienen TODO, las soluciones no, import seguro."""
import asyncio
import importlib.util
import py_compile
import re
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parent.parent
SRC, SOL = RAIZ / "src", RAIZ / "solutions"
STARTERS = ["02_agente_base.py", "03_agente_con_search.py", "04_herramienta_estado.py", "05_trazas.py"]
VARS_AZURE = (
    "FOUNDRY_PROJECT_ENDPOINT", "AZURE_AI_PROJECT_ENDPOINT", "FOUNDRY_MODEL", "AZURE_AI_MODEL_DEPLOYMENT_NAME",
    "FOUNDRY_EMBEDDING_MODEL", "AZURE_SEARCH_ENDPOINT", "AZURE_SEARCH_INDEX_NAME", "LAB_NIVEL_USUARIO",
)


def cargar(ruta: Path):
    """Importa un script con nombre numérico (02_...) sin ejecutarlo."""
    spec = importlib.util.spec_from_file_location("lab_" + ruta.stem.replace("-", "_"), ruta)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


@pytest.fixture
def sin_azure(monkeypatch):
    for nombre in VARS_AZURE:
        monkeypatch.delenv(nombre, raising=False)
    # evita que un .env real del participante contamine la prueba
    monkeypatch.setattr("config.cargar_env", lambda: None)


@pytest.mark.parametrize("ruta", sorted(SRC.glob("*.py")) + sorted(SOL.rglob("*.py")) + sorted((RAIZ / "instructores").glob("*.py")) + sorted((RAIZ / "herramientas").glob("*.py")), ids=lambda p: p.name)
def test_compila_sin_warnings(ruta):
    py_compile.compile(str(ruta), doraise=True, cfile=str(RAIZ / ".pytest_cache" / (ruta.stem + ".pyc")))
    assert not re.search(r"\t", ruta.read_text(encoding="utf-8")), "usa espacios, no tabs"


@pytest.mark.parametrize("nombre", STARTERS)
def test_starter_tiene_todo_y_solucion_no(nombre):
    assert "TODO" in (SRC / nombre).read_text(encoding="utf-8")
    assert (SOL / nombre).exists(), f"falta la solución de {nombre}"
    assert "TODO" not in (SOL / nombre).read_text(encoding="utf-8")


def test_scripts_de_instructores_y_utilitarios_existen():
    for nombre in ("00_verificar_entorno.py", "01_crear_indice.py", "05_caso_fallido.py"):
        assert (SRC / nombre).exists()
    assert (RAIZ / "instructores" / "README.md").exists()


@pytest.mark.parametrize("nombre", STARTERS + ["00_verificar_entorno.py", "01_crear_indice.py", "05_caso_fallido.py"])
def test_importar_un_script_no_toca_azure(nombre, sin_azure):
    pytest.importorskip("agent_framework")
    modulo = cargar(SRC / nombre)  # si hiciera llamadas a Azure al importar, fallaría aquí
    assert hasattr(modulo, "main")


@pytest.mark.parametrize("nombre", ["02_agente_base.py", "03_agente_con_search.py", "05_trazas.py"])
def test_starter_sin_env_termina_con_mensaje_claro(nombre, sin_azure):
    pytest.importorskip("agent_framework")
    modulo = cargar(SRC / nombre)
    args = (False,) if nombre.startswith("03") else ()
    with pytest.raises(SystemExit) as e:
        asyncio.run(modulo.main(*args))
    assert "Faltan variables" in str(e.value)


def test_starter_de_la_tarea_3_exige_completar_la_tool(sin_azure):
    pytest.importorskip("agent_framework")
    modulo = cargar(SRC / "04_herramienta_estado.py")
    with pytest.raises(SystemExit) as e:
        asyncio.run(modulo.main(True))
    assert "TODO" in str(e.value)


def test_solucion_tarea_3_funciona_sin_azure(capsys, sin_azure):
    pytest.importorskip("agent_framework")
    modulo = cargar(SOL / "04_herramienta_estado.py")
    asyncio.run(modulo.main(True))  # --solo-tool: no necesita Azure
    salida = capsys.readouterr().out
    assert "En revisión" in salida and "formato_invalido" in salida


def test_sin_secretos_en_el_kit():
    patrones = [r"InstrumentationKey=[0-9a-fA-F-]{36}", r"sk-[A-Za-z0-9]{20,}", r"Bearer ey[A-Za-z0-9._-]{20,}",
                r"AccountKey=[A-Za-z0-9+/=]{20,}", r"(?i)api[_-]?key\s*[:=]\s*['\"][A-Za-z0-9]{16,}"]
    for ruta in RAIZ.rglob("*"):
        if ruta.is_file() and ruta.suffix in {".py", ".md", ".txt", ".json", ".jsonl", ".example", ".ini"} \
                and ".pytest_cache" not in ruta.parts:
            texto = ruta.read_text(encoding="utf-8", errors="ignore")
            for patron in patrones:
                assert not re.search(patron, texto), f"posible secreto en {ruta.name}"


def test_requirements_y_env_example_coherentes():
    reqs = (RAIZ / "requirements.txt").read_text(encoding="utf-8")
    for paquete in ("agent-framework-foundry", "azure-search-documents", "azure-identity", "azure-monitor-opentelemetry"):
        assert paquete in reqs
    env = (RAIZ / ".env.example").read_text(encoding="utf-8")
    for variable in ("FOUNDRY_PROJECT_ENDPOINT", "FOUNDRY_MODEL", "AZURE_SEARCH_ENDPOINT", "AZURE_SEARCH_INDEX_NAME",
                     "FOUNDRY_EMBEDDING_MODEL", "LAB_NIVEL_USUARIO"):
        assert variable in env
    assert "KEY=" not in env.upper().replace("INSTRUMENTATIONKEY", "")


def test_extension_de_evaluacion_es_import_seguro(sin_azure):
    pytest.importorskip("agent_framework")
    modulo = cargar(SOL / "extensiones" / "ext_evaluar.py")
    assert hasattr(modulo, "main")
    with pytest.raises(SystemExit) as e:
        asyncio.run(modulo.main())
    assert "Faltan variables" in str(e.value)
