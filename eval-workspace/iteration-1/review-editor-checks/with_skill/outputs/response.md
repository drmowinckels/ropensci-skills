# Initial Editor Checks for a New rOpenSci Submission

Before assigning reviewers, work through the editor checks template below on the submission issue. The goal is to confirm the package is ready for review — not to review it yourself.

---

## Editor Checks Template

Post this on the submission issue (filling in the checkboxes as you go):

```markdown
### Editor checks:

- [ ] Documentation: The package has sufficient documentation available online (README, pkgdown docs) to allow for an assessment of functionality and scope without installing the package. In particular,
  - [ ] Is the case for the package well made?
  - [ ] Is the reference index page clear (grouped by topic if necessary)?
  - [ ] Are vignettes readable, sufficiently detailed and not just perfunctory?
- [ ] Fit: The package meets criteria for fit and overlap.
- [ ] Installation instructions: Are installation instructions clear enough for human users?
- [ ] Tests: If the package has some interactivity / HTTP / plot production etc. are the tests using state-of-the-art tooling?
- [ ] Contributing information: Is the documentation for contribution clear enough e.g. tokens for tests, playgrounds?
- [ ] License: The package has a CRAN or OSI accepted license.
- [ ] Project management: Are the issue and PR trackers in a good shape, e.g. are there outstanding bugs, is it clear when feature requests are meant to be tackled?

---

#### Editor comments
```

---

## What Each Check Means in Practice

**Documentation**
You should be able to assess what the package does and whether it is in scope without cloning or installing it. Check the README (is the need clearly stated?), the pkgdown reference index (are functions grouped logically?), and any vignettes (do they demonstrate real use, or are they just thin wrappers around `?help` pages?).

**Fit**
Does the package fall within [rOpenSci's scope](https://devguide.ropensci.org/softwarereview_policies.html#aims-and-scope)? Is there significant overlap with an existing rOpenSci or CRAN package that would make this submission redundant? If fit is borderline, discuss with other editors before proceeding.

**Installation instructions**
Read the README install section as a first-time user would. Are the instructions unambiguous for both CRAN and development versions? Are any system dependencies called out?

**Tests**
You don't run the tests yourself at this stage, but look at what testing infrastructure is present. If the package does HTTP requests, does it use `vcr` or `httptest2`? If it produces plots, does it use `vdiffr`? If it has interactive components, is there appropriate mocking?

**Contributing information**
Is there a `CONTRIBUTING.md` or equivalent? If tests require API tokens or other credentials, is it clear how a contributor would set those up?

**License**
The `DESCRIPTION` `License:` field must name a [CRAN-accepted or OSI-approved license](https://devguide.ropensci.org/softwarereview_policies.html#licenses). A non-standard license is a blocker.

**Project management**
Scan the GitHub issue and PR trackers briefly. A healthy tracker is not a prerequisite, but outstanding bugs or a large backlog of unacknowledged issues is worth noting in editor comments.

---

## Handling the pkgcheck Report

When the submission was opened, `@ropensci-review-bot` ran pkgcheck automatically.

- **❌ failures** must be fixed by the author before you proceed — ask the author to address them and re-run with `@ropensci-review-bot check package`.
- **👀 items** need your attention or a brief explanation from the author before you move on.

For **statistical packages**, also run:

```
@ropensci-review-bot check srr
```

---

## Once the Checks Pass: Assigning Reviewers

After all editor checks are satisfied:

- Assign **exactly two** reviewers:
  ```
  @ropensci-review-bot assign @username as reviewer
  ```
- Avoid people who have reviewed for rOpenSci in the past 6 months.
- Consider pairing a first-time reviewer with an experienced one (mentorship).
- The default due date is **21 days** from assignment.

Full bot command reference: <https://devguide.ropensci.org/bot_cheatsheet.html>
