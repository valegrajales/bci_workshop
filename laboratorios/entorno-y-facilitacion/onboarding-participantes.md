# Microsoft AI Foundry · BCI Training Day — Preparación para participantes

**Fechas:** 21, 22 y 23 de octubre de 2026 · **Horario:** 09:00–13:00, hora de Chile (Santiago; en octubre rige horario de verano, UTC−3 — *verificar en tu calendario*) · **Modalidad:** presencial en Microsoft Chile (Las Condes) o por Teams.
**Enlaces:** Teams `<LINK-TEAMS>` · Repositorio `<LINK-REPO>` · Autochequeo (pasos con capturas) `<LINK-SELFCHECK>` · Soporte `<CORREO-SOPORTE>`

> **Resumen:** antes del Día 1 **instala VS Code, Python 3.13, Git y Azure CLI** (sección 3). El miércoles 21 inicias sesión con tu cuenta del taller y un **Temporary Access Pass (TAP)** que te entregarán los organizadores. El laboratorio del Día 1 **comienza con una verificación de entorno de 15 minutos** (Bloque A).

## 1. Qué necesitas cada día

| Día | Qué haremos | Qué necesitas |
|---|---|---|
| **1 – Fundamentos (L100)** | Presentaciones y, desde las 11:40, laboratorio guiado de 65 minutos: **Bloque A** verificación del entorno y prerrequisitos (15 min), **Bloque B** tu primer agente con búsqueda en archivos (25 min) y **Bloque C** lectura de documentos (OCR) con Document Intelligence (25 min). Los facilitadores también harán una demo en vivo de Document Intelligence | Navegador actualizado (Edge o Chrome), **VS Code, Python 3.13, Git y Azure CLI ya instalados**, tu cuenta del taller `labNN` y tu **TAP** (sección 2) |
| **2 – Agentes en código (L200)** | Agente en Python con Azure AI Search, herramienta propia y trazas | Lo mismo que el Día 1 (ya instalado) + el repositorio clonado el día 21 por la tarde. Recibirás un **TAP nuevo** para el día 22 |
| **3 – Arquitectura (L300)** | Taller de decisiones de arquitectura; **sin laboratorio en la nube** | Solo tu participación (puedes llevar tus casos de uso, **sin datos reales**) |

## 2. Cuentas y acceso (Temporary Access Pass)
- Los organizadores te asignarán una **cuenta del taller** con el formato `labNN@mngenvmcap219366.onmicrosoft.com` (NN = tu número; por ejemplo, `lab07`). **No es tu cuenta corporativa de BCI.** Recibirás tu número y el nombre de tu proyecto (`lab-NN`) a más tardar el `<FECHA-LIMITE>` (*por confirmar* el canal de envío).
- Cada cuenta ya tiene su grupo de recursos `rg-bci-lab-NN`, un proyecto `lab-NN` y los modelos **ya desplegados** (`gpt-5.6-luna` como modelo principal y `gpt-5-mini` como respaldo). No necesitas crear ni desplegar nada.
- Las cuentas están protegidas con MFA y **no puedes registrar MFA en este tenant**: inicias sesión con un **Temporary Access Pass (TAP)** que te entregarán los organizadores `<CANAL-ENTREGA-TAP>`. Tu TAP del Día 1 **solo es válido el miércoles 21 de octubre, entre las 06:30 y las 14:30 (hora de Chile)**; por eso no podrás usarlo antes. Para los días 2 y 3 se genera un TAP nuevo cada noche.
- Si ves el error **AADSTS50079** o **AADSTS50076**, significa que no estás usando el TAP: elige **Use a Temporary Access Pass instead** e ingresa el código. Si el TAP aún no es válido (antes de las 06:30) o ya expiró, avisa a un facilitador.
- Si tu equipo tiene restricciones (VPN, acceso condicional, navegador con cookies de terceros bloqueadas), pruébalo antes y avísanos: Document Intelligence Studio necesita permitir cookies de terceros (error AADSTS50058).
- Todos los datos del taller son **ficticios**. No pegues información real de clientes, colaboradores ni de BCI en el laboratorio. Las sesiones se **graban** (ver sección 5).

## 3. Prerrequisitos que debes instalar antes de la sesión (≈15 min)
Instala estas herramientas **antes del miércoles 21**. En Windows (PowerShell):

```powershell
winget install -e --id Microsoft.VisualStudioCode
winget install -e --id Python.Python.3.13
winget install -e --id Git.Git
winget install -e --id Microsoft.AzureCLI
```

Cierra y vuelve a abrir la terminal, y verifica:

```powershell
code --version
python --version   # debe mostrar 3.13.x (3.14 aún no es compatible)
git --version
az --version
```

Además, necesitarás una suscripción de Azure activa: **la del taller ya está disponible a través de tu cuenta `labNN`**, no necesitas la tuya. Si ya tienes Python 3.14 instalado, instala también 3.13 y úsalo para el laboratorio (el laboratorio se probó con 3.13.12). Si tienes macOS o Linux, usa tu gestor de paquetes equivalente (*por confirmar* los pasos exactos).

**Qué hacemos con esto el Día 1 (Bloque A, 15 min, 11:40–11:55):** instalas la extensión **Foundry Toolkit for VS Code** (de Microsoft; algunas etiquetas aún pueden decir «AI Toolkit»), inicias sesión con tu cuenta `labNN` y tu TAP en `https://ai.azure.com` y con `az login --use-device-code --tenant eeee485f-b8f7-4983-b3dc-d5d97a0ad2bc`, y confirmas que ves tu proyecto y los modelos. **No puedes hacer el inicio de sesión antes**, porque el TAP solo sirve el día 21.

**Autochequeo previo (5 minutos):** ejecuta los cuatro comandos de verificación de arriba. Si algo falla, anota el mensaje exacto y escríbenos a `<CORREO-SOPORTE>` antes del evento.

**Clona el repositorio** con `git clone <LINK-REPO>` el **día 21 por la tarde**; no necesitas hacerlo antes.

## 4. Si tu notebook corporativo está restringido
No es un problema: elige una de estas opciones y avísanos con anticipación.
1. **Trabajo en pareja o trío:** si estás en la sala, comparte el equipo de un compañero. De todas formas, en el laboratorio las parejas o tríos comparten **un solo agente** por la cuota de los modelos.
2. **Codespaces / dev container:** ejecuta el laboratorio del Día 2 en el navegador desde `<LINK-REPO>` (requiere una cuenta de GitHub permitida por BCI; *verificar* con tu equipo de TI).
3. **Demo del instructor:** sigues el laboratorio en vivo por Teams y recibes el material y la grabación para repetirlo después.

Los bloques B y C del Día 1 se hacen en el navegador (portal de Foundry y Document Intelligence Studio), de modo que, si no puedes instalar herramientas, aún puedes seguirlos en pareja. El Día 3 no requiere nada instalado.

## 5. Durante el evento
- **Teams:** usa el chat para preguntas y marca «Lab» si estás bloqueado; una persona del equipo monitorea el chat. Mantén el micrófono en silencio salvo que preguntes.
- **Presencial:** llega 15 minutos antes (09:00 en punto comienza la sesión); lleva tu notebook, cargador y tu TAP.
- **Límites de uso:** el modelo principal tiene una cuota baja (≈4K TPM por cuenta). Si ves un error `429`, espera unos 10 segundos, usa textos más cortos o cambia al modelo `gpt-5-mini`.
- **Grabación y entregables:** se grabará la sesión; después recibirás grabación, repositorio y presentaciones.
- **Soporte:** `<CORREO-SOPORTE>` o el chat de `<LINK-TEAMS>`.

## Fuentes
Plan del evento y alcance por día: `MATERIALS_INDEX.md`, `presentaciones\content\day1.json`, `presentaciones\content\day2.json`. Prerrequisitos del laboratorio: ejercicio público de Microsoft Learn *mslearn-ai-agents* (`https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/Exercises/02-agent-custom-tools.html#prerequisites`) e instalación de Azure CLI (`https://learn.microsoft.com/cli/azure/install-azure-cli`). Requisitos de Python y herramientas del Día 2 y alternativa sin Azure: `repos\publico-workshops\foundry-hosted-agents-workshop\` (`.workshop\scripts\preflight.py`, dev container) y `repos\microsoftlearning-labs\mslearn-agent-quickstart\`. Roles y proyecto por participante: `laboratorios\entorno-y-facilitacion\guia-entorno-admin-bci.md`. Horario de verano en Chile: *verificar*.
