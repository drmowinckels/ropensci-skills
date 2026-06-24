# Setting up `finchdata` for rOpenSci Standards

This covers every layer of setup in the order you'd actually do it: naming, scaffold, DESCRIPTION, code conventions, dependencies, API-client specifics, auth/security, docs, testing, and CI.

---

## 1. Package naming

Your name `finchdata` is fine — it's short, lowercase, and domain-specific. Before committing:

```r
pak::pkg_name_check("finchdata")
```

Check that it isn't on CRAN, Bioconductor, or a major GitHub namespace. rOpenSci prefers names that are either unique (easier to track mentions) or topic-descriptive (easier to discover). Avoid abbreviations that are ambiguous outside ornithology.

---

## 2. Scaffold with usethis

```r
usethis::create_package("finchdata")
usethis::use_git()
usethis::use_github()          # creates repo; use main as default branch
usethis::git_vaccinate()       # populates .gitignore with build artefacts
usethis::use_mit_license()     # or Apache 2.0 — must be OSI-accepted
usethis::use_readme_rmd()
usethis::use_news_md()
usethis::use_package_doc()     # creates R/finchdata-package.R
```

The resulting structure:

```
finchdata/
├── R/
├── tests/
│   └── testthat/
├── man/
├── vignettes/
├── DESCRIPTION
├── NAMESPACE
├── README.Rmd
├── NEWS.md
├── .gitignore
└── .Rbuildignore
```

---

## 3. DESCRIPTION

rOpenSci enforces specific conventions here:

```dcf
Package: finchdata
Title: Download Bird Observation Data from the Finch API   # Title Case, no period
Version: 0.0.0.9000
Authors@R: c(
    person("Your", "Name", role = c("aut", "cre"),
           email = "you@example.com",
           comment = c(ORCID = "0000-0000-0000-0000")),
    person("Org Name", role = "fnd",
           comment = c(ROR = "0XXXXXXXXX"))   # if applicable
  )
Description: Provides access to bird observation records from the Finch
    observation database <https://api.finch-obs.example.com>. Includes
    functions for querying species sightings, filtering by geography and
    date, and downloading structured datasets.
License: MIT + file LICENSE
URL: https://github.com/yourorg/finchdata, https://docs.ropensci.org/finchdata
BugReports: https://github.com/yourorg/finchdata/issues
Encoding: UTF-8
Roxygen: list(markdown = TRUE)
RoxygenNote: 7.x.x
```

Key rules:
- No "in R", "with R", or "This package" in Title or Description.
- Web API URL goes in Description inside angle brackets `<url>`.
- Use `Authors@R` syntax, not the deprecated `Author`/`Maintainer` fields.
- Include ORCID IDs; they're expected for rOpenSci authors.
- Identify the data-issuing organization and a public URL to the data source.

---

## 4. Code conventions

### Function naming

Use `snake_case` throughout. Follow the `object_verb()` scheme where the **data object comes first** (pipe-friendly):

```r
# Good
birds_fetch(species, region, date_range)
birds_search(query, ...)
finchdata_auth()          # package-level setup function

# Avoid
get_birds()               # verb first
fetchBirds()              # camelCase
```

### Messages and output

Never use `print()` or `cat()` for user-facing messages. Use `cli`:

```r
cli::cli_inform("Fetching {nrow} records from {.url {url}}")
cli::cli_abort("API returned {status}: {message}")
cli::cli_warn("Rate limit approaching; pausing {secs}s")
```

Provide a way to silence informational messages via an option or environment variable, not a function parameter:

```r
# In each messaging call
if (!getOption("finchdata.quiet", FALSE)) {
  cli::cli_inform(...)
}
```

### Global environment

Never assign to the global environment inside functions. Side effects must be scoped (e.g., using environments, options, or package-level caches).

### Input validation

Pick one consistent approach and apply it everywhere — base R `stopifnot()`, `rlang::arg_match()`, or a custom validation helper.

---

## 5. Dependencies

**Imports** (required at runtime):
- `httr2` — preferred over `httr` for new packages; handles requests, auth, rate limiting, retries cleanly
- `cli` — for all user-facing messages and errors
- `jsonlite` or `rlang` as needed

**Suggests** (only for testing/docs):
- `testthat (>= 3.0.0)`
- `httptest2` or `vcr` — for HTTP mocking in tests
- `knitr`, `rmarkdown` — for vignettes
- `withr` — for test environment management

Rule: use `Imports`, never `Depends` (except possibly R itself). Minimise the Imports list — each dependency is a maintenance burden and a potential failure point. Check that your dependencies are actively maintained.

```r
usethis::use_package("httr2")
usethis::use_package("cli")
usethis::use_package("testthat", type = "Suggests", min_version = "3.0.0")
usethis::use_package("httptest2", type = "Suggests")
usethis::use_package("knitr", type = "Suggests")
usethis::use_package("rmarkdown", type = "Suggests")
```

---

## 6. API client specifics

### User agent

Every request must identify your package:

```r
ua <- httr2::req_user_agent(
  req,
  paste0("finchdata/", utils::packageVersion("finchdata"),
         " (https://github.com/yourorg/finchdata)")
)
```

Allow the user to override via an option:

```r
user_agent <- getOption("finchdata.user_agent", default_ua())
```

### Authentication

Store credentials in environment variables, not in plain `.Renviron` files on shared systems. Recommend `keyring` for OS-level secure storage:

```r
finchdata_auth <- function(key = NULL) {
  if (is.null(key)) {
    key <- Sys.getenv("FINCHDATA_API_KEY")
    if (nzchar(key)) return(invisible(key))
    if (requireNamespace("keyring", quietly = TRUE)) {
      key <- keyring::key_get("finchdata")
    }
  }
  if (!nzchar(key)) {
    cli::cli_abort(c(
      "No API key found.",
      "i" = "Set {.envvar FINCHDATA_API_KEY} or run {.fn finchdata_auth} with your key."
    ))
  }
  invisible(key)
}
```

Never echo credentials in messages, warnings, or error text.

### Rate limiting and pagination

Use `httr2::req_throttle()` and `httr2::req_retry()` for rate limiting. Handle pagination internally so callers get a complete result without looping:

```r
birds_fetch_all <- function(...) {
  # fetch page 1, detect total, fetch remaining pages, bind results
}
```

### Error handling

Reproduce API errors with context. Prefer `httr2::resp_check_status()` and wrap with informative `cli_abort()` messages that explain what the API said and what the user can do.

---

## 7. Documentation

### Roxygen2 for every exported function

```r
#' Fetch bird observations
#'
#' Downloads observation records from the Finch API for a given species
#' and date range.
#'
#' @param species Character. IUCN species code (e.g., `"FINCH_001"`).
#' @param region Character. ISO 3166-1 alpha-2 country code.
#' @param date_range Date vector of length 2. Start and end dates (inclusive).
#' @param limit Integer. Maximum records to return. Default `500`.
#'
#' @return A data frame with columns: `id`, `species`, `lat`, `lon`, `date`,
#'   `observer_id`.
#'
#' @examples
#' \dontrun{
#'   birds_fetch("FINCH_001", region = "US", date_range = c(Sys.Date() - 30, Sys.Date()))
#' }
#'
#' @family finchdata-core
#' @export
birds_fetch <- function(species, region, date_range, limit = 500L) { ... }
```

Requirements:
- Every exported function has `@param`, `@return`, and `@examples`.
- `@return` must describe the object type and structure, not just "a data frame".
- Use `@family` tags to group related functions; pkgdown uses these for navigation.
- Use `\dontrun{}` for examples requiring auth or network access.

### Package-level docs

`R/finchdata-package.R` (created by `usethis::use_package_doc()`):

```r
#' @keywords internal
"_PACKAGE"
```

Add a one-paragraph description of the package and link to the API.

### Vignette

At minimum one HTML vignette with a realistic end-to-end workflow:

```r
usethis::use_vignette("finchdata")
```

If the vignette requires credentials, precompute it or use cached fixtures (see HTTP testing below). rOpenSci's docs server cannot use live credentials.

### README.Rmd

Must include:
- Badges: CI status, test coverage (Codecov), repostatus.org (`Active`), rOpenSci peer-review (added after review)
- Installation: both CRAN (`install.packages()`) and development (`pak::pak("yourorg/finchdata")`)
- Authentication setup
- A minimal working example
- Link to pkgdown site

```r
usethis::use_badge("repostatus", "Active", "https://www.repostatus.org/#active")
```

### pkgdown site

```r
usethis::use_pkgdown_github_pages()
```

After rOpenSci review and transfer, the site auto-deploys to `https://docs.ropensci.org/finchdata`.

---

## 8. Testing

### Setup

```r
usethis::use_testthat(edition = 3)
```

Use `describe()`/`it()` structure per your conventions:

```r
describe("birds_fetch()", {
  it("returns a data frame with expected columns", {
    resp <- birds_fetch_mock_fixture()
    expect_s3_class(resp, "data.frame")
    expect_named(resp, c("id", "species", "lat", "lon", "date", "observer_id"))
  })

  it("errors when no API key is set", {
    withr::with_envvar(list(FINCHDATA_API_KEY = ""), {
      expect_error(birds_fetch("FINCH_001"), "No API key found")
    })
  })
})
```

### HTTP mocking

Never make live HTTP calls in tests. Use `httptest2` (for httr2) or `vcr`:

```r
# httptest2 approach
httptest2::with_mock_api({
  test_that("birds_fetch returns expected shape", {
    result <- birds_fetch("FINCH_001", region = "US",
                          date_range = c(as.Date("2024-01-01"), as.Date("2024-01-31")))
    expect_s3_class(result, "data.frame")
  })
})
```

Inspect all recorded fixtures before committing — ensure no credentials, tokens, or PII are captured in the cassettes.

### Skip directives

```r
skip_on_cran()        # for any test touching network or credentials
skip_if_offline()     # implies skip_on_cran(); use for network-dependent tests
skip_if_no_token()    # custom helper checking FINCHDATA_API_KEY is set
```

### Coverage target

rOpenSci expects coverage to be above 75%, and reviewers will push for higher. Aim for 90%+ on core logic from the start. Set up Codecov:

```r
usethis::use_github_action("test-coverage")
```

---

## 9. Continuous integration

### GitHub Actions workflows

```r
usethis::use_github_action("check-standard")   # R CMD check on Linux/macOS/Windows
usethis::use_github_action("test-coverage")    # Codecov reporting
```

`check-standard` tests against: R release, R devel, R oldrel — on Ubuntu, macOS, and Windows. rOpenSci requires all three platforms to pass.

The YAML files land in `.github/workflows/`. Add them to `.Rbuildignore`:

```r
usethis::use_build_ignore(".github")
```

### What CI must do

- `R CMD check --as-cran` must pass with no ERRORs or WARNINGs (NOTEs are reviewed case-by-case)
- Test coverage reported to Codecov on every push and PR
- README.Rmd rendered to README.md on push (optional but recommended)

---

## 10. Security checklist for an API package

- [ ] Credentials stored in env vars; `keyring` recommended for interactive use
- [ ] Credentials never appear in message/warning/error text
- [ ] GitHub issue template warns users not to paste tokens
- [ ] `vcr`/`httptest2` fixtures inspected for secrets before first commit
- [ ] HTTPS enforced (never fall back to HTTP)
- [ ] `skip_on_cran()` on all credential-dependent tests
- [ ] Examples using auth wrapped in `\dontrun{}`

---

## 11. Checklist before rOpenSci submission

- [ ] `R CMD check` clean on all three platforms
- [ ] Test coverage above 75% (aim for 90%)
- [ ] All exported functions documented with `@return` and `@examples`
- [ ] At least one vignette with a realistic use case
- [ ] `README.Rmd` with badges, install instructions, and a working example
- [ ] `NEWS.md` started
- [ ] `CITATION` file created (`usethis::use_citation()`)
- [ ] pkgdown site builds locally
- [ ] `pak::pkg_name_check("finchdata")` passes
- [ ] No live HTTP calls in tests
- [ ] Repostatus badge set to `Active`
- [ ] License is OSI-accepted

Submit via the rOpenSci software review portal at <https://github.com/ropensci/software-review/issues>.

---

## Quick-reference: key packages and tools

| Task | Tool |
|------|------|
| HTTP requests | `httr2` |
| User messages/errors | `cli` |
| Credential storage | `keyring` + env vars |
| HTTP test mocking | `httptest2` (httr2) or `vcr` |
| Code style | `air` (formatter) + `lintr` |
| Package setup | `usethis` |
| Docs website | `pkgdown` |
| Name check | `pak::pkg_name_check()` |
| CRAN check monitoring | `foghorn` |
