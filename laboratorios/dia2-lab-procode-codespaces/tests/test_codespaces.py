"""Valida la configuración de Codespaces (Python 3.12) de esta versión del laboratorio."""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
REPO = RAIZ.parent.parent
DEVCONTAINER = REPO / ".devcontainer" / RAIZ.name / "devcontainer.json"


def test_devcontainer_usa_python_312_y_apunta_a_esta_carpeta():
    assert DEVCONTAINER.exists(), "Codespaces solo lee .devcontainer/ en la raíz del repositorio"
    cfg = json.loads(DEVCONTAINER.read_text(encoding="utf-8"))
    assert "3.12" in cfg["image"]
    assert cfg["workspaceFolder"].endswith(f"laboratorios/{RAIZ.name}")
    assert "codespaces-setup.sh" in cfg["postCreateCommand"]


def test_script_de_setup_existe_y_se_fuerza_lf():
    script = RAIZ / "scripts" / "codespaces-setup.sh"
    assert b"requirements-dev.txt" in script.read_bytes()
    atributos = (REPO / ".gitattributes").read_text(encoding="utf-8")
    assert "*.sh text eol=lf" in atributos


def test_requirements_no_fijan_python_menor_a_310():
    for nombre in ("requirements.txt", "requirements-dev.txt"):
        assert "python_version < \"3.10\"" not in (RAIZ / nombre).read_text(encoding="utf-8")
