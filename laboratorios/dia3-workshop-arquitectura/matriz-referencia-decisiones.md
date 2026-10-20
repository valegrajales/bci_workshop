# Matriz de referencia de decisiones (Día 3 · Workshop BCI)

*Material de apoyo para facilitadores y grupos. Resume criterios para decisiones frecuentes al diseñar agentes en Microsoft Foundry; sirve para el paso 2 (Canvas) y para redactar los ADR. No es prescriptivo: cada fila indica un punto de partida y las señales que justifican cambiarlo. Las funciones en preview están marcadas y su estado puede cambiar; confirma en la documentación antes de decidir.*

## 1. Resumen en una página

| # | Decisión | Punto de partida razonable | Cambia a otra opción cuando… |
|---|---|---|---|
| 1 | Nivel de complejidad | Un agente con tools | Necesitas fronteras de seguridad distintas, dominios claramente separados o especialización paralela |
| 2 | Tipo de agente | Prompt agent | Necesitas tu propio código, control de cómputo, estado en archivos o protocolos propios (hosted agent) |
| 3 | Sesiones y usuarios | Una sesión por usuario | El pico de conversaciones abiertas se acerca al límite regional: capa intermedia que multiplexa |
| 4 | Acceso a sistemas | Tools publicadas vía Toolbox/MCP | El sistema ya tiene una API estable y un solo consumidor: llamada directa con una tool OpenAPI |
| 5 | Identidad frente al backend | Identidad del agente (Entra) | El backend debe aplicar permisos del usuario: OBO u OAuth identity passthrough |
| 6 | Coordinar agentes | Agente como tool dentro del mismo código | Otro equipo o runtime es dueño del agente remoto: A2A |
| 7 | Dónde aplicar políticas | Guardrails del agente + RBAC | Necesitas control uniforme entre equipos o proveedores: gateway/Control Plane (preview) |
| 8 | Memoria y estado | Historial administrado por la plataforma | Necesitas recordar entre sesiones (memoria, preview) o estado propio duradero (state store, preview, o tu base de datos) |
| 9 | Caché semántica | Desactivada | Hay consultas repetitivas sin datos por cliente y mediste el riesgo de respuesta cruzada |
| 10 | Acceso al modelo | Despliegue de modelo en Foundry | Necesitas un modelo detrás de tu propio gateway (BYOM): validar el alcance actual |
| 11 | Aprobación humana | Siempre en acciones con efecto | Solo lectura o acciones reversibles de bajo impacto con control compensatorio |
| 12 | Red | Decidir al crear la cuenta Foundry | Requisito de aislamiento: red privada desde el inicio (no se agrega después) |

## 2. Criterios por decisión

### 2.1 Nivel de complejidad: ¿un agente o varios?
- **Elige un agente con tools** si el caso es de un solo dominio y las solicitudes varían en qué herramientas necesitan; la guía de patrones lo describe como un buen punto de partida empresarial: usa el nivel más bajo de complejidad que cumpla el requisito.
- **Elige orquestador + especialistas** si hay dominios con datos o permisos distintos (por ejemplo, tesorería y comex), si quieres probar y evaluar cada especialista por separado o si necesitas fronteras de seguridad independientes.
- **Costo del cambio:** más agentes suman latencia, costo de tokens y puntos de falla; mide primero con un agente y divide cuando una métrica lo justifique.
- **PoC sugerido:** mismo golden set contra ambas variantes; compara calidad, p95 y costo por conversación.
- Fuente: `architecture-center-ai\ai-ml\guide\ai-agent-design-patterns.md`.

### 2.2 Prompt agent frente a hosted agent
- **Hosted agent** si necesitas traer tu código y framework, protocolos propios, controlar CPU/memoria del sandbox, persistir archivos y estado entre turnos, o trabajo de larga duración resiliente.
- **Prompt agent** si el agente se define con instrucciones y configuración de tools sin código propio; menos operación, menos control.
- El protocolo de un hosted agent se elige según el cliente: Responses (chat; la plataforma administra historial y streaming), Invocations (webhooks, lotes, payloads propios), Invocations WebSocket (voz o streaming bidireccional) y Activity (al publicar en Teams/Microsoft 365). Un agente puede exponer más de un protocolo.
- Fuente: `foundry\agents\concepts\hosted-agents.md`.

### 2.3 Sesión por usuario o sesiones multiplexadas
- **Una sesión por usuario (predeterminado)** mientras el pico de sesiones con cómputo activo esté cómodamente bajo el límite regional (predeterminado: 1.000 por suscripción y región; superarlo devuelve 429 `session_quota_exceeded`).
- **Multiplexar** con una capa intermedia (en el workshop: *Session Gateway*) cuando muchos usuarios deban compartir un conjunto acotado de sesiones. La plataforma aísla el historial de conversación por usuario; tú administras el mapeo usuario→sesión y la partición de los datos que guarde tu contenedor.
- **Requisitos:** permiso `UserIdentityImpersonation` (rol personalizado) para la identidad de la capa intermedia y el encabezado `x-ms-user-identity` fijado desde un contexto validado.
- **Estrategias de asignación:** sticky/menor carga, hash, round-robin, por grupo; elige según si necesitas mantener juntos los turnos de un usuario.
- **Alternativas al multiplexado:** bajar el idle timeout (2–60 min), liberar sesiones que no necesitan cómputo, o solicitar un aumento de límite por soporte indicando suscripción, región y concurrencia esperada.
- **Validar siempre:** prueba A-A-B (dos usuarios en la misma sesión, uno intenta ver al otro) y ensayo de carga.
- Fuentes: `foundry\agents\how-to\multiplex-session-users.md`, `foundry\agents\how-to\isolate-sessions-per-user.md`, `foundry\agents\concepts\limits-quotas-regions.md`.

### 2.4 MCP, Toolbox o llamada directa a la API
- **MCP server** cuando varias aplicaciones o agentes consumirán las mismas operaciones, quieres un contrato estándar de tools y un lugar para aplicar autenticación, validación y límites.
- **Toolbox (GA)** cuando quieres definir un conjunto curado de tools una vez, reutilizarlo entre agentes y runtimes, y centralizar credenciales, versiones y políticas detrás de un endpoint MCP administrado.
- **Llamada directa (tool OpenAPI o código)** cuando hay un solo consumidor, la API ya es estable y no necesitas reutilización; menos piezas, pero tú asumes autenticación y gobierno por agente.
- **En cualquier caso:** trata la salida de la tool como entrada no confiable, valida esquema, restringe operaciones y exige aprobación para acciones con efecto.
- Fuentes: `foundry\agents\concepts\toolbox-overview.md`, `foundry\agents\concepts\tool-best-practice.md`, `foundry\agents\how-to\tools\model-context-protocol.md`.

### 2.5 Identidad del agente, OBO o passthrough
| Necesidad | Opción | Nota |
|---|---|---|
| Todos los usuarios con el mismo nivel de acceso al backend | Identidad compartida (Entra del agente o de proyecto; también clave si no hay alternativa) | Más simple; el backend no distingue al usuario |
| Preservar identidad y permisos de cada usuario | OAuth identity passthrough (MCP y A2A) | El contexto de usuario persiste entre interacciones |
| Backend propio que debe aplicar permisos del usuario | OBO implementado por tu aplicación | La plataforma no lo hace por ti; define dónde vive el token |
- Evita claves siempre que exista alternativa; quien tiene acceso al proyecto puede usar las conexiones con clave.
- Fuentes: `foundry\agents\how-to\mcp-authentication.md`, `foundry\agents\concepts\agent-to-agent-authentication.md`, `foundry\agents\how-to\use-on-behalf-of-flow.md`.

### 2.6 A2A, MCP o agente como tool
- **Agente como tool en el mismo código/runtime** si el mismo equipo lo construye y despliega; mínima latencia y operación.
- **A2A** si el agente remoto es de otro equipo o runtime, tiene su propio ciclo de vida y se integra mediante un protocolo estándar. La herramienta `a2a` es GA (protocolo 1.0); `a2a_preview` (0.3) sigue en preview. Para Foundry como destino: solo modalidad de texto y sin streaming.
- **MCP** si lo que expones son operaciones o datos (tools), no razonamiento autónomo.
- **Evalúa** cómo se propaga la identidad del usuario en cada salto y qué agentes puede invocar el tuyo.
- Fuentes: `foundry\agents\how-to\tools\agent-to-agent.md`, `foundry\agents\concepts\agent-to-agent-authentication.md`.

### 2.7 Dónde aplicar políticas: guardrails, gateway o Control Plane
- **Guardrails de Foundry en el agente** para contenido y ataques (cuatro puntos de intervención). El guardrail del agente reemplaza por completo al del modelo; los controles de tool call y tool response son (preview) y aplican solo a las tools soportadas, así que para MCP necesitas controles compensatorios.
- **APIM/AI Gateway** para tráfico del cliente al agente o del agente al modelo: autenticación, límites de tokens, enrutamiento, registro y políticas que no quieres delegar en cada equipo. La gobernanza de tools con AI Gateway y la administración de AI Gateway en Foundry están en (preview).
- **Control Plane (preview)** para inventario, cumplimiento y límites por proyecto.
- **Regla práctica:** controles que dependen del contenido, en guardrails; controles de identidad, cuota y enrutamiento, en el gateway; no dependas de una sola capa.
- Fuentes: `foundry\guardrails\guardrails-overview.md`, `foundry\guardrails\intervention-points.md`, `architecture-center-ai\ai-ml\guide\generative-ai-gateway.md`, `foundry\control-plane\overview.md`.

### 2.8 Memoria y estado
- **Historial de conversación:** administrado por la plataforma con el protocolo Responses; suficiente para la mayoría de v1.
- **Memoria de largo plazo (preview):** solo si el caso lo exige (preferencias o contexto entre sesiones); define alcance por usuario y borrado; límites documentados: 100 scopes por store, 10.000 memorias por scope.
- **Durable state store (preview):** estado clave-valor JSON para checkpoints o historial administrado por tu aplicación, disponible para hosted agents.
- **Tu propia base de datos:** cuando el estado es parte del sistema de registro o debe cumplir retención y respaldo propios; AI Search es para retrieval, no tu fuente de verdad.
- Fuentes: `foundry\agents\concepts\what-is-memory.md`, `foundry\agents\concepts\agent-state-store.md`.

### 2.9 Caché semántica
- **Sí** para preguntas repetitivas y no personalizadas (por ejemplo, definiciones normativas públicas) y cuando medirás tasa de aciertos.
- **No** para respuestas que dependen del cliente, el saldo o la identidad del usuario; una clave de caché mal acotada puede servir la respuesta de un cliente a otro.
- **Validar:** umbral de similitud, alcance de la clave (por usuario/segmento), expiración y pruebas de respuesta cruzada. Referencia práctica: laboratorio `semantic-caching` del repositorio público AI-Gateway.
- Fuentes: `architecture-center-ai\ai-ml\guide\generative-ai-gateway.md`, `repos\publico-samples\AI-Gateway\labs\semantic-caching`.

### 2.10 Modelo directo o detrás de un gateway
- **Despliegue de modelo en Foundry** como punto de partida; límites de tokens por proyecto con Control Plane (preview).
- **Modelo detrás de tu gateway (BYOM):** la documentación de integración de AI Gateway indica que solo los prompt agents lo soportan hoy; si tu patrón es hosted agent, valida en un PoC cómo se enrutan las llamadas al modelo antes de basar la arquitectura en ello.
- Fuente: `foundry\agents\how-to\ai-gateway.md`.

### 2.11 Aprobación humana
- **Exigirla** en toda acción que cambie estado, mueva dinero o envíe información fuera de la entidad; la aprobación puede ser durable (esperar minutos, horas o días y sobrevivir reinicios).
- **Relajarla** solo en lectura o acciones reversibles de bajo impacto, con límites, auditoría y revisión periódica.
- Fuente: `foundry\agents\how-to\add-human-in-the-loop.md`.

### 2.12 Red
- La configuración de red privada (network injection) se define al crear la cuenta Foundry y no puede agregarse después a una cuenta existente; surte efecto al crear el primer hosted agent y no puede cambiarse luego. Planifícala antes del primer despliegue.
- Las trazas y los agentes de workflow no soportan por completo el aislamiento de red; Tracing en VNet es (preview). Revisa el estado actual antes de comprometer un diseño totalmente privado.
- Fuentes: `foundry\agents\concepts\networking-options.md`, `foundry\concepts\general-availability.md`.

## 3. Cómo usar esta matriz en el workshop

- En el **paso 2 (Canvas)**, cada fila de la columna *Criterio* puede apoyarse en una de estas decisiones; si el grupo no tiene criterio, la decisión pasa a *Estado ADR = Por redactar* y al backlog como PoC.
- En el **paso 4 (SLOs y evaluación)**, las decisiones 3, 9 y 10 generan métricas concretas (sesiones activas, tasa de aciertos de caché, latencia del modelo).
- Cuando una opción cambie por una función en preview, registra la excepción y el plan de salida en el ADR.
