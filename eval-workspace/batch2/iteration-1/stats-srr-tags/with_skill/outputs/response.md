# Documenting rOpenSci Statistical Standards with `srr` Tags

The `srr` package integrates with roxygen2 so that standard compliance is declared
directly in your package's source code. The roclet runs every time you call
`devtools::document()` or `roxygen2::roxygenise()`, which gives you immediate
feedback on coverage.

## Setup

Add `srr` to your package and register the roclet in `DESCRIPTION`:

```r
# Install srr
install.packages("srr")   # or: pak::pak("ropensci/srr")
```

```
# DESCRIPTION
Roxygen: list(markdown = TRUE, roclets = c("collate", "namespace", "rd",
    "srr::srr_stats_roclet"))
```

## Step 1 — scaffold the standards file

Call `srr_stats_roxygen()` with your categories. It creates
`R/srr-stats-standards.R` pre-filled with every applicable standard as an
`@srrstatsTODO` tag.

```r
srr::srr_stats_roxygen(category = c("regression", "general"))
```

Available category codes:

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

Include every category your package touches. You must satisfy (or explicitly
waive) all standards in each chosen category.

## The three tag types

### `@srrstatsTODO` — not yet documented

This is what the scaffold generates. It means "this standard has not been
addressed yet." Leaving any `@srrstatsTODO` tags in place causes
`srr_stats_pre_submit()` to block submission.

```r
#' @srrstatsTODO G2.0 Implement assertions on lengths of inputs
```

### `@srrstats` — standard is met

Move this tag to the roxygen block for the function (or the file) where the
standard is satisfied. Describe concretely how the code meets the standard.

```r
#' @srrstats {G2.0} Input length is validated via `check_length()` called at
#'   the top of `fit_model()`; an informative error is thrown for mismatches.
```

Place it as close as possible to the code that satisfies the standard. If a
standard is satisfied across multiple functions, put the tag in the most
representative one and mention the others in the description.

### `@srrstatsNA` — standard does not apply

Use this when a standard is genuinely inapplicable to your package. You must
provide a reason — the reviewer will read it.

```r
#' @srrstatsNA {RE4.3} This package does not produce prediction intervals;
#'   only point estimates are returned.
```

## Where to place tags

Tags go in roxygen blocks (`#'` comments). They can appear in any source file
in `R/`. Common patterns:

**In the function that satisfies the standard:**

```r
#' Fit a linear model
#'
#' @param formula A formula.
#' @param data A data frame.
#' @returns An object of class `"mymodel"`.
#'
#' @srrstats {G2.1} All inputs are checked with `checkmate::assert_data_frame()`
#'   and `checkmate::assert_formula()` before any computation.
#' @srrstats {G2.6} Missing values in `data` are detected and an informative
#'   error is raised listing the columns with NAs.
#'
#' @export
fit_model <- function(formula, data) {
  checkmate::assert_data_frame(data)
  checkmate::assert_formula(formula)
  ...
}
```

**In `R/srr-stats-standards.R` for package-level or NA tags:**

Some standards are satisfied by the package as a whole (e.g. documentation
standards, README requirements) or are not applicable. These live in the
central standards file rather than a specific function:

```r
#' srr_stats
#'
#' @srrstats {G1.0} Primary literature is cited in the README and in
#'   `?fit_model`.
#' @srrstats {G1.2} A lifecycle statement is included in the README.
#'
#' @srrstatsNA {RE2.4} This package does not implement dimension reduction
#'   as a preprocessing step.
#'
#' @noRd
NULL
```

The `@noRd` and `NULL` are required — they anchor the roxygen block without
generating a help page.

## Checking your work

After editing tags, run:

```r
# Re-runs the srr roclet and prints a coverage summary
devtools::document()

# Full HTML report of which standards are addressed, pending, or NA
srr::srr_report()

# Pre-submission gate — fails if any @srrstatsTODO tags remain
srr::srr_stats_pre_submit()
```

The HTML report groups standards by category and shows the tag type and
description for each one. Share this URL with your editor and reviewers.

## Autotest

Run `autotest` in addition to tagging — it mutates function inputs to surface
edge cases that standards require but that tests may not exercise:

```r
autotest::autotest_package()
```

Address or explain every issue it reports before submission.

## Full worked example

```r
# R/fit.R

#' Fit a regression model
#'
#' @param formula A formula specifying the model.
#' @param data A data frame containing the variables.
#' @param weights Optional numeric vector of observation weights.
#' @returns An object of class `"myfit"` with components `coefficients`,
#'   `residuals`, and `fitted.values`.
#'
#' @srrstats {G2.0} Input types validated via checkmate before any computation.
#' @srrstats {G2.1} Univariate inputs checked for correct type (numeric for
#'   weights); informative errors on mismatch.
#' @srrstats {G2.6} Missing values in `data` detected before fitting;
#'   error message names affected columns.
#' @srrstats {RE1.0} Formula interface follows standard R conventions
#'   (stats::lm-compatible).
#' @srrstats {RE2.0} `weights` parameter supports observation weighting.
#'
#' @export
fit_model <- function(formula, data, weights = NULL) {
  checkmate::assert_formula(formula)
  checkmate::assert_data_frame(data, any.missing = FALSE)
  if (!is.null(weights)) checkmate::assert_numeric(weights, len = nrow(data))
  ...
}
```

```r
# R/srr-stats-standards.R

#' srr_stats
#'
#' @srrstats {G1.0} The vignette and `?fit_model` cite the primary statistical
#'   reference (Ordinary Least Squares, Seber & Lee 2003).
#' @srrstats {G1.2} Lifecycle badge (stable) in README.
#'
#' @srrstatsNA {RE4.3} Package does not produce prediction intervals.
#' @srrstatsNA {RE4.4} Package does not compute confidence intervals on
#'   predictions; only on coefficients via `confint()`.
#'
#' @noRd
NULL
```

## Summary of the tag workflow

1. `srr_stats_roxygen()` scaffolds every applicable standard as `@srrstatsTODO`.
2. For each standard, decide: does my code satisfy it? Is it genuinely N/A?
3. Move the tag from the scaffold to the relevant function's roxygen block and
   change it to `@srrstats` (with how) or `@srrstatsNA` (with why).
4. Package-wide and N/A tags stay in `R/srr-stats-standards.R`.
5. `devtools::document()` runs the roclet on every save; `srr_report()` gives
   the full picture; `srr_stats_pre_submit()` is the final gate.
