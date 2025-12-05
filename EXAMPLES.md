# Exemplos de Uso do QA Automator

## 1. Criação de Projeto Básico

### Exemplo: Projeto com Cypress

```bash
# Executar o CLI
qa-automator start

# Responder as perguntas:
# Nome do projeto: meu-projeto-cypress
# Criar .env? (s/n): s
# GOOGLE_API_KEY: AIzaSy...
# Frameworks: 2 (Cypress)
```

### Exemplo: Projeto com Múltiplos Frameworks

```bash
qa-automator start

# Nome: projeto-completo
# API Key: sua_chave
# Frameworks: 1,2 (Karate e Cypress)
```

## 2. Estrutura de Projeto Gerado

### Cypress

```
meu-projeto/
├── subagent/
│   └── cypress_subagent/
│       ├── agent.py          # Agente Cypress
│       ├── prompt.py         # Prompts principais
│       └── prompts/
│           ├── main_prmpt.py      # Prompt principal
│           └── examples_prmpt.py  # Exemplos
```

### Karate

```
meu-projeto/
├── subagent/
│   └── karate_subagent/
│       ├── agent.py          # Agente Karate
│       └── prompt.py         # Prompts
```

## 3. Personalização

### Modificar Prompts do Orquestrador

Edite `prompts/prmt_main.py`:

```python
PERSONA: str = """
    Você é meu assistente personalizado...
"""
```

### Adicionar Novo Sub-agente

1. Crie a estrutura:

```
subagent/
└── novo_framework/
    ├── __init__.py
    ├── agent.py
    ├── prompt.py
    └── prompts/
        └── main_prmpt.py
```

2. Implemente o agente:

```python
# agent.py
from google.adk.agents import Agent
from .prompt import NOVO_FRAMEWORK_PRMPT

novo_framework_agent = Agent(
    name="NovoFramework_Subagent",
    instruction=NOVO_FRAMEWORK_PRMPT,
    description="Subagente para novo framework"
)

def get_novo_framework_agent() -> Agent:
    return novo_framework_agent
```

## 4. Executar o Projeto

### Modo Interativo

```python
# main.py
from agent import root_agent

# Interagir com o agente
response = root_agent.run("Crie um teste Cypress para login")
print(response)
```

### Modo Script

```python
# main.py
from agent import root_agent
from subagent.cypress_subagent.agent import get_cypress_agent

# Usar sub-agente diretamente
cypress_agent = get_cypress_agent()
response = cypress_agent.run("Gerar teste para página de checkout")
print(response)
```

## 5. Variáveis de Ambiente

### .env Básico

```bash
GOOGLE_API_KEY=sua_chave_aqui
GOOGLE_PROJECT_ID=
GOOGLE_LOCATION=us-central1

AGENT_NAME=meu-projeto
AGENT_MODEL=gemini-2.5-flash
```

### .env Avançado

```bash
# Google ADK
GOOGLE_API_KEY=AIzaSy...
GOOGLE_PROJECT_ID=meu-projeto-123
GOOGLE_LOCATION=us-central1

# Agent Config
AGENT_NAME=sistema-testes
AGENT_MODEL=gemini-2.5-flash
AGENT_TEMPERATURE=0.7
AGENT_MAX_TOKENS=2048

# Logging
LOG_LEVEL=INFO
LOG_FILE=agent.log

# Custom
BASE_URL=https://api.exemplo.com
TIMEOUT=30
```

## 6. Workflows Comuns

### Gerar Teste E2E

```python
from agent import root_agent

prompt = """
Preciso de um teste E2E para:
- URL: https://example.com/login
- Testar login com sucesso
- Validar redirecionamento
- Verificar mensagem de boas-vindas
"""

response = root_agent.run(prompt)
```

### Gerar Teste de API

```python
from agent import root_agent

prompt = """
Criar teste Karate para:
- Endpoint: POST /api/users
- Validar criação de usuário
- Verificar status 201
- Validar schema da resposta
"""

response = root_agent.run(prompt)
```

## 7. Dicas e Boas Práticas

### Organização de Prompts

```
prompts/
├── prmt_main.py        # Prompts principais
├── prmt_examples.py    # Exemplos específicos
├── prmt_patterns.py    # Padrões de teste
└── prmt_validations.py # Validações comuns
```

### Reutilização de Componentes

```python
# tools.py
def get_common_selectors():
    return {
        "login_button": "[data-cy='login-btn']",
        "email_input": "#email",
        "password_input": "#password"
    }

# Usar em prompts
from tools import get_common_selectors
```

### Versionar Projetos

```bash
git init
git add .
git commit -m "feat: setup inicial do projeto QA"
```

## 8. Troubleshooting

### Erro: GOOGLE_API_KEY não configurada

```bash
# Verificar se existe
cat .env | grep GOOGLE_API_KEY

# Adicionar se não existir
echo "GOOGLE_API_KEY=sua_chave" >> .env
```

### Erro: Módulo não encontrado

```bash
# Reinstalar dependências
pip install -r requirements.txt

# Ou reinstalar específico
pip install google-adk python-dotenv
```

### Erro: Importação de subagente

```python
# Verificar se __init__.py existe
# Verificar imports relativos
from .subagent.cypress_subagent.agent import get_cypress_agent
```

## 9. Recursos Adicionais

- [Documentação Google ADK](https://google.github.io/genai-agents/)
- [Cypress Docs](https://docs.cypress.io/)
- [Karate DSL](https://github.com/karatelabs/karate)

## 10. Contribuir

Encontrou um bug ou tem uma sugestão?

1. Abra uma issue no GitHub
2. Faça um fork e crie um PR
3. Entre em contato: jtsr@gft.com.br
