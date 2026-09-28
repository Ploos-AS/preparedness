#!/usr/bin/env python3
"""Validate Ploos Preparedness manifests and country data."""
from pathlib import Path
import json, sys
import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parents[1]

def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

def validate(path, schema):
    data=yaml.safe_load(path.read_text(encoding="utf-8"))
    errors=sorted(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(data), key=lambda e:list(e.path))
    for e in errors:
        print(f"{path}: {'/'.join(map(str,e.path)) or '<root>'}: {e.message}")
    return len(errors)

def main():
    errors=0
    errors+=validate(ROOT/"templates/book/book.yaml", load_json(ROOT/"schemas/book.schema.json"))
    cs=load_json(ROOT/"schemas/country.schema.json")
    for path in sorted((ROOT/"data/countries").glob("*.yaml")):
        errors+=validate(path, cs)
    if errors:
        print(f"FAILED: {errors} validation error(s)")
        return 1
    print("OK: preparedness metadata validates")
    return 0

if __name__=="__main__":
    sys.exit(main())
