# Ejercicio de Observabilidad (11:05–11:35) · Guía rápida para el facilitador

**Qué es:** el módulo "Observabilidad y ciclo de vida" del Día 3 (30 min, justo antes de este workshop).
Valentina presenta en 10-12 min la teoría de trazas, qué registrar (y qué nunca registrar) y el ciclo de
vida de un hosted agent; el resto del tiempo (≈18-20 min) los participantes hacen el ejercicio práctico de
abajo. Este módulo reemplaza en el horario al antiguo "GenAIOps" y retoma el contenido que antes era la
**Tarea 4** del laboratorio pro-code del Día 2 (se movió de día, no de proyecto).

## Cómo retomar el entorno

Los participantes abren de nuevo su carpeta `..\dia2-lab-procode\` — es el **mismo proyecto de ayer**: mismo
agente, mismo índice `normativa-austral`, mismo `.env`. Recuérdales que el TAP (token de acceso) del lab se
regenera a diario, pero el proyecto y los recursos de Azure (Foundry, Search, Application Insights) persisten
los 3 días, así que no hace falta reconstruir nada — si el `.env` quedó intacto, basta con activar el venv y
seguir.

Si alguien perdió su `.env` o el TAP no sirve, usa el mismo Plan B que el Día 2 (ver abajo).

## Comandos a ejecutar

Desde `..\dia2-lab-procode\` con el venv activo:

```powershell
python src\05_trazas.py
python src\05_caso_fallido.py --caso 1
python src\05_caso_fallido.py --caso 2   # si sobra tiempo
```

- `05_trazas.py` activa las trazas y corre 3 casos de referencia (deja Trace IDs impresos para abrir en el
  portal de Foundry o en Application Insights).
- `05_caso_fallido.py --caso 1` es el ejercicio principal: un agente que **no pasa el checklist**; el
  participante diagnostica mirando solo la traza (sin abrir el código del caso).
- `--caso 2` es una variante opcional para quien termine antes.

Apóyate en el checklist de éxito que antes vivía en la "Tarea 4" del README del Día 2 (ahora en su
**Apéndice — Ejercicio de trazas y diagnóstico**, pasos 1 a 4 de `..\dia2-lab-procode\README.md`):

- [ ] **Responde:** da el dato correcto en español.
- [ ] **Cita fuente:** incluye un id de fragmento válido `[NOR-xxx-xx]`.
- [ ] **Usa la tool:** llama a la herramienta correcta para cada tipo de pregunta.
- [ ] **Sin errores en la traza:** ninguna herramienta devolvió error y no hay spans con excepción.
- [ ] Sé cómo encontrar una traza por su Trace ID.

## Guía confidencial de los defectos plantados

Los dos defectos plantados (filtro de seguridad demasiado estricto y descripción de herramienta vaga), cómo
se ven en la traza, y los diffs de corrección están en
`..\dia2-lab-procode\instructores\README.md` (**no distribuir a participantes**). Úsala para dar pistas
escalonadas si un equipo se atasca más de 3 minutos.

## Plan B si algo falla

Reutiliza las mismas ideas de Plan B del laboratorio del Día 2 (`..\dia2-lab-procode\guia-facilitador.md`
§7 y `instructores\README.md`):

- `ENABLE_CONSOLE_EXPORTERS=true` en el `.env`: los spans se imprimen como JSON en la consola si el portal o
  Application Insights tardan o fallan.
- Traza pre-capturada (screenshots/JSON) del ensayo T-3 días, lista para mostrar en pantalla si la ingestión
  no llega a tiempo (puede demorar 2-5 min).
- Si un participante no tiene entorno (TAP vencido, `.env` perdido), que siga tu pantalla o trabaje en pareja
  con un vecino; un instructor lo atiende en paralelo.
