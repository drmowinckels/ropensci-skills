# Initial Editor Checks for a New rOpenSci Submission

As the handling editor, you should complete these checks within **5 working days** and post your results using the editor template before assigning reviewers.

---

## 1. Confirm the EiC Handoff

The Editor-in-Chief (EiC) should have already run:

```
@ropensci-review-bot assign @yourhandle as editor
```

This applies the `1/editor-checks` label to the issue. Verify this label is present and that the submission issue template was properly filled out by the author.

---

## 2. Run or Review Automatic Package Checks

The review bot automatically generates package check output. Your job is to:

- Review all **failures (❌)** — these must be resolved before review proceeds (exceptions are possible but must be justified).
- Review all items flagged with **👀** — these warrant attention and may require you to ask the author for more information.
- If checks haven't run yet, the author (or you) can trigger them:
  ```
  @ropensci-review-bot check package
  ```
- **For statistical software submissions**: Add the `stats` label to the issue. If the authors indicate they have documented standards via the `srr` package, also run:
  ```
  @ropensci-review-bot check srr
  ```
  The package must meet at least 50% of applicable standards to proceed.

The bot also generates a **Statistical Properties** section that flags unusual values (in the upper or lower fifth percentile compared to CRAN packages) for:

- Lines of code
- Exported function counts
- Package structure (interactive network visualization)

Assess whether these values indicate the package is too small (trivial) or too large/complex for a reasonable review scope.

---

## 3. Assess Scope and Fit

Check whether the package is within rOpenSci's scope. In-scope categories include:

- Data retrieval from scientific sources
- Data extraction from unstructured sources (text, images, PDFs)
- Data processing in domain-specific scientific formats
- Data deposition to repositories
- Data validation and testing
- Workflow automation and reproducibility tools
- Version control facilitators
- Citation and bibliometrics tools
- Scientific software wrappers
- Database access tools

**Out of scope:** general data visualization packages, statistical/ML modelling libraries (unless they wrap scientific software), and broad-purpose data manipulation utilities.

**Overlap policy:** A new package overlapping an existing one is acceptable only if it demonstrates significant improvement — better license, broader functionality, better performance, or actively maintained replacement for an abandoned package.

If you are uncertain about fit or overlap, raise the question in the `#software-review` Slack channel before proceeding.

---

## 4. Complete the Editor Checks Template

Post your initial editorial comment using the editor template. The checklist covers:

- [ ] **Documentation**: Package has sufficient online documentation (README, pkgdown site) to assess functionality without installing. Specifically:
  - Is the case for the package well made?
  - Is the reference index page clear (grouped by topic if necessary)?
  - Are vignettes readable, sufficiently detailed, and not just perfunctory?
- [ ] **Fit**: The package meets rOpenSci criteria for scope and does not unacceptably duplicate existing packages.
- [ ] **Installation instructions**: Are installation instructions clear enough for human users?
- [ ] **Tests**: If the package involves interactivity, HTTP requests, or plot production, are the tests using appropriate modern tooling?
- [ ] **Contributing information**: Is contribution documentation clear (e.g., tokens needed for tests, playgrounds)?
- [ ] **License**: The package has a CRAN or OSI-accepted license.
- [ ] **Project management**: Are the issue and PR trackers in reasonable shape? Are outstanding bugs tracked? Is it clear when feature requests will be addressed?

---

## 5. Verify Multi-Platform Testing

Confirm the package is tested across multiple operating systems (Windows, macOS, Linux) via GitHub Actions or a comparable CI service. This is a requirement before review.

---

## 6. Address Major Issues Before Assigning Reviewers

If your checks reveal significant problems:

- Request changes from the author directly in the issue.
- Ideally, any remarks you make should be addressed before reviewers are assigned.
- If the changes will take substantial time, put the submission on hold:
  ```
  @ropensci-review-bot put on hold
  ```
- When the author has addressed your comments and the submission is ready, you can proceed to find reviewers.

---

## References

- [Guide for Editors — rOpenSci Dev Guide](https://devguide.ropensci.org/softwarereview_editor.html)
- [Editor's Template — rOpenSci Dev Guide](https://devguide.ropensci.org/editortemplate.html)
- [Software Peer Review Policies — rOpenSci Dev Guide](https://devguide.ropensci.org/softwarereview_policies.html)
- [Statistical Software Peer Review — Guide for Editors](https://stats-devguide.ropensci.org/pkgsubmission.html)
