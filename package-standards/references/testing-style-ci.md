# Testing, Code Style, and Continuous Integration

Sources: <https://devguide.ropensci.org/pkg_building.html>,
<https://devguide.ropensci.org/pkg_ci.html>

## Testing

- All packages should pass `R CMD check` / `devtools::check()` on all major platforms.
- Have a test suite covering **major functionality and error behavior** (test that
  things fail the way they should, not just the happy path).
- **Coverage**: "Test coverage below 75% will likely require additional tests or
  explanation before being sent for review." Treat 75% as the line below which you
  must justify or add tests.
- Use **testthat** (or tinytest). Write tests as you write each function; keep
  tests self-contained; avoid code outside `test_that()` blocks.
- CRAN handling: `skip_on_cran()` for API calls that may fail on CRAN (since
  testthat 3.1.2 `skip_if_offline()` already calls `skip_on_cran()`), but those
  tests should still run on CI. Avoid long-running tests.
- Run tests locally before submitting (you may need `Sys.setenv(NOT_CRAN="true")`).
- Specialized tooling: **vdiffr** (plots, via snapshots), **shinytest2** (Shiny),
  HTTP testing via **httptest2 / httptest / vcr / webfakes** (see the "HTTP testing
  in R" book), **dittodb** (databases).

## Code style

- Follow the **tidyverse style guide** (<https://style.tidyverse.org/>).
- Auto-format with **Air** or **styler**; lint with **lintr**.
- Assignment: `=` or `<-` is fine as long as it's **consistent** within the
  package; avoid `->`. (R6 `=` inside `R6Class()` doesn't count as inconsistency.)
- Console output: use **cli** or base `message()`/`warning()`. Do **not** use
  `print()` or `cat()` except inside `print.*()` / `str.*()` methods — they're hard
  for users to suppress.
- Give users a way to opt out of verbosity, preferably at package level via an
  option/env var (like `usethis.quiet`) rather than a function argument; prefer
  multi-level ("none"/"inform"/"debug") over a binary switch.
- Use one consistent input-checking approach throughout the package.
- Startup messages: only when necessary (e.g. function masking). Avoid version
  banners and citation nags on attach.

## Cross-platform

- Packages should run on **Windows, macOS, and Linux**. Exceptions only for
  inherently system-specific functionality, and even then make every effort
  (system-specific compilation, containerizing external utilities).
- Monitor CRAN checks with **foghorn** or CRAN-checks badges.

## Continuous integration

- **Service**: GitHub Actions is recommended; usethis has first-class support.
  Use workflows from `r-lib/actions` (caching + multi-version testing built in).
- **R versions (required)**: test against the **latest, previous, and development**
  versions of R (release + oldrel + devel) for backward/forward compatibility.
- **Operating systems**: multi-OS testing is **required** when the package has
  compiled code, Java/other-language deps, system calls, encoding/text munging, or
  filesystem/path handling. When in doubt, add CI for all OSes.
- **What runs in CI**: `R CMD check` on all commits/PRs; unit tests; code
  coverage; and (after the repo transfers to the rOpenSci org) the pkgdown build.
- **Coverage tooling**: recommended **Codecov** —
  `usethis::use_github_action("test-coverage")`. Report both test status and
  coverage as **badges in the README**.
- **pkgcheck-action**: wire `ropensci-review-tools/pkgcheck-action` into CI so the
  package is continuously checked against rOpenSci's review checks before submission.

## pkgdown (after transfer to the rOpenSci org)

- Site rebuilds on the default branch, periodically, and on strong-dependency
  updates; it's styled with the `rotemplate`.
- For conditional execution use roxygen2 `@examplesIf` with the `IN_PKGDOWN` env
  var; in vignettes use `IN_PKGDOWN` + knitr eval options and cache HTTP responses
  with **vcr**.
