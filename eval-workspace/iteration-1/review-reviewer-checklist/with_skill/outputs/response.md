# How to Conduct Your rOpenSci Package Review

Congratulations on agreeing to review! rOpenSci reviews are open, signed, and
non-adversarial — your goal is to help the author improve the package, not to
gatekeep. Here is how to approach it from start to finish.

---

## Before you start

**Check for conflicts of interest.** If you have a close working relationship with
the authors, have been a co-author on related work, or have a financial stake in the
package's subject area, tell the editor before starting. When in doubt, ask.

**Target three weeks.** rOpenSci asks reviewers to complete their review within
21 days of accepting. If you need more time, let the editor know early.

**Read the submission materials first** without installing anything:

- The GitHub issue on `ropensci/software-review` (note the editor's initial
  comments and the scope decision)
- The package README
- The `@ropensci-review-bot` pkgcheck report attached to the issue
- CI badges and Codecov logs

For a climate-data API package, pay attention to: how the package handles API
authentication, rate limits, and error responses; whether it caches or avoids
redundant requests; and how it deals with the inherent messiness of real-world
climate data (missing values, unusual units, non-standard date formats).

**Optionally use pkgreviewr** to scaffold your review project:

```r
# install.packages("pkgreviewr")  # if not installed
pkgreviewr::pkgreview_create(
  pkg_repo = "owner/packagename",
  review_parent = "~/reviews"
)
```

This clones the package repo and creates a review document in RStudio.

---

## Do the hands-on work

Do not review from reading alone — exercise the package:

1. **Install it as documented** and confirm it works (both CRAN/development install).
2. **Run `devtools::check()` locally** — note any warnings or notes.
3. **Run `devtools::test()`** — all tests should pass; verify any skipped tests are
   justified (skipping because an API key is unavailable in CI is fine; skipping
   because a test is broken is not).
4. **Work through every vignette and example.** Confirm they run end-to-end. For an
   API package, check whether examples work without a live API key (mocked/cached
   responses) and whether the vignette explains how to obtain credentials.
5. **Try it on your own data or use case.** This surfaces real UX issues the author
   has not anticipated. For a climate package: can you fetch data for a region and
   time period you care about? Does the output land in a tidy format you can hand
   off to `ggplot2` or `dplyr` without heroics?

---

## What to evaluate (beyond the checkboxes)

The rOpenSci reviewer guide asks you to weigh in on these dimensions:

| Area                      | Things to look for                                                                                                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Packaging standards**   | Follows [rOpenSci packaging guide](https://devguide.ropensci.org/building.html): `DESCRIPTION`, `NEWS.md`, `LICENSE`, function naming conventions, `cli`/`message` over `cat`, no `library()` in package code |
| **Code quality**          | Style consistency, duplication, overly clever constructs                                                                                                                                                      |
| **Dependencies**          | Is each dependency pulling its weight? Could base R replace a helper?                                                                                                                                         |
| **UI/UX**                 | Argument names, function names, error messages, how results print                                                                                                                                             |
| **Performance**           | Any obvious bottlenecks? Does it handle pagination / large responses gracefully?                                                                                                                              |
| **Documentation**         | Multiple entry points (README, vignette, reference index); examples that teach, not just demonstrate; install instructions that cover API key setup                                                           |
| **API design**            | Do function names read naturally? Do arguments autocomplete sensibly? Is there a consistent naming pattern across the package?                                                                                |
| **Real-world robustness** | Does it fail gracefully on bad inputs, network timeouts, or API errors?                                                                                                                                       |

For a climate / public API package specifically, also consider:

- Does it expose the full range of the upstream API, or are important parameters
  missing?
- Is the tidy output actually tidy (one observation per row, one variable per
  column)?
- Does it document the units, coordinate reference systems, and time zone
  conventions of returned data?
- Does it provide a way to work offline / use cached data for reproducibility?

---

## Submit your review

Post your review as a comment on the `ropensci/software-review` GitHub issue.
Use the template below verbatim, check the boxes that apply, and add your comments
in the **Review Comments** section.

If you file issues or PRs directly on the package repository, link them from your
review comment so the editor can see the full picture.

---

## The reviewer checklist (paste this into your review comment)

```markdown
## Package Review

_Please check off boxes as applicable, and elaborate in comments below. Your review is not limited to these topics, as described in the reviewer guide_

- **Briefly describe any working relationship you have (had) with the package authors.**
- [ ] As the reviewer I confirm that there are no conflicts of interest for me to review this work (if you are unsure whether you are in conflict, please speak to your editor before starting your review).

#### Documentation

The package includes all the following forms of documentation:

- [ ] A statement of need: clearly stating problems the software is designed to solve and its target audience in README
- [ ] Installation instructions: for the development version of package and any non-standard dependencies in README
- [ ] Vignette(s): demonstrating major functionality that runs successfully locally
- [ ] Function Documentation: for all exported functions
- [ ] Examples: (that run successfully locally) for all exported functions
- [ ] Community guidelines: including contribution guidelines in the README or CONTRIBUTING, and DESCRIPTION with URL, BugReports and Maintainer (which may be autogenerated via Authors@R).

#### Functionality

- [ ] Installation: Installation succeeds as documented.
- [ ] Functionality: Any functional claims of the software have been confirmed.
- [ ] Performance: Any performance claims of the software have been confirmed.
- [ ] Automated tests: Unit tests cover essential functions of the package and a reasonable range of inputs and conditions. All tests pass on the local machine.
- [ ] Packaging guidelines: The package conforms to the rOpenSci packaging guidelines.

Estimated hours spent reviewing:

- [ ] Should the author(s) deem it appropriate, I agree to be acknowledged as a package reviewer ("rev" role) in the package DESCRIPTION file.

---

### Review Comments
```

---

## A few notes on filling in the template

- **Only check a box if it genuinely holds.** An unchecked box with an explanation
  is far more useful than a silently unchecked box or one checked out of optimism.
- **Record your honest time estimate.** It helps editors calibrate expectations for
  future reviewers.
- **The `"rev"` role is opt-in.** Agreeing means the author can add you to
  `DESCRIPTION` as a reviewer — only check it if you are comfortable with that.
- After you post, the editor (or bot) records your review with
  `@ropensci-review-bot submit review <url> time <hours>`.

---

## Conduct

- Be respectful and constructive. The rOpenSci [Code of Conduct](https://ropensci.org/code-of-conduct/)
  applies.
- If you have an email exchange with the author, summarise it back on the GitHub
  issue so the record stays public.
- After the author responds to your review, you will be asked to do a follow-up
  check. At that point you use the approval template provided by the editor.

---

## Useful references

- [Reviewer guide](https://devguide.ropensci.org/softwarereview_reviewer.html)
- [Review template](https://devguide.ropensci.org/reviewtemplate.html)
- [rOpenSci packaging guide](https://devguide.ropensci.org/building.html)
- [pkgreviewr](https://docs.ropensci.org/pkgreviewr/)
