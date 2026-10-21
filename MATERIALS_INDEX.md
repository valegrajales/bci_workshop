# BCI – Microsoft AI Foundry Training Day: índice de materiales por módulo

**Fechas:** mié 21 (L100) · jue 22 (L200) · vie 23 (L300) de octubre de 2026 · 09:00–13:00 hora Chile · híbrido (Microsoft Chile + Teams) · ~48 inscritos (21 presenciales / 27 Teams).
**Trainers locales:** Pablo Braconi + Valentina Grajales (reparto de módulos aún tentativo). Organiza: Robert Escalante.
**Generado:** 2026-10-19. Rutas relativas a esta carpeta (`BCI-Foundry-Workshop\`).

Leyenda de la columna *Estado*: 🟢 listo para reutilizar · 🟡 hay que adaptar/armar · 🔴 gap o bloqueo.

> **Confidencialidad.** Los decks de SharePoint (SSG IP Release), el courseware AI-103T00 (Learning Download Center) y los repos *internos* son material interno de Microsoft: sirven de fuente para armar los decks de BCI, pero no se entregan tal cual al cliente. Los repos públicos y los labs de MicrosoftLearning sí se pueden citar y compartir (respetando licencia).

---

## 0. Material "ancla" por día (lo que más conviene reutilizar)

| Día | Slides ancla | Labs ancla |
|---|---|---|
| **1 – L100** | AI-103T00 es-ES decks 01, 03, 04 · `Introduction to Microsoft Foundry.pptx` · `Building RAG apps.pptx` | `mslearn-agent-quickstart`, `mslearn-ai-studio`, `mslearn-ai-information-extraction`, `mslearn-ai-language` |
| **2 – L200** | AI-103T00 es-ES deck 02 · `Microsoft Agent Framework.pptx` · `Building Agents Based App.pptx` · `MAF-Python\PythonAgents-*.pptx` (6 decks) | `mslearn-ai-agents` (A0–A6, C0–C4, D1–D2) · `foundry-hosted-agents-workshop` · `agent-framework-workshop` (interno) · AgentFactory Lab 5/6 |
| **3 – L300** | Production-Readiness: *Agentic Architectures*, *AI Landing Zones*, *AI Security and Observability*, *AgentOps*, *Solution Optimisation*, *Frontier CoE & Governance* · AI-Governance-Accelerator (módulos 1–4) | `mslearn-ai-multi-agents` (labs 01–17) · `mslearn-ai-governance` (G0–G7) · `mslearn-genaiops` · `AI-Gateway` labs · `Azure/agentops` |

Dato clave de alineación: el curso **AI-103T00 "Develop AI apps and agents on Azure"** (es-ES, may-2026) cubre casi todo el temario de L100 y L200 y se apoya en los repos `mslearn-ai-studio` (LP1 Foundry), `mslearn-ai-agents` (LP2 Agentes), `mslearn-ai-language` (LP3) y `mslearn-ai-vision` + `mslearn-ai-information-extraction` (LP4), todos ya descargados.

Rutas base:
- AI-103T00 es-ES: `00-agenda-y-contexto\courseware-AI-103T00\es-ES-slides\` (versión en inglés en `en-US-slides\`; guía del instructor en PDF/TXT; outline de slides en `OUTLINE_slides_AI-103T00.md`).
- Decks SharePoint (VBD "Building AI Apps & Agents", GenAIOps, Governance…): `01-dia1-fundamentos\ip-sharepoint\`, `02-dia2-L200-agentes\ip-sharepoint\`, `03-dia3-L300-produccion\ip-sharepoint\`.
- Repos: `repos\<internal|publico-workshops|publico-samples|publico-cursos|microsoftlearning-labs>\<repo>\`.
- Documentación oficial offline (Markdown de Microsoft Learn): `docs-oficiales\<foundry|agent-framework|azure-ai-search|architecture-center-ai|ai-services-*>\` (cada carpeta tiene `_INDEX.md`).
- Inventario de todos los decks con títulos de slides: `DECKS_INVENTORY.md`.

---

## 1. Día 1 – L100: Fundamentos de Foundry y servicios de IA

| Módulo (min) | Slides | Lab / demo | Docs oficiales | Repos / samples | Estado |
|---|---|---|---|---|---|
| **Contexto y fundamentos** (25) · Valentina | AI-103 deck 01 (es-ES) slides 1–10: cargas de trabajo IA, Foundry, Foundry Tools, SDKs, IA responsable · `01-dia1…\ip-sharepoint\Introduction to Microsoft Foundry.pptx` (25 sl.) · `Solution Optimization for Microsoft Foundry Lifecycle.pptx` (contexto de ciclo de vida) | — (demo del portal) | `docs-oficiales\foundry\what-is-foundry.md`, `concepts\capabilities.md`, `concepts\capability-reference.md` | `repos\internal\GenAI-Use-Case-Building-Blocks` (iconografía y diagramas AIS/Agent Service) | 🟢 |
| **Plataforma Foundry** (35) · Pablo | AI-103 deck 01 slides 11–26: catálogo de modelos, benchmarks, deployments, evaluación, SDK, Responses vs ChatCompletions · `WorkshopPLUS - Azure AI Provisioned (PTU).pptx` · `WorkshopPLUS - Model Catalog.pptx` (🔒 ver §6) | `mslearn-ai-studio` ejercicios 01 *Explore*, 02 *Model catalog evaluation*, 03 *Foundry SDK*, 06 *Content filters* · WPLUS `Lab 00` y `Lab 01 - AI-Foundry` | `foundry\foundry-models\` (incl. `concepts\deployment-types.md`, `quotas-limits.md`), `foundry\concepts\foundry-models-overview.md`, `foundry\how-to\quota.md`, `foundry\how-to\develop\sdk-overview.md`, `foundry\openai\provisioned-quickstart.md` | `repos\publico-samples\foundry-samples\samples\python\quickstart`, `…\foundry-models` · `repos\publico-samples\azureai-samples` | 🟢 |
| **Azure AI Services** (30) · *sin asignar* | AI-103 deck 03 (Language, Speech, Voice Live, Traducción) y deck 04 (Visión, generación imagen/video, Content Understanding, Knowledge Mining) | `mslearn-ai-information-extraction` 01–03 (Content Understanding + **Document Intelligence**) · `mslearn-ai-document-intelligence` · `mslearn-ai-language` 01–07 · `mslearn-ai-vision` 01–04 | `docs-oficiales\ai-services-document-intelligence\`, `…content-understanding\`, `…speech-service\`, `…language-service\`, `…computer-vision\` | `document-intelligence-code-samples` (Python v4) · `azure-ai-document-processing-samples` · `azure-ai-content-understanding-python` · `content-processing-solution-accelerator` · `cognitive-services-speech-sdk\samples` (avatar js/python/csharp) · `agentic-ai-lab` (`content-understanding`, `ai-language`, `ai-vision`) | 🟢 (Document Intelligence no tiene slides propios en AI-103: usar labs y samples) |
| **Agentes y conocimiento** (40) · compartido | AI-103 deck 02 slides 4–30: agentes en Foundry+VS Code, tools personalizadas, MCP, Foundry IQ · `Building Agents Based App.pptx` (55 sl.) · `Knowledge Retrieval - RAG for enterprise agents with Azure AI Search.pptx` (34) · `Building RAG apps.pptx` (80) | `mslearn-ai-agents` A1 *Create and ground an agent*, A2 *Remote MCP* · `mslearn-agent-quickstart` | `foundry\agents\` (overview, quickstarts, conceptos), `foundry\agents\concepts\toolbox-overview.md`, `agents\concepts\what-is-foundry-iq.md`, `agents\how-to\foundry-iq-connect.md`, `azure-ai-search\` | `foundry-samples\samples\python\quickstart\create-agent` y `chat-with-agent` · `get-started-with-ai-agents` | 🟢 |
| **Lab guiado** (75) — *"Del catálogo de modelos a una experiencia de agente"* | — | Propuesta de armado (3 bloques cronometrados): **(a)** primer agente: `mslearn-agent-quickstart` + `mslearn-ai-agents` A0–A1 · **(b)** OCR: `mslearn-ai-information-extraction` 03 (Document Intelligence) o `mslearn-ai-document-intelligence` · **(c)** voz/avatar como *demo*: avatar samples de `cognitive-services-speech-sdk` + `mslearn-ai-language` 06 *Voice Live* | — | `agentic-ai-lab` (módulos listos con infra Bicep: `agents`, `content-understanding`, `ai-language`, `chat-rag`) · `ai-foundry-workshop\1-introduction` | 🟡 75 min es poco para los 3 bloques: dejar (c) como demo |

---

## 2. Día 2 – L200: Desarrollo de agentes y RAG con Azure AI Search

| Módulo (min) | Slides | Lab / demo | Docs oficiales | Repos / samples | Estado |
|---|---|---|---|---|---|
| **Arquitectura y runtime** (40) · Pablo | AI-103 deck 02 slides 42–47 (Agent Framework) · `Microsoft Agent Framework.pptx` (89 sl.) · `MAF-Python\PythonAgents-BuildingFirstAgent.pptx` (50) · `Building Agents Based App.pptx` | `mslearn-ai-agents` A6 *Promote your assistant to a hosted agent* | `docs-oficiales\agent-framework\` (183 págs.), `foundry\agents\concepts\hosted-agents.md`, `hosted-agent-contract.md`, `foundry\agents\how-to\deploy-hosted-agent-production.md`, `deploy-hosted-agent-code.md` | `agent-framework\python\samples\01-get-started`, `04-hosting` · `foundry-samples\samples\python\hosted-agents\agent-framework` · `foundry-hosted-agentframework-demos` · `Hosted_Agents_Workshop_dotNET` (si se elige .NET) | 🟢 |
| **Tools e integración** (40) · dividido | AI-103 deck 02 slides 13–22 (tools custom, MCP) · `Extending AI Agents with Azure Functions - Hackathon 2025.pptx` | `mslearn-ai-agents` A2 *Remote MCP*, A4 *Custom function tools*, A5 *Capstone: build your own MCP server* | `foundry\agents\how-to\tools\`, `foundry\mcp\` | `repos\internal\mcp-workshop` (cliente/servidor MCP, Entra ID, ai-foundry/agent_uses_mcp.py) · `mcp-for-beginners` (00–03, 05, 08) · `AI-Gateway\labs\model-context-protocol`, `mcp-from-api` · `remote-mcp-apim-functions-python` | 🟢 |
| **RAG y Azure AI Search** (45) · Pablo | `Building RAG apps.pptx` (80) · `Knowledge Retrieval…Azure AI Search.pptx` (34) · `Agentic RAG build a reasoning retrieval engine…pptx` (61) · `AgenticRAGWithReflection.pptx` (43) · `Advanced Retrieval Augmented Generation (RAG).pptx` (🔒) | `AgentFactory-Labs\Lab 5_Advanced Querying with Azure AI Search` (docx + Terraform + PDFs de demo) · `Lab 6_Foundry Agentic Retrieval with Foundry IQ` (docx + notebook) · `mslearn-ai-information-extraction` 04–05 · WPLUS `Lab 08 - RAG-Patterns`, `Lab 10 - Vector-DB` | `docs-oficiales\azure-ai-search\`, `architecture-center-ai\` (guía de diseño y evaluación RAG), `foundry\` (Foundry IQ / knowledge) | `azure-search-python-samples` · `azure-search-openai-demo` (docs + backend) · `ai-rag-chat-evaluator` · `gpt-rag` · `ignite25-LAB511-agentic-knowledge-bases` · `aitour-rag-with-ai-search` | 🟢 |
| **Lab pro-code** (55) — *"Agente pro-code con grounding y herramientas"* | `MAF-Python\PythonAgents-ContextMemory`, `-HITL`, `-FirstWorkflows`, `-AdvancedWorkflows` (si se agrega aprobación humana/workflows) | Candidatos base (elegir **uno**): **A)** `foundry-hosted-agents-workshop\travel_assistant` (pasos 0→9: tools, MCP, RAG, workflows, memoria; keyless) · **B)** `repos\internal\agent-framework-workshop` (retos, Agent Framework) · **C)** `mslearn-ai-agents` C0–C4 · **D)** `Hosted_Agents_Workshop_dotNET\labs` (Lab 0–5, .NET 10) | — | `microsoft\agent-framework\python\samples\02-agents`, `03-workflows`, `05-end-to-end` | 🟡 Falta cerrar **Python vs .NET** con BCI y armar dataset ficticio + proyecto inicial recuperable |

---

## 3. Día 3 – L300: Arquitecturas avanzadas, seguridad y operación

| Módulo (min) | Slides | Lab / ejercicio | Docs oficiales | Repos / samples | Estado |
|---|---|---|---|---|---|
| **Observabilidad y ciclo de vida** (30) · Valentina | `MAF-Python\PythonAgents-MonitoringEvaluating.pptx` (41) · Production-Readiness `04-agentops\AgentOps.pptx` (30) | `mslearn-ai-agents` D1 *Trace your agent*, D2 *Evaluate answer quality* · ejercicio de trazas sobre el proyecto `dia2-lab-procode\` | `foundry\observability\`, `foundry\concepts\evaluation-overview.md`, `concepts\built-in-evaluators.md`, `agents\how-to\configure-hosted-agent-telemetry.md`, `agents\how-to\debug-hosted-agent.md` | `azure-sdk-for-python_foundry-samples\…\azure-ai-projects\samples` y `…\azure-ai-evaluation\samples` · `repos\internal\foundry-observability-playground` · `foundry-samples\samples\python\external-agents\observability` | 🟢 |
| **Protocolos y multiagente** (40) · *sin asignar* | AI-103 deck 02 slides 48–55 (orquestación concurrente, secuencial, group chat, handoff, Magentic) · Production-Readiness `03-agent-architectures\Agentic Architectures.pptx` (58) | `mslearn-ai-multi-agents` 01–04 (stateful loops, orquestación avanzada, descomposición de tareas, **A2A**) · `mslearn-ai-agents` C2, C3 (A2A) | `agent-framework\` (workflows/orquestación), `foundry\agents\how-to\enable-agent-to-agent-endpoint.md`, `agents\concepts\agent-to-agent-authentication.md`, `agents\concepts\workflow.md`, `foundry\mcp\` | `a2aproject\A2A` (docs/spec) · `AI-Gateway\labs\mcp-a2a-agents` · `multi-agent-reference-architecture` · `mcp-workshop\risks` (tool poisoning, RCE) | 🟢 |
| **Arquitectura empresarial** (35) · Valentina | `03-agent-architectures\Agentic Architectures.pptx` (identidad, token mgmt/APIM, hub vs federación, networking) · `02-ai-landing-zones\Azure AI Landing Zones.pptx` (41) · `01-frontier-coe-governance\Frontier CoE and Governance.pptx` (51) | `mslearn-ai-governance` G0–G7 (gateway, contratos de acceso, PII, hosted agent + A2A, MCP vía APIM) | `architecture-center-ai\`, `foundry\control-plane\` (overview, enforce limits, compliance/security, fleet monitoring), `foundry\agents\concepts\hosted-agent-permissions.md`, `agents\concepts\limits-quotas-regions.md` | `AI-Gateway\labs` (zero-to-production, ai-foundry-hosted-agents, token-rate-limiting, semantic-caching, session-awareness, foundry-e2e-private) · `apim-foundry-governance` · `apim-landing-zone-accelerator` · `internal\ai-gateway-evaluation` · `internal\AIGateway` · `internal\well-governed-ai-agents` · `Azure\AI-Landing-Zones` · `internal\bicep-ptn-aiml-landing-zone` | 🟢 |
| **Seguridad y gobierno** (40) · Pablo | `05-ai-security-observability\AI Security and Observability.pptx` (68) · AI-Governance-Accelerator `Module 1–3`, `3.1 Responsible AI`, `3.2 FinOps`, `3.3 Data Governance`, `Module 4` (3 decks) | `AI-Red-Teaming-Playground-Labs` · `agentic-ai-lab\ai-red-teaming-agent`, `responsible-ai` · `mslearn-ai-agents` D3 *Red team* · `mslearn-ai-multi-agents` 10 *Zero-trust*, 11 *RAI governance* · datasets de ejemplo: `03-dia3…\ip-sharepoint\RAI-sample-files` | `foundry\guardrails\`, `foundry\responsible-ai\`, `foundry\concepts\ai-red-teaming-agent.md`, `foundry\how-to\develop\run-ai-red-teaming-cloud.md`, `run-scans-ai-red-teaming-agent.md`, `agents\how-to\add-hosted-agent-guardrails.md`, `ai-services-content-safety\` | `AzureAIGovernance` · `mcp-for-beginners\02-Security` · `ai-agents-for-beginners\18-securing-ai-agents` · `PyRIT` (no descargado, ver §6) | 🟢 |
| **Workshop BCI** (65) — *Architecture Decision Workshop* | Canvas a construir con: `03-…\ip-sharepoint\Agent-Factory-Architecture-Kit\` (checklists, guía de decisión de plataforma, worksheets .xlsx/.docx, stencils 🔒) · `AI-Governance…\Module 4 AI Checklists` | Ejercicio: canal→identidad→sesión→agente→modelo→tools→datos; Hosted Agent multiplexado + Session Gateway; controles APIM/MCP; SLO, amenazas, evaluaciones; backlog priorizado | `00-agenda-y-contexto\engms-resource-center-sp4\01-ai-apps\assess-prod-*.md` (AI Production Readiness Assessment) | `Production-Readiness-Workshop\specs\` (6 specs) | 🟡 Falta definir el caso BCI priorizado y armar el canvas/ADR |

---

## 4. Entorno de laboratorio (bloqueante para los 3 días)

| Necesidad | Material disponible |
|---|---|
| Aprovisionar proyecto Foundry de entrenamiento (modelos, cuotas, AI Search, App Insights/Log Analytics, RBAC) | `repos\internal\foundry-launchpad` (Terraform/AVM, público o privado) · `foundry-samples\infrastructure\infrastructure-setup-bicep` y `…terraform` · `agentic-ai-lab\infrastructure` + `docs\infrastructure.md` · `Hosted_Agents_Workshop_dotNET\infra` · `AgentFactory-Labs\Lab 5…\scripts` (Terraform) |
| Landing zone segura (si BCI la exige) | `Azure\AI-Landing-Zones` · `internal\bicep-ptn-aiml-landing-zone` · `internal\AI-Landing-Zones-Documentation` |
| Límite de sesiones | El DRAFT indica **máx. 16 sesiones** si el ambiente lo provisiona Microsoft; sin límite si lo provisiona BCI. Con ~48 inscritos conviene ambiente del lado BCI o proyectos por equipo. |

---

## 5. Documentación oficial offline (Markdown de Learn, 2026-10-19)

| Carpeta | Páginas | Cubre |
|---|---:|---|
| `docs-oficiales\foundry\` | 450 | Foundry completo: modelos, agentes (prompt/hosted), toolbox, observabilidad, evaluación, optimización, trust & safety, gobierno |
| `docs-oficiales\agent-framework\` | 182 | Microsoft Agent Framework (agentes, workflows, orquestación, hosting) |
| `docs-oficiales\azure-ai-search\` | 60 | Agentic retrieval, vector/híbrida/semantic, knowledge bases, seguridad |
| `docs-oficiales\architecture-center-ai\` | 60 | Guías de arquitectura IA/ML, RAG, multiagente |
| `docs-oficiales\ai-services-*\` | 14 c/u | Document Intelligence, Content Understanding, Speech, Language, Vision, Content Safety |
| `00-agenda-y-contexto\engms-resource-center-sp4\` | 181 archivos | Fuente Markdown del Azure Resource Center (eng.ms) para VBDs de AI Apps y AI Platform (delivery guides, datasheets, learning paths, `so-foundry-*`, `aigov-*`, `lza-*`, `ws-agentfactory`) |

Rutas de aprendizaje de Learn del AI-103: `learn.microsoft.com/training/paths/get-started-ai-apps-agents/`, `develop-generative-ai-apps-azure/`, `develop-ai-agents-azure/` y `learn.microsoft.com/training/courses/ai-103t00`.

---

## 6. Gaps, bloqueos y decisiones pendientes

**Material con acceso limitado**
1. 🔒 **Archivos cifrados por etiqueta de sensibilidad (MIP):** 22 archivos (decks, labs .docx, plantillas .xlsx) bajaron cifrados y solo abren en Office con tus credenciales; no los puedo leer desde acá. Lista completa con rutas locales y origen en `ENCRYPTED_FILES.md`. Los críticos: `Workshop_GenAIOPs.pptx` (GenAIOps), `WorkshopPLUS - Model Catalog.pptx`, `Advanced Retrieval Augmented Generation (RAG).pptx`, los labs 5 y 6 de Agent Factory y el kit de arquitectura para el workshop del viernes.
2. **microsoft/Foundry-Models-Accelerator** (el que compartiste con Valentina): no es accesible con la cuenta EMU ni de forma anónima. Requiere autorizar SSO de la org `microsoft` para tu cuenta `pablobraconi`. No es crítico para BCI.
3. **Courseware AI-103T00 (LDC)**: la distribución está restringida a MCT/MTT; usarlo como fuente, no reenviar los archivos.

**Material no descargado (por tamaño) — disponible bajo demanda en SharePoint `ASDIPRelease/AzureCloudAI/SP2 VBD/…`**
- WorkshopPLUS AI Platform & Services: *AI Agent Service L100/L300* (~139 MB c/u, de 2025), *Microsoft Foundry* (111–123 MB), *GenAI Security* (80 MB), *Model Management* (125 MB), *GraphRag* (41 MB), *VectorDatabases* (62 MB), *Responsible AI* (277 MB), *Content Understanding* (536 MB), *Speech* (522 MB), *Language* (127 MB).
- VBD "Building AI Apps & Agents": *Integrating Open AI in your app* (154 MB), *MCP + Azure AI Foundry* (339 MB), *Azure AI Agents – Debugged L300* (318 MB), *L300 Pitch Decks*.
- AI Governance Accelerator: módulo 3.5 *Zero Trust for Agents* (230 MB) y 3.6 *Compliance* (500 MB) + videos.
- Videos (.mp4) de Production-Readiness y de los módulos de gobierno.
- Repos grandes omitidos: `microsoft/RAG_Hack` (447 MB de slides, 2024), `PyRIT` (461 MB; se puede bajar solo `doc/` si hace falta), `content-processing-solution-accelerator` (solo `docs/`), `ai-agents-for-beginners` y `mcp-for-beginners` (solo lecciones relevantes, sin traducciones).
- `MicrosoftDocs/azure-ai-docs`: repo privado; se reemplazó por la conversión HTML→Markdown de las páginas de Learn.

**Decisiones abiertas**
- Reparto de módulos sin dueño: *Azure AI Services* (mié), *Protocolos y multiagente* (vie) y los cierres de cada día.
- **Lenguaje del lab L200:** Python (AI-103, mslearn-ai-agents, travel_assistant) vs .NET (`Hosted_Agents_Workshop_dotNET`). Hay perfiles BCI con LangGraph/LangChain (Jonathan Ramírez): `foundry-samples\…\hosted-agents\langgraph` está incluido.
- **Caso BCI** para el Architecture Decision Workshop del viernes y dataset ficticio sin información bancaria real.
- **Preview features** (tracing, evals, monitoring, agentic retrieval): validar por región/modelo/SDK y preparar demos de respaldo.
- **Quién monitorea Teams** mientras el otro presenta.
- Los labs de eng.ms/VBD asumen 2 días × 8 h; BCI son 3 × 4 h: hay que recortar labs (ver notas en cada módulo).

---

## 7. Próximos pasos sugeridos
1. Confirmar con Valentina/Robert: reparto, lenguaje del lab L200 y caso BCI.
2. Validar entorno (Foundry + cuotas + AI Search + App Insights) con el admin de BCI usando `foundry-launchpad`/`foundry-samples\infrastructure`.
3. Armar primero **Día 1** (más inminente): deck base desde AI-103 es-ES 01/03/04 + `Introduction to Microsoft Foundry`, y lab desde `mslearn-agent-quickstart` + `mslearn-ai-information-extraction`.
4. Luego **Día 2** (deck desde `Microsoft Agent Framework` + `Building Agents Based App` + RAG; lab elegido) y **Día 3** (decks de Production-Readiness + canvas BCI).

