# Submitting a Package to rOpenSci Software Peer Review

## Before You Submit

### Check Scope and Fit

rOpenSci only accepts packages that enable reproducible research and manage the data lifecycle for scientists. Before investing time in preparing a submission, confirm your package fits one of these categories:

- **Data retrieval** — accessing scientific data from online sources (must do more than simple downloads)
- **Data extraction** — retrieving data from unstructured sources (text, images, PDFs) or parsing scientific formats
- **Data munging** — processing data in specific scientific formats from workflows or instruments
- **Data deposition** — supporting research data repository deposits with formatting and metadata
- **Data validation and testing** — automated quality checking tools for scientific workflows
- **Workflow automation** — build systems and CI tools for scientific workflows
- **Scientific software wrappers** — non-trivial wrappers of research-specific utilities with significant added value
- **Geospatial data** — accessing, manipulating, and converting geospatial formats
- **Citation management and bibliometrics**
- **Database software bindings** — generic database API wrappers

General-purpose utilities, data visualization packages, and tools that replicate existing R packages without significant improvement are out of scope.

**If you are unsure whether your package fits**, open a pre-submission inquiry as a GitHub issue in [ropensci/software-review](https://github.com/ropensci/software-review) before doing a full submission. Editors will advise on fit and flag overlap with existing packages. This saves everyone time.

### Assess Readiness

Before submitting, make sure:

- Your package is mature enough for comprehensive reviewer assessment — all major functions are documented and tested
- You are willing and able to maintain the package for at least 2 years, or have someone lined up to take over
- The package has not been simultaneously submitted for review at another venue (JOSS, journal, etc.)
- You carry Active (repostatus.org) or Stable (lifecycle) badge status
- The README explains the package goals, usage, and similar packages clearly enough that an editor can assess scope without installing it

If you plan to submit to JOSS, do so _after_ the rOpenSci review completes. For _Methods in Ecology and Evolution_, you can submit after reviewers submit their assessments.

### Run pkgcheck

rOpenSci requires all authors to run the `pkgcheck` package locally before submitting:

```r
# install if needed
# remotes::install_github("ropensci-review-tools/pkgcheck")
library(pkgcheck)
checks <- pkgcheck()
summary(checks)
```

Alternatively, add the `pkgcheck` GitHub Action to your repository. The submission bot will also run this automatically when you open the issue, but you are expected to have already reviewed the results. If your package cannot pass certain checks, you will need to explain why in the submission template.

### Follow the Packaging Guide

Read the [rOpenSci Packaging Guide](https://devguide.ropensci.org/pkg_building.html) and ensure your package meets style and quality standards. Key requirements:

- roxygen2 documentation with `@examples` for all exported functions
- A vignette demonstrating essential functionality
- A test suite with continuous integration and coverage reporting
- A README with instructions for development installation
- CRAN- or OSI-accepted license
- No Terms of Service violations in the package

---

## The Submission

### Open a GitHub Issue

Go to [github.com/ropensci/software-review](https://github.com/ropensci/software-review) and open a new issue using the **"Submit software for review"** issue template.

### What the Template Asks For

The submission template contains HTML-comment-delimited variable blocks managed by the `ropensci-review-bot`. Fill in all required fields between the indicated markers. The template covers:

**Header fields:**

- Submitting author name and GitHub handle
- Other package authors' GitHub handles
- Repository URL
- Version being submitted
- Submission type (standard vs. statistical)

**Scope section:**

- Which category (or categories) your package belongs to — select from the list
- A 1–2 sentence explanation of the category selection
- Description of target audience and scientific applications
- How the package differs from similar existing tools, or why it qualifies as best-in-category
- Reference to any pre-submission inquiry, if you opened one
- Explanation of any `pkgcheck` items your package cannot pass, and why

**Technical checklist** (you confirm each item):

- [ ] Read the packaging guide and author guide
- [ ] Committing to 2-year maintenance
- [ ] No Terms of Service violations
- [ ] CRAN/OSI-accepted license
- [ ] README with development installation instructions
- [ ] roxygen2 docs with function examples
- [ ] Vignette demonstrating essential functions
- [ ] Test suite with CI and coverage reporting
- [ ] Compliance with ethics and data privacy guidance (if applicable)

**Additional disclosures:**

- Generative AI usage during package development (required as of 2026)
- Publication intentions (CRAN, Bioconductor, Methods in Ecology and Evolution)
- Code of Conduct agreement

---

## After Submission: The Review Process

### Step 1 — Automated Checks (Immediate)

The `ropensci-review-bot` immediately runs `pkgcheck` on your package and posts a report in the issue thread. Editors use this as a primary input for their initial assessment. Review this report carefully.

### Step 2 — Editorial Assessment (Within 5 Business Days)

An editor reads the submission and the bot report, then responds with one of:

- **Proceed to review** — the package meets minimum criteria; reviewers will be assigned
- **Revise before review** — the editor identifies gaps that need fixing before the review can start; once addressed, the review proceeds
- **Reject** — the package is out of scope or substantially overlaps with an existing package

### Step 3 — Reviewer Assignment

If the package proceeds, the editor assigns 1–3 external reviewers with relevant domain or technical expertise. Reviewers have 3 weeks to submit their assessments as comments on the GitHub issue.

### Step 4 — The Reviews

Reviewers post their feedback directly on the submission issue. They assess:

- Package functionality and correctness
- Documentation quality (README, function docs, vignettes)
- Test coverage
- API design and usability
- Adherence to rOpenSci packaging standards
- Any domain-specific concerns

This is an open, non-adversarial process — all review communication happens publicly on GitHub so the full record is preserved.

### Step 5 — Author Response and Revisions

After all reviewers have submitted, you have **2 weeks** to respond and submit revisions. Your response should:

1. Post a comment on the issue acknowledging each reviewer's points
2. Implement changes in your package
3. Update `NEWS.md` to document what changed
4. Link to the updated `NEWS.md` in your response comment
5. Submit your response via the bot command:
   ```
   @ropensci-review-bot submit response to reviewers
   ```

If your changes affect `pkgcheck` results, request a re-check:

```
@ropensci-review-bot check package
```

Conversations between authors and reviewers are encouraged throughout — ask for clarification if feedback is ambiguous, push back if you disagree, and negotiate what is in scope.

### Step 6 — Approval

Once reviewers and the editor are satisfied with the revisions, the editor marks the package as accepted. The review issue is closed.

### Step 7 — Post-Acceptance Onboarding

After acceptance, rOpenSci provides instructions to transfer your repository to the [ropensci GitHub organization](https://github.com/ropensci):

1. **Transfer the repo** via GitHub Settings → "Transfer ownership" → `ropensci`
2. You are made admin of the transferred repository
3. **Remove your existing Code of Conduct file** — rOpenSci's default CoC applies organization-wide
4. **Update all links** in your README, DESCRIPTION, and documentation to point to the new `github.com/ropensci/` URL
5. After transfer, a **pkgdown site** is automatically built and deployed to `https://docs.ropensci.org/<your-package-name>` on every push to the default branch, using rOpenSci's styling template

Your package is then listed on the rOpenSci website and is eligible for promotion through rOpenSci's blog and social channels.

---

## Key Links

- [rOpenSci Software Review repository](https://github.com/ropensci/software-review) — where you open your submission issue
- [Guide for Authors](https://devguide.ropensci.org/softwarereview_author.html) — complete author-facing instructions
- [Scope and Fit Policies](https://devguide.ropensci.org/softwarereview_policies.html) — what is in and out of scope
- [Packaging Guide](https://devguide.ropensci.org/pkg_building.html) — standards your package must meet
- [pkgcheck](https://github.com/ropensci-review-tools/pkgcheck) — automated checks to run before submitting

Sources:

- [Guide for Authors – rOpenSci Packages: Development, Maintenance, and Peer Review](https://devguide.ropensci.org/softwarereview_author.html)
- [Software Peer Review Policies – rOpenSci Packages](https://devguide.ropensci.org/softwarereview_policies.html)
- [rOpenSci Software Peer Review](https://ropensci.org/software-review/)
- [rOpenSci Software Peer Review Workshop](https://ropensci-training.github.io/software-review/en/)
- [Submit software for review – issue template](https://github.com/ropensci/software-review/blob/main/.github/ISSUE_TEMPLATE/A-submit-software-for-review.md)
- [pkgcheck – ropensci-review-tools](https://github.com/ropensci-review-tools/pkgcheck)
