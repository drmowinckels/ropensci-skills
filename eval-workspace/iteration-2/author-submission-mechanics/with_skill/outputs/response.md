# Submitting to rOpenSci Software Peer Review

Here is a complete walkthrough of what goes into a submission and what happens afterward.

---

## Before you submit: confirm scope and meet author commitments

**Scope check first.** Submission is wasted effort if the package is out of scope. rOpenSci accepts packages tied to the scientific data lifecycle: data retrieval, extraction, munging, deposition, validation, workflow automation, geospatial tools, database bindings, scientific software wrappers, and similar. Out-of-scope categories include data visualization packages, broad data-manipulation utilities, generic computing tools, and code parsers.

If a similar package already exists, you need to be able to articulate a _significant_ difference in functionality, usability, performance, maintenance, or license. "Follows rOpenSci guidelines" is not a sufficient distinction.

If you are not sure whether your package is in scope, open a **pre-submission enquiry** issue in `ropensci/software-review` before doing a full submission. This is the right move for borderline cases.

**Author commitments.** By submitting you agree to:

- Maintain the package for at least 2 years (or find a new maintainer).
- Submit _before_ publishing on CRAN or submitting a related software paper — reviewers and journal editors can give conflicting feedback otherwise.
- Not submit multiple packages simultaneously — wait for approval of the first.
- Be responsive during review over the following weeks or months.
- Follow the rOpenSci packaging guide, reviewer's guide, and code of conduct.

---

## What your package needs to be submission-ready

Editors screen for these things immediately, mostly by reading the README:

- **README** with: a statement of need, CI / coverage / repostatus badges, installation instructions, a usage demo, a comparison to similar packages, and citation information. The README must let an editor assess scope without installing the package and should assume little domain knowledge.
- A **CRAN- or OSI-accepted license**.
- A **code of conduct** and **contribution guidelines**.
- **CI running on multiple platforms**; test coverage ideally at or above 75%.
- Full **function documentation** and at least one **vignette**.

---

## Run pkgcheck before you submit

Every submission is automatically checked by `@ropensci-review-bot` running [`pkgcheck`](https://docs.ropensci.org/pkgcheck/). Run it yourself first so you are not submitting something the bot will immediately flag:

```r
pkgcheck::pkgcheck()
```

Alternatively, add the `ropensci-review-tools/pkgcheck-action` GitHub Action to your repository so it runs on every push.

Fix everything pkgcheck marks with ❌ and address all items flagged with 👀 before opening your submission issue.

---

## Opening the submission issue

Submit by opening an issue in **[ropensci/software-review](https://github.com/ropensci/software-review)** using the submission issue template. A few things to get right:

- **Preserve the HTML variable markers** (`<!---variable--->`) in the template and insert your answers between them. The bot parses these markers.
- Provide the **repository URL** — use the full URL to a specific branch if your submission is not on the default branch.
- Fill in the **statement of need**: what problem does your package solve and why is it useful to the rOpenSci community?
- Specify the **package category** (the template lists the options).
- Confirm that pre-submission checks pass.

All discussion with the editor and reviewers happens on that issue — it is the official record of the review. Make sure your GitHub notification settings ensure you will not miss comments.

You can trigger a manual pkgcheck run at any time by commenting on the issue:

```
@ropensci-review-bot check package
```

---

## How the review process works after submission

**1. Editorial screening (a few days to ~2 weeks)**

An editor checks that the package is in scope, the submission is complete, and pkgcheck passes. If there are issues, the editor will ask you to address them before assigning reviewers.

**2. Two reviewers are assigned**

The default review window is 3 weeks (21 days). Reviews are public, iterative, and non-adversarial — reviewers give structured feedback on the issue thread and you respond and update your package.

**3. Revision cycle**

You address reviewer comments, push updates to your repository, and respond on the issue. Multiple rounds of revision are normal and expected. The goal is a genuinely improved package, not a rubber stamp.

**4. Approval and transfer**

When the editor is satisfied, they (or the bot) run:

```
@ropensci-review-bot approve <pkgname>
```

After approval:

- Your repository **transfers to the `ropensci` GitHub organization**.
- rOpenSci sets up a **pkgdown documentation site** for the package.
- The package is **promoted** via the rOpenSci blog and social channels.
- You get the option of a **fast-tracked JOSS submission** (Journal of Open Source Software) — rOpenSci review counts as the JOSS review.

---

## Summary timeline

| Stage                              | Typical duration                 |
| ---------------------------------- | -------------------------------- |
| Pre-submission enquiry (if needed) | 1–2 weeks                        |
| Editorial screening                | Days to ~2 weeks                 |
| Reviewer assignment                | ~1 week after screening          |
| Review window (per reviewer)       | 3 weeks                          |
| Revision and re-review             | Varies; 1–3 rounds typical       |
| Approval                           | Whenever the editor is satisfied |

Total time from submission to approval is typically 2–4 months, though it varies with package complexity and reviewer availability.

---

## Key links

- Submission repository: <https://github.com/ropensci/software-review>
- Author guide: <https://devguide.ropensci.org/softwarereview_author.html>
- Policies (scope, overlap): <https://devguide.ropensci.org/softwarereview_policies.html>
- pkgcheck documentation: <https://docs.ropensci.org/pkgcheck/>
