# Ploos Preparedness Toolkit

The toolkit is an offline-first companion to the books, not a cloud service.

## Interface

The canonical command is `ploos-prep`.

Planned modules:

```text
ploos-prep water
ploos-prep power
ploos-prep battery
ploos-prep food
ploos-prep radio
ploos-prep checklist
```

Every calculation must be usable without an account, network connection or telemetry. Human-readable output is the default; `--json` will emit the stable result contract in `schemas/tool-output.schema.json`.

## Architecture

The preferred implementation language is Go. Calculation logic must live in reusable packages so CLI, GUI and future web/PWA frontends share the same tested core.

The toolkit may consume verified structured data from this repository. It must never silently turn country-neutral calculations into legal or regulatory advice.

## Design rules

- SI units internally and by default.
- Deterministic calculations.
- Explicit assumptions.
- No network dependency for core functions.
- No telemetry by default.
- Machine-readable output is versioned.
- Safety margins are named, not hidden.
- Radio transmit guidance is jurisdiction-aware.
- Books can reproduce the same calculations from documented formulas.

## M2 API boundary

M2 defines contracts and test vectors before feature-rich UI work. This prevents the books, CLI and later GUI from implementing subtly different calculations.
