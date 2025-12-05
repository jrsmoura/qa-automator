# 🚀 Quick Start - QA Automator

## ⚡ Instalação Rápida

```bash
# 1. Clone ou baixe o projeto
cd qa_automator_project

# 2. Instale em modo de desenvolvimento
pip install -e .

# 3. Verifique a instalação
qa-automator version
```

## 🎯 Criar Seu Primeiro Projeto

```bash
# Execute o CLI
qa-automator start
```

### Durante a execução, você será perguntado:

1. **Nome do projeto**: `meu-primeiro-projeto`
2. **Criar .env?**: `s` (sim)
3. **GOOGLE_API_KEY**: Cole sua chave da API do Google
4. **Frameworks**: `1,2` (para selecionar ambos) ou pressione Enter

### Resultado:

```
meu-primeiro-projeto/
├── agent.py          # Agente orquestrador
├── main.py           # Execute com: python main.py
├── .env              # Sua API key está aqui
└── subagent/         # Frameworks selecionados
```

## 🔑 Obter Google API Key

1. Acesse: https://aistudio.google.com/app/apikey
2. Crie uma nova chave
3. Copie e cole quando o CLI pedir

## 💻 Executar Seu Projeto

```bash
cd meu-primeiro-projeto
pip install -r requirements.txt
python main.py
```

## 📝 Personalizar

### Modificar Prompts

Edite `prompts/prmt_main.py` para customizar o comportamento do agente.

### Adicionar Lógica

Edite `main.py` para implementar sua lógica de execução.

### Usar Sub-agentes

```python
from subagent.cypress_subagent.agent import get_cypress_agent

cypress = get_cypress_agent()
result = cypress.run("Criar teste para login")
```

## 🆘 Problemas Comuns

### Erro: GOOGLE_API_KEY não configurada

```bash
# Verifique o .env
cat .env | grep GOOGLE_API_KEY

# Adicione se necessário
echo "GOOGLE_API_KEY=sua_chave" >> .env
```

### Erro: Comando não encontrado

```bash
# Reinstale o pacote
pip install -e . --force-reinstall
```

## 📚 Próximos Passos

1. ✅ Leia o [README.md](README.md) completo
2. ✅ Explore os [EXAMPLES.md](EXAMPLES.md)
3. ✅ Veja a [STRUCTURE.md](STRUCTURE.md)
4. ✅ Para publicar: [PUBLISHING.md](PUBLISHING.md)

## 💡 Dicas

- Use `qa-automator help` para ver todos os comandos
- Comece com um framework e adicione mais depois
- Personalize os prompts para seu caso de uso específico
- Consulte a documentação do Google ADK para recursos avançados

## 🎉 Pronto!

Você agora tem um projeto de automação de testes baseado em agentes funcionando!

**Happy Testing! 🧪**
