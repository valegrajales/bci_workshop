# Resultados: evaluación de groundedness

Evaluación `eval_e1003e6f244a4542b6b9dbffa50d9e9e` en el proyecto `bci-workshop` (Foundry), dataset `normativa-groundedness-eval` v1 (v2 solo corrige el texto de `ground_truth` de q01; las preguntas y el scoring son idénticos, y `ground_truth` no interviene en groundedness) (16 preguntas: 11 de incidentes/KYC/crédito/continuidad/etc., 4 de viajes y gastos como control y 1 fuera de corpus). Evaluador `builtin.groundedness` (escala 1-5, umbral 3), modelo juez `gpt-6.1-sol`. Los agentes se evaluaron como target (`azure_ai_agent`) sin modificarlos.

| Agente | Aprobadas (score ≥ 3) | No evaluables (sin evidencia recuperada) | Score promedio de las evaluables |
|---|---|---|---|
| `normativa-falla` | 5 / 16 (31 %) | 11 / 16 | 5,0 |
| `normativa-corregido` | 16 / 16 (100 %) | 0 / 16 | 5,0 |

## Cómo leerlo

- El evaluador marca "Not applicable" cuando la respuesta no trae resultados de herramienta: no hay contexto contra el cual verificar. En `normativa-falla` eso ocurre en las 11 preguntas de incidentes, KYC, crédito, etc., porque sus instrucciones le dicen que la base solo trata viajes y gastos y **no llama a la tool**; responde de forma genérica, sin respaldo en la normativa.
- En 5 preguntas (q12-q15 de viajes/gastos y q10 de regalos) `falla` sí llama a la tool y obtiene 5/5, igual que `corregido`. Ambos agentes usan el mismo modelo y la misma tool; solo cambian las instrucciones.
- "No evaluable" no equivale a "falso": significa que no hay evidencia recuperada contra la cual verificar. Por eso la tasa aprobadas/total combina cobertura de recuperación y groundedness; se declara así a propósito, porque es justamente lo que falla el agente defectuoso.
- Groundedness no mide corrección: que la respuesta esté respaldada por la evidencia no prueba que coincida con `ground_truth` (campo incluido en el dataset para una evaluación posterior, p. ej. `builtin.response_completeness`).
- El dataset (16 filas) está diseñado a propósito para exponer la falla: sirve para la demo, no para generalizar.
- `normativa-corregido` siempre consulta la base de conocimiento, cita la norma y en la pregunta fuera de corpus (q16) declara que no hay información, y se considera fundamentada.
- Métrica de la demo: **tasa de respuestas fundamentadas = aprobadas / total** (31 % vs 100 %). El promedio de score solo sobre las evaluables no discrimina, porque ambos agentes obtienen 5,0 cuando hay evidencia.

## Cómo reproducir

```powershell
az login
cd 03-dia3-L300-produccion\demo-agente-falla-trazas\evaluacion
python evaluar-groundedness.py
```

Ver resultados en el portal: Foundry → proyecto `bci-workshop` → **Build → Evaluations** → `normativa-groundedness` → comparar los dos runs.
