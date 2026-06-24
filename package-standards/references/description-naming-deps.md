# Naming, DESCRIPTION, and Dependencies

Source: <https://devguide.ropensci.org/pkg_building.html>

## Package naming

- Do **not** use a name already on CRAN or Bioconductor.
- **Strongly recommended**: short, descriptive, lower case.
- Check availability, informativeness, and whether it's offensive with
  `pak::pkg_name_check()` (this replaces the old `available` package).
- Search the web to confirm the name isn't offensive in another language and
  doesn't clash with a commercial service's branding guidelines.
- Trade-off: uniqueness (searchable/trackable) vs. discoverability (matches the topic).
- Heuristic to flag: anything with uppercase letters, dots, or unusual characters.

## Function and argument naming

- **Strongly recommend `snake_case`** over other styles, unless porting a package
  already in wide use with another convention.
- Consider an `object_verb()` scheme when functions share a data type or API
  (e.g. `stri_join()`, `stri_sort()`; `gs_auth()`, `gs_download()`).
- For functions that transform an object and return the same type, make that
  object the **first argument** (pipe-friendly).
- Avoid clashing with base R or popular packages (`ggplot2`, `dplyr`, `magrittr`,
  `data.table`).
- Keep argument names and order consistent across related functions.
- Functions should **return objects**, not assign into the global environment.

## DESCRIPTION file

- **Title**: Title Case, no trailing period, no "in R"/"with R". Single-quote
  external software/package names.
- **Description**: don't start with the package name or "This package…".
  Single-quote external software/package names. Wrap URLs in angle brackets
  `<https://...>`.
- **Authors@R** (required form): set roles — author (`aut`), creator (`cre`),
  contributor (`ctb`), reviewer (`rev`), copyright holder (`cph`). Add each
  person's ORCID via `comment = c(ORCID = "0000-...")`; organizations get a ROR ID.
  Add reviewers as `role = "rev"` **only with their consent**, with a comment
  that they reviewed for rOpenSci. **Do not list editors as contributors.**
- **License**: must be CRAN- or OSI-accepted. Mark copyright holders with `cph`
  (or a `Copyright` field / `inst/COPYRIGHTS` when needed).
- **URL** and **BugReports**: point to the repo/website and the issue tracker.
- **Bundled/derived code**: preserve copyright/license notices; don't
  misrepresent authorship; use `ctb`/`cph` as appropriate (CRAN Repository Policy).
- **Data-source packages**: include (1) a brief identification of the
  organisation issuing the data and (2) a URL to a public page describing/enabling
  data access.
- **SystemRequirements**: declare system deps; confirm they're in `sysreqsdb`;
  ship a `configure` script that checks for them and errors helpfully if missing.

## Dependency management

- **Fewer dependencies is generally better.**
- Use **`Imports`, not `Depends`**, for packages whose functions you use. To
  expose a dependency's functions to users, import and **re-export** them rather
  than using `Depends`.
- Put testing/doc tooling (testthat, knitr, roxygen2) and anything used only in
  examples/tests in **`Suggests`** (if not already in Imports).
- **Minimum versions** should be a conscious choice — only specify
  `pkg (>= x.y.z)` if the package actually breaks below that version.
- Import from where a function is **defined**, not re-exported
  (`magrittr::%>%`, not `dplyr::%>%`).
- Avoid deps added only for syntactic sugar; wrap base R instead. Avoid pulling in
  "modestly heavy" deps (e.g. **tibble** just to return tibbles). Don't duplicate
  functionality across overlapping deps.
- Small helper functions may be copied **with attribution** if the dep would
  otherwise be unused; don't copy complex functions (parsers, etc.).
- Check dependency health (actively maintained, not archived) — including
  GitHub-only deps.

### Preferred package per domain (discouraged → preferred)

| Task          | Prefer                          | Avoid                                         |
| ------------- | ------------------------------- | --------------------------------------------- |
| HTTP requests | `httr2`, `httr`, `curl`, `crul` | `RCurl`                                       |
| JSON          | `jsonlite`                      | `rjson`, `RJSONIO`                            |
| XML           | `xml2`                          | older XML packages                            |
| Spatial       | `sf`                            | `sp` (and retired `rgdal`/`maptools`/`rgeos`) |

- Bioconductor deps: give clear install instructions in README/vignette
  (recommend `BiocManager`) and note Bioconductor version requirements.

## Repo hygiene (version control)

- Track source with **Git**.
- Default branch must be **`main`**, not `master` (rename via `usethis`).
- `.gitignore`: ignore scrap like `.DS_Store`; use `usethis::git_vaccinate()` or
  the `gitignore` package.
- `.Rbuildignore`: include top-level non-package files (e.g. `paper.md`, CI configs).
