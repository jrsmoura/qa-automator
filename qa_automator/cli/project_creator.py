"""Criador de projetos QA Automator"""


from pathlib import Path
from qa_automator.templates.base.base_templates import create_base_structure
from qa_automator.templates.subagents.subagent_manager import get_subagent_copy_function


class ProjectCreator:
    """Gerencia a criação de projetos QA Automator"""
    FRAMEWORKS = {
        "1": {"name": "Karate", "key": "Karate"},
        "2": {"name": "Cypress", "key": "Cypress"},
    }

    def __init__(self):
        self.project_name = None
        self.project_path = None
        self.create_env = False
        self.google_api_key = None
        self.selected_frameworks = []

    def run(self):
        """Executa o fluxo completo de criação do projeto"""
        self.get_project_name()
        self.ask_env_configuration()
        self.select_frameworks()
        self.create_project_structure()
        self.show_completion_message()

    def get_project_name(self):
        """Solicita o nome do projeto"""
        while True:
            project_name = input("\\n📝 Digite o nome do projeto: ").strip()

            if not project_name:
                print("❌ O nome do projeto não pode ser vazio!")
                continue

            # Validar nome do projeto (apenas letras, números, _, -)
            if not project_name.replace("_", "").replace("-", "").replace(" ", "").isalnum():
                print("❌ Use apenas letras, números, '_', '-' e espaços")
                continue
            self.project_name = project_name
            self.project_path = Path.cwd() / project_name

            if self.project_path.exists():
                print(f"❌ O diretório '{project_name}' já existe!")
                continue
            break

    def ask_env_configuration(self):
        """Pergunta sobre configuração do arquivo .env"""
        print("\\n🔐 Configuração do Google ADK")
        response = input("Deseja criar o arquivo .env com as variáveis do \
                         Google ADK? (s/n): ").strip().lower()

        if response in ['s', 'sim', 'y', 'yes']:
            self.create_env = True
            self.google_api_key = input("Digite sua GOOGLE_API_KEY: ").strip()
        else:
            self.create_env = True
            self.google_api_key = ""

    def select_frameworks(self):
        """Permite seleção de múltiplos frameworks"""
        print("\\n🧪 Frameworks de Teste Disponíveis:")
        print("=" * 40)

        for key, framework in self.FRAMEWORKS.items():
            print(f"{key}. {framework['name']}")

        print("\\n💡 Digite os números separados por vírgula (ex: 1,2)")
        print("   Ou pressione Enter para selecionar todos")

        while True:
            selection = input("\\nFrameworks desejados: ").strip()

            if not selection:
                # Selecionar todos
                self.selected_frameworks = list(self.FRAMEWORKS.values())
                break

            # Parse da seleção
            try:
                selected_keys = [k.strip() for k in selection.split(",")]
                self.selected_frameworks = []

                for key in selected_keys:
                    if key not in self.FRAMEWORKS:
                        print(f"❌ Opção inválida: {key}")
                        raise ValueError()
                    self.selected_frameworks.append(self.FRAMEWORKS[key])

                break
            except ValueError:
                print("❌ Seleção inválida. Tente novamente.")
                continue

        print("\\n✅ Frameworks selecionados:")
        for fw in self.selected_frameworks:
            print(f"   - {fw['name']}")

    def create_project_structure(self):
        """Cria a estrutura de diretórios e arquivos"""
        print(f"\\n🚀 Criando projeto '{self.project_name}'...")

        # Criar diretório raiz
        self.project_path.mkdir(parents=True, exist_ok=True)

        # Criar estrutura base usando templates
        create_base_structure(self.project_path, self.project_name, self.selected_frameworks)

        # Criar .env
        self.create_env_file()

        # Criar .gitignore
        self.create_gitignore()

        # Criar README
        self.create_readme()

        # Criar requirements.txt
        self.create_requirements()

        # Copiar subagentes selecionados
        subagent_path = self.project_path / "subagent"
        for framework in self.selected_frameworks:
            copy_func = get_subagent_copy_function(framework['key'])
            if copy_func:
                copy_func(subagent_path)

        print("✅ Estrutura criada com sucesso!")

    def create_env_file(self):
        """Cria o arquivo .env"""
        env_content = f"""# Google ADK Configuration
GOOGLE_API_KEY={self.google_api_key}
GOOGLE_PROJECT_ID=
GOOGLE_LOCATION=us-central1

# Agent Configuration
AGENT_NAME={self.project_name}
AGENT_MODEL=gemini-2.5-flash
"""

        env_file = self.project_path / ".env"
        env_file.write_text(env_content)
        print("   ├── Criado: .env")

    def create_gitignore(self):
        """Cria .gitignore básico"""
        gitignore_content = """# Environment
.env
.env.local
venv/
env/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# IDEs
.vscode/
.idea/
*.swp
*.swo

# Test Reports
reports/
screenshots/
videos/

# OS
.DS_Store
Thumbs.db

# Locks
*.lock
"""

        gitignore_file = self.project_path / ".gitignore"
        gitignore_file.write_text(gitignore_content)
        print("   ├── Criado: .gitignore")

    def create_readme(self):
        """Cria README.md do projeto"""
        frameworks_list = "\\n".join([f"- {fw['name']}" for fw in self.selected_frameworks])

        readme_content = f"""# {self.project_name}

Projeto de automação de testes criado com QA Automator, baseado
em agentes do Google ADK.

## 📋 Frameworks Configurados

{frameworks_list}

## 🚀 Começando

### 1. Configure o ambiente

Certifique-se de ter Python 3.10+ instalado.

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente

Edite o arquivo `.env` e adicione sua `GOOGLE_API_KEY`:

```
GOOGLE_API_KEY=sua_chave_aqui
```

Para obter uma chave da API do Google:
1. Acesse [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Crie uma nova chave de API
3. Copie e cole no arquivo .env

### 4. Execute o agente

```bash
python main.py
```

## 📁 Estrutura do Projeto

```
{self.project_name}/
├── agent.py                # Agente orquestrador principal
├── prompt.py               # Configuração de prompts do orquestrador
├── main.py                 # Script de execução
├── tools.py                # Ferramentas customizadas
├── prompts/                # Prompts do sistema
│   └── prmt_main.py       # Prompts principais
├── subagent/              # Sub-agentes especializados
│   ├── cypress_subagent/  # Sub-agente Cypress (se selecionado)
│   └── karate_subagent/   # Sub-agente Karate (se selecionado)
├── .env                    # Variáveis de ambiente
└── requirements.txt        # Dependências Python
```

## 🤖 Como Funciona

Este projeto utiliza uma arquitetura de **agentes orquestradores**:

1. **Agente Orquestrador** (`agent.py`): Recebe as requisições do usuário e
identifica qual framework é mais adequado
2. **Sub-agentes Especializados** (`subagent/`): Cada um especializado em
gerar testes para um framework específico

## 📝 Uso

Edite o arquivo `main.py` para customizar a execução do seu agente. Você pode:

- Adicionar prompts personalizados
- Integrar com outras ferramentas
- Automatizar fluxos de trabalho
- Criar novos sub-agentes

## 🛠️ Desenvolvimento

### Adicionando Novos Sub-agentes

1. Crie um novo diretório em `subagent/`
2. Implemente `agent.py`, `prompt.py` e `prompts/`
3. Registre o sub-agente no orquestrador

### Personalizando Prompts

Edite os arquivos em `prompts/` para ajustar o comportamento do sistema.

## 📚 Recursos

- [Documentação Google ADK](https://google.github.io/genai-agents/)
- [QA Automator](https://github.com/seu-usuario/qa-automator)

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull
requests.

## 📄 Licença

Este projeto foi gerado pelo QA Automator.
"""

        readme_file = self.project_path / "README.md"
        readme_file.write_text(readme_content)
        print("   ├── Criado: README.md")

    def create_requirements(self):
        """Cria requirements.txt com as dependências necessárias"""
        requirements_content = """# Google ADK
google-adk>=1.16.0

# Environment Management
python-dotenv>=1.0.0

# Async Support
aiosqlite>=0.20.0

# HTTP Client
httpx>=0.27.0

# Data Validation
pydantic>=2.0.0

# Optional: Development Tools
# pytest>=8.0.0
# black>=24.0.0
# flake8>=7.0.0
"""

        requirements_file = self.project_path / "requirements.txt"
        requirements_file.write_text(requirements_content)
        print("   ├── Criado: requirements.txt")

    def show_completion_message(self):
        """Exibe mensagem de conclusão"""
        print("\\n" + "=" * 60)
        print("🎉 Projeto criado com sucesso!")
        print("=" * 60)
        print(f"\\n📂 Localização: {self.project_path}")
        print("\\n📋 Próximos passos:")
        print(f"   1. cd {self.project_name}")
        print("   2. pip install -r requirements.txt")
        print("   3. Configure a GOOGLE_API_KEY no arquivo .env")
        print("   4. python main.py")
        print("\\n💡 Consulte o README.md para mais informações.")
        print("\\n✨ Bons testes automatizados!\\n")
