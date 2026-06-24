# Documentation: roxygen2, README, Vignettes

Source: <https://devguide.ropensci.org/pkg_building.html>

## roxygen2

- rOpenSci **requests all submissions use roxygen2** (it also generates NAMESPACE;
  Markdown is supported).
- **All exported functions** must be fully documented **with examples**.
- Document every function's return value with `@return`.
- Document all parameters with `@param`, clearly indicating default values.
- Provide top-level package documentation so `?pkgname` works
  (`usethis::use_package_doc()`).
- Use `@family` to group related functions and cross-link "See also".
- Internal functions: `#' @keywords internal`; use `@noRd` to skip generating an
  `.Rd` file.
- R6 classes are supported (roxygen2 ≥ 7.0.0).

### Examples

- Include extensive, **runnable** examples. Examples not wrapped in `\dontrun{}`
  or `\donttest{}` run during `R CMD check`.
- Use `@examplesIf` for conditional examples; reserve `\dontrun{}` for examples
  that are long-running or need credentials.
- Run locally with `devtools::run_examples()`; on CI use `--run-dontrun` /
  `--run-donttest`.
- Note: pkgcheck flags `\dontrun{}` in examples — prefer `@examplesIf` where you can.

## README

- Every package needs a `README.md` at the repo root, **generated from
  `README.Rmd`** (`usethis::use_readme_rmd()`).
- The README must let an editor/reader assess the package **without installing
  it**, and should assume **little to no domain knowledge** — clarify all
  technical terms.
- Recommended sections, in order:
  1. Package name
  2. Badges: CI, test coverage, repostatus.org, rOpenSci peer-review (once
     started), optionally R-universe
  3. Short goal description with links to vignettes
  4. Installation instructions (remotes/pak/R-universe)
  5. Extra setup if needed (auth tokens, etc.)
  6. Brief usage demonstration
  7. Comparison/relationship to similar packages
  8. Citation info pointing to the preferred citation
- Link a code of conduct and contribution guidelines.
- With many badges, consider an HTML table (Development / Release / Stats),
  "more wide than long."
- rOpenSci peer-review badge (once accepted):
  `[![rOpenSci](https://badges.ropensci.org/<issue_id>_status.svg)](https://github.com/ropensci/software-review/issues/<issue_id>)`

## Vignettes

- At least **one HTML vignette** giving substantial coverage of the package's
  functions with realistic use cases.
- Examples should progress **basic → advanced**; state prerequisite knowledge up
  front; cite software/papers where appropriate.
- Advanced/developer functionality can go in a separate vignette.
- Data-access packages: give real context (don't just say "Provides access to
  GooberDB" — explain what GooberDB is and link its docs).

## CITATION

- Create with `usethis::use_citation()` if missing; use `bibentry()` (not the
  deprecated `citEntry()`).
- Add a Zenodo concept DOI if you archive releases; add the software paper after
  rOpenSci review; for wrapped data/algorithms use `citHeader()` to tell users how
  to cite the underlying source.
