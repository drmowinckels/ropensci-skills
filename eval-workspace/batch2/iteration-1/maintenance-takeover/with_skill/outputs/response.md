# Taking Over Maintenance of an rOpenSci Package

Congratulations on taking over! Here is a complete checklist of what to update and what to be aware of.

## 1. DESCRIPTION

This is the most critical file to update.

- Set yourself as the new maintainer with `role = c("aut", "cre")`.
- Downgrade the previous maintainer to `role = "aut"` only (remove `"cre"`).
- Example:

```r
person("New", "Maintainer", email = "new@example.com", role = c("aut", "cre"),
       comment = c(ORCID = "0000-0000-0000-0000")),
person("Former", "Maintainer", email = "old@example.com", role = "aut")
```

## 2. Update the maintainer name everywhere else

The `DESCRIPTION` change is not enough on its own. Also update:

- **Package-level man page** (`man/<packagename>-package.Rd` or its roxygen source).
- **`CONTRIBUTING.md`** — if it names or links to the maintainer.
- **`CITATION`** / `inst/CITATION` — update contact details if present.
- **`README`** — any maintainer badge, contact section, or "report bugs to" email.

## 3. CRAN handling (if the package is on CRAN)

- If the previous maintainer is still reachable: **they must email CRAN** at `cran@r-project.org` confirming the maintainer change in writing before you submit.
- When you submit your first new version, mention that email in the submission comments.
- If the package was orphaned/archived on CRAN you can submit without prior permission.

## 4. rOpenSci-specific community files

Verify these are in place (add them if missing):

### CONTRIBUTING.md

Must exist at `.github/CONTRIBUTING.md` or `docs/CONTRIBUTING.md`. Scaffold with:

```r
usethis::use_tidy_contributing()
```

Then link to the rOpenSci code of conduct. If you maintain a statistical package, a lifecycle statement here is required (General Standard G1.2). For other packages it is encouraged.

### Code of conduct in README

Add this exact block to your README if it is not there:

```
Please note that this package is released with a [Contributor
Code of Conduct](https://ropensci.org/code-of-conduct/). By
contributing to this project, you agree to abide by its terms.
```

### Repo-level CoC file

- **If the repo is already in the `ropensci` GitHub org**: delete any repo-level `CODE_OF_CONDUCT.md` — the org-level default applies.
- **If it has not been transferred yet**: replace any repo-level CoC content with the rOpenSci org default CoC text.

## 5. GitHub repository grooming

- Add **topics** to the repo: at minimum `r`, `r-package`, `rstats`, plus relevant domain topics. R-universe uses these for search.
- Review `.gitattributes` — add linguist overrides if needed:
  - HTML outside `docs/`: `*.html linguist-documentation=true`
  - Vendored JS/other: `inst/js/* linguist-vendored`

## 6. Your GitHub profile visibility

- Make your `ropensci` org membership **public** on GitHub.
- Pin the package repo on your GitHub profile.
- Ensure your profile has an avatar and display name.

## 7. Access and admin rights

- Confirm you have admin access to the repo. If you do not, email `[email protected]`.
- Join the `#package-maintenance` channel on rOpenSci Slack.
- If you need to invite co-maintainers to the `ropensci` GitHub org, contact rOpenSci staff rather than inviting directly.

## 8. Issue triage and GitHub hygiene

- Review open issues and PRs — close stale ones or add triage labels.
- Set up (or review) issue templates.
- Add useful labels: `help wanted`, `good first issue`, `Beginner`.
- Consider pinning up to 3 key issues.
- Set up milestones for planned releases.

## 9. Credits and attribution

- Add yourself to `DESCRIPTION` (done above) and to `NEWS.md` as the new maintainer.
- Keep the previous maintainer as `aut` — do not remove them.
- If others contributed during the transition, add them as `ctb` (small) or `aut` (large), and credit in `NEWS.md`.
- Reviewers from the rOpenSci review can be listed with role `"rev"` — only with their consent, and only if building on R ≥ 3.5 (otherwise CRAN raises a NOTE).
- Do not list rOpenSci editors as contributors.

## 10. Package lifecycle and curation context

- rOpenSci tags packages (`peer-reviewed`, `staff_maintained`, `incubator`, `archived`, `legacy`) — be aware of your package's current tag.
- Packages with long-failing CI are reviewed biannually; unresponsive maintainers may have the package archived after ~1 month. Staying active avoids this.
- The rOpenSci newsletter has a "Call For Contributors" section if you later need help finding a co-maintainer.

## Quick checklist summary

| Task                         | File / location                                   |
| ---------------------------- | ------------------------------------------------- |
| Update maintainer role       | `DESCRIPTION`                                     |
| Update maintainer references | man page, `CONTRIBUTING.md`, `CITATION`, `README` |
| CRAN change notification     | Old maintainer emails CRAN (if active on CRAN)    |
| Contributing guide           | `.github/CONTRIBUTING.md`                         |
| CoC block in README          | `README.md` / `README.Rmd`                        |
| Repo-level CoC               | Delete if in `ropensci` org                       |
| GitHub topics                | Repo settings                                     |
| `.gitattributes`             | Repo root                                         |
| GitHub org membership public | Your GitHub profile                               |
| Repo admin access            | Email `[email protected]` if missing              |
| Join rOpenSci Slack          | `#package-maintenance`                            |
| Triage issues/PRs            | GitHub issues                                     |
| Credits in NEWS.md           | `NEWS.md`                                         |

Once these changes are in place, cut a new release following the `ropensci-release` workflow to publish the updated maintainer information to CRAN and R-universe.
