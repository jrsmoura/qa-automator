"""Lógica do CLI do QA Automator."""

import sys
from qa_automator.cli.project_creator import ProjectCreator


def print_banner():
    """Imprime o banner do QA Automator."""
    banner = r"""
    ╔═══════════════════════════════════════════════════╗
    ║         QA Automator - Setup CLI v0.1.0           ║
    ║   Biblioteca para automação de testes baseada     ║
    ║        em agentes (Google ADK Framework)          ║
    ╚═══════════════════════════════════════════════════╝
    """
    print(banner)


def show_help():
    """Exibe ajuda do comando"""
    help_text = """
Uso: qa-automator COMANDO

Comandos disponíveis:
  start       Inicia o processo de criação de um novo projeto
  help        Exibe esta mensagem de ajuda
  version     Exibe a versão do QA Automator

Exemplos:
  qa-automator start
  qa-automator help

Para mais informações, visite: https://github.com/XXXXXXXXX/qa-automator
    """
    print(help_text)


def show_version():
    """Exibe a versão"""
    from qa_automator import __version__
    print(f"QA Automator v{__version__}")


def main():
    """Função principal do CLI"""
    if len(sys.argv) < 2:
        print("Erro: Nenhum comando fornecido")
        show_help()
        sys.exit(1)
    command = sys.argv[1].lower()
    if command == "start":
        print_banner()
        creator = ProjectCreator()
        creator.run()
    elif command in ["help", "--help", "-h"]:
        show_help()
    elif command in ["version", "--version", "-v"]:
        show_version()
    else:
        print(f"Erro: Comando desconhecido '{command}'")
        show_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
