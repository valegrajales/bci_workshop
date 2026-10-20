#!/usr/bin/env python3
"""
02_validar_entorno.py - Validación SOLO LECTURA del entorno de laboratorio BCI Foundry.

Propósito
    Confirmar, antes del taller (y con la cuenta de un participante de prueba), que:
      1. El endpoint del proyecto Foundry responde y el usuario tiene acceso (rol Foundry User).
      2. Los deployments de modelos esperados existen POR NOMBRE (y, sin fallar, gpt-5.6-luna del Día 1).
      3. Azure AI Search responde (y el índice del Día 2 existe, si se indica).
      4. Document Intelligence responde.
      5. La cadena de conexión de Application Insights está presente y bien formada.
      6. (Opcional, --egress) hay salida de red a los hosts clave (DNS + TCP 443).

    Imprime PASS / FAIL / WARN / SKIP por verificación. NO imprime tokens, claves ni la cadena de conexión
    completa (de Application Insights solo muestra el host de ingesta). NO crea, modifica ni elimina nada:
    solo realiza solicitudes GET y resoluciones DNS/TCP. No envía telemetría ni consume tokens de modelos.

NO EJECUTAR EN PRODUCCIÓN. Está pensado para la suscripción del laboratorio y no fue ejecutado por Microsoft
antes de su entrega (ver guia-entorno-admin-bci.md, sección 17).

Variables de entorno (también pueden pasarse como argumentos). Se aceptan los nombres del lab del Día 2
(laboratorios/dia2-lab-procode/.env.example) y, como alias, los del starter AZURE_AI_* del workshop de agentes:
    FOUNDRY_PROJECT_ENDPOINT (alias AZURE_AI_PROJECT_ENDPOINT)       https://<recurso>.services.ai.azure.com/api/projects/<proyecto>
    FOUNDRY_MODEL (alias AZURE_AI_MODEL_DEPLOYMENT_NAME)             nombre del deployment de chat (por defecto gpt-5-mini; el Día 1 usa gpt-5.6-luna con gpt-5-mini de respaldo)
    FOUNDRY_EMBEDDING_MODEL (alias AZURE_AI_EMBEDDING_MODEL_DEPLOYMENT_NAME)   nombre del deployment de embeddings (por defecto text-embedding-3-small)
    AZURE_SEARCH_ENDPOINT (alias AZURE_AI_SEARCH_ENDPOINT)           https://<servicio>.search.windows.net
    AZURE_SEARCH_INDEX_NAME (alias AZURE_AI_SEARCH_INDEX_NAME)       índice del Día 2 (opcional; el lab usa normativa-austral)
    DOCUMENT_INTELLIGENCE_ENDPOINT             https://<recurso>.cognitiveservices.azure.com (nombre de variable propio de este kit)
    APPLICATIONINSIGHTS_CONNECTION_STRING      cadena de conexión de Application Insights

Parámetros
    --deployments  lista separada por comas de deployments esperados además de los de las variables de entorno
                   (si FOUNDRY_MODEL / FOUNDRY_EMBEDDING_MODEL no están definidas se esperan gpt-5-mini y text-embedding-3-small)
                   Además, de forma NO fatal (WARN si falta), se comprueba que exista gpt-5.6-luna, el modelo principal del
                   Día 1 (4K TPM por cuenta; los 429 son posibles). No prueba Agent Service + file search con ese modelo.
    --respaldo     exige además el deployment gpt-4.1-mini (respaldo de la propuesta original; no está predesplegado en el
                   entorno real, donde el respaldo del Día 1 es gpt-5-mini)
    --sin-embeddings   no exige el deployment de embeddings (Plan B: índice solo texto)
    --skip-search / --skip-di / --skip-appi    omitir verificaciones
    --egress       agrega verificación de red a hosts clave (orientativa; confirmar lista con la guía, sección 10)
    --timeout      segundos por solicitud (por defecto 15)
    --json         salida en JSON
    --dry-run      muestra qué se verificaría y con qué variables, SIN hacer llamadas de red

Autenticación
    Usa azure-identity (DefaultAzureCredential, sin navegador interactivo) si está instalado; si no, usa
    'az account get-access-token'. Roles necesarios: ver guia-entorno-admin-bci.md, sección 6.

Código de salida: 0 = sin FAIL; 1 = al menos un FAIL; 2 = error de uso.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

PROJECT_API_VERSION = "v1"
DEFAULT_CHAT_DEPLOYMENT = "gpt-5-mini"
DEFAULT_EMBEDDING_DEPLOYMENT = "text-embedding-3-small"
FALLBACK_CHAT_DEPLOYMENT = "gpt-4.1-mini"
LUNA_DEPLOYMENT = "gpt-5.6-luna"
SEARCH_API_VERSION = "2024-07-01"
DI_API_VERSION = "2024-11-30"
SCOPE_FOUNDRY = "https://ai.azure.com/.default"
SCOPE_SEARCH = "https://search.azure.com/.default"
SCOPE_COGNITIVE = "https://cognitiveservices.azure.com/.default"

GUID_RE = re.compile(r"^[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}$")
SECRET_PATTERNS = [
    re.compile(r"Bearer\s+[A-Za-z0-9._\-]+", re.I),
    re.compile(r"eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]*"),
    re.compile(r"(InstrumentationKey|api-key|key)\s*[=:]\s*[^;\s,]+", re.I),
]

RESULTS: list[dict[str, str]] = []


def scrub(text: str, limit: int = 220) -> str:
    """Elimina patrones que parezcan secretos y acorta el texto."""
    text = " ".join(str(text).split())
    for pattern in SECRET_PATTERNS:
        text = pattern.sub("[oculto]", text)
    return text[:limit]


def record(name: str, status: str, detail: str = "", hint: str = "") -> None:
    RESULTS.append({"check": name, "status": status, "detail": scrub(detail), "hint": hint})


def cfg(args_value: str | None, *env_names: str) -> str:
    """Devuelve el argumento o la primera variable de entorno definida (ignora placeholders <...>)."""
    if args_value and args_value.strip():
        return args_value.strip()
    for name in env_names:
        value = os.environ.get(name, "").strip()
        if value and not value.startswith("<"):
            return value
    return ""


def build_credential():
    try:
        from azure.identity import DefaultAzureCredential  # type: ignore
    except ImportError:
        return None
    return DefaultAzureCredential(exclude_interactive_browser_credential=True)


def get_token(credential, scope: str) -> tuple[str | None, str]:
    if credential is not None:
        try:
            return credential.get_token(scope).token, ""
        except Exception as exc:  # noqa: BLE001 - se informa solo el tipo y un resumen saneado
            azure_error = f"{type(exc).__name__}: {scrub(exc, 120)}"
        else:
            azure_error = ""
    else:
        azure_error = "azure-identity no instalado"
    az_path = shutil.which("az")
    if not az_path:
        return None, f"{azure_error}; Azure CLI no encontrado (ejecuta az login o instala azure-identity)"
    resource = scope.removesuffix("/.default")
    try:
        proc = subprocess.run(
            [az_path, "account", "get-access-token", "--resource", resource, "--query", "accessToken", "-o", "tsv"],
            capture_output=True, text=True, timeout=45,
        )
    except Exception as exc:  # noqa: BLE001
        return None, f"{azure_error}; az falló: {type(exc).__name__}"
    token = (proc.stdout or "").strip()
    if proc.returncode != 0 or not token:
        return None, f"{azure_error}; az no entregó token (¿az login?): {scrub(proc.stderr, 120)}"
    return token, ""


def http_get(url: str, token: str | None, timeout: int) -> tuple[int | None, str, str]:
    headers = {"Accept": "application/json", "User-Agent": "bci-foundry-lab-validate/1.0"}
    if token:
        headers["Authorization"] = "Bearer " + token
    request = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.getcode(), response.read(1_000_000).decode("utf-8", errors="replace"), ""
    except urllib.error.HTTPError as exc:
        body = exc.read(2048).decode("utf-8", errors="replace")
        return exc.code, body, f"HTTP {exc.code}"
    except Exception as exc:  # noqa: BLE001
        return None, "", f"{type(exc).__name__}: {scrub(exc, 120)}"


def valid_https(url: str) -> urllib.parse.SplitResult | None:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or not parsed.netloc:
        return None
    return parsed


def extract_names(payload) -> list[str]:
    items = payload.get("value", []) if isinstance(payload, dict) else payload
    names: list[str] = []
    for item in items or []:
        if isinstance(item, str):
            names.append(item)
        elif isinstance(item, dict):
            for key in ("name", "deploymentName", "deployment_name"):
                if isinstance(item.get(key), str) and item[key]:
                    names.append(item[key])
                    break
    return sorted(set(names))


def http_hint(status: int | None, who: str) -> str:
    if status in (401, 403):
        return (f"Falta rol o acceso condicional bloquea el token. {who}: revisa la asignación de roles "
                "(guía, sección 6), espera unos minutos de propagación y verifica el acceso condicional (sección 10).")
    if status == 404:
        return "Ruta o nombre incorrecto: revisa el endpoint y el nombre del proyecto/recurso."
    if status == 429:
        return "Limitación (429): reintenta en 1 minuto; revisa cuota (guía, sección 5)."
    if status is None:
        return "Sin respuesta de red: revisa DNS, proxy/firewall y la lista de egress (guía, sección 10)."
    return "Respuesta inesperada: revisa el endpoint y la versión de API; verificar en el recurso."


def check_python() -> None:
    version = sys.version_info
    label = f"{version.major}.{version.minor}.{version.micro}"
    if (version.major, version.minor) == (3, 13):
        record("Python 3.13", "PASS", label)
    elif (version.major, version.minor) >= (3, 14):
        record("Python 3.13", "WARN", f"{label}; Python 3.14 aún NO es compatible con el laboratorio (probado con 3.13.12)", "Instala Python 3.13: winget install -e --id Python.Python.3.13")
    else:
        record("Python 3.13", "WARN", f"{label}; el pre-trabajo del Día 1 pide Python 3.13 (el lab del Día 2 acepta 3.10+)", "Instala Python 3.13: winget install -e --id Python.Python.3.13 (o usa Codespaces/dev container).")


def check_luna(names: list[str], expected: list[str]) -> None:
    """Verificación NO fatal: gpt-5.6-luna es el modelo principal del Día 1 (4K TPM por cuenta; posibles 429)."""
    if LUNA_DEPLOYMENT in expected:
        return
    if LUNA_DEPLOYMENT in names:
        record(f"Deployment {LUNA_DEPLOYMENT} (Día 1)", "PASS", "presente (4K TPM por cuenta: los 429 son posibles; respaldo gpt-5-mini)")
    else:
        record(f"Deployment {LUNA_DEPLOYMENT} (Día 1)", "WARN", f"no existe en el proyecto; existen: {', '.join(names) or 'ninguno'}",
               "Se despliega con provisionamiento\\Add-Modelo.ps1; el Día 1 puede usar gpt-5-mini como respaldo. Agent Service + file search con este modelo aún no está probado.")


def check_project(endpoint: str, expected: list[str], credential, timeout: int) -> None:
    parsed = valid_https(endpoint)
    if not endpoint:
        record("Endpoint del proyecto", "FAIL", "FOUNDRY_PROJECT_ENDPOINT (o AZURE_AI_PROJECT_ENDPOINT) no definido", "Copia el endpoint desde la página del proyecto en el portal de Foundry.")
        return
    if not parsed:
        record("Endpoint del proyecto", "FAIL", "debe ser una URL https válida", "Formato: https://<recurso>.services.ai.azure.com/api/projects/<proyecto>")
        return
    token, error = get_token(credential, SCOPE_FOUNDRY)
    if not token:
        record("Token Entra para Foundry", "FAIL", error, "Ejecuta az login con la cuenta del participante (o revisa acceso condicional).")
        return
    record("Token Entra para Foundry", "PASS", "token obtenido (no se muestra)")
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    if not any(key == "api-version" for key, _ in query):
        query.append(("api-version", PROJECT_API_VERSION))
    url = urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path.rstrip("/") + "/deployments", urllib.parse.urlencode(query), ""))
    status, body, error = http_get(url, token, timeout)
    if status != 200:
        record("Proyecto Foundry accesible", "FAIL", error or f"HTTP {status}", http_hint(status, "Se requiere Foundry User en el recurso o proyecto"))
        record("Deployments por nombre", "SKIP", "no se pudo listar")
        return
    record("Proyecto Foundry accesible", "PASS", f"host {parsed.netloc}")
    try:
        names = extract_names(json.loads(body))
    except ValueError:
        record("Deployments por nombre", "WARN", "respuesta no JSON; no se pudieron leer los nombres", "Verificar en el portal: Modelos + endpoints.")
        return
    check_luna(names, expected)
    if not expected:
        record("Deployments por nombre", "WARN", f"sin nombres esperados; existen: {', '.join(names) or 'ninguno'}", "Define FOUNDRY_MODEL (o AZURE_AI_MODEL_DEPLOYMENT_NAME) o usa --deployments.")
        return
    missing = [name for name in expected if name not in names]
    if missing:
        record("Deployments por nombre", "FAIL", f"faltan: {', '.join(missing)}; existen: {', '.join(names) or 'ninguno'}",
               "El nombre del deployment (no el del modelo) debe coincidir con la variable de entorno.")
    else:
        record("Deployments por nombre", "PASS", f"presentes: {', '.join(expected)}")


def check_search(endpoint: str, index: str, credential, timeout: int) -> None:
    if not endpoint:
        record("Azure AI Search", "FAIL", "AZURE_SEARCH_ENDPOINT (o AZURE_AI_SEARCH_ENDPOINT) no definido", "Copia la URL del servicio desde el portal de Azure.")
        return
    parsed = valid_https(endpoint)
    if not parsed:
        record("Azure AI Search", "FAIL", "debe ser una URL https válida", "Formato: https://<servicio>.search.windows.net")
        return
    token, error = get_token(credential, SCOPE_SEARCH)
    if not token:
        record("Azure AI Search", "FAIL", error, "Obtén el token con az login; el servicio debe permitir autenticación por roles (RBAC).")
        return
    base = f"https://{parsed.netloc}"
    if index:
        url = f"{base}/indexes/{urllib.parse.quote(index)}/docs/$count?api-version={SEARCH_API_VERSION}"
        status, body, error = http_get(url, token, timeout)
        if status == 200:
            count = scrub(body.strip().lstrip("\ufeff"), 30)
            record("Azure AI Search (índice)", "PASS", f"índice '{index}' responde; documentos: {count}")
        elif status == 404:
            record("Azure AI Search (índice)", "FAIL", f"el índice '{index}' no existe", "Los instructores crean el índice antes del Día 2 (guía, sección 7).")
        else:
            record("Azure AI Search (índice)", "FAIL", error or f"HTTP {status}", http_hint(status, "Se requiere Search Index Data Reader y control de acceso por roles habilitado"))
        return
    url = f"{base}/indexes?api-version={SEARCH_API_VERSION}&$select=name"
    status, body, error = http_get(url, token, timeout)
    if status == 200:
        try:
            names = extract_names(json.loads(body))
        except ValueError:
            names = []
        record("Azure AI Search", "PASS", f"servicio responde; índices: {', '.join(names) or 'ninguno'}")
    elif status in (401, 403):
        record("Azure AI Search", "WARN", f"HTTP {status} al listar índices (Search Index Data Reader solo consulta)",
               "Define AZURE_SEARCH_INDEX_NAME para verificar con una consulta de solo lectura.")
    else:
        record("Azure AI Search", "FAIL", error or f"HTTP {status}", http_hint(status, "Revisar rol y endpoint"))


def check_document_intelligence(endpoint: str, credential, timeout: int) -> None:
    if not endpoint:
        record("Document Intelligence", "FAIL", "DOCUMENT_INTELLIGENCE_ENDPOINT no definido", "Copia el endpoint desde el recurso en el portal de Azure.")
        return
    parsed = valid_https(endpoint)
    if not parsed:
        record("Document Intelligence", "FAIL", "debe ser una URL https válida", "Formato: https://<recurso>.cognitiveservices.azure.com")
        return
    url = f"https://{parsed.netloc}/documentintelligence/documentModels?api-version={DI_API_VERSION}"
    status, _, error = http_get(url, None, timeout)
    if status is None:
        record("Document Intelligence (red)", "FAIL", error, http_hint(None, "DI"))
        return
    record("Document Intelligence (red)", "PASS", f"el host {parsed.netloc} responde (HTTP {status} sin credenciales es normal)")
    token, token_error = get_token(credential, SCOPE_COGNITIVE)
    if not token:
        record("Document Intelligence (auth)", "WARN", token_error, "No se pudo probar la autorización con Entra ID.")
        return
    status, _, error = http_get(url, token, timeout)
    if status == 200:
        record("Document Intelligence (auth)", "PASS", "autorizado con Entra ID (Cognitive Services User)")
    elif status in (401, 403):
        record("Document Intelligence (auth)", "FAIL", error, "Falta Cognitive Services User o el recurso no tiene subdominio personalizado/Entra habilitado; verificar.")
    elif status == 404:
        record("Document Intelligence (auth)", "WARN", "HTTP 404 en la ruta de modelos", "Verificar versión de API/ruta en el recurso; la autorización puede estar bien.")
    else:
        record("Document Intelligence (auth)", "WARN", error or f"HTTP {status}", http_hint(status, "DI"))


def check_app_insights(connection_string: str) -> None:
    if not connection_string:
        record("Application Insights", "FAIL", "APPLICATIONINSIGHTS_CONNECTION_STRING no definida", "Copia la cadena desde Application Insights > Información general (no la compartas en chats públicos).")
        return
    parts = {}
    for chunk in connection_string.split(";"):
        if "=" in chunk:
            key, _, value = chunk.partition("=")
            parts[key.strip().lower()] = value.strip()
    problems = []
    if not GUID_RE.match(parts.get("instrumentationkey", "")):
        problems.append("InstrumentationKey ausente o con formato inválido")
    ingestion = parts.get("ingestionendpoint", "")
    host = urllib.parse.urlsplit(ingestion).netloc
    if not host:
        problems.append("IngestionEndpoint ausente")
    if problems:
        record("Application Insights", "FAIL", "; ".join(problems), "Usa la cadena de conexión completa (no solo la clave).")
        return
    try:
        socket.getaddrinfo(host, 443)
        record("Application Insights", "PASS", f"cadena presente y bien formada; host de ingesta {host} resuelve por DNS")
    except OSError as exc:
        record("Application Insights", "WARN", f"cadena presente; DNS de {host} no resuelve ({type(exc).__name__})", "Revisa DNS/egress (guía, sección 10).")


def check_egress(extra_hosts: list[str], timeout: int) -> None:
    hosts = ["login.microsoftonline.com", "management.azure.com", "ai.azure.com", "pypi.org", "github.com"]
    for host in extra_hosts:
        if host and host not in hosts:
            hosts.append(host)
    for host in hosts:
        try:
            with socket.create_connection((host, 443), timeout=timeout):
                record(f"Egress {host}:443", "PASS", "DNS + TCP OK")
        except OSError as exc:
            record(f"Egress {host}:443", "FAIL", type(exc).__name__, "Solicita al equipo de red permitir este host (guía, sección 10).")


def print_report(as_json: bool) -> int:
    failed = any(item["status"] == "FAIL" for item in RESULTS)
    if as_json:
        print(json.dumps({"resultado": "FAIL" if failed else "OK", "verificaciones": RESULTS}, ensure_ascii=False, indent=2))
    else:
        print("== Validación del entorno BCI Foundry (solo lectura) ==")
        for item in RESULTS:
            print(f"[{item['status']:<4}] {item['check']}" + (f" - {item['detail']}" if item["detail"] else ""))
            if item["status"] in ("FAIL", "WARN") and item["hint"]:
                print(f"       Sugerencia: {item['hint']}")
        counts = {key: sum(1 for item in RESULTS if item["status"] == key) for key in ("PASS", "WARN", "FAIL", "SKIP")}
        print(f"\nResumen: {counts['PASS']} PASS, {counts['WARN']} WARN, {counts['FAIL']} FAIL, {counts['SKIP']} SKIP")
        print("GO para este usuario." if not failed else "NO-GO para este usuario: corrige los FAIL y repite.")
    return 1 if failed else 0


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    parser = argparse.ArgumentParser(description="Validación de solo lectura del entorno BCI Foundry (PASS/FAIL).")
    parser.add_argument("--project-endpoint")
    parser.add_argument("--search-endpoint")
    parser.add_argument("--search-index")
    parser.add_argument("--di-endpoint")
    parser.add_argument("--deployments", help="lista separada por comas")
    parser.add_argument("--respaldo", action="store_true", help="exige también el deployment gpt-4.1-mini (respaldo de la propuesta original; no está predesplegado en el entorno real)")
    parser.add_argument("--sin-embeddings", action="store_true", help="no exige el deployment de embeddings (índice solo texto)")
    parser.add_argument("--skip-search", action="store_true")
    parser.add_argument("--skip-di", action="store_true")
    parser.add_argument("--skip-appi", action="store_true")
    parser.add_argument("--egress", action="store_true")
    parser.add_argument("--timeout", type=int, default=15)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    project = cfg(args.project_endpoint, "FOUNDRY_PROJECT_ENDPOINT", "AZURE_AI_PROJECT_ENDPOINT")
    search = cfg(args.search_endpoint, "AZURE_SEARCH_ENDPOINT", "AZURE_AI_SEARCH_ENDPOINT")
    index = cfg(args.search_index, "AZURE_SEARCH_INDEX_NAME", "AZURE_AI_SEARCH_INDEX_NAME")
    di = cfg(args.di_endpoint, "DOCUMENT_INTELLIGENCE_ENDPOINT")
    appi = os.environ.get("APPLICATIONINSIGHTS_CONNECTION_STRING", "").strip()
    chat = cfg(None, "FOUNDRY_MODEL", "AZURE_AI_MODEL_DEPLOYMENT_NAME") or DEFAULT_CHAT_DEPLOYMENT
    embedding = "" if args.sin_embeddings else (
        cfg(None, "FOUNDRY_EMBEDDING_MODEL", "AZURE_AI_EMBEDDING_MODEL_DEPLOYMENT_NAME") or DEFAULT_EMBEDDING_DEPLOYMENT)
    expected = [chat, embedding]
    if args.respaldo:
        expected.append(FALLBACK_CHAT_DEPLOYMENT)
    if args.deployments:
        expected += [name.strip() for name in args.deployments.split(",")]
    expected = [name for i, name in enumerate(expected) if name and name not in expected[:i]]

    if args.dry_run:
        print("== DRY-RUN: no se realizan llamadas de red ==")
        plan = [
            ("Python 3.13", "local"),
            ("Proyecto Foundry + deployments", f"GET <FOUNDRY_PROJECT_ENDPOINT>/deployments?api-version={PROJECT_API_VERSION} -> {'definido' if project else 'NO definido'}; esperados: {', '.join(expected) or 'ninguno'}"),
            (f"Deployment {LUNA_DEPLOYMENT} (no fatal)", "WARN si falta (modelo principal del Día 1, 4K TPM por cuenta); se omite si ya está en los esperados"),
            ("Azure AI Search", f"GET <AZURE_SEARCH_ENDPOINT>/indexes/<índice>/docs/$count?api-version={SEARCH_API_VERSION} -> {'definido' if search else 'NO definido'}; índice: {index or 'no indicado'}" + (" (OMITIDO)" if args.skip_search else "")),
            ("Document Intelligence", f"GET <DOCUMENT_INTELLIGENCE_ENDPOINT>/documentintelligence/documentModels?api-version={DI_API_VERSION} -> {'definido' if di else 'NO definido'}" + (" (OMITIDO)" if args.skip_di else "")),
            ("Application Insights", f"validación local de la cadena + DNS -> {'definida' if appi else 'NO definida'}" + (" (OMITIDO)" if args.skip_appi else "")),
            ("Egress (--egress)", "DNS + TCP 443 a hosts clave" if args.egress else "no solicitado"),
        ]
        for name, detail in plan:
            print(f"- {name}: {detail}")
        return 0

    check_python()
    credential = build_credential()
    check_project(project, expected, credential, args.timeout)
    if args.skip_search:
        record("Azure AI Search", "SKIP", "omitido por --skip-search")
    else:
        check_search(search, index, credential, args.timeout)
    if args.skip_di:
        record("Document Intelligence", "SKIP", "omitido por --skip-di")
    else:
        check_document_intelligence(di, credential, args.timeout)
    if args.skip_appi:
        record("Application Insights", "SKIP", "omitido por --skip-appi")
    else:
        check_app_insights(appi)
    if args.egress:
        hosts = [urllib.parse.urlsplit(value).netloc for value in (project, search, di) if value]
        check_egress(hosts, args.timeout)
    return print_report(args.json)


if __name__ == "__main__":
    sys.exit(main())
