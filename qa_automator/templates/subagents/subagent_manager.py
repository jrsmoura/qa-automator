"""Gerenciamento de templates de subagentes"""

from pathlib import Path
import shutil


SUBAGENTS_DIR = Path(__file__).parent


def copy_cypress_subagent(target_path: Path):
    """Copia a estrutura completa do Cypress subagent"""
    source = SUBAGENTS_DIR / "cypress_subagent"
    destination = target_path / "cypress_subagent"
    
    if source.exists():
        shutil.copytree(source, destination)
        print(f"   ├── Cypress subagent configurado")
    else:
        print(f"    Aviso: Template do Cypress não encontrado")


def copy_karate_subagent(target_path: Path):
    """Copia a estrutura completa do Karate subagent"""
    source = SUBAGENTS_DIR / "karate_subagent"
    destination = target_path / "karate_subagent"
    
    if source.exists():
        shutil.copytree(source, destination)
        print(f"   ├── Karate subagent configurado")
    else:
        print(f"     Aviso: Template do Karate não encontrado")


def get_subagent_copy_function(framework_name: str):
    """Retorna a função de cópia apropriada para o framework"""
    mapping = {
        "Cypress": copy_cypress_subagent,
        "Karate": copy_karate_subagent,
    }
    return mapping.get(framework_name)
