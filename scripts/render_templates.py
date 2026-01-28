#!/usr/bin/env python3
"""
Template Renderer per Manuale Clinica
Sostituisce le variabili {{ clinic.xxx }} nei file .md e in mkdocs.yml
usando i valori da clinic-config.yml

Usage:
    python scripts/render_templates.py [--config clinic-config.yml]
"""

import os
import re
import sys
import yaml
from pathlib import Path


def load_config(config_path: str) -> dict:
    """Carica la configurazione della clinica dal file YAML."""
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config.get('clinic', {})


def flatten_dict(d: dict, parent_key: str = '', sep: str = '.') -> dict:
    """Appiattisce un dizionario annidato in chiavi con dot notation."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, str(v) if v is not None else ''))
    return dict(items)


def replace_variables(content: str, variables: dict) -> str:
    """Sostituisce {{ clinic.xxx }} con i valori dal config."""
    def replacer(match):
        key = match.group(1).strip()
        # Supporta sia "clinic.name" che "name"
        if key in variables:
            return variables[key]
        # Prova senza prefisso "clinic."
        short_key = key.replace('clinic.', '')
        if short_key in variables:
            return variables[short_key]
        # Non trovato: lascia invariato
        return match.group(0)

    # Pattern: {{ clinic.xxx }} o {{ xxx }}
    pattern = r'\{\{\s*([\w.]+)\s*\}\}'
    return re.sub(pattern, replacer, content)


def process_file(file_path: Path, variables: dict, dry_run: bool = False) -> int:
    """Processa un singolo file, sostituendo le variabili. Ritorna il numero di sostituzioni."""
    content = file_path.read_text(encoding='utf-8')
    new_content = replace_variables(content, variables)

    if content == new_content:
        return 0

    changes = len(re.findall(r'\{\{\s*[\w.]+\s*\}\}', content)) - len(re.findall(r'\{\{\s*[\w.]+\s*\}\}', new_content))

    if not dry_run:
        file_path.write_text(new_content, encoding='utf-8')

    return changes


def main():
    # Determina la root del progetto
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    # Config path
    config_path = project_root / 'clinic-config.yml'
    if '--config' in sys.argv:
        idx = sys.argv.index('--config')
        if idx + 1 < len(sys.argv):
            config_path = Path(sys.argv[idx + 1])

    dry_run = '--dry-run' in sys.argv

    if not config_path.exists():
        print(f"Errore: file config non trovato: {config_path}")
        sys.exit(1)

    # Carica config
    clinic_data = load_config(str(config_path))
    variables = flatten_dict(clinic_data)

    print(f"Config caricato: {config_path}")
    print(f"Clinica: {variables.get('name', 'N/A')}")
    print(f"Variabili disponibili: {len(variables)}")
    if dry_run:
        print("MODALITA DRY-RUN: nessun file verra modificato")
    print()

    # File da processare
    docs_dir = project_root / 'docs'
    mkdocs_yml = project_root / 'mkdocs.yml'

    total_changes = 0
    files_changed = 0

    # Processa mkdocs.yml
    if mkdocs_yml.exists():
        changes = process_file(mkdocs_yml, variables, dry_run)
        if changes > 0:
            print(f"  mkdocs.yml: {changes} sostituzioni")
            total_changes += changes
            files_changed += 1

    # Processa tutti i .md nella directory docs
    for md_file in sorted(docs_dir.rglob('*.md')):
        changes = process_file(md_file, variables, dry_run)
        if changes > 0:
            rel_path = md_file.relative_to(project_root)
            print(f"  {rel_path}: {changes} sostituzioni")
            total_changes += changes
            files_changed += 1

    # Processa anche i file JS (per API base URL ecc.)
    for js_file in sorted(docs_dir.rglob('*.js')):
        changes = process_file(js_file, variables, dry_run)
        if changes > 0:
            rel_path = js_file.relative_to(project_root)
            print(f"  {rel_path}: {changes} sostituzioni")
            total_changes += changes
            files_changed += 1

    print(f"\nCompletato: {total_changes} sostituzioni in {files_changed} file")


if __name__ == '__main__':
    main()
