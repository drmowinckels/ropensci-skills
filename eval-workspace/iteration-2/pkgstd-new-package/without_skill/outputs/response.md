# Setting Up `finchdata` as an rOpenSci-Compliant R Package

Here is a complete walkthrough covering every aspect of an rOpenSci-compliant package from scratch.

---

## 1. Create the Package Skeleton

Use `usethis` throughout — it handles boilerplate and keeps infrastructure consistent.

```r
usethis::create_package("finchdata")
```

This creates the minimal structure:

```
finchdata/
├── DESCRIPTION
├── NAMESPACE
├── R/
└── .Rbuildignore
```

---

## 2. DESCRIPTION

This is the most important metadata file. Fill it out carefully.

```dcf
Package: finchdata
Title: Download Bird Observation Data from <API Name>
Version: 0.0.0.9000
Authors@R: 
    person("Your", "Name", , "you@example.com", role = c("aut", "cre"),
           comment = c(ORCID = "0000-0000-0000-0000"))
Description: Provides functions to query and download bird observation
    records from the <API Name> API. Supports filtering by species,
    region, date range, and observation type.
License: MIT + file LICENSE
URL: https://github.com/yourorg/finchdata,
    https://yourorg.github.io/finchdata
BugReports: https://github.com/yourorg/finchdata/issues
Encoding: UTF-8
Roxygen: list(markdown = TRUE)
RoxygenNote: 7.x.x
Imports:
    cli,
    httr2,
    rlang
Suggests:
    httptest2,
    knitr,
    rmarkdown,
    testthat (>= 3.0.0),
    vcr (>= 0.6.0),
    withr
Config/testthat/edition: 3
VignetteBuilder: knitr
```

Key points:
- Version `0.0.0.9000` signals active development (pre-release)
- `Authors@R` with ORCID — rOpenSci requires this
- `MIT + file LICENSE` is strongly preferred by rOpenSci
- `URL` includes both the GitHub repo and the pkgdown site
- `BugReports` must point to the GitHub issues page
- `Roxygen: list(markdown = TRUE)` enables Markdown in docs

---

## 3. LICENSE

```r
usethis::use_mit_license()
```

This creates `LICENSE` and `LICENSE.md`. Never omit the `LICENSE.md` — rOpenSci's `pkgcheck` will flag it.

---

## 4. Package-Level Documentation

Create `R/finchdata-package.R`:

```r
#' @keywords internal
"_PACKAGE"

## usethis namespace: start
#' @importFrom rlang abort
## usethis namespace: end
NULL
```

This gives `?finchdata` a landing page and is the correct place for `@importFrom` directives that apply package-wide.

---

## 5. File and Function Naming

rOpenSci conventions:
- One file per logical unit: `R/observations.R`, `R/species.R`, `R/auth.R`
- Function names: `snake_case`, verb-first where it reads naturally — `get_observations()`, `search_species()`, `fetch_checklist()`
- No dots in function names (reserved for S3 method dispatch and old-style R)
- Internal helpers: prefix with a dot or keep them unexported — `finchdata_request()` (package-prefixed unexported helper)
- Avoid generic names that shadow base R: never name a function `get()`, `print()`, or `format()` unless you are defining an S3 method

Suggested file layout:

```
R/
├── finchdata-package.R   # package doc + global imports
├── auth.R                # API key management
├── observations.R        # core data download functions
├── species.R             # species lookup helpers
├── utils.R               # internal helpers (unexported)
└── zzz.R                 # .onLoad / .onAttach if needed
```

---

## 6. HTTP Client: Use `httr2`

rOpenSci recommends `httr2` (not `httr`, not `curl` directly) for new packages.

A minimal pattern in `R/utils.R`:

```r
finchdata_base_url <- function() {
  "https://api.example-bird-db.org/v2"
}

finchdata_request <- function(endpoint, ...) {
  key <- finchdata_api_key()
  httr2::request(finchdata_base_url()) |>
    httr2::req_url_path_append(endpoint) |>
    httr2::req_headers(Authorization = paste("Bearer", key)) |>
    httr2::req_user_agent("finchdata R package (https://github.com/yourorg/finchdata)") |>
    httr2::req_error(is_error = \(resp) FALSE) |>
    httr2::req_perform()
}
```

Always set a `User-Agent` that identifies your package and links to its source. The API maintainer can contact you if there are problems.

---

## 7. API Key Management

Never store secrets in code. Follow the rOpenSci best practice: read from an environment variable, with a clear error if it is missing.

```r
finchdata_api_key <- function(key = NULL) {
  if (!is.null(key)) return(key)
  val <- Sys.getenv("FINCHDATA_API_KEY", unset = NA)
  if (is.na(val)) {
    cli::cli_abort(
      c(
        "No API key found.",
        i = "Set {.envvar FINCHDATA_API_KEY} in your {.file .Renviron}.",
        i = "Run {.run usethis::edit_r_environ()} to open that file."
      )
    )
  }
  val
}
```

Document this in a vignette and in the function's `@details`. Tell users to put the key in `.Renviron`, not in scripts.

---

## 8. Error Handling and Messages

Use `cli` for all user-facing messages — never `cat()`, `message()`, or `warning()` directly.

```r
# abort (error)
cli::cli_abort("Request failed with status {resp$status_code}.")

# warn
cli::cli_warn("Rate limit approaching: {remaining} requests left.")

# inform
cli::cli_inform("Fetched {nrow(df)} observations.")
```

Use `rlang::abort()` / `rlang::warn()` when you need structured conditions (for programmatic handling by callers). For human-readable messages, `cli` wrappers are preferred.

---

## 9. Documentation with roxygen2

Every exported function needs a full roxygen2 block:

```r
#' Get bird observations
#'
#' Downloads observation records for one or more species from the
#' <API Name> API.
#'
#' @param species Character. One or more species codes (e.g. `"HOFI"`).
#' @param region Character. ISO 3166-1 alpha-2 country code, or a
#'   sub-national region code.
#' @param start_date,end_date Date or character in `"YYYY-MM-DD"` format.
#'   Defaults to the last 30 days.
#' @param key Character. API key. If `NULL` (default), reads from the
#'   `FINCHDATA_API_KEY` environment variable.
#'
#' @return A data frame with one row per observation and columns:
#'   \describe{
#'     \item{species_code}{Four-letter species code.}
#'     \item{common_name}{Common name of the species.}
#'     \item{lat, lng}{Decimal latitude and longitude.}
#'     \item{observed_at}{POSIXct timestamp in UTC.}
#'   }
#'
#' @export
#' @examples
#' \dontrun{
#'   obs <- get_observations("HOFI", region = "US-CA")
#' }
get_observations <- function(species, region, start_date = NULL,
                              end_date = NULL, key = NULL) {
  ...
}
```

Requirements:
- Every `@param` documented
- `@return` describes the structure and columns of returned data frames
- `@examples` present; use `\dontrun{}` only for examples that require a live API key or internet — this is expected and fine
- `@seealso` links to related functions when helpful

Run `devtools::document()` after edits; never manually edit `NAMESPACE` or `.Rd` files.

---

## 10. NEWS.md

```r
usethis::use_news_md()
```

Maintain it from day one:

```markdown
# finchdata (development version)

* Added `get_observations()` to download species records (#1).
* Added `search_species()` for taxonomic lookup.
```

rOpenSci requires a `NEWS.md` at the root and enforces a specific format. Each item should reference a GitHub issue or PR number.

---

## 11. README

```r
usethis::use_readme_rmd()
```

Use `README.Rmd` (not `.md`) so examples stay executable. Structure:

1. One-sentence description
2. Installation (CRAN + dev via `pak` or `remotes`)
3. A working example (even if it needs a fake API key and `\dontrun`)
4. Link to the pkgdown site
5. rOpenSci peer review badge once submitted

Render with `devtools::build_readme()` before every commit that touches it.

---

## 12. Vignette

```r
usethis::use_vignette("finchdata")
```

Write at least one vignette showing the full workflow: authenticate, query, process results. Use `eval = FALSE` for chunks that hit the live API so the vignette builds on CRAN and CI without credentials.

---

## 13. Tests

```r
usethis::use_testthat(edition = 3)
```

**Mocking API calls** — this is mandatory for a package that hits a live API. Use `vcr` or `httptest2`:

```r
usethis::use_package("vcr", type = "Suggests")
usethis::use_package("httptest2", type = "Suggests")
```

`vcr` is the rOpenSci standard for recording and replaying HTTP fixtures.

Test file structure (`tests/testthat/test-observations.R`):

```r
describe("get_observations()", {
  it("returns a data frame with expected columns", {
    vcr::use_cassette("get_observations_hofi", {
      result <- get_observations("HOFI", region = "US-CA")
    })
    expect_s3_class(result, "data.frame")
    expect_named(result, c("species_code", "common_name", "lat", "lng", "observed_at"))
  })

  it("errors when API key is missing", {
    withr::with_envvar(c(FINCHDATA_API_KEY = NA), {
      expect_error(get_observations("HOFI"), "No API key")
    })
  })

  it("errors informatively on a 401 response", {
    vcr::use_cassette("get_observations_401", {
      expect_error(get_observations("HOFI"), class = "finchdata_auth_error")
    })
  })
})
```

Store VCR cassettes in `tests/fixtures/` and commit them. This lets CI run without network access and a real key.

---

## 14. pkgdown Site

```r
usethis::use_pkgdown()
usethis::use_pkgdown_github_pages()
```

`_pkgdown.yml` minimal structure:

```yaml
url: https://yourorg.github.io/finchdata

template:
  bootstrap: 5

reference:
  - title: Observations
    contents:
      - get_observations
      - search_species
  - title: Authentication
    contents:
      - finchdata_api_key
```

rOpenSci provides its own pkgdown template for packages that pass peer review:

```yaml
template:
  package: rotemplate
```

Add it after submission — not before.

---

## 15. CI with GitHub Actions

```r
usethis::use_github_actions()
usethis::use_github_action("check-standard")   # R CMD check on mac/win/linux
usethis::use_github_action("test-coverage")    # covr + Codecov
usethis::use_github_action("pkgdown")          # build + deploy docs
```

All three are r-lib/actions-based, which is the rOpenSci standard. The resulting `.github/workflows/` directory should contain:

- `R-CMD-check.yaml` — matrix over R versions and OS
- `test-coverage.yaml` — reports to Codecov
- `pkgdown.yaml` — deploys to GitHub Pages on push to main

Add a Codecov token secret in the repo settings and a coverage badge to the README.

---

## 16. `.Rbuildignore` and `.gitignore`

`usethis` manages `.Rbuildignore` automatically. Make sure these entries are present:

```
^\.github$
^_pkgdown\.yml$
^docs$
^\.Renviron$
^\.env$
```

Never commit `.Renviron` or any file containing a real API key.

---

## 17. `pkgcheck` — rOpenSci's Automated Review Tool

Before submitting for peer review, run:

```r
# install if needed
# install.packages("pkgcheck", repos = "https://ropensci.r-universe.dev")
pkgcheck::pkgcheck()
```

This replicates the automated checks run by the rOpenSci bot. Fix everything it flags before opening a submission issue.

Common checklist items:
- `goodpractice::gp()` passes
- No `T`/`F` instead of `TRUE`/`FALSE`
- No `1:length(x)` patterns
- `DESCRIPTION` has `URL` and `BugReports`
- `LICENSE.md` present
- `NEWS.md` present and parseable
- Exported functions have examples

---

## 18. Submission to rOpenSci

Once `pkgcheck` is clean:

1. Open a submission issue at https://github.com/ropensci/software-review/issues using the template
2. The bot runs automated checks and posts results
3. An editor triages within ~2 weeks; reviewers are assigned after scope confirmation
4. Address reviewer comments on your package repo; cross-reference the review issue in commits/PRs

---

## Summary: Files to Create

| File | How |
|---|---|
| `DESCRIPTION` | `usethis::create_package()` then edit |
| `LICENSE`, `LICENSE.md` | `usethis::use_mit_license()` |
| `R/finchdata-package.R` | manually |
| `R/observations.R` etc. | manually |
| `NEWS.md` | `usethis::use_news_md()` |
| `README.Rmd` | `usethis::use_readme_rmd()` |
| `vignettes/finchdata.Rmd` | `usethis::use_vignette()` |
| `tests/testthat/` | `usethis::use_testthat(3)` |
| `_pkgdown.yml` | `usethis::use_pkgdown()` |
| `.github/workflows/` | `usethis::use_github_action(...)` |
| `cran-comments.md` | `usethis::use_cran_comments()` (later) |

---

## Dependency Philosophy

- **`httr2`** for HTTP — modern, pipe-friendly, handles retries/rate-limiting
- **`cli`** for all messages — rOpenSci strongly prefers it
- **`rlang`** for error conditions and tidy eval if needed
- Avoid heavy dependencies (`tidyverse`, `data.table`) in `Imports` — put them in `Suggests` if only used in examples/vignettes
- Never import a package just for one function; use `package::function()` notation for infrequent calls, or list the specific import in `@importFrom`

The goal is to keep the dependency footprint minimal so users don't get dependency conflicts when installing `finchdata` alongside other packages.
