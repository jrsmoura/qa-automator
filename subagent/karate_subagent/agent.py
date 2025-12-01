"""
Orquestrador principal do sistema de automação de testes
"""
from google.adk.agent.agent import Agent
from prompt import ORCHETRATOR_PRMT
from subagent import karate_agent, cypress_agent


# Configuração do agente orquestrador com delegação para subagentes
orchestrator_agent = Agent(
    name="QA Automation Orchestrator",
    role="Orquestrador que gerencia e delega tarefas para agentes especializados em frameworks de teste",
    prompt=ORCHETRATOR_PRMT,
    delegates=[karate_agent, cypress_agent],
    description="""
    Agente principal responsável por:
    - Receber requisições de criação de testes
    - Identificar o framework apropriado (Karate ou Cypress)
    - Delegar para o subagente especializado
    - Coordenar a resposta final ao usuário
    """
)


def get_orchestrator():
    """
    Retorna a instância do orquestrador configurado
    """
    return orchestrator_agent