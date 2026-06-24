# Initial Editor Checks for a New rOpenSci Submission

As the handling editor, you perform a set of checks before assigning reviewers to confirm the submission is complete, appropriate, and ready for review. Here is what to do.

## 1. Confirm the Package is in Scope

Review the package against rOpenSci's scope criteria:

- It should fit one of the accepted categories (data access, data extraction, scientific software wrappers, workflow tools, etc.).
- It should not be a general utility package without a clear research/scientific use case.
- It should not duplicate an existing rOpenSci package without substantial improvement.

If scope is unclear, consult the rOpenSci Slack `#editors` channel or ping the editor-in-chief before proceeding.

## 2. Check the Submission Issue

The author opens a GitHub issue in the `ropensci/software-review` repo. Confirm:

- The submission template is complete (all sections filled in).
- The package repository URL is provided and publicly accessible.
- The author has confirmed the package is not under simultaneous review elsewhere.

## 3. Run Automated Checks with `pkgcheck`

Use the `pkgcheck` tool (or check the automated bot output if already triggered) to assess:

- Package structure and metadata (DESCRIPTION fields, LICENSE, README).
- Documentation completeness (all exported functions documented, examples present).
- Test coverage.
- Compliance with rOpenSci packaging guidelines.

The `@ropensci-review-bot check package` command in the issue triggers this automatically. Review the output and flag any critical failures to the author before proceeding.

## 4. Install and Basic Functionality Check

Install the package from the author's repository and do a quick manual check:

```r
remotes::install_github("author/package")
```

- Confirm it installs without errors.
- Run `?package` or browse the documentation to confirm it does what it claims.
- Confirm the README includes a working example.

## 5. Check Against rOpenSci Packaging Guide

Manually verify key standards from the [rOpenSci Packaging Guide](https://devguide.ropensci.org/):

- Has a `README` with install instructions and a usage example.
- Has a `NEWS.md` or changelog.
- Uses `testthat` (or another test framework) with reasonable coverage.
- Uses `roxygen2` for documentation.
- Has a `DESCRIPTION` with a meaningful `Title`, `Description`, `Authors@R`, and `URL`/`BugReports` fields.
- Preferably uses `cli` or similar for user-facing messages rather than bare `cat()`/`message()`.

## 6. Check for Obvious Policy or Ethics Issues

- Does the package access sensitive data or make network requests? If so, confirm there is appropriate handling (API key management, no hardcoded credentials, etc.).
- Does the README or vignette mention relevant terms of service for any third-party APIs?

## 7. Assess Reviewer Fit

Once the package passes initial checks, identify two reviewers who:

- Have domain expertise relevant to the package's topic.
- Have R package development experience.
- Have no conflicts of interest with the authors.

Use the rOpenSci reviewer database and Slack to identify candidates.

## 8. Communicate with the Author

Post an editor comment in the submission issue:

- Confirm you are the handling editor and the package is in scope.
- Mention if any issues need to be addressed before review begins.
- Let them know you are seeking reviewers and give a rough timeline (typically 2–3 weeks to find reviewers).

You can use the bot command `@ropensci-review-bot assign editor @yourhandle` if not already assigned.

---

**Key resource:** [rOpenSci Dev Guide — Editors' Guide](https://devguide.ropensci.org/editorguide.html)
