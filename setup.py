from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="qa-automator",
    version="0.1.0",
    author="JRSMoura",
    author_email="jtrs@gft.com.br",
    description="Biblioteca para automação de criação de testes de QA.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seu-usuario/seu-pacote",
    project_urls={
        "Bug Tracker": "https://github.com/jrsmoura/qa-automator",
        "Documentation": "https://qa-automator.readthedocs.io",
    },
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.25.0",
        # adicione suas dependências aqui
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.9",
        ],
    },
    entry_points={
        "console_scripts": [
            "seu-comando=seu_pacote.main:main",
        ],
    },
)
