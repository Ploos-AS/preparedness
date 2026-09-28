#!/usr/bin/env python3
"""Validate Ploos Preparedness contracts, provenance and language parity."""
from pathlib import Path
from datetime import date
import json, sys
import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parents[1]

def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

def load_yaml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))

def schema_errors(path, schema):
    data=load_yaml(path)
    errors=sorted(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(data), key=lambda e:list(e.path))
    for e in errors:
        print(f"{path}: {'/'.join(map(str,e.path)) or '<root>'}: {e.message}")
    return len(errors)

def provenance_errors(path):
    data=load_yaml(path)
    errors=0
    if data.get("status") == "verified":
        if not data.get("verified_on"):
            print(f"{path}: verified data requires verified_on")
            errors += 1
        if not data.get("sources"):
            print(f"{path}: verified data requires at least one source")
            errors += 1
    due=data.get("review_due")
    if due and date.fromisoformat(str(due)) < date.today() and data.get("status") == "verified":
        print(f"{path}: review_due has passed; set status to review-due or re-verify")
        errors += 1
    return errors

def parity_errors():
    manifest=load_yaml(ROOT/"templates/book/chapters.yaml")
    errors=0
    for chapter in manifest.get("chapters", []):
        if chapter.get("parity") != "required":
            continue
        for lang in ("no","en"):
            rel=chapter.get(lang)
            if not rel or not (ROOT/"templates/book"/rel).is_file():
                print(f"templates/book/chapters.yaml: {chapter.get('id')}: missing {lang} chapter {rel!r}")
                errors += 1
    return errors

def main():
    errors=0
    errors += schema_errors(ROOT/"templates/book/book.yaml", load_json(ROOT/"schemas/book.schema.json"))
    country_schema=load_json(ROOT/"schemas/country.schema.json")
    for path in sorted((ROOT/"data/countries").glob("*.yaml")):
        errors += schema_errors(path, country_schema)
        errors += provenance_errors(path)
    errors += parity_errors()
    if errors:
        print(f"FAILED: {errors} validation error(s)")
        return 1
    print("OK: preparedness contracts, provenance and language parity validate")
    return 0

if __name__=="__main__":
    sys.exit(main())
