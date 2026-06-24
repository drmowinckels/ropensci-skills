# Submitting a Bayesian Regression Package to rOpenSci Statistical Software Review

Submitting to rOpenSci's statistical software review track is meaningfully different from general rOpenSci submission. Your package will be evaluated against a formal set of standards, and you must document compliance with those standards directly in your code before reviewers ever see it. Here is what that requires in practice.

---

## 1. Confirm Scope and Category

Your Bayesian regression package almost certainly falls under **two categories simultaneously**:

- **Bayesian and Monte Carlo Software (BS)** — because it estimates posterior distributions
- **Regression and Supervised Learning (RE)** — because it maps inputs to outputs via a model

Both category-specific standard sets apply. Before doing anything else, verify this fit by checking the standards chapter at <https://stats-devguide.ropensci.org/standards.html>. If there is any ambiguity, send a pre-submission enquiry to the editors — this is encouraged and saves significant rework.

---

## 2. Set Up the `srr` Package

The `srr` (Software Review Roclets) package is how you document standards compliance. It extends roxygen2 so that compliance evidence lives in the code, not in a separate document.

**Step 1: Add the roclet to your DESCRIPTION**

```
Roxygen: list(markdown = TRUE, roclets = c("namespace", "rd", "srr::srr_stats_roclet"))
```

You do not need to add `srr` to `Imports` or `Suggests`.

**Step 2: Generate the standards stubs**

Run this in your package directory — once for each applicable category:

```r
srr::srr_stats_roxygen(category = c("regression", "bayesian"))
```

This creates `R/srr-stats-standards.R` containing every applicable standard marked `@srrstatsTODO`.

**Step 3: Annotate your code**

Move each standard to the location in your code where it is addressed and change the tag:

| Tag                    | Meaning                                                      |
| ---------------------- | ------------------------------------------------------------ |
| `@srrstatsTODO {G1.0}` | Not yet addressed — must be cleared before submission        |
| `@srrstats {G1.0}`     | Addressed here — add a brief explanation of how              |
| `@srrstatsNA {G1.0}`   | Not applicable — must explain why in an `NA_standards` block |

Standards can appear in any `.R` file, in test files, or in `src/` source files. Put them near the code that satisfies them.

**Step 4: Verify completion**

```r
srr::srr_stats_pre_submit()
```

No `@srrstatsTODO` tags may remain at submission time. Run `devtools::document()` after changes to see the roclet output showing addressed, non-applicable, and remaining TODO items.

---

## 3. Standards You Must Address

### General Standards (G prefix) — apply to all statistical software

Key requirements beyond normal package standards:

- **G1.0** Cite at least one primary academic reference
- **G1.1** State whether the algorithm is novel, the first R implementation, or an improvement on existing implementations
- **G1.2** Include a Life Cycle Statement describing the current and anticipated development state
- **G2.0–G2.16** Comprehensive input validation: assert lengths and types, handle `NA`/`NaN`/`Inf`, handle missing data explicitly, never silently drop information
- **G3.0** Never compare floating-point numbers for equality
- **G5.0–G5.9** Thorough testing: use standard datasets with known properties, test all error/warning conditions, use fixed random seeds for stochastic tests, include parameter recovery tests, edge condition tests, and noise susceptibility tests
- **G5.10** Extended tests (slow/large) should be gated behind an environment variable flag

### Bayesian Standards (BS prefix)

**Documentation requirements:**

- **BS1.0** Explicitly define "hyperparameter" if you use the term
- **BS1.1** Describe data input methods in text and code examples
- **BS1.2** Document prior distribution specifications in README, vignettes, and function docs, with examples
- **BS1.3** Document all computational control parameters (chain length, thinning, seed, convergence checker)
- **BS1.3a** Document how to use previous run output as starting points
- **BS1.3b** Document support for different sampling algorithms
- **BS1.4** Document convergence checkers explicitly with examples

**Input validation:**

- **BS2.1** Validate that input data is dimensionally commensurate
- **BS2.2–BS2.5** Validate distributional parameters: vector lengths, numeric validity (non-negative variances, etc.)
- **BS2.6** Validate that computational parameters are within plausible ranges
- **BS2.7** Allow explicit control of starting values
- **BS2.8** Allow previous run results as starting values for subsequent runs
- **BS2.9** Use different seeds for different chains by default
- **BS2.10** Warn when identical seeds are passed to distinct chains
- **BS2.12–BS2.15** Implement verbosity control: allow suppression of messages/progress, suppression of warnings, and graceful handling of errors

**Algorithm requirements:**

- **BS4.0** Document the sampling algorithm with a literature citation
- **BS4.1** Provide explicit comparisons with external samplers demonstrating the intended advantage
- **BS4.2** Implement at least one means to validate posterior estimates
- **BS4.3** Implement at least one convergence checker with a documented reference
- **BS4.4** Allow computation to stop on convergence (not necessarily the default)
- **BS4.5** Handle models that do not converge appropriately

**Return values:**

- **BS5.0** Return starting values and seeds for each chain
- **BS5.1** Return metadata about types/classes and dimensions
- **BS5.2** Return the prior specification or make it accessible via a function
- **BS5.3** Return convergence statistics
- **BS5.4** Return which convergence checker was used (when multiple are available)
- **BS5.5** Return diagnostic statistics indicating absence of convergence

**Output methods:**

- **BS6.0** Default `print` method for the return object
- **BS6.1** Default `plot` method for the return object
- **BS6.2** Ability to plot posterior sample sequences with burn-in periods distinguished
- **BS6.3** Ability to plot posterior distributional estimates

**Testing:**

- **BS7.0** Demonstrate recovery of parametric estimates of prior distributions
- **BS7.1** Demonstrate prior recovery absent additional data
- **BS7.2** Demonstrate expected posterior recovery given a specified prior and data
- **BS7.3** Test algorithmic efficiency scaling with input data size
- **BS7.4** Test that fitted values are on approximately the same scale as input data

### Regression Standards (RE prefix)

**Input and formula interface:**

- **RE1.0** Support a formula interface, or explicitly document why not
- **RE1.1** Document how formula interfaces convert to matrix representations
- **RE1.2** Document expected types/classes of predictor variables
- **RE1.3** Preserve row/column names and attributes through input-to-output transformations
- **RE1.4** Document distributional assumptions about input data

**Pre-processing:**

- **RE2.0** Document any transformations applied to input data; provide ways to disable defaults
- **RE2.1** Implement explicit parameters for missing value handling, distinguishing `NA`/`NaN` from `Inf`
- **RE2.2** Handle missing values in predictors and response separately
- **RE2.3** Support centering/offsetting via explicit parameters, with clear documentation
- **RE2.4** Detect perfect collinearity — both among predictors and between predictors and response

**Convergence:**

- **RE3.0** Issue warnings for models that fail to converge
- **RE3.1** Allow convergence messages to be suppressed, but still store convergence status in the object
- **RE3.2** Document convergence thresholds with sensible defaults
- **RE3.3** Allow explicit setting of convergence thresholds

**Return object:**

- **RE4.0** Return a model object using or extending standard class structures
- **RE4.2** Coefficients accessible via `coef()`
- **RE4.3** Confidence intervals accessible via `confint()`
- **RE4.4** Formula accessible via `formula()`
- **RE4.5** Number of observations accessible via `nobs()`
- **RE4.6** Variance-covariance matrix accessible via `vcov()`
- **RE4.7** Convergence statistics in the return object
- **RE4.8** Response variables and metadata accessible
- **RE4.9** Fitted values accessible
- **RE4.10** Residuals accessible with sufficient documentation for interpretation
- **RE4.11** Goodness-of-fit statistics (effect sizes, R², WAIC, LOO-IC, etc.)
- **RE4.17** Default `print` method with an on-screen summary

**Visualization:**

- **RE6.0** Default `plot` method on model objects
- **RE6.2** Default plot shows fitted values, with optional confidence intervals

**Testing:**

- **RE7.0** Tests with exact noiseless relationships between predictor variables
- **RE7.1** Tests with exact noiseless relationships between predictors and response
- **RE7.2** Output objects retain input row/case names
- **RE7.3** Test all accessor methods on returned objects

---

## 4. Run `autotest`

The `autotest` package performs mutation testing by systematically varying input types to find unexpected behavior:

```r
autotest::autotest_package()
```

Run this continuously during development. Aim for clean (`NULL`) results before submitting. It is strongly recommended, not strictly required, but reviewers will run it and flag issues found.

---

## 5. Run `pkgcheck`

Before submitting, run the same checks the review bot will run:

```r
pkgcheck::pkgcheck()
```

The output must include the statement **"This package may be submitted"** before you open a submission issue. Key thresholds:

- Test coverage must exceed **75%**
- No `@srrstatsTODO` tags may remain
- All srr standards must be either addressed (`@srrstats`) or explicitly excluded (`@srrstatsNA`)
- R CMD check must pass

---

## 6. Choose a Badge Grade

Statistical software submissions declare a target badge level in the submission template:

| Badge      | Requirement                                                                                                                                                  |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Bronze** | Meets the minimum applicable standards                                                                                                                       |
| **Silver** | Exceeds bronze in at least one of four defined aspects (e.g., notably excellent design, generality beyond one use case, exceeding minimal standards by 25%+) |
| **Gold**   | Complies with all applicable standards plus fulfills three of the four silver aspects; requires active maintenance as standards evolve                       |

Bronze is a legitimate target — it does not imply inadequacy.

---

## 7. Open the Submission

Submit via a GitHub issue in `ropensci/software-review` using the **statistical software submission template** (distinct from the general template). The template asks for:

- Package scope and category declaration
- Target badge grade
- Confirmation that `pkgcheck()` reports the package may be submitted
- Summary of how the package advances the field

The review bot will run `@ropensci-review-bot check srr` automatically. Editors verify at least 50% standards compliance before assigning reviewers.

---

## Summary Checklist

- [ ] Confirm dual-category scope (Bayesian + Regression)
- [ ] Add `srr` roclet to `DESCRIPTION`
- [ ] Generate standards stubs for both categories
- [ ] Annotate all standards — no `@srrstatsTODO` remaining
- [ ] Prior specification returned or accessible
- [ ] Convergence checker implemented and documented
- [ ] Starting values and seeds returned per chain
- [ ] `print`, `plot`, `coef`, `confint`, `formula`, `nobs`, `vcov` methods implemented
- [ ] Posterior sample and distribution plots implemented
- [ ] Parameter recovery tests present with fixed seeds
- [ ] `autotest_package()` returns clean results
- [ ] `pkgcheck()` reports "This package may be submitted"
- [ ] Target badge grade chosen
- [ ] Submit via statistical software template in `ropensci/software-review`

---

## Key References

- [rOpenSci Statistical Software Peer Review Guide](https://stats-devguide.ropensci.org/)
- [Standards Version 0.2.0](https://stats-devguide.ropensci.org/standards.html)
- [Guide for Authors](https://stats-devguide.ropensci.org/pkgdev.html)
- [srr package documentation](https://docs.ropensci.org/srr/)
- [srr workflow vignette](https://docs.ropensci.org/srr/articles/srr-stats.html)
- [pkgcheck package](https://docs.ropensci.org/pkgcheck/)
