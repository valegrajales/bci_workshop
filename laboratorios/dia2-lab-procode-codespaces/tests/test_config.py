"""Pruebas de la configuración (sin Azure, sin leer tu .env real)."""
import pytest

import config as c


def _limpiar(monkeypatch):
    for nombre in (
        "FOUNDRY_PROJECT_ENDPOINT", "AZURE_AI_PROJECT_ENDPOINT", "FOUNDRY_MODEL",
        "AZURE_AI_MODEL_DEPLOYMENT_NAME", "FOUNDRY_EMBEDDING_MODEL", "AZURE_SEARCH_ENDPOINT",
        "AZURE_SEARCH_INDEX_NAME", "LAB_NIVEL_USUARIO",
    ):
        monkeypatch.delenv(nombre, raising=False)


def test_valores_por_defecto(monkeypatch):
    _limpiar(monkeypatch)
    s = c.cargar_settings(recargar_env=False)
    assert s.nivel_usuario == "interno" and s.search_index == "normativa-austral"
    assert s.usa_vectores is False


def test_alias_del_workshop_y_placeholders(monkeypatch):
    _limpiar(monkeypatch)
    monkeypatch.setenv("AZURE_AI_PROJECT_ENDPOINT", "https://x.services.ai.azure.com/api/projects/p")
    monkeypatch.setenv("FOUNDRY_MODEL", "<tu-deployment>")  # placeholder de .env.example: se ignora
    monkeypatch.setenv("AZURE_AI_MODEL_DEPLOYMENT_NAME", "gpt-4o")
    s = c.cargar_settings(recargar_env=False)
    assert s.project_endpoint.endswith("/projects/p") and s.model == "gpt-4o"


def test_nivel_invalido_falla(monkeypatch):
    _limpiar(monkeypatch)
    monkeypatch.setenv("LAB_NIVEL_USUARIO", "superadmin")
    with pytest.raises(ValueError):
        c.cargar_settings(recargar_env=False)


def test_exigir_lista_lo_que_falta(monkeypatch):
    _limpiar(monkeypatch)
    s = c.cargar_settings(recargar_env=False)
    with pytest.raises(SystemExit) as e:
        c.exigir(s, "project_endpoint", "model")
    assert "project_endpoint" in str(e.value) and "model" in str(e.value)


def test_enmascarar_no_filtra_el_valor():
    assert c.enmascarar("InstrumentationKey=abcdef") == "Inst…"
    assert c.enmascarar("") == "(vacío)"
