# CI and Publishing Integration

Ploos Preparedness follows the shared Ploos-AS project standards rather than duplicating common infrastructure.

## Publishing

The canonical publishing implementation lives in the Ploos-AS `publishing` project.

Preparedness book repositories should consume that pipeline for all first-class publication formats:

- HTML
- EPUB
- Kindle-compatible output
- PDF

Preparedness-specific repositories own content, metadata, localisation and preparedness validation. They should not fork general publishing logic unless a narrowly scoped extension is unavoidable.

## CI

General repository validation should use shared Ploos-AS CI conventions. Preparedness-specific checks may be added locally when they concern:

- book manifests;
- NO/EN structural parity;
- provenance and verification dates;
- country data schemas;
- preparedness safety policy;
- publishing qualification.

## hardware-ci

The shared `hardware-ci` standard should be used by preparedness projects only when a project actually has hardware qualification needs, for example reproducible testing of a radio accessory, measurement device or other physical companion hardware.

Pure books, data repositories and software-only calculators must not add hardware CI merely for consistency.

When hardware qualification is relevant, depend on the canonical Ploos-AS `hardware-ci` action/tag rather than copying its implementation into this repository.

## Release qualification

A finished book release should eventually require:

1. content validation;
2. provenance validation for regulated/safety-sensitive claims;
3. localisation checks;
4. successful builds for HTML, EPUB, Kindle-compatible output and PDF;
5. publication metadata validation;
6. release artefact smoke tests.
