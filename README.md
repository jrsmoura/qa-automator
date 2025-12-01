# Biblioteca de Automação de Testes

- author: JRSMoura
- starting date: [26.11.2025]
- contact: <jtsr@gft.com.br>
- deadline: [05.12.2025]

---

## 📝 Changelog

### [01.12.2025] v0.0.2

OBS.: 
- ainda preciso colocar exemplos de saídas dos scripts de testes
- avaliar se mantenho o `setup.py`, ou se altero para o `pyproject.toml`


- ✨ Implementação inicial do `setup.py`
- 📖 Reestruturação README.md
- 🔨 Configuração .env
- 🔨 Configuração do Karate
  - - `agent.py`
  - - `__init__.py`
- 🔨 Configuração do Cypress
  - - `prompt.py`
  - - `agent.py`
  - - `__init__.py`
- ♻️ Integração do orquestrador/root com delegação via ADK
- 🛠 Sistema de prompts especializados
- 🔨 Configuração ADK Web
- 📖 Documentação atualizada

### [28.11.2025] v0.0.1

- 🔨 Construção da v1 do `/prompts/prmt_main.py`

### [27.11.2025] v0.0.1

- 🔨 Versão inicial com diretrizes básicas e estruturas

---

## 📋 Descrição

Sistema multi-agente que automatiza a criação de testes para diferentes frameworks, utilizando o Google ADK (Agent Development Kit) com interface web.

### Arquitetura

```
┌─────────────────────────────────────┐
│    Orquestrador Principal           │
│  (QA Automation Orchestrator)       │
└──────────────┬──────────────────────┘
               │
       ┌───────┴────────┐
       │                │
┌──────▼─────┐   ┌─────▼──────┐
│  Karate    │   │  Cypress   │
│  Agent     │   │  Agent     │
│  🥋 API    │   │  🌲 E2E    │
└────────────┘   └────────────┘
```

---

## Tecnologias

- Python >= 3.13
- Google-ADK >=1.16
- pip ou poetry

### Instalação das dependências

```bash
# Clone o repositório (quando disponível)
git clone [url-do-repo]
cd qa_automator

# Instale as dependências
pip install -r requirements.txt

# Ou usando poetry
poetry install
```

### Configuração

1. Copie o arquivo de exemplo de variáveis de ambiente:

```bash
$ cp .env.example .env
```

2. Edite o arquivo `.env` se necessário (opcional para maioria dos casos)

---

## 🎯 Como Usar

### Iniciando o Sistema

```bash
$ adk web
```

O sistema iniciará na porta 8000. Acesse via navegador:
[http://localhost:8000](http://localhost:8000)

### Interface ADK Web

A interface ADK Web permite interação via chat com o orquestrador. Exemplos de uso:

#### Exemplo 1: Teste Karate

```bash
Usuário: Crie um teste Karate para validar o endpoint POST /api/users
```

#### Exemplo 2: Teste Cypress

```bash
Usuário: Preciso de um teste Cypress para validar o login em https://example.com
```

#### Exemplo 3: Sem especificar framework

```bash
Usuário: Preciso testar uma API REST
Orquestrador: Identifiquei que você precisa testar uma API. Vou delegar para o Karate Agent...
```
---

## 📦 Frameworks Disponíveis

### 🥋 Karate Framework

- **Tipo**: Testes de API REST
- **Formato**: `.feature` (Gherkin/Karate DSL)
- **Uso**: GET, POST, PUT, DELETE, validações JSON/XML

### 🌲 Cypress Framework  

- **Tipo**: Testes End-to-End
- **Formato**: `.spec.js` ou `.cy.js`
- **Uso**: Testes de interface web, componentes, integração

### 🚧 Em desenvolvimento

- Appium (mobile)
- JMeter (performance)
- K6 (load testing)

## 📁 Estrutura do Projeto

```BASH
qa_automator/
├── agent.py              # Orquestrador principal
├── main.py              # Entry point da aplicação
├── config.py            # Configurações
├── prompt.py            # Prompt do orquestrador
├── requirements.txt     # Dependências
├── .env.example         # Exemplo de variáveis de ambiente
├── prompts/
│   └── prmt_main.py     # Prompts do orquestrador
└── subagent/
    ├── karate_subagent/
    │   ├── agent.py     # Agente Karate
    │   └── prompts.py   # Prompts Karate
    └── cypress_subagent/
        ├── agent.py     # Agente Cypress
        └── prompts.py   # Prompts Cypress
```

## TODO LIST - implementação

- [X] Estrutura de pastas base
- [X] repositório git - pedir ao Agapito
- [X] Configuração dos `__init__.py`
- [ ] `config.py`
- [ ] `USAGE.md`
- [x] `setup.py`
- [X] estrutura de prompts
- [ ] comando `qa-auto start`
- [ ] orquestrador
  - [X] `agent.py`
  - [X] `prompt.py`
  - [ ] TESTES
- [ ] Implementaçã dos frameworks
  - [ ] Karate
    - [X] `agent.py`
    - [ ] `prompt.py`
    - [ ] TESTES
  - [X] Cypress
    - [X] `agent.py`
    - [X] `prompt.py`
    - [ ] TESTES
  - [ ] Appium
    - [ ] `agent.py`
    - [ ] `prompt.py`
    - [ ] TESTES
  - [ ] JMeter
    - [ ] `agent.py`
    - [ ] `prompt.py`
    - [ ] TESTES
  - [ ] K6
    - [ ] `agent.py`
    - [ ] `prompt.py`
    - [ ] TESTES
