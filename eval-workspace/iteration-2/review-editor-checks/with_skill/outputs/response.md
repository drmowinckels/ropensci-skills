# Initial Editor Checks for rOpenSci Submissions

Before assigning reviewers, you run a set of initial checks to confirm the package is ready for review. These are documented in the [rOpenSci editor guide](https://devguide.ropensci.org/softwarereview_editor.html) and the [editor template](https://devguide.ropensci.org/editortemplate.html).

## 1. Review the pkgcheck bot report

When a package is submitted, `@ropensci-review-bot` automatically runs pkgcheck and posts the results on the issue.

- **Red ❌ failures** must be fixed by the author before you proceed.
- **Eyes 👀 items** need attention or clarification from the author before you move on.
- For **statistical packages**, also trigger: `@ropensci-review-bot check srr`

Do not assign reviewers until pkgcheck is clean or outstanding items are addressed.

## 2. Work through the editor checklist

Post the following checklist as a comment on the submission issue (fill in checkboxes as you go):

```markdown
### Editor checks:

- [ ] Documentation: The package has sufficient documentation available online
      (README, pkgdown docs) to allow for an assessment of functionality and
      scope without installing the package. In particular,
  - [ ] Is the case for the package well made?
  - [ ] Is the reference index page clear (grouped by topic if necessary)?
  - [ ] Are vignettes readable, sufficiently detailed and not just perfunctory?
- [ ] Fit: The package meets criteria for fit and overlap.
- [ ] Installation instructions: Are installation instructions clear enough
      for human users?
- [ ] Tests: If the package has some interactivity / HTTP / plot production
      etc. are the tests using state-of-the-art tooling?
- [ ] Contributing information: Is the documentation for contribution clear
      enough e.g. tokens for tests, playgrounds?
- [ ] License: The package has a CRAN or OSI accepted license.
- [ ] Project management: Are the issue and PR trackers in a good shape,
      e.g. are there outstanding bugs, is it clear when feature requests are
      meant to be tackled?

---

#### Editor comments
```

### What each item means in practice

**Documentation** — you should be able to assess the package's purpose and functionality from the online docs alone, without installing it. Check the README, pkgdown reference index, and any vignettes. Vignettes should give a real walkthrough, not just echo the function docs.

**Fit** — confirm the package is in scope for rOpenSci and does not substantially duplicate an existing rOpenSci package. If scope is uncertain, discuss with the editorial board before proceeding.

**Installation instructions** — a human unfamiliar with the package should be able to install it from the README without guessing.

**Tests** — if the package does HTTP requests, produces plots, or involves interactive sessions, the tests should use modern tooling (e.g. `httptest2`/`vcr` for HTTP, `vdiffr` for plots) rather than ad-hoc approaches.

**Contributing information** — contributors should know how to get set up, including any API tokens or test fixtures needed to run the full test suite locally.

**License** — must be CRAN-accepted or OSI-approved (e.g. MIT, Apache 2.0, GPL). Non-standard licenses are a blocker.

**Project management** — look at the issue and PR trackers. Accumulated stale bugs or unexplained open PRs are a signal about maintainability. You don't need to resolve them, but flag anything concerning in your editor comments.

## 3. Assign reviewers

Once the checklist passes:

- Assign **exactly two** reviewers with:
  `@ropensci-review-bot assign @username as reviewer`
- Avoid reviewers who have reviewed for rOpenSci in the **last 6 months**.
- Consider pairing a first-time reviewer with a more experienced one (the bot supports a mentorship flag).
- The default due date is **21 days** from assignment.

Full bot command reference: <https://devguide.ropensci.org/bot_cheatsheet.html>
