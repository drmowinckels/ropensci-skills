---
name: package-review
description: >-
  Help a reviewer (or editor) conduct an rOpenSci software peer review of an R
  package. Use this whenever someone has agreed to review a package for rOpenSci,
  asks "how do I review this package", wants the rOpenSci reviewer checklist /
  review template, needs to evaluate a package's docs/tests/code/UX for review, or
  is an editor doing initial editor checks. Covers the official reviewer checklist
  and template, what to evaluate beyond the checkboxes, reviewer conduct and
  timing, the pkgreviewr tooling, and the editor checks. This is for people
  REVIEWING a package; authors preparing to submit should use
  peer-review-author instead.
---

# rOpenSci Peer Review — Reviewer & Editor Guide

This skill helps you carry out a constructive, open, non-adversarial review of an R
package for rOpenSci. Reviews happen publicly on the `ropensci/software-review`
GitHub issue and are signed (non-anonymous).

**Using the references efficiently.** The summaries below answer "what's on the
checklist" and "what do editors check" on their own. Open
`references/review-template.md` when you're actually filling in a review and need
the verbatim template, and `references/editor-checks.md` when you need the full
editor checklist text — not by default.

Primary sources:
<https://devguide.ropensci.org/softwarereview_reviewer.html>,
<https://devguide.ropensci.org/reviewtemplate.html>,
<https://devguide.ropensci.org/softwarereview_editor.html>.

## Before you start

- **Confirm no conflict of interest.** If unsure, ask the editor before starting.
- **Timing**: strive to complete the review **within 3 weeks** of accepting.
- Read the package's submission issue, README, and pkgcheck report first.
- Optionally scaffold your review project with the **pkgreviewr** package — it
  clones the repo and sets up the review document in RStudio.

## Do the hands-on checks

Don't review from reading alone — exercise the package:

- Run `devtools::check()` and `devtools::test()` locally; confirm all tests pass.
- Verify any **skipped tests** are justified.
- **Install it as documented** and confirm installation succeeds.
- Work through the vignette(s) and examples; confirm they run.
- Try the package on **your own data/problem** — this surfaces real UX issues.
- Read the `@ropensci-review-bot` pkgcheck report and the CI / Codecov logs.
- If the package changed substantially, re-trigger checks with
  `@ropensci-review-bot check package`.

## Fill in the review template

When you actually write the review, use the official template verbatim (full text in
`references/review-template.md`). Check boxes as applicable and **elaborate in
comments** — your review isn't limited to the checkboxes. The template groups into:

- **Documentation**: statement of need, install instructions, vignette(s),
  function documentation, examples, community guidelines (CONTRIBUTING +
  DESCRIPTION with URL/BugReports/Maintainer).
- **Functionality**: installation, functional claims, performance claims,
  automated tests, conformance to the packaging guidelines.
- **Estimated hours spent** and whether you agree to be credited as reviewer
  (`"rev"` role).

## Evaluate beyond the checkboxes

The reviewer guide asks you to weigh in on:

1. Compliance with the rOpenSci **packaging guide** (see `package-standards`).
2. **Code quality** — style, patterns, duplication.
3. **Dependencies** — could base R or a lighter dep replace helper code?
4. **UI/UX** improvements.
5. **Performance** / optimization opportunities.
6. **Documentation** — installation, vignettes, examples; multiple points of entry.
7. **API design** — function/argument names that read well and autocomplete sensibly.
8. **Real-world testing** — does it hold up on actual problems?

## Conduct

- **Be respectful and kind.** Reviews are open, non-adversarial, and aimed at
  improving the software. The code of conduct applies.
- Capture any off-thread discussion back on the issue with links.
- Submit your review as a comment on the GitHub issue; link any PRs/issues you file
  on the package itself.
- When re-reviewing after the author responds, use the approval template.

## If you are the editor

Editors do initial checks before assigning two reviewers. The full editor checks
template is in `references/editor-checks.md`. In brief:

- Documentation sufficient to assess scope **without installing**; case for the
  package well made; clear reference index; vignettes more than perfunctory.
- **Fit**: meets scope/overlap criteria.
- Clear installation instructions; state-of-the-art tooling for interactivity /
  HTTP / plot tests; clear contributing info; CRAN/OSI license; healthy issue & PR
  trackers.
- Assign **exactly two** reviewers (`@ropensci-review-bot assign @user as
reviewer`), avoid reviewers who reviewed in the last 6 months, default 21-day
  due date. For statistical packages also run `@ropensci-review-bot check srr`.

## Related skills

- The standards you're checking against → `package-standards`.
- Reviewing a **statistical** package → `stats-standards` (assess
  `@srrstats` standards compliance).
- The author's side of the same process → `peer-review-author`.
