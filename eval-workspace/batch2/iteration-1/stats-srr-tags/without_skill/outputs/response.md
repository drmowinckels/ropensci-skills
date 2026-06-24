# Documenting rOpenSci Statistical Standards with the srr Package

The `srr` package (Software Review Roclets) lets you document compliance with [rOpenSci statistical software standards](https://stats-devguide.ropensci.org/standards.html) directly in your R package code using `roxygen2` tags. The roclets run every time you call `devtools::document()` or `roxygen2::roxygenise()` and produce a summary of which standards you've addressed, which are still pending, and which you've marked as not applicable.

## Setup

### 1. Enable the srr roclet in DESCRIPTION

Add the `srr` roclet to your `Roxygen` line in `DESCRIPTION`. You do not need to add `srr` to `Imports` or `Depends`.

```
Roxygen: list(markdown = TRUE, roclets = c("namespace", "rd", "srr::srr_stats_roclet"))
```

### 2. Generate the initial standards file

Run `srr_stats_roxygen()` from within your package directory. Pass the category (or categories) that describe your package. To see available categories:

```r
srr::srr_stats_categories()
```

Then generate the standards file:

```r
srr::srr_stats_roxygen(
  category = "regression",  # replace with your category
  filename  = "srr-stats-standards.R"
)
```

This creates `R/srr-stats-standards.R` with every applicable standard listed under `@srrstatsTODO` tags. The file looks like:

```r
#' @srrstatsTODO {G1.0} Statistical Software should list at least one
#'   primary reference from published academic literature.
#'
#' @srrstatsTODO {G1.1} Statistical Software should document whether the
#'   algorithm is an original implementation or a wrapper around existing code.
#'
#' ... (many more)
#'
#' @noRd
NULL
```

Every block must end with `NULL` (or a function definition) to be parsed correctly by roxygen2.

## The Three Tags

### `@srrstatsTODO` — Standard not yet addressed

This is the starting state for every standard. It marks a standard you still need to work on.

```r
#' @srrstatsTODO {G1.1} Document whether the algorithm is an original
#'   implementation or a wrapper.
#' @noRd
NULL
```

### `@srrstats` — Standard addressed

When you have addressed a standard, move the tag from the initial file to the location in your code where it is addressed, and change `@srrstatsTODO` to `@srrstats`. Replace the standard's original description with a brief explanation of _how_ your code addresses it.

Tags can go inside any roxygen2 block on a function:

```r
#' Fit a linear model
#'
#' @srrstats {G1.1} This is an original implementation; not a wrapper.
#' @srrstats {G1.2, G1.3} Documented in README and vignette.
#' @srrstats {G2.0} Input lengths are validated with `stop()` before fitting.
#'
#' @param x Numeric vector of predictors.
#' @param y Numeric vector of response values.
#' @return A list with class `"myfit"`.
#' @export
fit_model <- function(x, y) {
  # ...
}
```

Tags can also go in `tests/`, `src/`, and `.Rmd` files — see below.

### `@srrstatsNA` — Standard not applicable

Standards you deem not applicable must be collected in a dedicated block titled `NA_standards`. This block must end with `NULL`.

```r
#' NA_standards
#'
#' @srrstatsNA {RE3.3} Not applicable: this package does not implement
#'   iterative optimization and has no convergence criterion.
#' @srrstatsNA {RE4.4} Not applicable: the model has no tuning parameters.
#' @noRd
NULL
```

You can have multiple `NA_standards` blocks in different files. A common pattern is to co-locate the non-applicable test-related standards in a block inside `tests/testthat/`.

## Formatting Rules

1. Tags must immediately follow the roxygen2 comment prefix (`#' @srrstats`).
2. Standard numbers must be inside curly braces: `{G1.0}` or `{G1.0, G1.1}` for multiples.
3. Explanatory text can appear before or after the curly braces on the same line.
4. Only the **first** pair of curly braces on a tag line is parsed. To reference multiple standards, either put them all in one pair of braces or use separate tag lines.
5. A standard can only carry **one** tag type across the whole package: it must be exclusively `@srrstats`, `@srrstatsNA`, or `@srrstatsTODO`. Mixing causes an error.

```r
# Correct: multiple standards in one tag
#' @srrstats {G2.0, G2.1} Input types checked on entry.

# Correct: separate tags
#' @srrstats {G2.0} Length validated.
#' @srrstats {G2.1} Type validated.

# Wrong: only G2.0 is parsed; G2.1 in the second braces is silently ignored
#' @srrstats {G2.0} as well as {G2.1}.
```

## Where to Place Tags

### In R/ (roxygen2 blocks)

Inside any roxygen2 block attached to a function. To add tags where no documentation block exists, create a minimal block:

```r
#' @srrstats {G2.3} Input trimming handled here.
#' @noRd
helper_trim <- function(x) trimws(x)
```

Or attach to `NULL` when not associated with a function:

```r
#' @srrstats {G1.4} Algorithm references are in the vignette.
#' @noRd
NULL
```

### In tests/

Tags in test files do **not** need `@noRd` or `NULL`:

```r
#' @srrstats {RE2.2} Edge case: single-observation input handled correctly.
test_that("single observation input", {
  expect_no_error(fit_model(1, 1))
})
```

### In src/ (C/C++ via Rcpp)

Use doxygen-style comment blocks (`//'`). Include `@noRd` to suppress `.Rd` generation:

```cpp
//' @srrstats {G2.3} Input validated in C++ before computation.
//' @noRd
// [[Rcpp::export]]
int compute(int x) { return x; }
```

### In README.Rmd / vignettes

Place tags in a dedicated code chunk with `echo = FALSE`:

````markdown
```{r srr-tags, eval = FALSE, echo = FALSE}
#' @srrstats {G1.4} Primary reference listed in Introduction section.
#' @srrstats {G1.5} Software compared to reference implementation in benchmarks.
```
````

The chunk should contain **only** roxygen2 lines. Use `eval = FALSE` if any other R code is needed in the chunk.

## Typical Workflow

1. Run `srr_stats_roxygen(category = "your_category")` to populate `R/srr-stats-standards.R` with all standards as `@srrstatsTODO`.
2. Add the `srr` roclet to `DESCRIPTION`.
3. Run `devtools::document()` to confirm the roclet works. You should see every standard listed under `@srrstatsTODO`.
4. Distribute standards across your codebase: cut-paste groups of related `@srrstatsTODO` blocks near the code that will address them (e.g., input-validation standards near input-checking code, test standards into `tests/`).
5. For each standard you address: move it to the precise location, change the tag to `@srrstats`, and replace the boilerplate description with a brief explanation of how your code satisfies the standard.
6. For each standard that does not apply: move it to an `NA_standards` block and change the tag to `@srrstatsNA` with a justification.
7. Re-run `devtools::document()` regularly to track progress.
8. Before submission, run the pre-submission check — it confirms no standards remain as `@srrstatsTODO`:

```r
srr::srr_stats_pre_submit()
```

The goal is that every standard in the full list ends up as either `@srrstats` (addressed, at the relevant location) or `@srrstatsNA` (justified as not applicable), with zero `@srrstatsTODO` remaining.
