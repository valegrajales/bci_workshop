# Laboratorios – BCI Microsoft AI Foundry Training Day

Estado al 2026-10-20. **Casi nada de este material se pudo probar contra un Foundry real.** Lo único probado hasta ahora son llamadas básicas de `gpt-5.6-luna` (Chat Completions y Responses API en eastus2); el resto (agente, file search, Studio, Foundry Toolkit) está sin validar. Cada kit trae una checklist de validación para correr en el entorno antes de la sesión.

| Carpeta | Qué es | Cuándo se usa | Prueba previa |
|---|---|---|---|
| `entorno-y-facilitacion\` | Guía para el admin de BCI (recursos, modelos, cuota, roles), scripts de validación, onboarding de participantes, runbook de los 3 días, plan B y borradores de comunicaciones | Antes del Día 1 | `scripts\02_validar_entorno.py` |
| `dia1-lab-guiado\` | Lab del Día 1 (65 min): **A** preparación del entorno y prerrequisitos con TAP (≈15 min), **B** tu primer agente en el portal + file search (≈25 min), **C** OCR con Document Intelligence (≈25 min). Incluye además la **demo en vivo de Document Intelligence** de los facilitadores (≈10 min, dentro del módulo Azure AI Services; guion en `demo-document-intelligence.md`) y datos ficticios de Austral Bank | Mié 21, lab 11:40–12:45 (demo ≈10:40–10:50; cierre 12:45–13:00) | `checklist-validacion.md` (18 pasos, incluye la demo) |
| `dia2-lab-procode\` | Lab del Día 2 (55 min): agente Python con grounding en AI Search, herramienta propia, trazas y caso fallido. 107 pruebas locales | Jue 22, 11:45–12:40 | `checklist-validacion.md` (20 puntos) |
| `dia3-workshop-arquitectura\` | Architecture Decision Workshop: caso ficticio, plantillas Excel/Word, guía del facilitador, ejemplo resuelto, checklist de producción y seguridad | Vie 23, 11:35–12:40 | no requiere nube |

## Agenda del Día 1 (hora de Chile)
09:00–09:30 Presentación de apertura (franja de 30–40 min; horario exacto por confirmar) · 09:30–09:45 Contexto y fundamentos · 09:45–10:15 Plataforma Foundry · 10:15–10:55 Azure AI Services (con demo en vivo de Document Intelligence ≈10:40–10:50) · 10:55–11:30 Agentes y conocimiento · 11:30–11:40 Pausa · 11:40–12:45 Laboratorio guiado (A 11:40–11:55, B 11:55–12:20, C 12:20–12:45) · 12:45–13:00 Preguntas y cierre.

## Lo primero que hay que probar (riesgos conocidos)
1. **`gpt-5.6-luna` + Foundry Agent Service + file search desde una cuenta de participante: NO PROBADO todavía.** `gpt-5.6-luna` es el modelo principal del laboratorio (predesplegado en cada cuenta); solo se comprobaron llamadas básicas con Chat Completions y Responses API en eastus2. Si el agente o file search fallan con este modelo, el respaldo es `gpt-5-mini` (también predesplegado). Probar los pasos 8 a 11 de `dia1-lab-guiado\checklist-validacion.md`.
2. **Cuota de `gpt-5.6-luna`: 4K TPM por cuenta; los `429` son reales.** Con ≈3K tokens de entrada dos veces seguidas se supera la cuota y devuelve error de límite de tasa. Por eso las parejas o tríos comparten un solo agente, se pide pegar textos cortos y la guía explica esperar ≈10 s o cambiar a `gpt-5-mini` (10K TPM). Cuota total usada: 62 cuentas × 4K = 248K TPM (GlobalStandard en 37 cuentas, inst01–04 y lab01–lab33; DataZoneStandard en 25 cuentas, lab34–lab58). Estimación de cuota del Día 2: por revisar (ver guía del facilitador del Día 2).
3. **Inicio de sesión con TAP:** las cuentas `labNN` están protegidas con MFA y no pueden registrarlo; solo funciona el Temporary Access Pass (válido el miércoles 21 de octubre entre 06:30 y 14:30, hora de Chile; los de los días 2 y 3 se regeneran cada noche). Probar `az login --use-device-code`, el portal y Foundry Toolkit con TAP, y definir quién reemite TAP durante el taller.
4. **`gpt-5-mini` + Azure AI Search / functions (Día 2):** la documentación marca esas herramientas como no soportadas para ese modelo en Agent Service. Probar `03_agente_con_search.py`; si falla, usar `FOUNDRY_MODEL=gpt-4.1-mini` (no está predesplegado en las cuentas: habría que desplegarlo; por confirmar).
5. **File search del Día 1:** subida de archivos con cuenta de participante (el aprovisionamiento asigna Foundry User y Reader en el RG y Cognitive Services User en la cuenta Foundry; Storage Blob Data Contributor por confirmar) e indexación.
6. **Document Intelligence Studio (Bloque C y demo en vivo):** cada cuenta `labNN`/`instNN` usa **su propia cuenta Foundry** (AIServices, sin recurso aparte) y tiene **Cognitive Services User** sobre ella: `participante.bicep` lo asigna en despliegues nuevos y `entorno-y-facilitacion\provisionamiento\Add-RolCognitiveServicesUser.ps1` lo agrega al entorno ya desplegado (ejecutar `-WhatIf` y luego real; idempotente). Falta probar el Studio con una cuenta `labNN` y las cookies de terceros (AADSTS50058).
7. **Application Insights del Día 2:** si tiene autenticación local deshabilitada, activar `LAB_APPINSIGHTS_ENTRA=true`.

## Decisiones abiertas
Quién administra el tenant y el entorno (cuentas `labNN@mngenvmcap219366.onmicrosoft.com` aprovisionadas con `entorno-y-facilitacion\provisionamiento\`; el límite de ~16 sesiones de un entorno compartido de Microsoft no aplica), Python vs .NET, monitor de Teams, quién reemite TAP, quién presenta la demo de Document Intelligence, política de grabación, uso de funciones en preview.

## Notas de formato
Los `.docx` pueden quedar cifrados por una etiqueta de sensibilidad aplicada por OneDrive/Purview: antes de enviarlos a BCI confirma que se abren con su cuenta, o expórtalos a PDF.
