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

## M3 — First toolkit implementation — DONE

- Go module and `ploos-prep` CLI.
- Water, battery and power calculations from M2 test vectors.
- `--json` output conforming to the M2 contract.
- Unit and contract tests plus CI build qualification.
- UI-independent calculation core.

## M4 — First book bootstrap — DONE

**Når strømmen går / When the Power Goes Out** now has its canonical manifest, nine-chapter NO/EN structure, opening manuscript, worksheet contract and CI parity validation under `books/power/`.

The source is ready to move to a dedicated book repository when that repository is created.

## M5 — Radio series foundation

- Radio when networks are unavailable.
- ATS-20 receive-oriented guide.
- Baofeng handheld guide with jurisdiction-aware transmit guidance.
- Shared radio terminology and country profiles.

## Later

Water, rotating food storage, budget preparedness, apartment/cabin preparedness, digital preparedness, 72-hour starter guides and a comprehensive handbook.
