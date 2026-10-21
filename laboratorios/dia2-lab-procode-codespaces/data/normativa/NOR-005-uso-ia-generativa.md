---
id: NOR-005
titulo: Política de uso de IA generativa
area: Tecnología
nivel_acceso: interno
version: 1.2
vigencia: 2026-04-01
---

# Política de uso de IA generativa (Austral Bank, documento ficticio)

## Herramientas autorizadas

Solo se pueden usar herramientas de IA generativa incluidas en el catálogo aprobado por el Comité de IA. Está prohibido pegar información de clientes, datos personales, secretos comerciales o código fuente propietario en herramientas no aprobadas.

## Clasificación de datos y casos de uso

Los casos de uso se clasifican por riesgo. Riesgo bajo: redacción de borradores, resúmenes de documentos públicos y apoyo a la documentación técnica. Riesgo medio: asistentes internos que consultan normativa o procesos con datos internos. Riesgo alto: cualquier decisión que afecte a un cliente (créditos, límites, bloqueos), que siempre requiere una persona que revise y decida.

## Supervisión humana y trazabilidad

Todo agente de IA que opere con datos internos debe registrar trazas de su ejecución (consulta, herramientas invocadas y fuentes citadas) y conservarlas por 12 meses. Las respuestas de un asistente deben citar la fuente interna usada. Los prompts y respuestas con datos personales no se guardan en las trazas de producción.

## Evaluación previa a producción

Antes de pasar a producción, un asistente debe superar una evaluación de calidad (fundamentación, relevancia y seguridad) con un conjunto de preguntas de prueba aprobado por el área dueña del proceso. El resultado se adjunta a la solicitud de paso a producción.
