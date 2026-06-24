# Editor Checks Template (verbatim)

Source: <https://devguide.ropensci.org/editortemplate.html>
(canonical: `ropensci/dev_guide/templates/editor.md`)

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

## Editorial workflow (high level)

Source: <https://devguide.ropensci.org/softwarereview_editor.html>

- On submission the bot runs pkgcheck: ❌ failures must be fixed; 👀 items need
  attention/info before proceeding. For statistical submissions also run
  `@ropensci-review-bot check srr`.
- Assign **exactly two** reviewers:
  `@ropensci-review-bot assign @username as reviewer`. Avoid reviewers who reviewed
  in the past 6 months; consider mentorship for first-time reviewers; default due
  date 21 days.
- Record reviews: `@ropensci-review-bot submit review <url> time <hours>`; manage
  status labels (e.g. `5/awaiting-reviewer-response`).
- Approve: `@ropensci-review-bot approve <package-name>`, then coordinate repo
  transfer to the `ropensci` org and promotion.

Full bot command set: <https://devguide.ropensci.org/bot_cheatsheet.html>
