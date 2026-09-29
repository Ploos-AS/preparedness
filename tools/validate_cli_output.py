#!/usr/bin/env python3
"""Validate machine-readable CLI output against the public toolkit schema."""
import json
from pathlib import Path
import subprocess
import sys

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schemas/tool-output.schema.json").read_text(encoding="utf-8"))
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())

CASES = [
    ["water", "-people", "2", "-days", "7", "-json"],
    ["battery", "-voltage", "12", "-ah", "100", "-json"],
    ["power", "-usable-wh", "500", "-load-w", "100", "-json"],
]


def main():
    binary = ROOT / "ploos-prep"
    errors = 0
    for args in CASES:
        proc = subprocess.run([str(binary), *args], cwd=ROOT, text=True, capture_output=True)
        if proc.returncode != 0:
            print(f"{args[0]}: CLI failed: {proc.stderr.strip()}")
            errors += 1
            continue
        try:
            data = json.loads(proc.stdout)
        except json.JSONDecodeError as exc:
            print(f"{args[0]}: invalid JSON: {exc}")
            errors += 1
            continue
        for err in sorted(VALIDATOR.iter_errors(data), key=lambda e: list(e.path)):
            where = "/".join(map(str, err.path)) or "<root>"
            print(f"{args[0]}: {where}: {err.message}")
            errors += 1
    if errors:
        print(f"FAILED: {errors} CLI output contract error(s)")
        return 1
    print("OK: CLI JSON output validates against tool-output.schema.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
