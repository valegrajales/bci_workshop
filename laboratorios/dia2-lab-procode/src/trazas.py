"""Tarea 4 — trazas con OpenTelemetry (Application Insights o consola).

Spans que verás por cada pregunta:  invoke_agent  >  chat  +  execute_tool
  - invoke_agent: la ejecución completa del agente (incluye gen_ai.tool.definitions)
  - chat:         cada llamada al modelo (finish_reason = tool_calls | stop)
  - execute_tool: cada herramienta (gen_ai.tool.call.arguments / gen_ai.tool.call.result)

Fuentes: agent-framework/python/samples/02-agents/observability/foundry_tracing.py,
docs-oficiales/foundry/observability/how-to/trace-agent-framework.md
"""
from __future__ import annotations

import os
from contextlib import contextmanager


async def configurar_trazas(client) -> str:
    """Activa OpenTelemetry y devuelve el destino: 'consola' | 'app-insights'.

    - ENABLE_CONSOLE_EXPORTERS=true      -> trazas en la consola (plan B, sin App Insights)
    - APPLICATIONINSIGHTS_CONNECTION_STRING -> usa esa conexión
    - (por defecto)                      -> toma la conexión del proyecto de Foundry
    LAB_APPINSIGHTS_ENTRA=true -> envía con Microsoft Entra ID (si App Insights tiene la autenticación local
    deshabilitada; requiere el rol Monitoring Metrics Publisher).
    ENABLE_SENSITIVE_DATA=true guarda prompts y argumentos en los spans: solo para el taller,
    nunca en producción con datos reales.
    """
    from agent_framework.observability import configure_otel_providers

    if os.environ.get("ENABLE_CONSOLE_EXPORTERS", "").strip().lower() == "true":
        configure_otel_providers(enable_console_exporters=True, enable_sensitive_data=True)
        return "consola"

    conexion = os.environ.get("APPLICATIONINSIGHTS_CONNECTION_STRING", "").strip()
    extra = {}
    if os.environ.get("LAB_APPINSIGHTS_ENTRA", "").strip().lower() == "true":
        from azure.identity import DefaultAzureCredential  # el exportador de Azure Monitor es síncrono

        extra["credential"] = DefaultAzureCredential()
    if conexion:
        from agent_framework.observability import (
            create_metric_views,
            create_resource,
            enable_instrumentation,
        )
        from azure.monitor.opentelemetry import configure_azure_monitor

        configure_azure_monitor(
            connection_string=conexion, resource=create_resource(), views=create_metric_views(), **extra
        )
        enable_instrumentation(enable_sensitive_data=True)
    else:
        await client.configure_azure_monitor(enable_sensitive_data=True, **extra)
    return "app-insights"


@contextmanager
def traza_con_nombre(nombre: str):
    """Span propio que agrupa una pregunta; entrega el trace id para buscarlo en el portal."""
    from agent_framework.observability import get_tracer
    from opentelemetry.trace import SpanKind
    from opentelemetry.trace.span import format_trace_id

    with get_tracer().start_as_current_span(nombre, kind=SpanKind.CLIENT) as span:
        yield format_trace_id(span.get_span_context().trace_id)


@contextmanager
def span_propio(nombre: str, **atributos):
    """Span hijo con atributos propios (p. ej. el filtro de búsqueda) para diagnosticar.

    Aparecen como customDimensions en Application Insights. Si no configuraste trazas
    (Tareas 1-3), es un span vacío y no hace nada.
    """
    from agent_framework.observability import get_tracer

    with get_tracer().start_as_current_span(nombre) as span:
        for clave, valor in atributos.items():
            span.set_attribute(clave, valor)
        yield span


def vaciar_trazas() -> None:
    """Envía los spans pendientes antes de terminar el proceso (si no, pueden perderse)."""
    from opentelemetry import trace

    proveedor = trace.get_tracer_provider()
    if hasattr(proveedor, "force_flush"):
        proveedor.force_flush()
