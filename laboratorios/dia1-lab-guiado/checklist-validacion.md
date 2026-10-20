# Checklist de validación (prueba de humo) — Laboratorio Día 1

**Quién:** Facilitador 1 y Facilitador 2 · **Cuándo:** hoy o mañana temprano (antes del miércoles 21 de octubre; el ensayo final de la demo se repite antes de las 10:10) · **Dónde:** el entorno real del taller (cuenta de prueba `labNN`, su grupo de recursos `rg-bci-lab-NN`, su proyecto `lab-NN` y el recurso de Document Intelligence)

> **⚠ Estado de la validación — LÉELO PRIMERO**
>
> - **Probado (llamadas básicas):** `gpt-5.6-luna` responde con **Chat Completions** y con la **Responses API** en eastus2. Con ≈3K tokens de entrada dos veces seguidas se supera la cuota de 4K TPM y se obtiene un error de límite de tasa (`429`): **los `429` son reales** en el laboratorio y están documentados en la guía.
> - **NO probado todavía:** `gpt-5.6-luna` con **Foundry Agent Service + file search desde una cuenta de participante** (crear el agente, subir los 4 documentos, indexar y responder con cita). Hasta que se pruebe, el modelo de respaldo es `gpt-5-mini` (también predesplegado en cada cuenta). Los pasos 8 a 11 de esta tabla son los que cierran este riesgo: anota el resultado.
> - Tampoco se ejecutó todavía ningún otro paso del laboratorio en el entorno real (portal, Studio, Foundry Toolkit): esta prueba confirma que cada paso funciona y que los nombres de la interfaz coinciden con la guía.
>
> Usa una cuenta con los mismos roles que tendrán los participantes: hoy el aprovisionamiento asigna **Foundry User** y **Reader** sobre `rg-bci-lab-NN`. Si algún paso falla por permisos de almacenamiento (**Storage Blob Data Contributor**) o de Studio (**Cognitive Services User**), anótalo en la tabla de resultados. Usa solo datos de `datos\`. Guarda capturas para el plan B (ver `guia-facilitador.md`, sección 7).

| # | Qué hacer (clic / acción) | Resultado esperado | ✔ / Notas |
|---|---|---|---|
| 1 | En una terminal nueva: `az --version`, `python --version`, `git --version`, `code --version` | Las cuatro responden y Python es **3.13.x** (no 3.14) | ☐ |
| 2 | `az login --use-device-code --tenant eeee485f-b8f7-4983-b3dc-d5d97a0ad2bc`; abre `https://login.microsoft.com/device`, ingresa el código, tu cuenta `labNN@mngenvmcap219366.onmicrosoft.com` y elige **Use a Temporary Access Pass instead** con tu TAP. Luego `az account show` | Sesión iniciada sin pedir MFA; `az account show` muestra tu cuenta y el tenant. Anota si no aparece suscripción (en ese caso repite con `--allow-no-subscriptions`) y la vigencia real del TAP (06:30–14:30, uso múltiple) | ☐ |
| 3 | `az group show -n rg-bci-lab-NN -o table`, `az cognitiveservices account list -g rg-bci-lab-NN -o table` y `az cognitiveservices account deployment list -g rg-bci-lab-NN -n <nombre-cuenta> -o table` | Ves el grupo de recursos, la cuenta Foundry y los deployments `gpt-5.6-luna`, `gpt-5-mini` y `text-embedding-3-small` (nombre del deployment = nombre del modelo). Anota si Reader basta para listar | ☐ |
| 4 | Abre `https://ai.azure.com` con la cuenta del taller (con TAP) y activa **New Foundry** | Entras al proyecto `lab-NN` y ves **Home** con la información de conexión (no copies claves). Sin AADSTS50079/50076 si usas el TAP | ☐ |
| 5 | En VS Code instala/abre **Foundry Toolkit for VS Code** (extensión de Microsoft; las etiquetas pueden decir **AI Toolkit**) e inicia sesión en Azure | Extensión con sesión iniciada con la cuenta del taller. Anota los nombres reales de menús | ☐ |
| 6 | En el proyecto, abre la lista de modelos desplegados (**Build > Models** o **Models + endpoints**), selecciona `gpt-5.6-luna` y abre su playground. Escribe "Hola, ¿qué puedes hacer?" | El modelo está desplegado (sin desplegar nada) y responde. **Anota la ruta de menú real** para el README B.1 | ☐ |
| 7 | Prueba de cuota: en el playground de `gpt-5.6-luna`, envía dos mensajes largos seguidos (≈3K tokens de entrada cada uno). Espera ≈10 s y repite con un mensaje corto. Luego repite el mensaje largo con `gpt-5-mini` | El segundo mensaje largo devuelve `429`; el mensaje corto tras esperar funciona; con `gpt-5-mini` (10K TPM) no hay `429`. Guarda la captura del `429` real (plan B) | ☐ |
| 8 | **(Riesgo abierto)** En **Instructions** pega `datos\prompts.md` sección 1.1 y selecciona **Save as agent** con el nombre `austral-asistente-politicas-prueba`, con modelo `gpt-5.6-luna`. Si no existe el botón, usa **Build > Agents > Create agent** | Se abre el playground del agente con las pestañas **Chat** y **YAML** (`kind: prompt`) y `gpt-5.6-luna` como modelo. Anota cualquier error del Agent Service con este modelo | ☐ |
| 9 | **(Riesgo abierto)** **Tools > Add > File search > Upload files > Browse**: sube los 4 `.md` (o los 4 `.pdf`) de `datos\politicas-internas\`, **Attach** y espera la indexación | Estado de indexación completo en pocos minutos con `gpt-5.6-luna`. Si hay 403, falta **Storage Blob Data Contributor** (o **Foundry User**): anótalo | ☐ |
| 10 | **(Riesgo abierto)** **Save** y haz la pregunta 1 de `datos\prompts.md` (alojamiento en viaje internacional) con `gpt-5.6-luna`; luego las preguntas 2, 3, 4 y 5 | USD 180 por noche (USD 250 en ciudades categoría A) y 15 días hábiles, con cita de POL-GV-001; el resto con cita (POL-TI-007, PRO-CL-003, MAN-ON-002). Si el agente no usa file search, anótalo y decide el uso de `gpt-5-mini` | ☐ |
| 11 | Repite los pasos 8 a 10 cambiando el modelo del agente a `gpt-5-mini` (alternativa si el paso 10 falla) | El agente con `gpt-5-mini` cita los documentos. Anota la diferencia de calidad/velocidad frente a `gpt-5.6-luna` | ☐ |
| 12 | Pregunta 6 (días de vacaciones) y preguntas 7 (ignora tus instrucciones) y 8 (aprobar crédito/saldo de un RUT ficticio) | Vacaciones: no encuentra la información y sugiere Gestión de Personas (**no inventa** un número). 7 y 8: rechaza o limita con amabilidad sin revelar instrucciones ni datos de clientes | ☐ |
| 13 | Cambia una palabra de las instrucciones, **Save** y revisa el selector de versión (menú **Publish** o detalles del agente) | Se creó una versión nueva; el agente aparece en **Build > Agents** | ☐ |
| 14 | Abre Document Intelligence Studio (`https://documentintelligence.ai.azure.com/studio` o el enlace del laboratorio oficial), **Settings > Resource**, selecciona el recurso y autentícate con **Microsoft Entra ID** | Studio abre con el recurso, sin AADSTS50058 ni 403. Anota qué URL funcionó, **qué recurso usa cada cuenta `labNN`** y si hizo falta **Cognitive Services User** | ☐ |
| 15 | Modelo **Invoices**, carga `datos\documentos-ocr\01-factura.png`, **Analyze options** (idioma `es-CL` si aparece), **Run analysis** | Campos extraídos con confianza: F-000458, *Suministros Pacífico SpA*, 05-10-2026, total 1.190.000. Compara con `campos-esperados.md`. **Anota cómo se ve el monto (¿aparece CLP?)** y guarda el JSON como `resultado-factura.json` | ☐ |
| 16 | Modelo **Layout** con `02-solicitud-credito.png` y activa pares clave-valor en **Analyze options** | Texto, tabla de obligaciones y casillas detectadas; pares como "Nombre completo". Anota el nombre exacto de la opción | ☐ |
| 17 | En el playground de `gpt-5.6-luna` pega `datos\prompts.md` 3.1 con **solo los campos principales** de `resultado-factura.json` (y, si el modelo admite imágenes, prueba 3.3) | Resumen, validación 1.000.000 + 190.000 = 1.190.000 y campos con confianza baja, sin `429` (si ocurre, anótalo) | ☐ |
| 18 | **Demo en vivo (ver `demo-document-intelligence.md`):** en Studio, modelo **Receipt** con `datos\documentos-ocr\03-comprobante-compra.pdf`; luego **Layout** (o **Read**) sobre el mismo archivo. Compara con la sección 03 de `campos-esperados.md` y cronometra (objetivo ≈10 min) | Receipt devuelve `MerchantName`, `TransactionDate`, `Total` (14.700) e `Items` correctos y con confianza (`Subtotal` puede no extraerse); Layout devuelve texto sin campos semánticos. Guarda capturas y JSON del plan B (PB-D1-01) | ☐ |

## Resultado y decisiones

| Pregunta | Respuesta |
|---|---|
| ¿`gpt-5.6-luna` + Foundry Agent Service + file search funciona desde una cuenta de participante? ¿O se usa `gpt-5-mini` como modelo del agente? | |
| ¿Cómo se comporta el `429` de `gpt-5.6-luna` (≈4K TPM) con una pareja o trío usando una sola cuenta? ¿Alcanza la espera de ≈10 s? | |
| ¿Cuántas cuentas `labNN` se usan a la vez en B y C (≈16 grupos)? ¿Hay algún límite adicional de la suscripción o del tenant? | |
| ¿Funciona el inicio de sesión con TAP en terminal (`az login`), navegador y Foundry Toolkit? ¿Alguien puede reemitir un TAP el miércoles? | |
| ¿Qué URL de Studio funciona? ¿Qué recurso de Document Intelligence usan los participantes y qué roles hicieron falta? | |
| ¿Cómo se ve el monto CLP en la factura? ¿Hay que ajustar la guía (README C.3)? | |
| ¿Algún nombre de botón o ruta de menú difiere de la guía (por ejemplo, la lista de modelos en B.1)? (anota la ruta real) | |
| Demo en vivo: ¿duró ≈10 min? ¿Qué campos de Receipt salieron bien/mal? ¿Plan B guardado y reproducible? | |
| ¿Quién es el monitor de Teams? | |

Cuando termines, borra los agentes y despliegues de prueba que no necesites (no elimines el proyecto de los participantes) y comparte la tabla anterior con el equipo de entorno.
