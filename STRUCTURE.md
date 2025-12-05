





# Estrutura Final do QA Automator

## 📦 Estrutura do Pacote

```
qa_automator_project/
├── qa_automator/                      # Pacote principal
│   ├── __init__.py                   # Inicialização do pacote
│   ├── main.py                        # Entry point do CLI
│   │
│   ├── cli/                           # Módulos CLI
│   │   ├── __init__.py
│   │   ├── cli.py                     # Lógica principal do CLI
│   │   └── project_creator.py         # Criador de projetos
│   │
│   └── templates/                     # Templates para geração
│       ├── __init__.py
│       │
│       ├── base/                      # Templates base
│       │   ├── __init__.py
│       │   └── base_templates.py      # Funções de criação base
│       │
│       └── subagents/                 # Templates de subagentes
│           ├── __init__.py
│           ├── subagent_manager.py    # Gerenciador de subagentes
│           │
│           ├── cypress_subagent/      # Template Cypress
│           │   ├── __init__.py
│           │   ├── agent.py
│           │   ├── prompt.py
│           │   └── prompts/
│           │       ├── __init__.py
│           │       ├── main_prmpt.py
│           │       └── examples_prmpt.py
│           │
│           └── karate_subagent/       # Template Karate
│               ├── __init__.py
│               ├── agent.py
│               └── prompt.py
│
├── pyproject.toml                     # Configuração do projeto
├── README.md                          # Documentação principal
├── LICENSE                            # Licença MIT
├── EXAMPLES.md                        # Exemplos de uso
├── MANIFEST.in                        # Inclusão de arquivos
└── .gitignore                         # Arquivos ignorados

```

## 🎯 Projeto Gerado pelo CLI

Quando você executa `qa-automator start`, a seguinte estrutura é criada:

```
meu-projeto/                           # Nome escolhido pelo usuário
├── agent.py                           # Agente orquestrador
├── prompt.py                          # Prompts do orquestrador
├── main.py                            # Script de execução
├── tools.py                           # Ferramentas customizadas
├── __init__.py                        # Inicialização
│
├── prompts/                           # Diretório de prompts
│   ├── __init__.py
│   └── prmt_main.py                  # Prompts principais
│
├── subagent/                          # Subagentes selecionados
│   ├── __init__.py
│   │
│   ├── cypress_subagent/             # Se selecionado
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── prompt.py
│   │   └── prompts/
│   │       ├── __init__.py
│   │       ├── main_prmpt.py
│   │       └── examples_prmpt.py
│   │
│   └── karate_subagent/              # Se selecionado
│       ├── __init__.py
│       ├── agent.py
│       └── prompt.py
│
├── .env                               # Variáveis de ambiente
├── .gitignore                         # Git ignore
├── README.md                          # Documentação do projeto
└── requirements.txt                   # Dependências Python
```

## 📝 Fluxo de Criação

1. **Usuário executa**: `qa-automator start`
2. **CLI pergunta**:
   - Nome do projeto
   - Configuração da GOOGLE_API_KEY
   - Frameworks desejados (Cypress, Karate, ou ambos)
3. **Sistema cria**:
   - Estrutura base (agent.py, prompt.py, main.py, tools.py)
   - Diretório prompts/ com configurações
   - Diretório subagent/ com os frameworks selecionados
   - Arquivos de configuração (.env, .gitignore, README.md)
4. **Resultado**: Projeto completo pronto para uso

## 🚀 Comandos Disponíveis

### Criar projeto
```bash
qa-automator start
```

### Ajuda
```bash
qa-automator help
```

### Versão
```bash
qa-automator version
```

## 📦 Publicação no PyPI

### 1. Preparar o pacote
```bash
# Instalar ferramentas
pip install build twine

# Criar o pacote
python -m build
```

### 2. Testar no TestPyPI
```bash
# Upload para TestPyPI
twine upload --repository testpypi dist/*

# Instalar do TestPyPI
pip install --index-url https://test.pypi.org/simple/ qa-automator
```

### 3. Publicar no PyPI
```bash
# Upload para PyPI
twine upload dist/*

# Usuários podem instalar
pip install qa-automator
```

## 🔧 Manutenção

### Atualizar templates

Para adicionar ou modificar templates de frameworks:

1. Adicione o template em `qa_automator/templates/subagents/`
2. Crie a função de cópia em `subagent_manager.py`
3. Adicione a opção no `FRAMEWORKS` dict em `project_creator.py`
4. Atualize a documentação

### Adicionar novo framework

```python
# Em subagent_manager.py
def copy_novo_framework(target_path: Path):
    source = SUBAGENTS_DIR / "novo_framework"
    destination = target_path / "novo_framework"
    shutil.copytree(source, destination)
    print(f"   ├── Novo Framework configurado")

# Em project_creator.py
FRAMEWORKS = {
    "1": {"name": "Karate", "key": "Karate"},
    "2": {"name": "Cypress", "key": "Cypress"},
    "3": {"name": "Novo Framework", "key": "NovoFramework"},  # Adicionar aqui
}
```

## 📊 Estatísticas

- **Arquivos Python**: ~15 arquivos
- **Templates incluídos**: 2 frameworks (Cypress, Karate)
- **Dependências principais**: google-adk, python-dotenv
- **Tamanho aproximado**: ~50KB (sem dependências)

## ✅ Checklist de Funcionalidades

- [x] CLI interativo
- [x] Criação de estrutura base
- [x] Template Cypress completo
- [x] Template Karate
- [x] Configuração .env
- [x] Geração de README.md
- [x] Geração de .gitignore
- [x] Geração de requirements.txt
- [x] Suporte a múltiplos frameworks
- [x] Validação de entrada do usuário
- [x] Mensagens de erro amigáveis
- [x] Documentação completa

## 🎨 Personalização

O pacote é altamente personalizável:

1. **Templates**: Modifique os templates em `qa_automator/templates/`
2. **Prompts**: Ajuste os prompts em `base_templates.py`
3. **CLI**: Customize o comportamento em `cli.py` e `project_creator.py`
4. **Frameworks**: Adicione novos frameworks facilmente

## 📞 Suporte

- **Issues**: Abra uma issue no GitHub
- **Email**: jtsr@gft.com.br
- **Docs**: README.md e EXAMPLES.md
