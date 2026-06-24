---
name: peer-review-author
description: >-
  Guide an R package author through preparing for and submitting to rOpenSci
  software peer review (the ropensci/software-review process). Use this whenever
  someone wants to submit a package to rOpenSci, asks "is my package in scope",
  "am I ready to submit to rOpenSci", "what does the submission need", how to
  fill in the submission issue, how to run pkgcheck before submitting, or how the
  @ropensci-review-bot and the review process work from the author's side. Covers
  the scope/fit and overlap policy, the pre-submission checklist, running
  pkgcheck, the submission template, and what to expect during review. For making
  the package itself compliant, pair with package-standards; for
  statistical packages also use stats-standards.
---

# rOpenSci Peer Review — Author Guide

This skill helps an author get a package **ready to submit** to rOpenSci software
peer review and through the submission itself. The package must already follow the
packaging standards — use `package-standards` for that — this skill adds
the submission-specific steps.

**Using the references efficiently.** The steps below answer the common case on
their own. Open `references/scope-and-policies.md` only when scope is genuinely
borderline or you need the exact category wording, and `references/pkgcheck-and-bot.md`
only when you need the full pkgcheck list or exact `@ropensci-review-bot` command
syntax. Don't read either by default.

Primary sources:
<https://devguide.ropensci.org/softwarereview_author.html>,
<https://devguide.ropensci.org/softwarereview_policies.html>,
<https://devguide.ropensci.org/softwarereview_intro.html>.

## Step 1 — Check scope and fit (do this first)

Submission is wasted effort if the package isn't in scope. Before anything else,
confirm the package fits an in-scope category and doesn't overlap problematically
with an existing package. The gut-check below resolves most cases; if it's
borderline, the full category list and overlap policy are in
`references/scope-and-policies.md`.

Quick gut-check:

- Is it a **general-purpose tool tied to the data lifecycle / scientific
  reproducibility** (data retrieval, extraction, munging, deposition, validation,
  workflow automation, geospatial, database bindings, scientific software
  wrappers, etc.)?
- **Out of scope** includes: data visualization packages, broad data-manipulation
  utilities, generic computing tools, code parsers.
- If a similar package exists, can you articulate a **significant difference**
  (functionality, usability, performance, maintenance, license)? "Follows rOpenSci
  guidelines" is not a sufficient difference.

If scope is uncertain, the right move is a **pre-submission enquiry** issue rather
than a full submission.

## Step 2 — Meet the author commitments

By submitting, the author agrees to:

- **Maintain the package for at least 2 years** (or find a new maintainer).
- Submit **before** publishing on CRAN or submitting a software paper (avoids
  conflicting feedback).
- **Not** submit multiple packages at once — wait for approval.
- Be responsive to reviews over the following weeks/months.
- Follow the packaging guide, the reviewer's guide, and the code of conduct.

## Step 3 — Run pkgcheck and clear it

Every submission is auto-checked by `@ropensci-review-bot` running
[`pkgcheck`](https://docs.ropensci.org/pkgcheck/). Run it yourself first so you
submit something clean:

```r
pkgcheck::pkgcheck()
```

or add the `ropensci-review-tools/pkgcheck-action` GitHub Action. Fix everything it
flags (❌) and address the items that need attention (👀). The full list of
pkgcheck checks is in `references/pkgcheck-and-bot.md`.

## Step 4 — Confirm the submission-readiness essentials

These are the things editors screen for immediately. The README does a lot of work
here — it must let an editor assess scope **without installing the package** and
assume the reader has little domain knowledge.

- README: statement of need, **CI + coverage + repostatus badges**, install
  instructions, usage demo, comparison to similar packages, citation info.
- A CRAN- or OSI-accepted **license**.
- **Code of conduct** and **contribution guidelines** present.
- CI on multiple platforms; test coverage ideally ≥ 75%.
- Full function docs + at least one good vignette.

(All of these are detailed in `package-standards` — this is the
submission-time subset editors check first.)

## Step 5 — Open the submission issue

Submit by opening an issue in **`ropensci/software-review`** using the submission
template. Key points:

- Preserve the HTML variable markers (`<!---variable--->`) and insert your values
  between them.
- Provide the repository URL (full URL to the branch if it isn't the default).
- Include the **statement of need**, the **package category**, and confirmation
  that pre-submission checks pass.
- All discussion happens on that issue — it's the official record. Set your GitHub
  notifications so you don't miss anything.

The template structure and the `@ropensci-review-bot` commands an author uses
(e.g. `@ropensci-review-bot check package`) are in `references/pkgcheck-and-bot.md`.

## What happens next (so you can set expectations)

1. Editor screens for scope and completeness; the bot runs pkgcheck.
2. Two reviewers are assigned (default ~3-week / 21-day review window).
3. Iterative, public, non-adversarial feedback on the issue.
4. Approval via `@ropensci-review-bot approve <pkg>`, then the repo transfers to
   the `ropensci` org, gets a docs site, and is promoted (blog/social), with an
   optional fast-tracked JOSS submission.

## Related skills

- Make the package itself compliant → `package-standards`.
- Statistical package → `stats-standards` (adds `srr` standards the editor
  will check via `@ropensci-review-bot check srr`).
- After acceptance, writing the release/announcement → `package-release`,
  `blog-post`.
