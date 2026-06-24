# Submitting to rOpenSci Software Peer Review

Here is what the submission involves and what happens afterward.

---

## Before you submit: confirm scope and overlap

The first thing to check — before investing time in polishing anything — is whether your package is actually in scope.

**In-scope categories include:** data retrieval, data extraction, data munging, data deposition, data validation and testing, workflow automation, version control, citation management and bibliometrics, scientific software wrappers, field and laboratory reproducibility tools, database software bindings, geospatial data, and translation of scientific resources.

**Out of scope:** data visualization packages, broad data-manipulation utilities (think reshape2/tidyr-style tools), generic computing tools, generic cloud clients without a focused data source, and code parsers.

If a similar package already exists (on CRAN, rOpenSci, or elsewhere), you need a **significant difference** in at least one of: license openness, breadth of functionality, usability, performance, or maintenance status. "My package follows rOpenSci guidelines" is not a sufficient difference.

If you are unsure about either scope or overlap, open a **pre-submission enquiry** issue in `ropensci/software-review` rather than a full submission. Editors will advise you before you invest further.

---

## Author commitments

By submitting, you are agreeing to:

- Maintain the package for **at least two years** (or arrange a hand-off to a new maintainer).
- Submit **before** publishing on CRAN and before submitting any software paper (e.g. JOSS). This avoids conflicting reviewer feedback.
- **Not** submit multiple packages simultaneously — wait for a decision on one before submitting another.
- Respond to review feedback over the following weeks or months.
- Follow the packaging guide, the reviewer guide, and the code of conduct.

---

## Run pkgcheck before submitting

Every submission is automatically checked by `@ropensci-review-bot` running `pkgcheck`. Run it yourself first so you are not surprised:

```r
pkgcheck::pkgcheck()
```

Or add the `ropensci-review-tools/pkgcheck-action` GitHub Action to your repo so it runs on every push.

`pkgcheck` bundles `R CMD check`, `goodpractice`, `pkgstats`, and around 25 rOpenSci-specific structural checks. Among the things it checks:

- All functions have examples and document their return values.
- No `\dontrun{}` in examples.
- Has a `CONTRIBUTING` file and `inst/CITATION`.
- License is CRAN- or OSI-accepted.
- No failed lintr checks.
- `R/` directory is flat (no subdirectories).
- `DESCRIPTION` has valid `URL` and `BugReports` fields.
- At least one vignette.
- CI badges are present and currently passing.
- No junk files (e.g. `.DS_Store`).

Fix everything flagged with ❌ (failures) before submitting. Items marked 👀 need either a fix or a written explanation before the editor will proceed.

---

## What goes into the submission

Open an issue in **`ropensci/software-review`** using the submission issue template. The template contains HTML variable markers in this form: `<!---variable--->`. Preserve those markers exactly and insert your content between them.

The submission template asks for:

- **Repository URL** — full URL; include the branch URL if you are submitting from a non-default branch.
- **Statement of need** — what problem the package solves and who the users are. Write this so an editor can assess scope without installing or running the package, and assume the reader has limited domain knowledge.
- **Package category** — which of the in-scope categories it fits.
- **Scope confirmation** — that you have checked the overlap policy.
- **Pre-submission checklist** — confirming README, license, CoC, CI, coverage, docs, and vignette are all in place.

Concretely, the README must contain: a statement of need, CI/coverage/repostatus badges, install instructions, a usage demonstration, a comparison to similar packages, and citation information.

All discussion happens on that GitHub issue — it is the official record. Set your GitHub notifications so you do not miss comments from the editor or reviewers.

---

## What happens after you submit

1. **Editor screening** — an editor checks scope and completeness. The bot automatically runs pkgcheck and posts the results on the issue. If something is missing or needs fixing, the editor will note it and may ask you to address issues before assigning reviewers.

2. **Reviewer assignment** — two reviewers are assigned. The default review window is three weeks (21 days) per reviewer.

3. **Review** — reviewers post their feedback as comments on the issue. The process is iterative and public but non-adversarial. You respond to each point, push changes, and use `@ropensci-review-bot check package` to re-run pkgcheck after updates.

4. **Approval and transfer** — when the editor is satisfied, they (or the bot) run `@ropensci-review-bot approve <pkg>`. Your repository then transfers to the `ropensci` GitHub organization, gets a pkgdown documentation site deployed automatically, and is promoted via the rOpenSci blog and social channels. There is also an option for a fast-tracked JOSS submission at this point.

---

## The one author bot command you need

During review, the main command you will use is:

```
@ropensci-review-bot check package
```

Post this as a comment on your submission issue after pushing changes to trigger a fresh pkgcheck run. The full bot command reference is at <https://devguide.ropensci.org/bot_cheatsheet.html>.
