# How to Conduct an rOpenSci Package Review

Congratulations on agreeing to review! Here is a complete guide to the process and the checklist you need to fill out.

---

## Overview of the Process

### 1. Prepare before you start

- Base your review on the **latest commit on the default branch** of the package's GitHub repository, unless the editor specifies otherwise.
- Check the **automated `pkgcheck` report** posted by `@ropensci-review-bot` in the submission issue — it runs `R CMD check`, `goodpractice`, and rOpenSci-specific structural checks. Read it before touching the code.
- Install the package and all its dependencies locally so you can run examples and tests.
- Optionally use the [`pkgreviewr`](https://github.com/ropensci-org/pkgreviewr) package, which clones the repo and scaffolds a review project with the template pre-loaded.

### 2. Work through the package

Go through the package systematically. For a climate data / API package, pay attention to the areas below (details in the "What to look for" section).

### 3. Write and submit your review

- Copy the **review template** (reproduced in full below).
- Fill in the checkboxes and write your narrative comments.
- Post your completed review as a **single comment** in the GitHub issue for the submission on [ropensci/software-review](https://github.com/ropensci/software-review).
- If you opened any issues or PRs directly in the package repository, link to them from your review comment.

### 4. Timeline

Complete your review within **3 weeks** of accepting. The editor will send reminders. If you cannot finish in time, let the editor know as early as possible.

### 5. After the review

Authors have approximately **2 weeks** to respond and push changes. You then assess whether the changes adequately address your concerns and post a follow-up comment. When satisfied, use the approval template the editor provides.

---

## What to Look For

### General quality (any package)

- Does the package follow the [rOpenSci packaging guide](https://devguide.ropensci.org/pkg_building.html)?
- Are functions an appropriate size, with minimal duplication?
- Are dependencies justified — could base R or a lighter package do the same job?
- Is the user interface clear and consistent (naming conventions, argument order)?
- Is documentation thorough and accurate, with working examples?
- Do all tests pass locally? Is coverage reasonable?

### Specific to API / climate data packages

Because this package wraps a public API and tidies climate data, also check:

**HTTP client and user agent**
The package should use `httr2`, `httr`, `curl`, or `crul` (not `RCurl`). It must set a user-agent string that identifies the package and version, with a way for users to override it.

**Authentication**
Credentials (API keys, tokens) must never be hard-coded. The package should use environment variables and document clearly how to set them. Secrets must not appear in examples, vignettes, or test fixtures.

**Pagination and rate limiting**
The package should handle pagination transparently so users do not have to manage it manually. Rate-limiting behaviour should follow the API's own specifications.

**Error handling**
API errors should be surfaced as informative R errors — not silent failures or raw HTTP responses. Check whether the error messages help a user understand what went wrong.

**Data source documentation**
The `DESCRIPTION` file and the README/vignettes must identify the data-issuing organisation and link to the public data access page. This is a hard rOpenSci requirement for packages accessing external data.

**Testing**
API calls in tests must be mocked so they do not hit the live service on CRAN. Recommended packages: `httptest2` (httr2), `httptest` (httr), `vcr` (httr/crul), or `webfakes`. Tests that call the real API should use `skip_on_cran()` and should still run in CI.

**Data tidying**
Review the output format. Is it consistently tidy (one row per observation, one column per variable)? Are column names, units, and data types sensible and documented?

---

## The Review Checklist (Official Template)

Post this as your review comment in the GitHub issue. Check boxes off as you go and add narrative comments under "Review Comments".

---

```
## Package Review

*Please check off boxes as applicable, and elaborate in comments below.
Your review is not limited to these topics, as described in the reviewer guide.*

- **Briefly describe any working relationship you have (had) with the package authors.**
- [ ] As the reviewer I confirm that there are no [conflicts of interest](https://devguide.ropensci.org/policies.html#coi) for me to review this work (if you are unsure whether you are in conflict, please speak to your editor _before_ starting your review).

#### Documentation

The package includes all the following forms of documentation:

- [ ] **A statement of need:** clearly stating problems the software is designed to solve and its target audience in README
- [ ] **Installation instructions:** for the development version of package and any non-standard dependencies in README
- [ ] **Vignette(s):** demonstrating major functionality that runs successfully locally
- [ ] **Function Documentation:** for all exported functions
- [ ] **Examples:** (that run successfully locally) for all exported functions
- [ ] **Community guidelines:** including contribution guidelines in the README or CONTRIBUTING, and DESCRIPTION with `URL`, `BugReports` and `Maintainer` (which may be autogenerated via `Authors@R`).

#### Functionality

- [ ] **Installation:** Installation succeeds as documented.
- [ ] **Functionality:** Any functional claims of the software have been confirmed.
- [ ] **Performance:** Any performance claims of the software have been confirmed.
- [ ] **Automated tests:** Unit tests cover essential functions of the package and a reasonable range of inputs and conditions. All tests pass on the local machine.
- [ ] **Packaging guidelines**: The package conforms to the rOpenSci packaging guidelines.

Estimated hours spent reviewing:

- [ ] Should the author(s) deem it appropriate, I agree to be acknowledged as a package reviewer ("rev" role) in the package DESCRIPTION file.

---

### Review Comments

```

---

## Tone and Conduct

Reviews should be open, respectful, and non-adversarial. You are helping improve the software, not gatekeeping. The [rOpenSci code of conduct](https://ropensci.org/code-of-conduct/) applies throughout. If you have substantive discussions with the authors outside the issue thread (Slack, email), capture the key points in your review comment so the record is complete.

---

## Useful Resources

- [Reviewer guide](https://devguide.ropensci.org/softwarereview_reviewer.html)
- [rOpenSci packaging guide](https://devguide.ropensci.org/pkg_building.html) — the standard the package is being held to
- [pkgreviewr](https://github.com/ropensci-org/pkgreviewr) — helper package to scaffold your review workflow
- [Approved submissions](https://github.com/ropensci/software-review/issues?q=is%3Aissue+is%3Aclosed+label%3A6%2Fapproved) — browse past reviews for examples of depth and style
