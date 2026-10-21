"""Corpus de normativa: metadatos, fragmentación (chunking), filtros de acceso y citas.

Todo es lógica local (sin Azure) para poder probarla con pytest.
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

from config import DATA_DIR, NIVELES

CAMPOS_OBLIGATORIOS = ("id", "titulo", "area", "nivel_acceso")
MAX_CARACTERES = 800
# Acepta [NOR-001-02] (fragmento) y también [NOR-001] (documento)
PATRON_CITA = re.compile(r"\[(NOR-\d{3}(?:-\d{2})?)\]")


def _sin_acentos(texto: str) -> str:
    base = unicodedata.normalize("NFD", texto)
    return "".join(c for c in base if unicodedata.category(c) != "Mn")


def normalizar_nivel(valor: str) -> str:
    """'Público' -> 'publico'. Lanza ValueError si no es un nivel válido."""
    nivel = _sin_acentos(valor).strip().lower()
    if nivel not in NIVELES:
        raise ValueError(f"nivel_acceso inválido: '{valor}' (válidos: {NIVELES})")
    return nivel


def parsear_documento(texto: str) -> tuple[dict[str, str], str]:
    """Separa el encabezado de metadatos (--- clave: valor ---) del cuerpo markdown."""
    lineas = texto.lstrip("\ufeff").splitlines()
    if not lineas or lineas[0].strip() != "---":
        raise ValueError("El documento no empieza con un encabezado de metadatos '---'")
    try:
        fin = next(i for i in range(1, len(lineas)) if lineas[i].strip() == "---")
    except StopIteration:
        raise ValueError("El encabezado de metadatos no está cerrado con '---'") from None
    meta: dict[str, str] = {}
    for linea in lineas[1:fin]:
        if ":" in linea:
            clave, _, valor = linea.partition(":")
            meta[clave.strip()] = valor.strip()
    faltan = [c for c in CAMPOS_OBLIGATORIOS if not meta.get(c)]
    if faltan:
        raise ValueError(f"Faltan metadatos obligatorios: {faltan}")
    meta["nivel_acceso"] = normalizar_nivel(meta["nivel_acceso"])
    return meta, "\n".join(lineas[fin + 1 :]).strip()


def dividir_en_secciones(cuerpo: str) -> list[tuple[str, str]]:
    """Divide por encabezados '## ' y devuelve [(sección, texto)]. Ignora el título '# '."""
    secciones: list[tuple[str, list[str]]] = []
    for linea in cuerpo.splitlines():
        if linea.startswith("## "):
            secciones.append((linea[3:].strip(), []))
        elif secciones:
            secciones[-1][1].append(linea)
    return [(t, "\n".join(ls).strip()) for t, ls in secciones if "".join(ls).strip()]


def _partir_largo(texto: str, max_caracteres: int) -> list[str]:
    """Agrupa párrafos hasta max_caracteres; un párrafo nunca se corta a la mitad."""
    partes: list[str] = []
    actual = ""
    for parrafo in re.split(r"\n\s*\n", texto):
        candidato = f"{actual}\n\n{parrafo}".strip() if actual else parrafo.strip()
        if actual and len(candidato) > max_caracteres:
            partes.append(actual)
            actual = parrafo.strip()
        else:
            actual = candidato
    if actual:
        partes.append(actual)
    return partes


def crear_fragmentos(
    meta: dict[str, str], cuerpo: str, max_caracteres: int = MAX_CARACTERES
) -> list[dict]:
    """Un fragmento por sección (o varios si la sección es larga). IDs: NOR-001-01, -02..."""
    fragmentos: list[dict] = []
    for seccion, texto in dividir_en_secciones(cuerpo):
        for parte in _partir_largo(texto, max_caracteres):
            fragmentos.append(
                {
                    "id": f"{meta['id']}-{len(fragmentos) + 1:02d}",
                    "doc_id": meta["id"],
                    "titulo": meta["titulo"],
                    "seccion": seccion,
                    "area": meta["area"],
                    "nivel_acceso": meta["nivel_acceso"],
                    "contenido": parte,
                }
            )
    return fragmentos


def texto_para_embedding(fragmento: dict) -> str:
    """Texto que se vectoriza: título y sección dan contexto al fragmento."""
    return f"{fragmento['titulo']} — {fragmento['seccion']}\n{fragmento['contenido']}"


def cargar_corpus(directorio: Path | None = None) -> list[dict]:
    """Lee todos los .md de data/normativa y devuelve los fragmentos de todos los documentos."""
    directorio = directorio or DATA_DIR / "normativa"
    fragmentos: list[dict] = []
    for ruta in sorted(directorio.glob("*.md")):
        meta, cuerpo = parsear_documento(ruta.read_text(encoding="utf-8"))
        fragmentos.extend(crear_fragmentos(meta, cuerpo))
    ids = [f["id"] for f in fragmentos]
    if len(ids) != len(set(ids)):
        raise ValueError("Hay ids de fragmento duplicados en el corpus")
    return fragmentos


# ---- Seguridad (security trimming simulado con nivel_acceso) ----------------------------------


def niveles_permitidos(nivel_usuario: str) -> tuple[str, ...]:
    """Un usuario 'interno' ve público e interno; 'restringido' ve todo."""
    nivel = normalizar_nivel(nivel_usuario)
    return NIVELES[: NIVELES.index(nivel) + 1]


def construir_filtro_acceso(nivel_usuario: str) -> str:
    """Filtro OData para Azure AI Search. El nivel sale de la sesión, NUNCA del modelo."""
    return "search.in(nivel_acceso, '{}', ',')".format(",".join(niveles_permitidos(nivel_usuario)))


# ---- Presentación de resultados y citas -------------------------------------------------------


def formatear_resultados(fragmentos: list[dict]) -> str:
    """Convierte los fragmentos recuperados en texto para el modelo, con id citable."""
    if not fragmentos:
        return (
            "SIN_RESULTADOS: no hay fragmentos de normativa accesibles para esta consulta. "
            "No inventes la respuesta."
        )
    bloques = [
        f"[{f['id']}] {f['titulo']} › {f['seccion']} (nivel: {f['nivel_acceso']})\n{f['contenido']}"
        for f in fragmentos
    ]
    return "\n\n".join(bloques)


def extraer_citas(texto: str) -> list[str]:
    """Ids citados como [NOR-001-02] o [NOR-001], sin repetidos y en orden de aparición."""
    return list(dict.fromkeys(PATRON_CITA.findall(texto or "")))


def citas_validas(citas: list[str], corpus: list[dict]) -> list[str]:
    """Devuelve solo las citas que existen en el corpus (fragmento o documento)."""
    ids_frag = {f["id"] for f in corpus}
    ids_doc = {f["doc_id"] for f in corpus}
    return [c for c in citas if c in ids_frag or c in ids_doc]
