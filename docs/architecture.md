# Architecture

## Purpose

`preparedness` is the common platform behind **Ploos Preparedness** and **Ploos Beredskap**. It is not intended to contain every finished book. Individual books may live in their own repositories while consuming the policies, schemas, templates and reusable data defined here.

## Layers

1. **Editorial layer** — scope, tone, sourcing, safety and translation policy.
2. **Data layer** — reusable common facts and country-specific facts.
3. **Book layer** — templates and conventions for bilingual book repositories.
4. **Tool layer** — offline-first calculators, planners and checklists.
5. **Publishing layer** — delegated to the Ploos `publishing` project for HTML, EPUB, Kindle-compatible and PDF output.
6. **CI layer** — validation, links, schemas, language parity and publishing qualification.

## Book repository convention

```text
book-name/
├── README.md
├── book.yaml
├── no/
│   ├── 00-forord.md
│   └── ...
├── en/
│   ├── 00-preface.md
│   └── ...
├── assets/
├── data/
├── references/
└── .github/workflows/
```

The Norwegian and English trees should have equivalent editorial coverage, but they do not need sentence-by-sentence identity.

## Shared data

Country-specific facts should be represented as structured data wherever practical. This supports validation, reuse and clearly scoped claims.

Examples include:

- electrical system assumptions;
- emergency numbers;
- official preparedness authorities;
- radio services and regulatory notes;
- country-specific terminology;
- source URLs and verification dates.

The data model must distinguish factual values from explanatory prose and should carry provenance for safety- or regulation-sensitive fields.

## Tools

A future `ploos-prep` tool family should provide reusable calculations and planning functions, initially:

```text
ploos-prep water
ploos-prep food
ploos-prep power
ploos-prep battery
ploos-prep radio
ploos-prep checklist
```

Core requirements:

- offline-first;
- deterministic calculations where applicable;
- no mandatory account or cloud service;
- no telemetry by default;
- SI units first;
- country profile selectable where regulation or infrastructure differs;
- CLI suitable for scripting plus a friendly GUI/web experience later.

## Publishing integration

`preparedness` owns preparedness-specific standards and content conventions. The shared Ploos `publishing` project owns general publishing mechanics, metadata conventions and multi-format production.

Book CI should eventually qualify all four first-class outputs:

- HTML
- EPUB
- Kindle-compatible package
- PDF

## CI direction

M1 should add machine validation for:

- YAML/schema correctness;
- required provenance on regulated/safety-sensitive data;
- internal links;
- NO/EN chapter manifest parity;
- publishing metadata;
- stale verification dates;
- generated artefact smoke tests.
