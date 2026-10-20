# Caso Austral Bank: Asistente de Tesorería para clientes corporativos

**Workshop BCI · Architecture Decision Workshop · Día 3 (12:05–12:40) · Material del participante**
*Caso 100 % ficticio. No contiene datos reales de BCI ni de ningún otro banco. Puedes adaptarlo a tu propio caso después del training.*

## 1. Contexto de negocio

Austral Bank es un banco universal ficticio. Su banca de empresas atiende a unas 3.800 empresas con tesorerías activas (multi-moneda, comercio exterior, varias cuentas y apoderados). Hoy sus tesoreros llaman al ejecutivo o navegan varios módulos del portal para saber su posición, pedir una cotización de divisas o revisar una carta de crédito. El banco quiere un **asistente conversacional de Tesorería** que reduzca esas consultas, libere al contact center y mejore la experiencia, **sin aumentar el riesgo operativo ni regulatorio**.

## 2. Alcance de la v1 (solo lectura e información indicativa)

| Capacidad | Ejemplo de pregunta | Origen de los datos (ficticio) |
|---|---|---|
| Saldos y posiciones | «¿Cuál es mi posición en USD y EUR al cierre de ayer?» | APIs de core bancario (detrás de MCP) |
| Cotización FX indicativa | «¿A cuánto está el dólar para 500 mil USD?» | Servicio de precios FX (API) |
| Estado de operaciones de comex | «¿En qué estado está mi carta de crédito 8841?» | APIs de comex (detrás de MCP) + documentos adjuntos (PDF) |
| Resumen de normativa y políticas | «¿Qué documentos exige el banco para una cobranza documentaria?» | Azure AI Search sobre políticas y manuales |

Fuera de alcance de la v1: ejecutar operaciones (transferencias, compra/venta de divisas, apertura de cartas de crédito). Es una **pregunta abierta** si una v2 podría iniciarlas.

## 3. Canales y usuarios

| Canal | Quién lo usa | Volumen estimado (supuesto) | Pista de SLA |
|---|---|---|---|
| Portal web | Tesoreros, analistas y apoderados del cliente | ~25.000 usuarios habilitados; ~6.000 activos/día | Primer texto visible p95 ≤ 3 s |
| App móvil | Apoderados y gerentes financieros | Pico de ~1.500 usuarios con conversación abierta en 15 min (09:00–12:00 y cierres de mes) | Respuesta completa con consulta a core p95 ≤ 8 s |
| Contact center | ~300 ejecutivos del banco (asistente de apoyo, el ejecutivo atiende al cliente en llamada) | ~140 simultáneos en horario punta | Respuesta ≤ 5 s (hay una persona al teléfono) |

Teams (ejecutivos internos) es opcional y queda a criterio del grupo. Disponibilidad esperada de consultas: 24/7, objetivo 99,9 % mensual (pista, no compromiso).

## 4. Activos existentes (ficticios)

- **Azure API Management (APIM)** corporativo con validación JWT y políticas básicas.
- **Azure AI Search** con ~12.000 documentos de políticas y manuales; cada documento tiene etiquetas de segmento y de acceso.
- **APIs de core bancario** (saldos, posiciones, comex) expuestas hoy detrás de **3 servidores MCP** autohospedados (Tesorería, FX, Comex), aún sin gobierno central.
- **Entra ID** para empleados del banco; un **IdP de clientes** (OIDC/OAuth2) para el portal y la app.
- **AI Landing Zone** ya desplegada (red privada, endpoints privados, Log Analytics / Application Insights) y un proyecto Foundry de pruebas. Sin agentes en producción.

## 5. Requisitos duros (no negociables)

1. **RD-1 Aislamiento:** un usuario jamás ve datos de otro cliente ni de cuentas para las que no tiene permiso.
2. **RD-2 Auditoría:** cada respuesta con datos financieros debe ser trazable (quién, qué pidió, qué fuentes y herramientas se usaron).
3. **RD-3 Sin acciones transaccionales sin control humano** (v1 es solo lectura; cualquier acción futura exige aprobación).
4. **RD-4 Residencia:** datos de clientes y trazas permanecen en la región aprobada del banco y no viajan a terceros no aprobados.
5. **RD-5 Red privada:** sin endpoints públicos hacia datos ni herramientas.
6. **RD-6 FX responsable:** toda cotización se muestra como *indicativa*, con hora y vigencia; el asistente nunca inventa tasas.
7. **RD-7 Español financiero correcto** y respuestas con fuente citada cuando provienen de políticas.
8. **RD-8 Funcionalidades en preview** solo en piloto y con excepción formal del comité de riesgo.

## 6. Preguntas abiertas (decídanlas o declaren el supuesto)

- ¿Un solo agente con herramientas o agente orquestador con especialistas (p. ej., Comex)?
- Con ~1.500 usuarios en pico, ¿sesión por usuario o sesión multiplexada? Revisen en la documentación los límites de sesiones concurrentes de los Hosted Agents y compárenlos con el pico.
- ¿Dónde vive la identidad del usuario final y cómo llega hasta la API de core? ¿Y en el contact center, el agente actúa por el ejecutivo o por el cliente?
- ¿Qué se puede cachear (preguntas normativas, cotizaciones, saldos) y qué no?
- ¿Qué pasa si el core está lento o en ventana de mantención (00:00–02:00)?
- ¿Dónde se guardan conversaciones y trazas, y quién puede leerlas? ¿Se permite memoria de largo plazo?
- ¿Cómo se mide la calidad antes y después de producción, y con qué datos?

## 7. Supuestos que puedes cambiar (decláralos en el canvas)

| Supuesto base | ¿Cambiable? | Si lo cambias, ¿qué mueve? |
|---|---|---|
| v1 solo lectura | Sí | Identidad, aprobación humana, amenazas |
| Una región Azure aprobada para todo | Sí | Disponibilidad de servicios, DR, latencia |
| ~1.500 usuarios en pico; 25.000 habilitados | Sí | Sesión, costo, cuotas |
| Core con ventana de mantención 00:00–02:00 | Sí | SLOs, degradación elegante |
| Documentos de comex llegan como PDF adjuntos | Sí | Prompt injection indirecto, Content Safety |
| Nada de lo anterior es dato real de BCI | **No** | Regla del ejercicio |

## 8. Cómo trabajar (35 min, 5 pasos)

Contexto 5 min → Canvas 10 → Amenazas 8 → SLOs y evaluación 7 → Backlog 5. Prefiere una decisión **con su criterio y su supuesto** antes que un diagrama perfecto. Plantillas: `Workshop_BCI_Plantillas.xlsx` (una hoja por paso).
