# Submitting a Bayesian Regression Package to rOpenSci Statistical Software Review

The rOpenSci statistical software review is a **direct extension** of the general rOpenSci review process — not a replacement. You must first meet all the normal package requirements (DESCRIPTION, documentation, tests, CI, naming conventions, etc.) covered by the general rOpenSci dev guide. The statistical standards layer sits on top of that.

---

## Step 1: Identify your categories

Your package implements Bayesian regression, so it touches **two** standard sets:

| Code | Category                                         |
| ---- | ------------------------------------------------ |
| `BS` | Bayesian & Monte Carlo (~70 standards)           |
| `RE` | Regression & Supervised Learning (~25 standards) |

You must satisfy every standard in both categories, or explicitly document why a given standard does not apply. The full text of both sets is at <https://stats-devguide.ropensci.org/standards.html>.

---

## Step 2: Install and scaffold with `srr`

```r
install.packages("srr")   # or pak::pak("ropensci/srr")
```

Run the scaffolding function with both categories:

```r
srr::srr_stats_roxygen(category = c("bayesian", "regression"))
```

This writes `R/srr-stats-standards.R` pre-filled with every applicable standard as an `@srrstatsTODO` tag — roughly 95+ tags between `BS` and `RE`. These are placeholders you must resolve before submission.

---

## Step 3: Annotate every standard in your code

Work through each `@srrstatsTODO` tag and convert it to one of:

- **`@srrstats {G2.0a}` followed by a description** — the standard is met; explain where and how.
- **`@srrstatsNA {BS2.1}` followed by a reason** — the standard genuinely does not apply; state why.

Place the tag near the code that satisfies the standard, not just in the catch-all `srr-stats-standards.R` file. Running `devtools::document()` triggers the srr roclet and reports unresolved TODOs.

```r
#' @srrstats {G5.5} All correctness tests use `set.seed(42)` for reproducibility.
#' @srrstats {BS4.1} MCMC chain convergence is diagnosed via Rhat; chains with
#'   Rhat > 1.05 trigger a warning with the affected parameters named.
#' @srrstatsNA {RE4.4} This package does not produce influence or leverage
#'   statistics; the method is fully Bayesian and has no hat matrix.
```

---

## Step 4: Key areas to address for Bayesian regression specifically

### General Standards (applies to every package)

**Documentation (G1)**

- Cite the primary academic reference for the method (`G1.0`).
- State whether this is a novel algorithm, the first R implementation, or an improvement on existing ones (`G1.1`).
- Include a Life Cycle Statement in `CONTRIBUTING.md` (`G1.2`).
- Define all statistical terminology used (`G1.3`).
- If you make performance claims, include reproducible code (`G1.5`, `G1.6`).

**Input validation (G2)**

- Assert and document input types and lengths (`G2.0`, `G2.0a`, `G2.1`, `G2.1a`).
- Handle missing data explicitly — choose between erroring, ignoring, or imputing, and document the behavior (`G2.13`–`G2.16`).
- Use `match.arg()` for character options like `family`, `prior`, `method` (`G2.3a`).

**Testing (G5)**

- Test against datasets with known properties (`G5.0`).
- Write correctness tests that compare output to known published values or an established implementation (`G5.4`, `G5.4a`–`G5.4c`).
- Use a fixed random seed for all correctness tests (`G5.5`).
- Write parameter-recovery tests: generate data from the model, fit it, verify the posterior means are within tolerance of the true values — with multiple seeds (`G5.6`, `G5.6a`, `G5.6b`).
- Test edge conditions: zero rows, all-NA columns, degenerate data (`G5.8a`–`G5.8d`).
- Test noise susceptibility: adding trivial noise should not qualitatively change results (`G5.9a`).

### Bayesian & Monte Carlo Standards (BS)

The BS standards are the most extensive (~70). Key themes:

- **Prior specification**: Document the priors available, their parameterization, and defaults. Justify default priors and provide references. Users must be able to specify any proper prior for all parameters.
- **MCMC diagnostics**: Implement or expose Rhat (potential scale reduction factor) and effective sample size (ESS) for all monitored parameters. Warn when convergence diagnostics indicate problems (Rhat > 1.05 is a common threshold). Document what diagnostics are computed and how to interpret them.
- **Chain handling**: Support multiple chains. Expose the number of warmup/burn-in iterations and allow users to set them. Allow thinning.
- **Posterior summaries**: Return credible intervals (not just point estimates). Document whether intervals are equal-tailed or HDI. Return the full posterior samples or make them accessible.
- **Model comparison**: If you support WAIC, LOO-CV, or Bayes factors, document their computation, assumptions, and limitations.
- **Algorithmic transparency**: Document the sampler used (HMC, NUTS, Gibbs, MH, etc.), its parameters, and the defaults. Expose step-size and tree-depth diagnostics where applicable.

### Regression Standards (RE)

- **Formula interface**: If you implement a formula interface, it must behave consistently with standard R regression functions.
- **Coefficient output**: Return named coefficient estimates. For Bayesian methods this means posterior summaries (mean/median, SD, credible interval) for all parameters.
- **Prediction**: Implement a `predict()` method. Document whether it returns posterior predictive draws, means, or summaries. Distinguish in-sample from out-of-sample behavior.
- **Residuals**: Implement a `residuals()` method where applicable; document the type (raw, Pearson, etc.).
- **Model description**: Implement `print()` and `summary()` methods that include the model formula, family/link, number of observations, and key fit information.
- **Intercept handling**: Document intercept behavior and allow suppression with `-1` or `0` in the formula if applicable.

---

## Step 5: Generate the compliance report

```r
srr::srr_report()          # opens an HTML report of all standards and their status
srr::srr_stats_pre_submit()  # gate check — must pass before submitting
```

`srr_stats_pre_submit()` will error if any `@srrstatsTODO` tags remain unresolved. Fix them all before opening the submission issue.

---

## Step 6: Run `autotest`

`autotest` mutates your function inputs to surface undocumented or incorrectly handled edge cases:

```r
autotest::autotest_package()
```

Review all output. Either fix the flagged behavior or, where the test is not applicable to a Bayesian method (e.g., certain type-coercion mutations), document why in your submission. Reviewers will check that `autotest` issues are addressed.

---

## Step 7: Submit

Submit through the normal rOpenSci process via a new issue at <https://github.com/ropensci/software-review>. Use the statistical software submission template. In the issue:

- List your categories (`BS`, `RE`).
- Link to the `srr_report()` output (render it to a file or GitHub Pages).
- Note any `autotest` findings you've addressed or explicitly marked as not applicable.

The editor will run `@ropensci-review-bot check srr` to verify your standards documentation is complete. `pkgcheck` also includes an srr completeness gate.

---

## Step 8: Graded badges

Statistical packages receive **graded badges** based on how thoroughly they meet standards and pass `autotest`. Broader standards coverage, resolved `autotest` issues, and comprehensive test suites earn higher grades. These are visible on the package repository and the rOpenSci registry.

---

## Quick checklist

- [ ] All general rOpenSci package requirements met (DESCRIPTION, docs, tests, CI)
- [ ] `srr` installed and `srr_stats_roxygen(category = c("bayesian", "regression"))` run
- [ ] All `@srrstatsTODO` tags resolved to `@srrstats` or `@srrstatsNA`
- [ ] `srr_report()` reviewed for gaps
- [ ] `srr_stats_pre_submit()` passes with no errors
- [ ] `autotest::autotest_package()` run and all findings addressed or documented
- [ ] Parameter-recovery tests written with multiple seeds
- [ ] MCMC diagnostics (Rhat, ESS) implemented and tested
- [ ] Prior documentation complete with references
- [ ] `predict()`, `print()`, `summary()`, `residuals()` methods implemented and documented
- [ ] Life Cycle Statement in `CONTRIBUTING.md`
- [ ] Primary method reference cited in documentation
