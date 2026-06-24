---
name: stats-standards
description: >-
  Help authors and reviewers apply rOpenSci's Statistical Software peer review
  standards (stats-devguide.ropensci.org) to a statistical R package. Use this
  whenever a package implements a statistical method, model, or algorithm
  (Bayesian, regression, machine learning, EDA/summary stats, time series,
  spatial, dimensionality reduction/clustering, probability distributions) and
  someone wants to comply with or review against the rOpenSci statistical
  standards, document standards with the srr package (@srrstats tags), run srr or
  autotest, or understand the graded badges. This is an EXTENSION of the general
  rOpenSci process — always apply package-standards first; this skill
  adds the statistical standards on top.
---

# rOpenSci Statistical Software Standards

The statistical software review process is a **direct extension of the general
rOpenSci process**, not a replacement. Everything in `package-standards`
(naming, DESCRIPTION, docs, tests, CI, security) and `peer-review-author`
/ `package-review` still applies. **Start there.** This skill adds the
statistics-specific layer: explicit, machine-checkable **standards** documented in
code with the `srr` package.

**Using the reference efficiently.** The categories table and workflow below answer
the common "how does this work / what do I do" question on their own. Open
`references/standards-categories.md` only when you need the exact wording of a
specific standard or the full list for a category you're actually documenting — not
by default.

Primary sources: <https://stats-devguide.ropensci.org/>,
standards: <https://stats-devguide.ropensci.org/standards.html>,
srr: <https://docs.ropensci.org/srr/>.

## What "standards" means here

Unlike the general guide's "guidelines", statistical review centers on explicit
**standards** that can be tracked automatically:

- **General Standards** (`G`-prefixed, e.g. `G1.0`, `G2.0a`, `G5.4`) apply to
  **every** statistical package — documentation, input validation, algorithm
  robustness, output consistency, testing.
- **Category-specific standards** apply per analytical domain. Every package must
  comply with the **General Standards plus at least one category**.

Codes are hierarchical alphanumerics with decimal sub-standards (e.g. `G2.0a`,
`RE1.1`). The full text of all standards is in `references/standards-categories.md`.

### Categories

| Code      | Category                                                     |
| --------- | ------------------------------------------------------------ |
| `BS`      | Bayesian & Monte Carlo                                       |
| `EA`      | Exploratory Data Analysis & Summary Statistics               |
| `ML`      | Machine Learning                                             |
| `RE`      | Regression & Supervised Learning                             |
| `SP`      | Spatial                                                      |
| `TS`      | Time Series                                                  |
| `UL`/`US` | Dimensionality Reduction, Clustering & Unsupervised Learning |
| `PD`      | Probability Distributions                                    |

Pick every category your package touches; you must satisfy each category's
standards (or mark them not-applicable with a reason).

## Workflow for authors

1. **Make the package generally compliant first** with `package-standards`.
2. **Identify your categories** from the table above.
3. **Scaffold standards documentation** with srr:

   ```r
   srr::srr_stats_roxygen(category = c("regression"))   # your categories
   ```

   This writes `R/srr-stats-standards.R` pre-filled with every applicable standard
   as an `@srrstatsTODO` tag.

4. **Annotate the code.** For each standard, near the code that satisfies it,
   change the tag from `@srrstatsTODO` to either:
   - **`@srrstats "G2.0a" describe how this is met`** — the standard is satisfied;
     say where/how.
   - **`@srrstatsNA "RE1.2" reason it does not apply`** — the standard genuinely
     doesn't apply; give the reason.

   The srr roclet runs on `devtools::document()` / `roxygen2::roxygenise()` and
   reports the state of standards on screen. Leaving `@srrstatsTODO` tags means the
   documentation is incomplete.

5. **Generate the compliance report and pre-submission check:**

   ```r
   srr::srr_report()             # HTML report of standards coverage
   srr::srr_stats_pre_submit()   # completeness gate before submitting
   ```

6. **Run `autotest`** to catch undocumented/incorrect edge-case behavior — it
   mutates inputs to surface mishandled cases:

   ```r
   autotest::autotest_package()
   ```

7. Submit via the normal `ropensci/software-review` process (see
   `peer-review-author`). The editor verifies standards with
   `@ropensci-review-bot check srr`, and pkgcheck includes a "srr documentation
   complete" check.

## Workflow for reviewers

- Do everything in `package-review`, **plus** assess alignment against
  **each applicable standard** rather than just the general checklist.
- Read the `srr_report()` output: is each standard either satisfied (`@srrstats`)
  or justifiably not-applicable (`@srrstatsNA`)? Are the claims accurate?
- Check that the chosen categories actually cover what the package does.
- Confirm `autotest` issues are addressed or explained.

## Graded badges

Statistical packages receive **graded badges** publicizing how thoroughly they
meet standards (broader standards coverage and `autotest` / full-test compliance
earn higher grades). See <https://stats-devguide.ropensci.org/> for the current
tier definitions.

## Tooling summary

- **srr** — standards roclets: `srr_stats_roxygen()`, `@srrstats` / `@srrstatsNA`
  tags, `srr_report()`, `srr_stats_pre_submit()`.
- **autotest** — automated mutation/edge-case testing for statistical packages.
- **pkgcheck** / **@ropensci-review-bot check srr** — verify standards docs are
  complete.

## Related skills

- **Always apply first**: `package-standards` (general standards).
- Submission process: `peer-review-author`.
- Reviewing: `package-review`.
