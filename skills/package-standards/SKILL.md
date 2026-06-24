---
name: package-standards
description: >-
  Build or audit an R package so it meets rOpenSci's package development
  standards from the rOpenSci Developer Guide (devguide.ropensci.org). Use this
  whenever someone is writing, reviewing, refactoring, or preparing an R package
  and wants it to follow rOpenSci / tidyverse best practices — even if they only
  say "make my package better", "is this package up to standard", "set up CI",
  "fix my DESCRIPTION", "add roxygen docs", or "get this ready for CRAN/rOpenSci".
  Covers package naming, DESCRIPTION and Authors@R, dependency choices, roxygen2
  documentation, README, testing and coverage, code style, continuous
  integration, and security. This is the foundation skill; the peer-review,
  stats-standards, release, and maintenance skills build on it.
---

# rOpenSci Package Standards

This skill encodes the standards from the **"Building Your Package"** part of the
rOpenSci Developer Guide so you can build a new package to spec or audit an
existing one. The goal is a package that would pass rOpenSci software peer review.

**Using the references efficiently.** The checklist and workflow below are written
to answer the common case on their own — a DESCRIPTION/naming/dependency audit, a
"what do I fix" review, or a CI question can almost always be answered from the
checklist without opening anything. Reach for a `references/` file only when you hit
the long tail it adds beyond the checklist (e.g. `description-naming-deps.md` for
`SystemRequirements`, bundled-code attribution, data-source-package rules, or
function/argument naming schemes). A broad "set up a whole package from scratch"
request may legitimately need a couple of references; a narrow question usually needs
none. Reading a reference you don't need just spends context.

## How rOpenSci phrases standards (so you flag the right things)

The guide distinguishes hard requirements from suggestions, and you should too:

- **"require" / "must"** → a gate. Flag non-compliance as a problem that blocks review.
- **"strongly recommend"** → flag it, but as a strong recommendation, not a blocker.
- **"recommend" / "consider"** → mention as an improvement, don't be heavy-handed.

Don't turn every soft recommendation into a blocking error — that erodes trust.
Report what's actually required separately from what's nice to have.

## Workflow

1. **Figure out the starting point.** Is this a new package or an existing one?
   For an existing package, read `DESCRIPTION`, the `R/` files, `tests/`,
   `README`, and the CI config under `.github/workflows/` before judging anything.

2. **Prefer the automated gate.** rOpenSci checks every submission with
   [`pkgcheck`](https://docs.ropensci.org/pkgcheck/). If R is available, the
   fastest path to a real answer is to run it rather than eyeballing:

   ```r
   pkgcheck::pkgcheck()        # local report
   ```

   or wire in the GitHub Action `ropensci-review-tools/pkgcheck-action`. Treat a
   clean pkgcheck run as the source of truth; use this skill to interpret and fix
   what it flags, and to cover the things pkgcheck can't see (doc quality, vignette
   usefulness, API design).

3. **Audit/build by area.** The checklist below covers the gates for each area;
   reach for a reference only when you need the exact rule, list, or procedure for
   the specific area in front of you. Work in this order — earlier items unblock later:
   - Naming, DESCRIPTION, dependencies → `references/description-naming-deps.md`
   - Documentation: roxygen2, README, vignettes → `references/documentation.md`
   - Testing, code style, CI, cross-platform → `references/testing-style-ci.md`
   - Security (secrets, fixtures, CI) → `references/security.md`

4. **Use `usethis` to scaffold**, don't hand-write boilerplate. It produces
   exactly the structure rOpenSci expects: `use_readme_rmd()`, `use_testthat()`,
   `use_vignette()`, `use_citation()`, `use_package_doc()`, `use_github_action()`,
   `use_tidy_contributing()`, `git_vaccinate()`.

5. **Report** as two lists: **Required fixes** (gates) and **Recommendations**.
   Tie each item to the area it came from so the user can act on it.

## The quick checklist (the gates worth memorizing)

These are the high-signal, frequently-missed requirements — enough to answer most
audit and setup questions directly. Only open the matching reference when you need
the detail or long tail behind one of these lines.

- **Name**: lowercase, not already on CRAN/Bioconductor; check with `pak::pkg_name_check()`.
- **Title**: Title Case, no trailing period, and no "in R"/"with R" (R is implied);
  single-quote external software/package names.
- **Description**: don't start with the package name or "This package…"; lead with
  what it does; wrap URLs in `<angle brackets>`.
- **License**: a CRAN- or OSI-accepted license, with copyright holders marked `cph`.
- **Authors@R**: roles set; ORCIDs via `comment = c(ORCID = ...)`; don't list editors.
- **Dependencies**: `Imports` not `Depends` (re-export rather than `Depends` if you
  must expose a dep); test/doc tooling in `Suggests`; fewer is better. Prefer the
  modern package per domain: HTTP → `httr2`/`httr`/`curl`/`crul` (not `RCurl`);
  JSON → `jsonlite` (not `rjson`/`RJSONIO`); XML → `xml2`; spatial → `sf` (not
  `sp`/`rgdal`). Don't add a dep for syntactic sugar you can write in base R.
- **Docs**: roxygen2 for everything; every exported function has `@param`, `@return`,
  and a runnable `@examples`; package-level `?pkgname` doc exists.
- **README**: generated from `README.Rmd`; has badges (CI, coverage, repostatus),
  install instructions, a usage demo, and citation info — readable with no domain knowledge.
- **Vignette**: at least one HTML vignette with a realistic, basic→advanced walkthrough.
- **Tests**: a testthat suite covering major functionality _and_ error paths;
  **coverage below 75% needs justification** before review.
- **Code style**: tidyverse style (Air or styler to format, lintr to check);
  use cli/`message()` for output, never `print()`/`cat()` outside print methods.
- **CI**: GitHub Actions running `R CMD check` on **release, oldrel, and devel** R;
  coverage reported (Codecov); badges in README. Multi-OS when there's compiled
  code, system calls, encoding/text work, or path handling.
- **Repo hygiene**: Git; default branch `main` not `master`; `NEWS.md` present;
  `.Rbuildignore` and `.gitignore` populated (`usethis::git_vaccinate()`).
- **Secrets**: API keys from env vars / keyring, never printed; fixtures scrubbed.

## Related skills

- Preparing to **submit** for peer review → `peer-review-author`.
- A **statistical** package → `stats-standards` (this skill still applies;
  stats adds machine-checkable standards on top).
- **Releasing** (NEWS, versioning, CRAN, GitHub release) → `package-release`.
- **Maintaining** (CONTRIBUTING, CoC, lifecycle, archiving) → `package-maintenance`.

Primary sources: <https://devguide.ropensci.org/pkg_building.html>,
<https://devguide.ropensci.org/pkg_ci.html>,
<https://devguide.ropensci.org/pkg_security.html>.
