# Auto-asignación de laboratorio vía Form + Power Automate + SharePoint

> **Decisiones tomadas (20/21-oct-2026):**
> 1. TAP: opción **A** — se regenera cada mañana con `Provision-Lab.ps1 -SoloTap` y se refresca la Lista **antes** de abrir el Form ese día (no generación en tiempo real desde el flujo).
> 2. Fuente de verdad: **Lista de SharePoint** (no Excel) para evitar condiciones de carrera con 58→34 participantes enviando el Form casi al mismo tiempo.
> 3. Forms con respuesta anónima/externa: **confirmado habilitado** en el tenant.
> 4. TAP + usuario se envían **en texto plano** por correo (se acepta el riesgo acotado; el TAP expira en 8 h).

Dato clave verificado: las cuentas `labNN`/`instNN` **no tienen buzón** (no se les puede enviar correo a ellas mismas). El correo con las credenciales va a la dirección **externa** que el participante escribe en el Form.

No pude crear la Lista/Form/Flow de forma automática: el token de `az rest` usado en esta sesión solo tiene permisos de lectura en Graph para este tenant (no `Sites.Manage.All`). Todo lo de abajo se hace manualmente en el navegador, con el tenant `mngenvmcap219366.onmicrosoft.com` activo (no el de Microsoft corp).

## 1. Dataset listo para importar

Archivo ya generado con los TAP vigentes de **hoy** (21-oct, válidos hasta ~14:30 hora Chile):

```
C:\Users\pabracon\bci-lab-secrets\BCI-Lab-Asignaciones-Dia1.csv
```

34 filas (`lab01`–`lab30` + `inst01`–`inst04`), columnas:

| Columna | Tipo | Contenido inicial |
|---|---|---|
| `LabNumero` | Texto | `lab01`, `inst01`, etc. |
| `AccountUPN` | Texto | `lab01@mngenvmcap219366.onmicrosoft.com` |
| `Asignado` | Sí/No | `FALSE` para todas |
| `ParticipanteEmail` | Texto | vacío |
| `FechaAsignacion` | Fecha y hora | vacío |
| `TAPDia1` | Texto | TAP vigente de hoy |
| `TAPDia2` | Texto | vacío (se completa mañana) |
| `TAPDia3` | Texto | vacío (se completa pasado mañana) |

**No subas este CSV a SharePoint tal cual** (tiene TAPs reales). Dos formas de pasarlo a una Lista sin exponerlo en la nube de forma innecesaria:
- Abrir SharePoint → **New → List → From Excel/CSV** y subir este archivo directamente (SharePoint lo consume y lo descarta del disco local; el archivo fuente queda en tu equipo). O
- Crear la Lista vacía con el esquema de la tabla de arriba y pegar los datos desde Excel (abrir el CSV localmente, copiar, pegar en la vista de cuadrícula de la Lista).

## 2. Microsoft Form

1. `forms.office.com` (sesión en el tenant del lab) → **New Form** → nombre: `BCI Foundry Training Day — Registro de laboratorio`.
2. Un solo campo obligatorio: **"Tu correo electrónico"** (tipo texto, validación de formato email si el campo de Forms lo permite, o añade una nota pidiendo que lo revisen antes de enviar).
3. **Settings (⚙️) → Who can fill out this form → "Anyone"** (respuesta anónima/externa). Si no aparece esa opción, es el ajuste de tenant que se confirmó habilitado — revisar en Forms Settings si no se refleja.
4. **Settings → Response receipts**: desactivar (no tiene sentido para externos) y **"Record name"**: desactivado (no pedimos login).
5. Copia el enlace del Form para compartirlo con los participantes.

## 3. Lista de SharePoint "BCI-Lab-Asignaciones"

Esquema ya definido en la sección 1. Importa el CSV filtrado (sin TAPs reales si quieres repasar el esquema antes) o pega los datos reales directamente.

## 4. Flujo de Power Automate — Día 1 (asignación)

**Trigger:** Microsoft Forms → *When a new response is submitted* (selecciona el Form del paso 2).
**Importante:** en la configuración del trigger (⋯ → Settings) activa **Concurrency Control = 1** (evita que dos respuestas casi simultáneas asignen el mismo lab).

| Paso | Acción | Detalle |
|---|---|---|
| 1 | Forms: *Get response details* | Form Id + Response Id del trigger |
| 2 | SharePoint: *Get items* | Lista `BCI-Lab-Asignaciones`; filtro OData: `Asignado eq 'FALSE'`; Top Count: `1` |
| 3 | Condition | `length(body('Get_items')?['value'])` es mayor que `0` |
| 3a | **Si sí** → SharePoint: *Update item* | Id = `first(body('Get_items')?['value'])?['ID']`; `Asignado` = `TRUE`; `ParticipanteEmail` = email de la respuesta del Form; `FechaAsignacion` = `utcNow()` |
| 3b | → Outlook: *Send an email (V2)* | Para: email del Form; Asunto: `BCI Foundry Training Day — Tu acceso al laboratorio (Día 1)`; Cuerpo: incluir `AccountUPN` y `TAPDia1` de la fila asignada (del paso 2, `first(...)`), instrucciones de inicio de sesión ("Use a Temporary Access Pass instead"), horario de vigencia del TAP, y enlace al proyecto |
| 3c | **Si no** (sin cupos) → Outlook: *Send an email (V2)* | Mensaje de lista de espera / contactar al equipo facilitador |

## 5. Flujo (o acción manual) — Días 2 y 3

Cada mañana del evento, **antes** de que empiece el bloque del día:

1. Ejecutar `Provision-Lab.ps1 -SoloTap` (regenera los TAP de todas las cuentas; ya es la rutina diaria conocida).
2. Actualizar la Lista: pegar los nuevos TAP en `TAPDia2` (día 2) o `TAPDia3` (día 3) para las filas con `Asignado = TRUE`.
3. Correr un segundo flujo (manual o programado a una hora fija, p. ej. 08:00) que:
   - SharePoint: *Get items* con filtro `Asignado eq 'TRUE'`.
   - *Apply to each* fila → Outlook: *Send an email (V2)* a `ParticipanteEmail` con el `AccountUPN` + el TAP del día correspondiente (`TAPDia2` o `TAPDia3`).

Esto evita re-ejecutar el Form: el participante ya quedó vinculado a su `labNN` el día 1, y solo recibe el TAP renovado los días siguientes.

## 6. Qué NO hacer

- No subir el CSV con TAPs reales a ningún repositorio o chat.
- No dejar el Form abierto después del cupo lleno (edita el mensaje de "sin cupos" o cierra el Form manualmente al llegar a 34 asignaciones).
- No reutilizar esta Lista/Form después del evento sin purgar los TAP (son datos sensibles aunque de corta vida).
