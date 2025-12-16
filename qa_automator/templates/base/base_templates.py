"""Templates para os arquivos base do projeto de agente"""

from pathlib import Path


def get_agent_py() -> str:
    """Template para agent.py"""
    return '''from google.adk import Agent
from .prompt import ORCHESTRATOR_PRMT


root_agent = Agent(
    model="gemini-2.5-flash",
    name="Orchestrator_Agent",
    description="An orchestrator that manages and delegates tasks to specialized agents based on the provided objectives.",
    instruction=ORCHESTRATOR_PRMT,
)
'''


def get_prompt_py() -> str:
    """Template para prompt.py"""
    return '''from .prompts.prmt_main import (
    MENSAGEM_INICIAL, MENSAGEM_DE_DESPEDIDA, BOAS_PRATICAS,
    OBJETIVOS, PERSONA, DIRETRIZES, DADOS_DE_ENTRADA
)

ORCHESTRATOR_PRMT: str = PERSONA + MENSAGEM_INICIAL + OBJETIVOS + DADOS_DE_ENTRADA + DIRETRIZES + BOAS_PRATICAS + MENSAGEM_DE_DESPEDIDA
'''


def get_tools_py() -> str:
    """Template para tools.py"""
    return '''"""Ferramentas e utilitários para o agente"""
# Adicione suas ferramentas personalizadas aqui
'''


def get_init_py() -> str:
    """Template para __init__.py"""
    return ''


def get_main_py(project_name: str) -> str:
    """Template para main.py"""
    return f'''"""
{project_name} - Main Agent Runner
Executar: python main.py
"""
import os
from dotenv import load_dotenv
from agent import root_agent

# Carregar variáveis de ambiente
load_dotenv()


def main():
    """Função principal para executar o agente orquestrador"""
    print(" Iniciando {project_name}...")
    
    # Verificar se a API key está configurada
    if not os.getenv('GOOGLE_API_KEY'):
        print(" ERRO: GOOGLE_API_KEY não configurada no arquivo .env")
        print("Configure a chave da API antes de continuar.")
        return
    
    print(" Ambiente configurado")
    print("=" * 60)
    
    # Aqui você pode adicionar a lógica de execução do seu agente
    # Por exemplo:
    # response = root_agent.run("Seu prompt aqui")
    # print(response)
    
    print("\n💡 Agente pronto para uso!")
    print("Edite este arquivo (main.py) para personalizar a execução.")


if __name__ == "__main__":
    main()
'''


def get_prmt_main_py(frameworks: list) -> str:
    """Template para prompts/prmt_main.py"""
    frameworks_list = "\n    * ".join(frameworks)
    frameworks_enum = "\n    * ".join(frameworks)
    
    return f'''PERSONA: str = """
    Você é um sistema baseado em agentes, especializado na criação de testes
    usando diferentes frameworks, a saber:

    * {frameworks_list}

    Você tem como principal funcionalidade guiar o usuário para o framework
    correto e então delegar a tarefa para o sub-agente responsável.
"""

MENSAGEM_INICIAL: str = """
    ️ BEM VINDO AO SISTEMA DE CRIAÇÃO DE TESTES AUTOMÁTICO️

    Este sistema foi concebido para agilizar a criação de testes automatizados
    em diferentes frameworks:

    * {frameworks_enum}

    Você agora poderá selecionar qual o framework que deseja usar e eu irei
    orientá-lo da melhor maneira possível, para que sua experiência seja
    sempre excelente.
"""


OBJETIVOS: str = """
    1. Identificar o framework de teste mais adequado com base nas necessidades
       do usuário.
    2. Delegar a tarefa de criação de testes ao sub-agente especializado no
       framework selecionado.
    3. Fornecer orientações claras e concisas ao usuário durante todo o
       processo.
"""

DADOS_DE_ENTRADA: str = """
    - O usuário poderá fornecer ou o nome do framework desejado ou uma
      descrição das necessidades do teste.
    - Caso o usuário forneça uma descrição, você deverá analisar e sugerir o
      framework mais adequado.
"""

DIRETRIZES: str = """
    - Sempre buscar entender completamente as necessidades do usuário antes
      de sugerir um framework.
    - Fornecer instruções claras e passo a passo para o usuário.
    """
    
BOAS_PRATICAS: str = """
    - Manter a comunicação clara e objetiva.
    - Ser paciente e fornecer suporte contínuo ao usuário.
    - Atualizar-se constantemente sobre as melhores práticas em testes
      automatizados.
"""


MENSAGEM_DE_DESPEDIDA: str = """
    👋 OBRIGADO POR USAR O SISTEMA DE CRIAÇÃO DE TESTES AUTOMÁTICOS
"""
'''


def create_base_structure(project_path: Path, project_name: str, frameworks: list):
    """Cria a estrutura base do projeto"""
    # Criar __init__.py na raiz
    (project_path / "__init__.py").write_text(get_init_py(), encoding='utf-8')
    
    # Criar agent.py
    (project_path / "agent.py").write_text(get_agent_py(), encoding='utf-8')
    
    # Criar prompt.py
    (project_path / "prompt.py").write_text(get_prompt_py(), encoding='utf-8')
    
    # Criar tools.py
    (project_path / "tools.py").write_text(get_tools_py(), encoding='utf-8')
    
    # Criar main.py
    (project_path / "main.py").write_text(get_main_py(project_name), encoding='utf-8')
    
    # Criar diretório prompts
    prompts_path = project_path / "prompts"
    prompts_path.mkdir(exist_ok=True)
    (prompts_path / "__init__.py").write_text(get_init_py(), encoding='utf-8')
    
    # Criar prmt_main.py
    framework_names = [fw["name"] for fw in frameworks]
    (prompts_path / "prmt_main.py").write_text(get_prmt_main_py(framework_names), encoding='utf-8')
    
    # Criar diretório subagent
    subagent_path = project_path / "subagent"
    subagent_path.mkdir(exist_ok=True)
    (subagent_path / "__init__.py").write_text(get_init_py())
    
    print("   ├── Estrutura base criada")
