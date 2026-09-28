# Ploos Preparedness / Ploos Beredskap

Practical, calm and evidence-oriented preparedness for Europe.

**Ploos Preparedness** is the English, Europe-first edition of the project.  
**Ploos Beredskap** is the Norwegian edition, with Norway-first guidance where national rules, authorities or infrastructure matter.

This repository is the shared platform for the series: editorial policy, book templates, reusable structured data, schemas, tooling conventions and publishing integration.

## Principles

- Practical preparedness, not fear-based marketing.
- Europe-first assumptions in English-language material.
- Norway-first localisation in Norwegian-language material.
- SI units by default.
- Country-specific rules are treated as data and clearly scoped.
- Receiving and transmitting by radio are always distinguished.
- Legal, safety and regulatory claims should identify jurisdiction and source/date.
- Books should be useful offline.
- Shared facts should be reusable across books without coupling prose to one country.
- Norwegian and English editions are editorial siblings, not blind translations.

## Project layers

```text
preparedness
├── policy and standards
├── reusable country/common data
├── book and chapter templates
├── schemas and validation
├── toolkit specifications
└── publishing/CI integration

individual book repositories
├── no/       Norwegian edition
├── en/       European English edition
├── assets/
├── data/
└── book.yaml
```

Candidate books include:

- *Når strømmen går* / *When the Power Goes Out*
- *ATS-20 for beredskap* / *ATS-20 for Preparedness*
- *Baofeng for beredskap* / *Baofeng for Preparedness*
- *Radio når nettet er nede* / *Radio When the Network Is Down*
- *Digital beredskap* / *Digital Preparedness*
- *Beredskap på budsjett* / *Preparedness on a Budget*
- *72 timer* / *72 Hours*

## Publishing

Book projects are intended to build from shared sources to:

- HTML
- EPUB
- Kindle-compatible package
- PDF

Production should integrate with the Ploos `publishing` repository rather than duplicating publishing logic here.

## Tooling

The future **Ploos Preparedness Toolkit** should work offline and expose reusable calculations through both CLI and a user-friendly application. Initial modules are expected to cover water, food, power/batteries, radio planning and checklists.

See [`docs/architecture.md`](docs/architecture.md) and [`docs/roadmap.md`](docs/roadmap.md).

## Status

**M2 — toolkit and reusable data contracts**

The repository now defines reusable book/data/tool contracts, provenance and NO/EN parity validation, an offline-first toolkit architecture and a canonical book bootstrap. See [`docs/m2.md`](docs/m2.md).

## Licensing

See [`LICENSES.md`](LICENSES.md). Different parts of the repository may use different licenses according to their role; applicability is documented explicitly.
