# Setting up `finchdata` to rOpenSci standards

Here is a complete walkthrough covering every area rOpenSci checks, in the order you should tackle them.

---

## 1. Package name

`finchdata` is lowercase, descriptive, and readable — it passes the style heuristic. Before going further, verify it is not already taken:

```r
pak::pkg_name_check("finchdata")
```

Also do a quick web search to confirm it does not clash with any commercial product or carry unintended meaning in another language.

---

## 2. Scaffold with `usethis`

Start from a clean scaffold rather than hand-writing boilerplate. All of the following produce exactly the structure rOpenSci expects:

```r
usethis::create_package("finchdata")
usethis::use_readme_rmd()
usethis::use_news_md()
usethis::use_testthat()
usethis::use_vignette("finchdata")
usethis::use_package_doc()
usethis::use_citation()
usethis::git_vaccinate()          # populates .gitignore and .Rbuildignore
usethis::use_mit_license()        # or whichever OSI-accepted license you choose
```

Set Git up with the default branch named `main` (not `master`):

```r
usethis::use_git()
# if you already have a repo on GitHub and want to rename the branch:
# git branch -m master main
```

---

## 3. DESCRIPTION

Fill in every field carefully — reviewers read this closely.

```
Package: finchdata
Title: Download Bird Observation Data from <API Name>
Version: 0.0.0.9000
Authors@R:
    person("Your", "Name",
           email = "you@example.com",
           role = c("aut", "cre"),
           comment = c(ORCID = "0000-0000-0000-0000"))
Description: Provides access to bird observation records from the
    <Organisation Name> API (<https://api.example.com>). The API
    covers <brief description of scope and geographic coverage>.
License: MIT + file LICENSE
URL: https://github.com/yourorg/finchdata, https://yourorg.github.io/finchdata
BugReports: https://github.com/yourorg/finchdata/issues
Encoding: UTF-8
Roxygen: list(markdown = TRUE)
RoxygenNote: 7.x.x
Imports:
    httr2,
    jsonlite
Suggests:
    httptest2,
    knitr,
    rmarkdown,
    testthat (>= 3.0.0),
    vcr (>= 1.2.2)
```

Key rules applied here:

- **Title**: Title Case, no trailing period, no "in R" or "with R". The API name is quoted in the Description, not the title.
- **Description**: does not start with the package name or "This package". Includes the organisation name and a URL in angle brackets, as required for data-source packages.
- **Authors@R**: use `Authors@R`, not the plain `Author`/`Maintainer` fields. Add your ORCID. Mark copyright holders with `cph` if needed (e.g. if the organisation's data has a license requiring attribution). Do not list rOpenSci editors — that field is for contributors, not reviewers. Reviewers may be added as `role = "rev"` only with their consent, after review.
- **License**: must be CRAN- or OSI-accepted. MIT is fine; Apache 2.0 is also common.
- **Imports vs. Depends**: list packages whose functions you call inside your code under `Imports`. Never use `Depends` unless you intend to attach the dependency to the user's search path (almost never the right call). Tooling goes in `Suggests`.

---

## 4. Dependencies

For a bird observation API package, the canonical stack is:

| Need              | Use                  | Avoid                                              |
| ----------------- | -------------------- | -------------------------------------------------- |
| HTTP requests     | `httr2`              | `RCurl`, `httr` (for new packages, prefer `httr2`) |
| JSON parsing      | `jsonlite`           | `rjson`, `RJSONIO`                                 |
| HTTP test mocking | `httptest2` or `vcr` | recording real calls in tests                      |

Prefer `httr2` over `httr` for new packages — it has a modern, pipe-friendly API and better error handling. Only add `jsonlite` if the API returns JSON (it almost certainly does). Do not pull in `tibble` just to return tibbles if your data is naturally a data frame; base `data.frame` is fine. Every dependency is a maintenance burden — fewer is better.

Add them properly:

```r
usethis::use_package("httr2")
usethis::use_package("jsonlite")
usethis::use_package("httptest2", type = "Suggests")
usethis::use_package("vcr", type = "Suggests")
```

---

## 5. Function and argument naming

- Use `snake_case` throughout.
- Consider an `object_verb()` scheme: `observations_get()`, `observations_search()`, `species_list()`. This groups related functions and makes tab-completion predictable.
- Make the primary data object the **first argument** so functions compose with pipes.
- Keep argument names consistent across related functions (e.g. always `species`, never sometimes `species_name`).
- Functions must **return values** — never assign into the global environment.
- Avoid names that clash with base R or popular packages.

---

## 6. API key / credential handling

Because `finchdata` downloads from an API, treat credential handling as a first-class concern from day one.

- Read the API key from an **environment variable**, e.g. `FINCHDATA_API_KEY`. Never accept it as a plain function argument that users might paste into scripts.
- Support **keyring** as an alternative to `.Renviron` so keys are stored in the OS credential store.
- Never print the key in any message, warning, or error, even in debug mode.
- Guide users to `usethis::edit_r_environ()` in your README and vignette so they set it up safely and it never lands in `.Rhistory` or a committed script.

A minimal key-retrieval helper:

```r
finchdata_key <- function() {
  key <- Sys.getenv("FINCHDATA_API_KEY")
  if (identical(key, "")) {
    cli::cli_abort(
      "No API key found. Set {.envvar FINCHDATA_API_KEY} in your {.file .Renviron}.",
      call = rlang::caller_env()
    )
  }
  key
}
```

---

## 7. roxygen2 documentation

Use roxygen2 with Markdown (`Roxygen: list(markdown = TRUE)` in DESCRIPTION, already set above).

Every exported function needs:

- `@param` for every argument, stating type and default
- `@return` describing what the function returns
- `@examples` with a runnable example (or `@examplesIf` / `\dontrun{}` for calls that require credentials)
- `@export` to export it

For credential-gated examples, use `@examplesIf` rather than `\dontrun{}` where possible — pkgcheck flags bare `\dontrun{}`:

```r
#' Get bird observations
#'
#' Downloads observation records from the Finch API for a given species.
#'
#' @param species Character. Species name or code to query.
#' @param limit Integer. Maximum number of records to return. Default `100`.
#' @param api_key Character. API key. Defaults to the value of the
#'   `FINCHDATA_API_KEY` environment variable.
#'
#' @return A data frame with one row per observation and columns for
#'   `species`, `date`, `latitude`, `longitude`, and `count`.
#'
#' @examplesIf nchar(Sys.getenv("FINCHDATA_API_KEY")) > 0
#' observations_get("Geospiza fortis", limit = 10)
#'
#' @export
observations_get <- function(species, limit = 100L, api_key = finchdata_key()) {
  # ...
}
```

Provide a package-level doc page (already scaffolded by `use_package_doc()`):

```r
#' @keywords internal
"_PACKAGE"
```

Use `@family` to group related functions and generate cross-links automatically.

---

## 8. README

Generate from `README.Rmd` (already created by `use_readme_rmd()`). The required sections, in order:

1. Package name and one-line description
2. **Badges**: R CMD check, test coverage (Codecov), repostatus.org (`Concept` or `WIP` initially)
3. Short goal description linking to the vignette
4. Installation instructions (`pak::pak("yourorg/finchdata")`)
5. Setup: how to get and store an API key (`usethis::edit_r_environ()`)
6. Brief usage demo (a real, short code example with output)
7. Any similar packages and how `finchdata` differs
8. Citation info

The README must let an editor assess the package without installing it. Explain what the API is — do not assume domain knowledge. A reader unfamiliar with bird observation databases should still understand what the package does after reading the first two paragraphs.

Do not commit `README.md` by hand — render it from `README.Rmd`:

```r
devtools::build_readme()
```

---

## 9. Vignette

At minimum one HTML vignette (`usethis::use_vignette("finchdata")`) that:

- Explains what the API is and links its documentation
- Walks through authentication setup
- Progresses from basic usage (a single `observations_get()` call) to more realistic workflows (filtering, combining species, visualising)
- Pre-computes output or uses `vcr` to cache HTTP responses so it builds without live credentials on CRAN/CI

```r
usethis::use_vignette("finchdata", title = "Getting started with finchdata")
```

---

## 10. Tests

Set up the test suite and aim for at least 75% coverage before submitting to review.

```r
usethis::use_testthat()
```

For an API package, use **vcr** or **httptest2** to record and replay HTTP interactions so tests are fast, deterministic, and never hit the live API on CRAN:

```r
# tests/testthat/test-observations.R
test_that("observations_get returns a data frame", {
  vcr::use_cassette("observations_get_basic", {
    result <- observations_get("Geospiza fortis", limit = 5)
  })
  expect_s3_class(result, "data.frame")
  expect_named(result, c("species", "date", "latitude", "longitude", "count"))
  expect_true(nrow(result) <= 5)
})

test_that("observations_get errors informatively with no key", {
  withr::with_envvar(c(FINCHDATA_API_KEY = ""), {
    expect_error(observations_get("Geospiza fortis"), "FINCHDATA_API_KEY")
  })
})
```

**Before committing cassettes/fixtures**, inspect them to ensure no API keys or tokens are present. Configure vcr to redact secrets:

```r
# tests/testthat/helper-vcr.R
vcr::vcr_configure(
  filter_sensitive_data = list("<<API_KEY>>" = Sys.getenv("FINCHDATA_API_KEY")),
  dir = vcr::vcr_test_path("fixtures")
)
```

Tests that require a live connection should call `skip_if_offline()` (which automatically calls `skip_on_cran()` in modern testthat). Document in `CONTRIBUTING.md` that fork PRs will not have the API key secret and some tests will skip.

---

## 11. Code style

- Format with **Air** or **styler**; lint with **lintr**. Run both before every commit.
- Use `cli::cli_abort()` / `cli::cli_warn()` / `cli::cli_inform()` for user-facing messages — not `print()`, `cat()`, or `message()`. This gives users suppressibility and consistent formatting.
- Give users a way to silence verbose output via a package option (e.g. `options(finchdata.quiet = TRUE)`) rather than a per-call `verbose` argument.
- Be consistent about assignment (`<-` throughout, or `=` throughout, but not mixed outside of function call arguments).

---

## 12. Continuous integration

Set up GitHub Actions using `r-lib/actions`:

```r
# R CMD check on release, oldrel, and devel R:
usethis::use_github_action("check-standard")

# Test coverage reported to Codecov:
usethis::use_github_action("test-coverage")
```

Because `finchdata` makes network requests but has no compiled code, multi-OS is not strictly required by the rules — but it is still good practice and easy to enable. If you add any path handling, system calls, or compiled code later, multi-OS becomes required.

Also wire in pkgcheck to continuously validate against rOpenSci's review criteria:

```yaml
# .github/workflows/pkgcheck.yaml
# Use: ropensci-review-tools/pkgcheck-action
```

Add coverage and CI status badges to `README.Rmd`.

---

## 13. Repo hygiene

```r
usethis::git_vaccinate()   # .gitignore and .Rbuildignore
usethis::use_news_md()     # NEWS.md — required
```

`NEWS.md` must be present. Start it with:

```markdown
# finchdata (development version)

- Initial release.
```

Make sure `.Rbuildignore` excludes top-level files that are not part of the package (`.github/`, `README.Rmd`, `_pkgdown.yml`, etc.).

---

## 14. Verify with pkgcheck

Once the scaffold is in place, run:

```r
pkgcheck::pkgcheck()
```

This is the same tool rOpenSci runs on every submission. Fix everything it flags before opening a submission issue. The items above will get you to a clean run, but pkgcheck catches edge cases (leftover `\dontrun{}`, missing `@return`, low coverage, stale DESCRIPTION fields) that are easy to miss.

---

## Summary checklist

| Area         | Action                                                                                    |
| ------------ | ----------------------------------------------------------------------------------------- |
| Name         | `pak::pkg_name_check("finchdata")` — confirm available                                    |
| DESCRIPTION  | Title Case title, `Authors@R` with ORCID, URL + BugReports, data-source description       |
| License      | OSI-accepted (e.g. MIT)                                                                   |
| Dependencies | `httr2`, `jsonlite` in Imports; testing tooling in Suggests                               |
| API key      | Env var + keyring; never printed; `vcr`/`httptest2` for fixtures                          |
| Functions    | `snake_case`, `object_verb()` scheme, first arg is the data                               |
| roxygen2     | All exports documented with `@param`, `@return`, `@examples`; package-level doc           |
| README       | Generated from `README.Rmd`; badges, auth setup, usage demo                               |
| Vignette     | At least one HTML vignette, basic → advanced, pre-computed or vcr-cached                  |
| Tests        | testthat + vcr; ≥ 75% coverage; error paths tested; fixtures scrubbed of secrets          |
| Style        | Air/styler + lintr; `cli` for messages; never `print()`/`cat()`                           |
| CI           | `check-standard` (release + oldrel + devel); `test-coverage` → Codecov; `pkgcheck-action` |
| Git          | `main` branch; `NEWS.md`; `.gitignore`/`.Rbuildignore` via `git_vaccinate()`              |
