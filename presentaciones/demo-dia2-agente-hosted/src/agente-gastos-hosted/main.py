"""Agente hosted (Microsoft Agent Framework + protocolo Responses) con una function tool propia.

Demo Día 2 - "Un agente hosted con una tool propia". Escenario y datos ficticios (Austral Bank).
Local:  python main.py  (escucha en http://localhost:8088)
Foundry: el mismo código corre en contenedor como hosted agent (ver README.md).
"""
import json
import os
from typing import Annotated

from agent_framework import Agent, tool
from agent_framework.foundry import FoundryChatClient
from agent_framework_foundry_hosting import ResponsesHostServer
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
from pydantic import Field

from limites import consultar_limite

load_dotenv()

INSTRUCCIONES = (
    "Eres el asistente interno de gastos de viaje de Austral Bank (escenario ficticio). "
    "Responde siempre en español y de forma breve. "
    "Para cualquier tope de alojamiento o alimentación DEBES llamar a la herramienta "
    "consultar_limite_gastos; no respondas cifras de memoria. "
    "Si falta el ámbito (nacional o internacional) o el concepto, pregúntalo antes de llamar a la herramienta. "
    "Termina cada respuesta con la fuente que devolvió la herramienta. "
    "Si la herramienta devuelve un error, explícalo sin inventar valores. "
    "No respondas temas que no sean gastos de viaje."
)


@tool(approval_mode="never_require")
def consultar_limite_gastos(
    concepto: Annotated[str, Field(description="Concepto del gasto: 'alojamiento' (por noche) o 'alimentacion' (por día).")],
    ambito: Annotated[str, Field(description="Ámbito del viaje: 'nacional' o 'internacional'.")],
    ciudad: Annotated[
        str | None,
        Field(description="Ciudad de destino, opcional. Solo cambia el resultado en alojamiento internacional (ej.: 'Tokio')."),
    ] = None,
) -> str:
    """Consulta el tope de gasto de viaje vigente (alojamiento por noche o alimentación diaria) de Austral Bank.

    Úsala cuando la persona pregunte cuánto puede gastar en un viaje. No la uses para aprobaciones,
    transporte aéreo, rendición ni reembolsos. Devuelve el límite, la moneda y la fuente del dato.
    """
    return json.dumps(consultar_limite(concepto, ambito, ciudad), ensure_ascii=False)


def main() -> None:
    client = FoundryChatClient(
        project_endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=DefaultAzureCredential(),
    )
    agent = Agent(
        client=client,
        name="asistente-gastos-viaje",
        instructions=INSTRUCCIONES,
        tools=[consultar_limite_gastos],
        # El historial lo administra la infraestructura de hosting.
        default_options={"store": False},
    )
    ResponsesHostServer(agent).run()


if __name__ == "__main__":
    main()
