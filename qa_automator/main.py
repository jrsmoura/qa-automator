"""Entry point para o CLI qa-automator"""

import sys
from qa_automator.cli.cli import main as cli_main


def main():
    """Entry point para o CLI qa-automator"""
    try:
        cli_main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operação cancelada pelo usuário.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
