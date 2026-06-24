# Submitting Your Government PDF Scraper to rOpenSci

## Is it in scope?

Yes, almost certainly. Your package falls squarely into two in-scope categories:

- **Data extraction** — retrieving data from unstructured sources (PDFs).
- **Data munging** — processing and tidying that extracted data for analysis.

These are explicitly listed as in-scope categories in the rOpenSci scope policy. Because the data comes from government reports (a scientific/research use case), and the output is tidy data ready for analysis, this aligns well with rOpenSci's mission around the data lifecycle and scientific reproducibility.

The one thing to confirm before submitting: **does a similar package already exist?** If another package scrapes the same (or a closely related) class of government PDFs, you will need to articulate a significant difference — in functionality, usability, performance, maintenance, or license openness. "It follows rOpenSci guidelines" is not sufficient. If you are unsure, open a **pre-submission enquiry** issue in `ropensci/software-review` first; editors will advise you before you invest in a full submission.

---

## What to do before you submit

Work through these steps in order.

### 1. Meet the author commitments

By submitting you agree to:

- Maintain the package for **at least 2 years** (or find a successor maintainer if you cannot).
- Submit **before** releasing to CRAN and before submitting a software paper (e.g. JOSS). Conflicting feedback from parallel processes is the reason.
- Not submit multiple packages at the same time — wait for one to be approved.
- Respond to reviewers within weeks/months.

### 2. Get your README into shape

The README is what editors use to assess scope without installing the package. It needs:

- A clear **statement of need** — what problem does this solve, for whom, and why does it matter?
- **Badges**: CI status, test coverage, and a [repostatus.org](https://www.repostatus.org/) badge (at minimum `Active`).
- Install instructions.
- A short **usage demo** — show the key workflow from raw PDF to tidy data.
- A comparison to similar packages (even if brief — "unlike X, this package handles Y").
- Citation information.

### 3. Check the package essentials

- **License**: must be CRAN- or OSI-accepted (MIT, Apache 2.0, GPL-3, etc.).
- **Code of conduct**: include one (e.g. use `usethis::use_code_of_conduct()`).
- **Contributing guidelines**: a `CONTRIBUTING.md` or equivalent.
- **CI on multiple platforms**: at minimum Linux + Windows; macOS is a bonus.
- **Test coverage**: aim for ≥ 75%. PDF scraping code can be tricky to test — consider shipping small sample PDFs as test fixtures in `inst/testdata/`.
- **Full function documentation**: every exported function needs `@return`, `@examples` (no `\dontrun{}`), and `@param` for all arguments.
- **At least one vignette**: walk through a realistic end-to-end workflow.
- **`inst/CITATION`**: add a citation file (use `usethis::use_citation()`).

### 4. Run pkgcheck and clear it

Every submission is auto-checked by the `@ropensci-review-bot` via [`pkgcheck`](https://docs.ropensci.org/pkgcheck/). Run it yourself first so you do not get surprised:

```r
# install if needed
# install.packages("pkgcheck", repos = "https://ropensci.r-universe.dev")
pkgcheck::pkgcheck()
```

Alternatively, add the `ropensci-review-tools/pkgcheck-action` GitHub Action so it runs on every push.

Fix everything marked ❌ (failures) and address items marked 👀 (needs attention) before submitting. Common things pkgcheck will flag:

- Default branch named `master` (rename to `main`).
- Functions missing examples or `@return` documentation.
- `\dontrun{}` in examples (remove it — use real, runnable examples or, for slow examples, `\donttest{}`).
- Missing `URL` or `BugReports` fields in `DESCRIPTION`.
- Missing `CONTRIBUTING` file.
- Failing CI badges.
- Junk files (`.DS_Store`, etc.) committed to the repo.

### 5. Open the submission issue

When pkgcheck is clean, go to [ropensci/software-review](https://github.com/ropensci/software-review/issues/new/choose) and open a new issue using the submission template.

Key things to do in the template:

- Preserve all the HTML comment markers (`<!---variable--->`) and insert your values between them — do not delete or reorder them.
- Provide the full URL to your repository (or the specific branch if it is not the default).
- Write a clear **statement of need** in the template field — this is separate from the README version; keep it concise.
- Select the correct **package category** (Data Extraction and/or Data Munging).
- Confirm that you have run pre-submission checks.

Set your GitHub notification settings to "watching" on the issue so you do not miss anything — all review discussion happens there.

---

## What happens next

1. An editor screens for scope and completeness; the `@ropensci-review-bot` runs pkgcheck and posts results on the issue. You can re-trigger this yourself at any time with `@ropensci-review-bot check package` after pushing fixes.
2. Two reviewers are assigned; they typically have 3 weeks (21 days) to complete their review.
3. Reviewers post public, constructive feedback on the issue. You respond and push changes iteratively.
4. Once both reviewers approve and the editor is satisfied, the editor runs `@ropensci-review-bot approve <pkgname>`. Your repo transfers to the `ropensci` GitHub org, gets a `pkgdown` docs site, and rOpenSci promotes it via blog and social channels. You also become eligible for a fast-tracked JOSS submission if you want a citable paper.

---

## Quick checklist before you open the issue

- [ ] Scope confirmed (data extraction / data munging from government PDFs)
- [ ] No significantly overlapping package (or significant difference documented)
- [ ] 2-year maintenance commitment understood
- [ ] Not yet on CRAN; no software paper submitted elsewhere
- [ ] README has: statement of need, badges, install, demo, comparison, citation
- [ ] CRAN/OSI-accepted license
- [ ] Code of conduct present
- [ ] Contributing guidelines present
- [ ] CI on multiple platforms; coverage ≥ 75%
- [ ] All functions documented with `@return` and working `@examples`
- [ ] At least one vignette
- [ ] `inst/CITATION` present
- [ ] `pkgcheck::pkgcheck()` passes with no ❌ and all 👀 addressed
