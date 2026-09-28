# Roadmap

## M0 — Foundation — DONE

- Identity, Europe-first/NO-first scope, localisation and editorial policy.
- Repository architecture, licensing and initial structured country data.

## M1 — Validation and book contract — DONE

- Book and country JSON Schemas.
- CI validation.
- NO/EN reusable book skeleton.
- Publishing contract for HTML, EPUB, Kindle and PDF.

## M2 — Toolkit and reusable data contracts — DONE

- Define stable `ploos-prep` machine-readable result contract.
- Establish offline-first Go-oriented toolkit architecture.
- Add deterministic water and battery/power test vectors.
- Add NO/EN chapter parity contract and validation.
- Add provenance/freshness rules for verified country data.
- Document canonical book bootstrap contract.

## M3 — First toolkit implementation

- Create the Go module and `ploos-prep` CLI.
- Implement water, battery and power calculations from M2 test vectors.
- Add `--json` output conforming to the M2 schema.
- Add unit tests and offline help.
- Prepare GUI boundary without coupling core calculations to a UI.

## M4 — First book

Primary candidate: **Når strømmen går / When the Power Goes Out**.

Build a concise European household power-cut guide with Norwegian localisation, worksheets and toolkit integration.

## M5 — Radio series foundation

- Radio when networks are unavailable.
- ATS-20 receive-oriented guide.
- Baofeng handheld guide with jurisdiction-aware transmit guidance.
- Shared radio terminology and country profiles.

## Later

Water, rotating food storage, budget preparedness, apartment/cabin preparedness, digital preparedness, 72-hour starter guides and a comprehensive handbook.
