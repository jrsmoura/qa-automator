# Guia de Publicação no PyPI

## 📋 Pré-requisitos

1. Conta no [PyPI](https://pypi.org/account/register/)
2. Conta no [TestPyPI](https://test.pypi.org/account/register/) (opcional, para testes)
3. Python 3.10+
4. Ferramentas de build instaladas

## 🔧 Instalação das Ferramentas

```bash
pip install build twine --upgrade
```

## 📝 Preparação do Pacote

### 1. Verificar pyproject.toml

Certifique-se de que todas as informações estão corretas:

```toml
[project]
name = "qa_automator"  # Nome único no PyPI
version = "0.1.0"       # Versão semântica
description = "..."     # Descrição breve
authors = [...]         # Seus dados
```

### 2. Verificar MANIFEST.in

Garanta que todos os templates sejam incluídos:

```
include README.md
include LICENSE
recursive-include qa_automator/templates *
```

### 3. Atualizar README.md

- Descrição clara
- Exemplos de instalação
- Exemplos de uso básico
- Links para documentação

## 🏗️ Build do Pacote

### Limpar builds anteriores

```bash
rm -rf build/ dist/ *.egg-info/
```

### Criar o pacote

```bash
python -m build
```

Isso criará:
- `dist/qa_automator-0.1.0.tar.gz` (source distribution)
- `dist/qa_automator-0.1.0-py3-none-any.whl` (wheel)

### Verificar o pacote

```bash
twine check dist/*
```

## 🧪 Testar no TestPyPI

### 1. Configurar credenciais

Crie `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-...  # Seu token do TestPyPI

[pypi]
username = __token__
password = pypi-...  # Seu token do PyPI
```

### 2. Upload para TestPyPI

```bash
twine upload --repository testpypi dist/*
```

### 3. Instalar do TestPyPI

```bash
# Em um ambiente limpo
python -m venv test_env
source test_env/bin/activate

# Instalar
pip install --index-url https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple/ \
    qa-automator
```

### 4. Testar a instalação

```bash
qa-automator version
qa-automator help
```

## 🚀 Publicar no PyPI

### 1. Verificar tudo novamente

- [ ] Versão correta no pyproject.toml
- [ ] README.md atualizado
- [ ] CHANGELOG.md atualizado (se houver)
- [ ] Todos os testes passando
- [ ] Build limpo sem warnings

### 2. Criar tag Git

```bash
git tag -a v0.1.0 -m "Release version 0.1.0"
git push origin v0.1.0
```

### 3. Upload para PyPI

```bash
twine upload dist/*
```

### 4. Verificar no PyPI

Acesse: https://pypi.org/project/qa-automator/

## 📊 Pós-publicação

### 1. Atualizar documentação

- README.md com badge do PyPI
- Instruções de instalação via pip

### 2. Criar release no GitHub

- Vá em Releases
- Crie nova release
- Anexe os arquivos .tar.gz e .whl

### 3. Anunciar

- Twitter/X
- LinkedIn
- Reddit (r/Python)
- Blog post

## 🔄 Atualizações Futuras

### Versionamento Semântico

- **MAJOR** (1.0.0): Mudanças incompatíveis
- **MINOR** (0.1.0): Novas funcionalidades compatíveis
- **PATCH** (0.0.1): Bug fixes

### Processo de atualização

1. Atualizar código
2. Atualizar versão em `pyproject.toml` e `__init__.py`
3. Atualizar CHANGELOG.md
4. Build novo pacote
5. Testar no TestPyPI
6. Publicar no PyPI
7. Criar tag Git
8. Criar release no GitHub

## 🛡️ Segurança

### Proteger tokens

```bash
# Nunca commite tokens
echo ".pypirc" >> .gitignore

# Use tokens de API, não senhas
# Limite escopos dos tokens
# Rotacione tokens regularmente
```

### Verificar dependências

```bash
pip install safety
safety check -r requirements.txt
```

## 📋 Checklist de Publicação

- [ ] Código testado e funcionando
- [ ] Versão atualizada
- [ ] README.md completo
- [ ] LICENSE incluído
- [ ] MANIFEST.in correto
- [ ] Build sem erros
- [ ] Testado no TestPyPI
- [ ] Tag Git criada
- [ ] Upload para PyPI
- [ ] Release no GitHub
- [ ] Documentação atualizada

## 🐛 Troubleshooting

### Erro: Package already exists

```bash
# Incrementar versão em pyproject.toml
version = "0.1.1"  # ou próxima versão
```

### Erro: Invalid credentials

```bash
# Verificar ~/.pypirc
# Regenerar tokens na interface web
```

### Erro: Files missing

```bash
# Verificar MANIFEST.in
# Rebuild o pacote
python -m build
```

### Warning: Long description

```bash
# Verificar se README.md está no formato correto
# Usar markdown válido
```

## 📚 Recursos

- [PyPI Help](https://pypi.org/help/)
- [Python Packaging Guide](https://packaging.python.org/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Semantic Versioning](https://semver.org/)

## 💡 Dicas

1. **Sempre teste no TestPyPI primeiro**
2. **Use tokens de API, não senhas**
3. **Mantenha CHANGELOG.md atualizado**
4. **Documente breaking changes claramente**
5. **Use CI/CD para automatizar publicações**
6. **Responda issues rapidamente**
7. **Aceite contribuições da comunidade**

## 🎯 Próximos Passos

Após primeira publicação:

1. Adicionar badges ao README.md:
   - PyPI version
   - Downloads
   - License
   - Build status

2. Configurar CI/CD:
   - GitHub Actions
   - Testes automatizados
   - Deploy automático

3. Criar documentação:
   - ReadTheDocs
   - GitHub Pages
   - Wiki

4. Marketing:
   - Blog post
   - Video tutorial
   - Apresentações

---

**Boa sorte com sua publicação! 🚀**
