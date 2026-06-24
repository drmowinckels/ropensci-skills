# Scope, Fit, and Overlap Policy

Source: <https://devguide.ropensci.org/softwarereview_policies.html>

A package must fit rOpenSci's mission (the data lifecycle and scientific
reproducibility) and be **general in scope** — "solve a problem as broadly as
possible while maintaining a coherent user interface."

## In-scope categories

- **Data retrieval** — accessing/downloading data from online sources with
  scientific applications.
- **Data extraction** — retrieving data from unstructured sources (text, images,
  PDFs).
- **Data munging** — processing data from the formats above.
- **Data deposition** — depositing data into research repositories.
- **Data validation and testing** — automated validation/quality checking of data.
- **Workflow automation** — tools that automate and link workflows (e.g. build
  systems).
- **Version control** — facilitating version control in scientific workflows.
- **Citation management and bibliometrics.**
- **Scientific software wrappers** — wrapping non-R utility programs for research.
- **Field and laboratory reproducibility tools.**
- **Database software bindings** — wrappers for generic database APIs.
- **Geospatial data** — accessing/manipulating/converting geospatial formats.
- **Translation** — translation/publication of scientific resources.

**Interactive/GUI tools** must include a mechanism to make the workflow
reproducible, such as code generation.

## Out of scope

- Data visualization packages (explicitly no longer in scope).
- General computing utilities.
- Broad data-manipulation tools (reshape2-/tidyr-style).
- Generic cloud clients without a focused data source.
- Code parsers.

## Overlap policy

A new package that duplicates an existing one (rOpenSci or otherwise) must show a
**significant difference** in at least one of:

- license openness,
- breadth of functionality,
- usability,
- performance,
- maintenance status.

Merely following rOpenSci's guidelines is **not** a sufficient difference.

## When unsure

Open a **pre-submission enquiry** issue in `ropensci/software-review` rather than a
full submission. Editors will advise on scope and overlap before you invest in a
full submission.

## Author policies (commitments on submission)

- Maintain the package **at least 2 years**, or hand off to a new maintainer.
- Submit **before** CRAN release and before submitting any software paper.
- Don't submit multiple packages simultaneously.
- Respond to review feedback within weeks/months.
- Follow the packaging guide, the reviewer guide, and the code of conduct.
