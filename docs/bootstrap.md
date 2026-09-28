# Bootstrapping a book repository

A new Ploos Preparedness book should be created from the shared book contract rather than copied from an older title.

Minimum initial structure:

```text
README.md
book.yaml
chapters.yaml
no/
en/
assets/
data/
references/
```

The initial manifest must validate against `schemas/book.schema.json`; chapter pairs declared with `parity: required` must exist in both language editions.

The book repository owns prose, book-specific assets and book-specific references. This repository owns shared contracts and reusable preparedness data. `Ploos-AS/publishing` owns production mechanics for HTML, EPUB, Kindle and PDF.

A future bootstrap command may materialise this template, but the template itself remains the canonical source.
