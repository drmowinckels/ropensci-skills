# Submitting Your Government PDF Scraper to rOpenSci

## Is it in scope?

Yes — your package is a strong fit. rOpenSci's scope covers data retrieval and
extraction packages that support the scientific data lifecycle. A package that
scrapes and tidies data from government PDF reports is precisely that: it makes
otherwise inaccessible public data available to researchers in a tidy,
programmatic form. This falls squarely into the **data access / data retrieval**
category.

One thing to confirm: does a similar package already exist that does the same
job for the same source? If so, you will need to articulate a significant
difference — functionality, usability, maintenance, or license — not just "mine
follows rOpenSci guidelines." If there is no real overlap, you are clear.

If you have any doubt after checking, open a **pre-submission enquiry** issue in
`ropensci/software-review` rather than a full submission. Editors respond quickly
and it saves you work if they spot an issue.

---

## What to do before you submit

Work through these five areas in order.

### 1. Author commitments

By submitting you agree to:

- Maintain the package for at least **2 years** (or hand it to a new
  maintainer).
- Submit **before** publishing on CRAN or submitting a JOSS/similar paper —
  conflicting feedback is the risk otherwise.
- Not submit more than one package at a time.
- Stay responsive to review discussion over the weeks/months it takes.

### 2. Run pkgcheck and fix everything it flags

Install and run `pkgcheck` locally before you submit:

```r
# install if needed
install.packages("pkgcheck", repos = "https://ropensci.r-universe.dev")

pkgcheck::pkgcheck()
```

Alternatively, add the `ropensci-review-tools/pkgcheck-action` GitHub Action to
your repo so it runs on every push.

Fix every ❌ (blocking failure) and address every 👀 (needs attention) before
opening the submission issue. The bot will run the same checks immediately after
you submit, and an editor will screen against them.

### 3. Submission-readiness checklist

These are what an editor checks in the first few minutes:

**README**

- [ ] Statement of need — why does this package exist, who is it for?
- [ ] Badges: CI status, test coverage, repostatus (at minimum `active`)
- [ ] Installation instructions
- [ ] Short worked example (enough to show what the package does without
      installing it)
- [ ] Comparison to similar packages, if any exist
- [ ] Citation information (`citation("yourpkg")` and/or a `CITATION` file)

**Licensing**

- [ ] A CRAN- or OSI-accepted open-source license in `LICENSE` / `DESCRIPTION`

**Community files**

- [ ] Code of conduct (`CODE_OF_CONDUCT.md`)
- [ ] Contributing guidelines (`CONTRIBUTING.md`)

**CI and testing**

- [ ] CI running on at least two platforms (e.g. ubuntu + macOS, or ubuntu +
      windows)
- [ ] Test coverage ≥ 75% (aim higher; PDF scraping logic is testable with
      fixture files)

**Documentation**

- [ ] All exported functions have full roxygen2 docs (title, description, all
      params, return value, at least one `@example`)
- [ ] At least one vignette that walks through a real use-case end to end

### 4. Open the submission issue

Go to <https://github.com/ropensci/software-review/issues/new/choose> and
select the **Package Submission** template.

Key things when filling it in:

- Preserve the HTML variable markers (`<!---variable--->`) exactly — the bot
  parses them.
- Provide the full repository URL (link to a specific branch if it is not the
  default).
- Write a clear **statement of need** — assume the editor has little domain
  knowledge about government PDF reports.
- Select the correct **package category** (data access / data retrieval for
  your case).
- Confirm that pre-submission checks pass.

All review discussion happens on that issue. Make sure your GitHub notifications
are turned on for it.

---

## What happens after you submit

1. An editor screens for scope and completeness; `@ropensci-review-bot` runs
   pkgcheck automatically.
2. Two reviewers are recruited (the default review window is ~3 weeks each).
3. Review is public, iterative, and non-adversarial — more like code review from
   supportive colleagues than gatekeeping.
4. Once approved, `@ropensci-review-bot approve <pkg>` is issued, your repo
   transfers to the `ropensci` GitHub org, you get a `pkgdown` docs site, and
   the package is promoted via the rOpenSci blog and social channels.
5. You also get the option of a fast-tracked JOSS submission if you want a
   citable software paper.

---

## Summary: the short version

Your package is in scope. Before submitting:

1. Run `pkgcheck::pkgcheck()` and clear all failures.
2. Make sure your README covers need, badges, install, demo, and comparison.
3. Add a code of conduct and contributing guide.
4. Get CI green on multiple platforms with ≥ 75% test coverage.
5. Write at least one vignette.
6. Open the submission issue at `ropensci/software-review` using the template.
