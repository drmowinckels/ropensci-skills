# Releasing an rOpenSci Package to CRAN (v0.3.0)

## Pre-release preparation

### Update version and metadata

1. Bump the version in `DESCRIPTION` from the current development version to `0.3.0` (remove any `.9000` suffix).
2. Update `NEWS.md` — make sure all user-facing changes since `0.2.0` are documented under a `# packagename 0.3.0` heading with the release date.
3. Run `usethis::use_cran_comments()` if you don't already have a `cran-comments.md` file; update it with your submission notes (test environments, downstream dependencies checked, any CRAN NOTE explanations).

### Run checks locally

```r
devtools::check()           # full R CMD check
devtools::check_win_devel() # Windows R-devel via win-builder
devtools::check_rhub()      # or rhub::check_for_cran() for multi-platform checks
```

Address all ERRORs and WARNINGs. Explain any remaining NOTEs in `cran-comments.md`.

### Check reverse dependencies (if applicable)

If this package has CRAN reverse dependencies, run:

```r
revdepcheck::revdep_check()
```

Document results in `cran-comments.md`.

---

## rOpenSci-specific steps

### 1. Notify the rOpenSci Slack before submitting

Post in the `#package-releases` channel (or `#general`) to let the community know a new CRAN release is coming. This is a community norm, not a hard requirement, but it helps.

### 2. Use the rOpenSci review infrastructure

Before submitting to CRAN, run `pkgcheck` (the rOpenSci automated checks):

```r
pkgcheck::pkgcheck()
```

This mirrors what rOpenSci's editor bots run and catches issues specific to rOpenSci standards (e.g. `pkgstats`, `goodpractice`).

### 3. Verify compliance with rOpenSci packaging guide

Double-check your package still conforms to the [rOpenSci Packaging Guide](https://devguide.ropensci.org/):

- README has installation instructions and a usage example with output.
- All exported functions have complete roxygen2 docs (title, description, `@param`, `@return`, `@examples`).
- `@examples` are runnable (not wrapped in `\dontrun{}` unnecessarily).
- `DESCRIPTION` has a `URL` field pointing to the GitHub repo and a `BugReports` field.
- License is CRAN-compatible and correctly listed.

### 4. Tag the release on GitHub

After CRAN accepts the package:

```bash
git tag v0.3.0
git push origin v0.3.0
```

Then create a GitHub Release from that tag. rOpenSci packages conventionally include the `NEWS.md` section for this version in the release notes body.

### 5. Post a release announcement

rOpenSci has a blog and a community forum. Options:

- **rOpenSci blog** — if the release has significant new features, you can pitch a blog post to `info@ropensci.org`. The rOpenSci team actively promotes package release posts.
- **rOpenSci forum / Slack** — post a brief announcement in `#package-releases` after CRAN acceptance.
- **Social media** — tag `@rOpenSci` on Mastodon/Bluesky when announcing.

### 6. Update the rOpenSci registry (if needed)

If your package metadata (e.g. maintainer, URL) changed, the rOpenSci registry at <https://github.com/ropensci/roregistry> may need updating. Usually this is automatic via the `ropensci-review-bot`, but verify the registry entry still reflects current `DESCRIPTION` fields.

---

## Submission to CRAN

```r
devtools::submit_cran()
# or
usethis::use_github_action("check-release") # ensure CI is passing first
```

Alternatively, submit manually via <https://cran.r-project.org/submit.html> and upload the tarball built with `devtools::build()`.

---

## Post-acceptance checklist

- [ ] CRAN page updated and package installable via `install.packages()`
- [ ] GitHub Release created with tag `v0.3.0` and NEWS content
- [ ] Development version bumped to `0.3.9000` in `DESCRIPTION`
- [ ] `NEWS.md` has a new `# packagename 0.3.9000` (or `(development version)`) section header
- [ ] rOpenSci Slack / forum notified
- [ ] Blog post submitted or social media announcement posted (if warranted)

---

## Key references

- [rOpenSci Developer Guide — Releasing](https://devguide.ropensci.org/releasing.html)
- [usethis release checklist](https://usethis.r-lib.org/reference/use_release_issue.html): `usethis::use_release_issue()` creates a GitHub issue with a pre-filled checklist tailored to CRAN releases — highly recommended as a coordination tool.
- [CRAN Policies](https://cran.r-project.org/web/packages/policies.html)
