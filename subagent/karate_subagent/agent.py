from google.adk.agents import Agent
from .prompt import KARATE_PRMPT

karate_agent = Agent(
    name="Karate_Subagent",
    instruction=KARATE_PRMPT,
    description=""""
    Subagente especializado em gerar testes automatizados usando Cypress.
    Cria arquivos .spec.js ou .cy.js com sintaxe moderna para testes E2E.
    Segue as melhores práticas e padrões de mercado do Cypress Framework.
    """
)

def get_karate_agent() -> Agent:
    """Retorna o subagente especializado em Karate Framework."""
    return karate_agent