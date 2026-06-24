# Releasing an rOpenSci Package to CRAN (v0.3.0)

## Let the tooling do the heavy lifting

Start by creating a GitHub issue that tracks the full release checklist:

```r
usethis::use_release_issue()
```

This creates an issue in your repo with the canonical CRAN checklist — version bump, `R CMD check`, spell check, URL check, reverse-dependency checks, win-builder, `cran-comments.md`, and more. Work through every item on that issue.

When you're ready to submit to CRAN, run the interactive submission workflow:

```r
devtools::release()
```

This runs all pre-submission checks and handles the actual CRAN upload. Do not hand-roll these steps — the tools cover them comprehensively.

## Before submission: version and NEWS

**Version number:** `0.3.0` follows semantic versioning correctly. Make sure your development version (between releases) used a `.9000` suffix (e.g. `0.2.0.9000`), and that suffix is now removed for the release.

**NEWS.md** (mandatory for rOpenSci packages):

- Add a dated header for this version:
  ```
  pkgname 0.3.0 (2026-06-23)
  ==========================
  ```
- Group changes under headings: **NEW FEATURES**, **MINOR IMPROVEMENTS**, **BUG FIXES**, **DEPRECATED AND DEFUNCT**, **DOCUMENTATION FIXES**.
- Link every item to its GitHub issue using `(#123)` — these become clickable links in the GitHub release notes.
- Follow the [tidyverse NEWS style guide](https://style.tidyverse.org/news.html).

Example:

```markdown
# pkgname 0.3.0 (2026-06-23)

### NEW FEATURES

- `new_function()` does X (#42).

### BUG FIXES

- Fixed crash when input is empty (#55).
```

## After CRAN accepts the package

1. **Tag the release** and push it:

   ```bash
   git tag v0.3.0
   git push origin v0.3.0
   ```

2. **Create a GitHub Release** for the tag:
   - Title: `pkgname v0.3.0`
   - Body: paste the `0.3.0` section from `NEWS.md` directly.

3. **Bump to a development version** immediately after:
   ```r
   usethis::use_dev_version()  # sets version to 0.3.0.9000
   ```

## rOpenSci-specific announcements

- **R Weekly:** open a PR to [rweekly.org](https://github.com/rweekly/rweekly.org) adding a line under "New Releases" (or "New Packages" if this is the first CRAN release). This is the highest-impact low-effort announcement.
- **rOpenSci newsletter:** your CRAN release will be picked up automatically by the rOpenSci newsletter — no action needed.
- **Tech note:** consider writing a short blog post / tech note on the rOpenSci blog describing what's new. Use the `ropensci-blog-post` skill for guidance on that.
- **CRAN Task Views:** if your package fits a Task View, submit it.

## Release checklist (rOpenSci layer)

- [ ] Version is `0.3.0` with `.9000` suffix removed
- [ ] `NEWS.md` has a dated `0.3.0` header with grouped, issue-linked items
- [ ] `usethis::use_release_issue()` checklist worked through completely
- [ ] `devtools::release()` clean — no ERRORs or WARNINGs
- [ ] Git tag `v0.3.0` created and pushed to GitHub
- [ ] GitHub Release created, titled `pkgname v0.3.0`, notes copied from NEWS
- [ ] Development version bumped to `0.3.0.9000`
- [ ] R Weekly PR opened
- [ ] CRAN Task View submission (if applicable)

## If a critical bug appears shortly after release

CRAN dislikes too-frequent updates, but if something serious is discovered soon after release, submit a patch explaining the situation in `cran-comments.md`. Be brief and factual about what broke and why the fix couldn't wait.
