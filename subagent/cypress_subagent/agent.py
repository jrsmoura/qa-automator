from google.adk.agents import Agent
from subagent.cypress_subagent.prompts.main_prmpt import CYPRESS_PRMPT

cypress_agent = Agent(
    name="Cypress_Subagent",
    instruction=CYPRESS_PRMPT,
    description=""""
    Subagente especializado em gerar testes automatizados usando Cypress.
    Cria arquivos .spec.js ou .cy.js com sintaxe moderna para testes E2E.
    Segue as melhores práticas e padrões de mercado do Cypress Framework.
    """
)

def get_cypress_agent() -> Agent:
    """Retorna o subagente especializado em Cypress Framework."""
    return cypress_agent