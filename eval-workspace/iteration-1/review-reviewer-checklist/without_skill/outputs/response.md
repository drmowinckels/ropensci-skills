# How to Review an rOpenSci Package

Congratulations on agreeing to review! Here is a structured guide to conducting an rOpenSci review for a climate data package.

---

## 1. Understand the Review Framework

rOpenSci uses a transparent, open peer review process. Reviews happen publicly on GitHub (in the submission issue on the `ropensci/software-review` repository). The editor manages the process; you communicate directly with the authors and editor by commenting on that issue.

Key documents to read before you start:

- [rOpenSci Reviewer Guide](https://devguide.ropensci.org/reviewerguide.html)
- [rOpenSci Review Template](https://devguide.ropensci.org/reviewtemplate.html)
- [General Review Criteria](https://devguide.ropensci.org/reviewcriteria.html)

---

## 2. Set Up Your Environment

```r
# Install the package from the submission source (usually GitHub)
remotes::install_github("author/packagename", dependencies = TRUE)

# Optionally use pak for better dependency handling
pak::pak("author/packagename")
```

Also install `goodpractice` and `covr` for automated checks:

```r
install.packages(c("goodpractice", "covr"))
```

---

## 3. Structure Your Review

Work through these areas in order. Take notes as you go — you will paste them into the review template.

### 3a. Documentation

- Does the README clearly explain what the package does and why?
- Are all exported functions documented with `roxygen2`? Are `@param`, `@return`, `@examples` present and accurate?
- Is there at least one vignette / article showing a realistic end-to-end workflow (e.g., fetching climate data, tidying it, plotting it)?
- For a climate data package specifically: are the data sources, variable names, units, and any caveats about data quality documented?

### 3b. Functionality

- Install and run all examples. Do they work without errors?
- Work through the vignette(s) manually.
- Try the package against the actual API: does it handle authentication (if needed), pagination, rate limits, and network errors gracefully?
- Check that the "tidying" layer produces genuinely tidy output (one observation per row, one variable per column, consistent column naming).

### 3c. Code Quality

```r
goodpractice::gp("path/to/package")
```

Look for:

- Consistent style (tidyverse style guide is common in rOpenSci packages)
- No `library()` / `require()` calls inside package functions — use `pkg::fn()` or `@importFrom`
- No hardcoded credentials or API keys
- Sensible error messages (prefer `cli::cli_abort()` over `stop()`)
- No unnecessary dependencies

### 3d. Tests

```r
devtools::test()
covr::package_coverage()
```

- Is there a test suite? Does it cover the main functions?
- For API packages: are HTTP calls mocked (e.g., with `httptest2` or `vcr`) so tests run offline and reproducibly?
- Is coverage reasonable (rOpenSci expects meaningful coverage, not a specific percentage, but aim for >75% as a rough guide)?

### 3e. R CMD check

```r
devtools::check()
```

There should be 0 errors and 0 warnings. Notes should be explained or minimal.

### 3f. Package Infrastructure

- Is there a `DESCRIPTION` with a clear `Title`, `Description`, `License` (must be an open license), `URL`, and `BugReports`?
- Is there a `NEWS.md` or `CHANGELOG`?
- Is there a `CONTRIBUTING.md` or contribution guidance in the README?
- Is CI set up (GitHub Actions)?
- Does the package follow rOpenSci's packaging guide conventions?

---

## 4. The Review Checklist

When you post your review to the GitHub issue, use the official rOpenSci review template. Copy and paste the following into your comment:

---

### Package Review

**Reviewer:** <!-- your GitHub handle -->
**Date:** <!-- YYYY-MM-DD -->

#### Documentation

- [ ] **Installation instructions**: Package can be installed from source following README.
- [ ] **Vignette(s)**: At least one vignette demonstrating major use cases is present.
- [ ] **Function documentation**: All exported functions have `@param`, `@return`, and `@examples`.
- [ ] **Examples**: All examples run without errors.
- [ ] **Community guidelines**: Package has `CONTRIBUTING.md` or equivalent guidance.

#### Functionality

- [ ] **Installation**: Package installs cleanly with dependencies.
- [ ] **Functionality**: Package performs the stated functions.
- [ ] **Performance**: No unexpectedly slow operations without explanation.
- [ ] **Automated tests**: Tests pass cleanly (`devtools::test()`).
- [ ] **API coverage**: Key API endpoints or data sources are exposed and documented.

#### For a Climate / Web API Package (additional checks)

- [ ] Authentication is handled securely (credentials are not stored in code, use environment variables or keyring).
- [ ] Network errors produce informative messages.
- [ ] Tests mock HTTP requests (e.g., `vcr`, `httptest2`) so they pass offline.
- [ ] Units and variable definitions are documented.
- [ ] Rate limits or usage constraints are mentioned in documentation.

#### Final Assessment

- [ ] **Significant major issues** requiring changes before acceptance?
- [ ] **Minor issues** to address (list below)?
- [ ] **Recommended for acceptance** (with or without revisions)?

**Estimated time spent on review:** <!-- e.g., 4 hours -->

**Major issues:**

<!-- List here, or "None" -->

**Minor issues / suggestions:**

<!-- List here, or "None" -->

**Overall recommendation:**

<!-- Approve / Approve with minor revisions / Major revisions required -->

---

## 5. Writing Good Feedback

- Be specific: point to file names, line numbers, and function names.
- Be constructive: explain *why* something is a problem and suggest a fix.
- Separate blocking issues from suggestions: make clear what must change vs. what would be nice.
- Acknowledge strengths: note what the package does well — authors work hard on these.
- Tone: rOpenSci reviews are collaborative, not adversarial. The goal is to help the package succeed.

---

## 6. Submitting Your Review

Post your completed review as a comment on the submission issue in `ropensci/software-review`. Tag the editor if you have questions. Reviews are typically due within 3 weeks of accepting, but communicate with the editor if you need more time.

---

## Useful Links

| Resource | URL |
|---|---|
| rOpenSci Dev Guide | https://devguide.ropensci.org |
| Review Template | https://devguide.ropensci.org/reviewtemplate.html |
| Reviewer Guide | https://devguide.ropensci.org/reviewerguide.html |
| software-review repo | https://github.com/ropensci/software-review |
| `goodpractice` | https://github.com/mangothecat/goodpractice |
| `vcr` (HTTP mocking) | https://docs.ropensci.org/vcr/ |
| `httptest2` | https://enpiar.com/httptest2/ |
