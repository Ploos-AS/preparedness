#!/usr/bin/env python3
"""Validate Ploos Preparedness contracts, provenance and language parity."""
from pathlib import Path
from datetime import date
import json, sys
import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parents[1]

# PyYAML defaults to YAML 1.1 boolean spellings, where unquoted "no"/"NO"
# become False. Preparedness metadata uses ISO language/country codes, so use
# YAML 1.2-style booleans: only true/false are booleans.
class YAML12SafeLoader(yaml.SafeLoader):
    pass

for first, resolvers in list(YAML12SafeLoader.yaml_implicit_resolvers.items()):
    YAML12SafeLoader.yaml_implicit_resolvers[first] = [
        (tag, regexp) for tag, regexp in resolvers
        if tag != "tag:yaml.org,2002:bool"
    ]

import re
YAML12SafeLoader.add_implicit_resolver(
    "tag:yaml.org,2002:bool",
    re.compile(r"^(?:true|false)$", re.IGNORECASE),
    list("tTfF"),
)

def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

def load_yaml(path):
    return yaml.load(path.read_text(encoding="utf-8"), Loader=YAML12SafeLoader)

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

def safety_source_errors(base):
    manifest=load_yaml(base/"chapters.yaml")
    registry_path=base/"references"/"safety.yaml"
    hazard_chapters=[c for c in manifest.get("chapters", []) if c.get("hazards")]
    if not hazard_chapters:
        return 0
    if not registry_path.is_file():
        print(f"{base/'chapters.yaml'}: hazard chapters require {registry_path}")
        return 1
    registry=load_yaml(registry_path)
    sources={source.get("id"): source for source in registry.get("sources", [])}
    errors=0
    for chapter in hazard_chapters:
        refs=chapter.get("safety_sources", [])
        if not refs:
            print(f"{base/'chapters.yaml'}: {chapter.get('id')}: hazards require safety_sources")
            errors += 1
        covered=set()
        for ref in refs:
            if ref not in sources:
                print(f"{base/'chapters.yaml'}: {chapter.get('id')}: unknown safety source {ref!r}")
                errors += 1
                continue
            covered.update(sources[ref].get("supports", []))
        missing=set(chapter.get("hazards", [])) - covered
        if missing:
            print(f"{base/'chapters.yaml'}: {chapter.get('id')}: hazards lack qualified source coverage: {', '.join(sorted(missing))}")
            errors += 1
    return errors

def parity_errors(base):
    manifest_path=base/"chapters.yaml"
    manifest=load_yaml(manifest_path)
    errors=0
    referenced={"no": set(), "en": set()}
    seen_ids=set()
    for chapter in manifest.get("chapters", []):
        chapter_id=chapter.get("id")
        if chapter_id in seen_ids:
            print(f"{manifest_path}: duplicate chapter id {chapter_id!r}")
            errors += 1
        seen_ids.add(chapter_id)
        if chapter.get("parity") != "required":
            continue
        for lang in ("no","en"):
            rel=chapter.get(lang)
            if not rel or not (base/rel).is_file():
                print(f"{manifest_path}: {chapter_id}: missing {lang} chapter {rel!r}")
                errors += 1
                continue
            if rel in referenced[lang]:
                print(f"{manifest_path}: duplicate {lang} chapter path {rel!r}")
                errors += 1
            referenced[lang].add(rel)

    for lang in ("no","en"):
        lang_dir=base/lang
        if not lang_dir.is_dir():
            continue
        actual={str(path.relative_to(base)) for path in lang_dir.glob("*.md")}
        for rel in sorted(actual - referenced[lang]):
            print(f"{manifest_path}: unreferenced {lang} chapter {rel!r}")
            errors += 1
    return errors

def baseline_provenance_errors(path):
    data=load_yaml(path)
    errors=0
    for jurisdiction, override in data.get("jurisdiction_overrides", {}).items():
        for domain, value in override.items():
            if not isinstance(value, dict) or value.get("status") != "authoritative":
                continue
            source=value.get("source", {})
            verified=source.get("verified_on")
            due=source.get("review_due")
            if not verified or not due:
                continue
            verified_date=date.fromisoformat(str(verified))
            due_date=date.fromisoformat(str(due))
            label=f"{jurisdiction}/{domain}"
            if due_date <= verified_date:
                print(f"{path}: {label}: review_due must be after verified_on")
                errors += 1
            if due_date < date.today():
                print(f"{path}: {label}: authoritative source review is overdue ({due_date.isoformat()})")
                errors += 1
    return errors

def worksheet_errors(base, schema):
    worksheet_dir=base/"worksheets"
    if not worksheet_dir.is_dir():
        return 0
    errors=0
    seen={}
    for path in sorted(worksheet_dir.glob("*.yaml")):
        errors += schema_errors(path, schema)
        data=load_yaml(path)
        worksheet_id=data.get("worksheet")
        expected=path.stem
        if worksheet_id != expected:
            print(f"{path}: worksheet id {worksheet_id!r} must match filename {expected!r}")
            errors += 1
        if worksheet_id in seen:
            print(f"{path}: duplicate worksheet id {worksheet_id!r}; first defined in {seen[worksheet_id]}")
            errors += 1
        else:
            seen[worksheet_id]=path
    return errors

def main():
    errors=0
    errors += schema_errors(ROOT/"templates/book/book.yaml", load_json(ROOT/"schemas/book.schema.json"))
    errors += schema_errors(ROOT/"data/common/baseline.yaml", load_json(ROOT/"schemas/baseline.schema.json"))
    errors += baseline_provenance_errors(ROOT/"data/common/baseline.yaml")
    country_schema=load_json(ROOT/"schemas/country.schema.json")
    for path in sorted((ROOT/"data/countries").glob("*.yaml")):
        errors += schema_errors(path, country_schema)
        errors += provenance_errors(path)
    chapter_schema=load_json(ROOT/"schemas/chapters.schema.json")
    worksheet_schema=load_json(ROOT/"schemas/worksheet.schema.json")
    errors += schema_errors(ROOT/"templates/book/chapters.yaml", chapter_schema)
    errors += parity_errors(ROOT/"templates/book")
    for base in sorted((ROOT/"books").glob("*")) if (ROOT/"books").exists() else []:
        if (base/"book.yaml").is_file():
            errors += schema_errors(base/"book.yaml", load_json(ROOT/"schemas/book.schema.json"))
        if (base/"chapters.yaml").is_file():
            errors += schema_errors(base/"chapters.yaml", chapter_schema)
            safety_registry=base/"references"/"safety.yaml"
            if safety_registry.is_file():
                errors += schema_errors(safety_registry, load_json(ROOT/"schemas/safety-sources.schema.json"))
            errors += safety_source_errors(base)
            errors += parity_errors(base)
        errors += worksheet_errors(base, worksheet_schema)
    if errors:
        print(f"FAILED: {errors} validation error(s)")
        return 1
    print("OK: preparedness contracts, provenance and language parity validate")
    return 0

if __name__=="__main__":
    sys.exit(main())
