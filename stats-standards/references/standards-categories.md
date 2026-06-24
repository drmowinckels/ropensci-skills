# Statistical Standards: General + Categories

Sources: <https://stats-devguide.ropensci.org/standards.html> (standards v0.2.0),
<https://docs.ropensci.org/srr/>

Every statistical package must comply with **all applicable General Standards**
plus **at least one category set**. Below is the structure and codes of the General
Standards so you can recognize and apply them. For exact prose and for the
category-specific standards, read the live standards page — it's long and updated,
so don't rely on memory for the precise wording.

## General Standards (G)

### G1 Documentation

- **G1.0** List the primary academic reference.
- **G1.1** State whether the algorithm is novel, the first R implementation, or an
  improvement on existing ones.
- **G1.2** Include a Life Cycle Statement (in CONTRIBUTING.md).
- **G1.3** Clarify all statistical terminology unambiguously.
- **G1.4** Use roxygen2 for documentation; **G1.4a** document internal functions
  with `@noRd`.
- **G1.5** Include code reproducing any performance claims.
- **G1.6** Include code comparing performance with alternative implementations.

### G2 Input Structures

- **G2.0** Assert input lengths; **G2.0a** document length expectations.
- **G2.1** Assert input types; **G2.1a** document type expectations.
- **G2.2** Prohibit multivariate input where univariate is expected.
- **G2.3** Handle character input: **G2.3a** use `match.arg()` for permitted
  values; **G2.3b** handle case sensitivity explicitly.
- **G2.4** Provide type conversion (**G2.4a–e** specific conversions).
- **G2.5** Document factor-ordering expectations.
- **G2.6** Preprocess one-dimensional input regardless of class.
- **G2.7** Accept diverse tabular input forms; **G2.8** dispatch to consistent
  handling; **G2.9** warn on information loss.
- **G2.10–G2.12** Consistent column extraction; handle columns without standard
  class attributes; handle list columns.
- **G2.13–G2.16** Missing/undefined data: check for it, provide handling options
  (**G2.14a–c** error / ignore / impute), never assume non-missingness, handle
  undefined values (Inf/NaN).

### G3 Algorithms

- **G3.0** Never compare floating-point numbers for equality.
- **G3.1 / G3.1a** Let users choose covariance algorithms; document this.

### G4 Output Structures

- **G4.0** When outputs are written to file, parse file-name parameters and
  auto-generate suffixes.

### G5 Testing

- **G5.0** Use standard datasets with known properties; **G5.1** export test
  datasets users can verify against.
- **G5.2** Demonstrate error/warning behavior; **G5.2a** unique messages;
  **G5.2b** test the conditions that trigger each.
- **G5.3** Test that outputs are free of missing/undefined values.
- **G5.4** Correctness tests against fixed data; **G5.4a–c** new methods vs.
  existing implementations vs. published outputs.
- **G5.5** Use a fixed random seed for correctness tests.
- **G5.6** Parameter-recovery tests; **G5.6a** define tolerance; **G5.6b** multiple
  seeds.
- **G5.7** Performance scales as expected as data properties change.
- **G5.8** Edge conditions: **G5.8a–d** zero-length, unsupported types, all-NA,
  out-of-scope data.
- **G5.9** Noise susceptibility: **G5.9a** trivial noise; **G5.9b** different seeds.
- **G5.10–G5.12** Extended tests behind an env-var flag, with downloadable assets
  (**G5.11a** skip — don't fail — when downloads are unavailable) and documentation
  of requirements.

## Category-specific standard sets

Pick every category your package touches and satisfy its standards (read the full
text online):

| Code      | Category                                                     | Approx. # |
| --------- | ------------------------------------------------------------ | --------- |
| `BS`      | Bayesian & Monte Carlo                                       | ~70       |
| `EA`      | Exploratory Data Analysis & Summary Statistics               | ~30       |
| `ML`      | Machine Learning                                             | ~60       |
| `RE`      | Regression & Supervised Learning                             | ~25       |
| `SP`      | Spatial                                                      | ~20       |
| `TS`      | Time Series                                                  | ~15       |
| `UL`/`US` | Dimensionality Reduction, Clustering & Unsupervised Learning | ~25       |
| `PD`      | Probability Distributions                                    | ~15       |

Full category text: <https://stats-devguide.ropensci.org/standards.html>

## How standards appear in code (srr)

```r
#' @srrstats {G2.0a} Documented and asserted that `x` has length 1.
#' @srrstats {G5.5} Correctness tests use set.seed(1) for reproducibility.
#' @srrstatsNA {G4.0} No outputs are written to file, so this does not apply.
```

`@srrstatsTODO` tags are placeholders left by `srr_stats_roxygen()`; convert each to
`@srrstats` (met) or `@srrstatsNA` (not applicable, with reason) before submission.
