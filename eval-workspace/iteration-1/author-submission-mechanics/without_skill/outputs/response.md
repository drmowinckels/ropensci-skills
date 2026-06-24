# Submitting to rOpenSci Software Peer Review

## Before You Submit

rOpenSci only reviews packages that fit their scope. Check the [scope guidelines](https://devguide.ropensci.org/policies.html#aims-and-scope) first — packages should be focused on data lifecycle (acquisition, processing, analysis, publication) and ideally fill a gap not already covered by an existing rOpenSci package.

Run the `pkgcheck` package before submitting:

```r
# install.packages("pkgcheck", repos = "https://ropensci.r-universe.dev")
pkgcheck::pkgcheck()
```

This runs the same automated checks the editors will run. Fix anything that fails before opening the issue.

## Opening the Submission

Submissions happen as GitHub issues in the [`ropensci/software-review`](https://github.com/ropensci/software-review) repository. There is an issue template — use it exactly.

The template asks for:

- **Package name and description** — what it does in plain language
- **Scope** — which category it fits (data retrieval, data munging, etc.)
- **Target audience** — who would use it
- **Dependencies** — list non-standard ones, especially anything heavy
- **Links** — your repository URL and any pkgdown/documentation site
- **Prior art** — what similar packages exist and how yours differs
- **`pkgcheck` output** — paste the summary or link to a CI run
- **Checklist** — confirm you have read the author guide, the package passes `R CMD check` cleanly, has a `DESCRIPTION` with all required fields, has a `NEWS.md`, has a `README`, has tests with reasonable coverage, and has function-level documentation

The checklist in the template is not optional boilerplate — editors look at it.

## What Happens After Submission

### Editorial Triage (days to ~2 weeks)

An editor checks scope and basic quality. They may ask clarifying questions or request you fix pkgcheck failures before proceeding. If the package is out of scope, it will be closed here with an explanation.

### Editor Assignment

Once accepted into review, an editor-in-charge is assigned. They find two reviewers from the rOpenSci reviewer pool (or sometimes suggested by the author). Reviewers are volunteers; finding them can take a few weeks.

### Review Period (~3–6 weeks per reviewer)

Reviewers use the [review template](https://devguide.ropensci.org/reviewtemplate.html) and post their review as a comment on your issue. The template covers:

- Functionality and correctness
- API design and usability
- Documentation completeness (vignettes, README, function docs)
- Test coverage
- Code quality and style
- rOpenSci-specific standards (use of `cli`, lifecycle practices, etc.)

You are expected to respond to each review point. Common workflow:

1. Reviewer posts review as issue comment
2. You reply acknowledging receipt and give a rough timeline
3. You work through the review items, committing fixes
4. You post a comment summarising what you changed and what you disagreed with (with reasoning)
5. Reviewer approves or asks follow-up questions

Both reviewers post their reviews (sometimes staggered). You address each. The editor may also weigh in.

### Approval and Transfer

Once both reviewers and the editor are satisfied, the editor posts an approval comment. You then:

1. Tag a release (e.g., `v1.0.0`) on GitHub
2. Transfer the repository to the `ropensci` GitHub organization (the editor initiates this)
3. Add the rOpenSci review badge to your README

After transfer, you retain full commit access. rOpenSci adds its own CI checks and links the package in their registry.

## Timeline Expectations

- Scope check: 1–2 weeks
- Reviewer assignment: 2–6 weeks (this is the most variable step)
- Each review round: 3–6 weeks
- Total from submission to acceptance: typically 2–5 months

You can check in on the issue if there has been no editor response in 2 weeks, or no reviewer found after 4 weeks.

## Practical Tips

- Keep your repository public from day one — reviewers need access
- Make sure pkgcheck passes before submitting; editors deprioritise issues with failing checks
- Be specific in your scope statement — vague descriptions slow down triage
- Respond to reviews promptly and professionally; this is collaborative, not adversarial
- You can suggest reviewers in your submission if you know someone with relevant expertise
- If your package wraps an API, document authentication clearly — reviewers flag this heavily
