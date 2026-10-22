"""Configuración del laboratorio: variables de entorno y .env.

Este módulo NO importa SDKs de Azure, así que se puede importar y probar en local.
Autenticación: sin llaves. Los SDKs usan DefaultAzureCredential (az login en tu máquina).
"""
from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from pathlib import Path

# La consola de Windows puede usar cp1252: forzamos UTF-8 para poder imprimir tildes y ✔/✘
for _flujo in (sys.stdout, sys.stderr):
    try:
        _flujo.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

RAIZ = Path(__file__).resolve().parent.parent
DATA_DIR = RAIZ / "data"

# Niveles de acceso de menor a mayor privilegio (ver data/normativa/*.md)
NIVELES = ("publico", "interno", "restringido")

# Nombre canónico -> alias aceptados (el workshop travel_assistant usa los AZURE_AI_*)
ALIAS = {
    "FOUNDRY_PROJECT_ENDPOINT": ("AZURE_AI_PROJECT_ENDPOINT",),
    "FOUNDRY_MODEL": ("AZURE_AI_MODEL_DEPLOYMENT_NAME",),
}


def cargar_env() -> None:
    """Carga el archivo .env de la raíz del lab (Agent Framework no lo hace solo)."""
    try:
        from dotenv import load_dotenv
    except ImportError:  # python-dotenv es opcional si ya exportaste las variables
        return
    load_dotenv(RAIZ / ".env", override=True)


def obtener(nombre: str, por_defecto: str = "") -> str:
    """Devuelve la variable `nombre` (o uno de sus alias) sin espacios; '' si no existe."""
    for clave in (nombre, *ALIAS.get(nombre, ())):
        valor = os.environ.get(clave, "").strip()
        # Ignora los placeholders de .env.example (<tu-...>, ..., vacío)
        if valor and not valor.startswith("<") and valor != "...":
            return valor
    return por_defecto


@dataclass(frozen=True)
class Settings:
    project_endpoint: str
    model: str
    embedding_model: str
    search_endpoint: str
    search_index: str
    nivel_usuario: str
    embedding_model_name: str = ""

    @property
    def usa_vectores(self) -> bool:
        """Búsqueda híbrida solo si hay deployment de embeddings configurado."""
        return bool(self.embedding_model)


def cargar_settings(recargar_env: bool = True) -> Settings:
    if recargar_env:
        cargar_env()
    nivel = obtener("LAB_NIVEL_USUARIO", "interno").lower()
    if nivel not in NIVELES:
        raise ValueError(f"LAB_NIVEL_USUARIO debe ser uno de {NIVELES}, no '{nivel}'")
    return Settings(
        project_endpoint=obtener("FOUNDRY_PROJECT_ENDPOINT"),
        model=obtener("FOUNDRY_MODEL"),
        embedding_model=obtener("FOUNDRY_EMBEDDING_MODEL"),
        search_endpoint=obtener("AZURE_SEARCH_ENDPOINT"),
        search_index=obtener("AZURE_SEARCH_INDEX_NAME", "normativa-austral"),
        nivel_usuario=nivel,
        embedding_model_name=obtener("FOUNDRY_EMBEDDING_MODEL_NAME"),
    )


def faltantes(settings: Settings, requeridos: tuple[str, ...]) -> list[str]:
    """Nombres de campos requeridos que están vacíos."""
    return [campo for campo in requeridos if not getattr(settings, campo)]


def exigir(settings: Settings, *requeridos: str) -> Settings:
    """Termina el script con un mensaje claro si falta configuración."""
    vacios = faltantes(settings, requeridos)
    if vacios:
        raise SystemExit(
            "Faltan variables en tu .env: "
            + ", ".join(vacios)
            + ". Revisa .env.example y ejecuta: python src\\00_verificar_entorno.py"
        )
    return settings


def enmascarar(valor: str, visibles: int = 4) -> str:
    """Oculta casi todo el valor (para mostrar connection strings sin filtrarlos)."""
    if not valor:
        return "(vacío)"
    return valor[:visibles] + "…" if len(valor) > visibles else "…"


def completar_todos(**valores) -> None:
    """Detiene el script (sin traza de error) si aún quedan placeholders `None` de los TODO."""
    pendientes = [nombre for nombre, valor in valores.items() if valor is None]
    if pendientes:
        raise SystemExit("Aún quedan TODO por completar en este archivo: " + ", ".join(pendientes))


def diagnosticar(settings: Settings) -> list[tuple[str, str, str]]:
    """Revisión local de formato (sin red). Devuelve [(variable, 'ok'|'error'|'aviso', detalle)]."""
    filas: list[tuple[str, str, str]] = []

    def agregar(nombre, ok, detalle_ok, detalle_error, nivel_error="error"):
        filas.append((nombre, "ok" if ok else nivel_error, detalle_ok if ok else detalle_error))

    pe = settings.project_endpoint
    agregar("FOUNDRY_PROJECT_ENDPOINT", pe.startswith("https://") and "/api/projects/" in pe,
            host_de(pe), "debe verse como https://<recurso>.services.ai.azure.com/api/projects/<proyecto>")
    agregar("FOUNDRY_MODEL", bool(settings.model), settings.model,
            "falta el nombre del deployment de chat")
    se = settings.search_endpoint
    agregar("AZURE_SEARCH_ENDPOINT", se.startswith("https://") and ".search.windows.net" in se,
            host_de(se), "debe verse como https://<servicio>.search.windows.net")
    agregar("AZURE_SEARCH_INDEX_NAME", bool(settings.search_index), settings.search_index, "falta el nombre del índice")
    agregar("FOUNDRY_EMBEDDING_MODEL", settings.usa_vectores, settings.embedding_model,
            "vacío: se usará búsqueda solo texto + semántica (válido si el índice no tiene vectores)",
            nivel_error="aviso")
    agregar("LAB_NIVEL_USUARIO", settings.nivel_usuario in NIVELES, settings.nivel_usuario, "nivel no válido")
    return filas


def host_de(url: str) -> str:
    """Solo el host de una URL (nunca rutas con identificadores ni parámetros)."""
    resto = url.split("://", 1)[-1]
    return resto.split("/", 1)[0] or "(vacío)"
