---
name: package-release
description: >-
  Guide an R package maintainer through releasing a new version the rOpenSci way —
  updating NEWS.md, choosing a semantic version, running the CRAN release checks,
  tagging the release, writing GitHub release notes, and announcing it. Use this
  whenever someone is about to release/ship a package version, asks "how do I
  release this to CRAN", "bump the version", "write the NEWS file", "do a GitHub
  release", "what's the release checklist", or wants to announce/market a release.
  Built on the rOpenSci Developer Guide "Releasing" and "Marketing" chapters. For
  ongoing maintenance, lifecycle/deprecation, and archiving use
  package-maintenance; for a release blog post use blog-post.
---

# Releasing an rOpenSci Package

rOpenSci's release guidance is deliberately thin because it leans on the standard
**`usethis` + `devtools` release machinery** for the CRAN checklist, then layers on
a few rOpenSci-specific conventions (NEWS format, git tags, GitHub releases,
announcements). Drive the release with the tools; use this skill for the
rOpenSci-specific pieces and to make sure nothing is skipped.

Primary sources: <https://devguide.ropensci.org/maintenance_releases.html>,
<https://devguide.ropensci.org/maintenance_marketing.html>.

## Use the tooling for the heavy lifting

```r
usethis::use_release_issue()   # creates a GitHub issue with the full release checklist
devtools::release()            # runs the CRAN submission checklist interactively
```

`use_release_issue()` + `devtools::release()` generate and run the canonical CRAN
checklist (version bump, `R CMD check`, spell check, URL check, reverse-dependency
checks, win-builder, `cran-comments.md`, etc.). rOpenSci doesn't re-list those —
**don't hand-roll them; let the tools remind you.** The optional **`fledge`**
package can streamline NEWS updates and versioning.

## Versioning

- **Strongly recommended: semantic versioning** (`MAJOR.MINOR.PATCH`).
- Use a `.9000` development suffix between releases (e.g. `0.3.0.9000`).
- See the R Packages lifecycle chapter: <https://r-pkgs.org/lifecycle.html>.

## NEWS file (mandatory)

- A **`NEWS` or `NEWS.md` file in the package root is mandatory.** Prefer
  **`NEWS.md`** (more browsable). If you use plain `NEWS`, add it to
  `.Rbuildignore`; if `NEWS.md`, do **not**.
- **Update NEWS before every CRAN release**, with one header per version:

  ```
  foobar 0.2.0 (2016-04-01)
  =========================
  ```

- Group items under headings as needed: **NEW FEATURES**, **MINOR IMPROVEMENTS**,
  **BUG FIXES**, **DEPRECATED AND DEFUNCT**, **DOCUMENTATION FIXES** (add custom
  headings for large change groups).
- Each item describes the change and **links the related GitHub issue** like
  `(#12)` — these resolve to links in the GitHub release notes.
- Follow the tidyverse NEWS style guide: <https://style.tidyverse.org/news.html>.

## Release operations

1. **Git tag each release** after every CRAN submission.
2. Push the tag to GitHub.
3. Create a **GitHub Release** for the tag, titled like `pkgname v0.1.0`, and paste
   that version's NEWS items into the release notes.
4. CRAN dislikes too-frequent updates — but if a major problem appears soon after a
   release, explain it in `cran-comments.md` and submit a fix.

## Announce and market the release

From the Marketing chapter, on each release (and especially the first CRAN release):

- Open a PR to **R Weekly** with a line under "New Releases" (or "New Packages" for
  a first GitHub/CRAN release).
- Consider a short **tech note** about the release on the rOpenSci blog
  (→ `blog-post`).
- Submit the package to relevant **CRAN Task Views** and package lists.
- New CRAN releases are also written up in the rOpenSci newsletter.

## Release checklist (rOpenSci-specific layer)

- [ ] Version bumped following semver; `.9000` removed for the release.
- [ ] `NEWS.md` updated with a dated version header and grouped, issue-linked items.
- [ ] `usethis::use_release_issue()` checklist worked through.
- [ ] `devtools::release()` (CRAN checks) clean.
- [ ] Git tag created and pushed.
- [ ] GitHub Release created, titled `pkgname vX.Y.Z`, notes from NEWS.
- [ ] Announcement: R Weekly PR; optional tech note; CRAN Task View where relevant.

## Related skills

- Package must be compliant first → `package-standards`.
- Deprecation, lifecycle, maintainer changes, archiving → `package-maintenance`.
- Writing the release blog post / tech note → `blog-post`.
