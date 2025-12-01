from google.adk.agents import Agent
from .prompt import CYPRESS_PRMPT

cypress_agent = Agent(
    name="Cypress Subagent",
    prompt=CYPRESS_PRMPT,
    role="Especialista em criação de testes automatizados E2E usando Cypress Framework",
    description=""""
    Subagente especializado em gerar testes automatizados usando Cypress.
    Cria arquivos .spec.js ou .cy.js com sintaxe moderna para testes E2E.
    Segue as melhores práticas e padrões de mercado do Cypress Framework.
    """
)

def get_cypress_agent() -> Agent:
    """Retorna o subagente especializado em Cypress Framework."""
    return cypress_agent