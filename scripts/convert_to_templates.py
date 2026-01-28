#!/usr/bin/env python3
"""
Converte i riferimenti hardcoded nei file .md in variabili template {{ clinic.xxx }}.
Da eseguire UNA VOLTA per trasformare il manuale in template.
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DOCS_DIR = PROJECT_ROOT / 'docs'

# Mapping: testo hardcoded -> variabile template
# Ordine importante: match piu lunghi prima per evitare sostituzioni parziali
REPLACEMENTS = [
    # Indirizzi completi (prima dei parziali)
    ("Via Monte Circeo 12, 00015 Monterotondo (RM)", "{{ clinic.full_address }}"),
    ("Via Monte Circeo 12, Monterotondo (RM)", "{{ clinic.full_address }}"),
    ("Via Monte Circeo 12 - 00015 Monterotondo (RM)", "{{ clinic.full_address }}"),
    ("Via Monte Circeo, 12 - 00015 Monterotondo (RM)", "{{ clinic.full_address }}"),

    # Nome completo
    ("Studio Dentistico Smiledoc", "{{ clinic.full_name }}"),
    ("STUDIO DENTISTICO SMILEDOC", "{{ clinic.full_name }}"),
    ("Studio Smiledoc", "{{ clinic.full_name }}"),
    ("Smiledoc S.r.l.", "{{ clinic.legal_name }}"),

    # Email (prima dei nomi generici)
    ("privacy@smiledoc.it", "{{ clinic.email_privacy }}"),
    ("direzione@smiledoc.it", "{{ clinic.email_direzione }}"),
    ("info@smiledoc.it", "{{ clinic.email }}"),

    # Telefono
    ("06 90623936", "{{ clinic.phone }}"),

    # Indirizzo parziale
    ("Via Monte Circeo 12", "{{ clinic.address }}"),
    ("Via Monte Circeo, 12", "{{ clinic.address }}"),

    # Citta
    ("Monterotondo (RM)", "{{ clinic.city }} ({{ clinic.province }})"),
    ("00015 Monterotondo", "{{ clinic.cap }} {{ clinic.city }}"),

    # Nome clinica (ULTIMO - per evitare sostituzioni dentro stringhe gia convertite)
    # Non sostituire dentro URL, path di file, o email
]

# Pattern per "Smiledoc" standalone (non in URL, email, path)
SMILEDOC_PATTERN = re.compile(
    r'(?<![/@\w.])Smiledoc(?![@.\w/])'  # Non preceduto/seguito da caratteri URL/email
)


def process_file(file_path: Path, dry_run: bool = False) -> int:
    """Processa un file, applicando le sostituzioni."""
    content = file_path.read_text(encoding='utf-8')
    original = content
    changes = 0

    for old, new in REPLACEMENTS:
        if old in content:
            count = content.count(old)
            content = content.replace(old, new)
            changes += count

    # Smiledoc -> {{ clinic.name }} ma solo standalone
    # Evitiamo di toccare: manuale-smiledoc, smiledoc.it, @smiledoc, Smiledoc S.r.l. (gia convertito)
    def smiledoc_replacer(match):
        return "{{ clinic.name }}"

    new_content = SMILEDOC_PATTERN.sub(smiledoc_replacer, content)
    if new_content != content:
        smiledoc_count = len(SMILEDOC_PATTERN.findall(content))
        changes += smiledoc_count
        content = new_content

    if content != original:
        if not dry_run:
            file_path.write_text(content, encoding='utf-8')
        return changes

    return 0


def main():
    import sys
    dry_run = '--dry-run' in sys.argv

    print("Conversione dati hardcoded in variabili template")
    print(f"{'DRY RUN - ' if dry_run else ''}Directory: {DOCS_DIR}")
    print()

    total_changes = 0
    files_changed = 0

    # Processa mkdocs.yml
    mkdocs = PROJECT_ROOT / 'mkdocs.yml'
    if mkdocs.exists():
        changes = process_file(mkdocs, dry_run)
        if changes:
            print(f"  mkdocs.yml: {changes} sostituzioni")
            total_changes += changes
            files_changed += 1

    # Processa tutti i .md
    for md_file in sorted(DOCS_DIR.rglob('*.md')):
        changes = process_file(md_file, dry_run)
        if changes:
            rel = md_file.relative_to(PROJECT_ROOT)
            print(f"  {rel}: {changes} sostituzioni")
            total_changes += changes
            files_changed += 1

    # Processa JS (per API URL)
    for js_file in sorted(DOCS_DIR.rglob('*.js')):
        changes = process_file(js_file, dry_run)
        if changes:
            rel = js_file.relative_to(PROJECT_ROOT)
            print(f"  {rel}: {changes} sostituzioni")
            total_changes += changes
            files_changed += 1

    print(f"\nTotale: {total_changes} sostituzioni in {files_changed} file")
    if dry_run:
        print("Nessun file modificato (dry-run). Rimuovi --dry-run per applicare.")


if __name__ == '__main__':
    main()
