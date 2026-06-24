---
name: package-maintenance
description: >-
  Help maintain an rOpenSci R package over its lifetime per the Developer Guide's
  "Maintaining Packages" chapters. Use this whenever someone is setting up
  collaboration/community files (CONTRIBUTING, code of conduct), grooming a GitHub
  repo (topics, .gitattributes, labels), changing or taking over a package
  maintainer, deprecating or renaming functions/arguments/datasets/packages,
  managing the package lifecycle, or archiving a package. Triggers on phrases like
  "add a contributing guide", "set up code of conduct", "deprecate this function",
  "rename this package", "I'm taking over maintenance", "archive this package", or
  "make my repo more discoverable". For cutting a release use package-release; for
  initial package standards use package-standards.
---

# Maintaining an rOpenSci Package

This skill covers the recurring work after a package exists: making it
collaboration-friendly, keeping the GitHub repo healthy, handing over maintenance,
evolving the API responsibly, and eventually archiving. The detail-heavy topics
(lifecycle/deprecation and archiving) live in reference files.

**Using the references efficiently.** The sections below answer most maintenance
questions directly. Open `references/lifecycle-evolution.md` only when you're
actually deprecating/renaming an exported function, argument, dataset, or package,
and `references/archiving.md` only when you're actually archiving — one topic at a
time, not both by default.

Primary sources: <https://devguide.ropensci.org/maintenance_collaboration.html>,
<https://devguide.ropensci.org/maintenance_github_grooming.html>,
<https://devguide.ropensci.org/maintenance_changing_maintainers.html>,
<https://devguide.ropensci.org/maintenance_evolution.html>,
<https://devguide.ropensci.org/maintenance_curation.html>.

## Collaboration & community files

- **CONTRIBUTING is compulsory.** Have a contributing file at
  `.github/CONTRIBUTING.md` or `docs/CONTRIBUTING.md`. Scaffold with
  `usethis::use_tidy_contributing()`, then link the rOpenSci code of conduct.
- **Code of conduct.** Put this exact text in the README:

  ```
  Please note that this package is released with a [Contributor
  Code of Conduct](https://ropensci.org/code-of-conduct/). By
  contributing to this project, you agree to abide by its terms.
  ```

  - If the repo is in the `ropensci` org: **delete** any repo-level CoC (the org
    default applies).
  - If it's not (yet) transferred: replace the repo CoC content with the rOpenSci
    org default CoC.

- **Lifecycle statement** in CONTRIBUTING.md is encouraged — and **required for
  statistical packages** (General Standard G1.2).
- **Issue hygiene**: issue templates; labels like `help wanted`, `good first
issue`, `Beginner`; pinned issues (up to 3); milestones.
- **Code style**: enforce with Air, styler, or lintr; style PRs before merging.

### Attribution rules

- Add contributors to `DESCRIPTION`: `ctb` for small contributions, `aut` for
  large ones; also credit them in `NEWS.md`.
- Reviewers may be added with role `"rev"` — **only with their consent**. Note that
  `rev` raises a CRAN NOTE unless the package is built on R ≥ 3.5.
- **Do not list editors as contributors.**
- Optionally automate with the `allcontributors` package.
- Granting write access? Contact rOpenSci staff to invite the new contributor to
  the `ropensci` GitHub org and Slack.

## GitHub grooming (discoverability)

- Add repo **topics**: at minimum `r`, `r-package`, `rstats`, plus other relevant
  topics. R-universe uses these for package pages and search.
- **GitHub linguist overrides** via `.gitattributes` so the repo is detected as R:
  - HTML stored outside `docs/` (e.g. in `vignettes/`):
    `*.html linguist-documentation=true`
  - Vendored code you didn't author (e.g. JS): `inst/js/* linguist-vendored`
- Promote your account: make `ropensci` org membership public; pin the repo on your
  profile; add an avatar and name to your GitHub profile.

## Changing / taking over a maintainer

- In `DESCRIPTION`, set the new maintainer to `role = c("aut", "cre")` and make the
  former maintainer `aut` only.
- Update the maintainer name **everywhere else** too: package-level man page,
  `CONTRIBUTING.md`, `CITATION`, etc.
- **CRAN handling**: if the package is archived/orphaned, no permission is needed.
  If it's active, the **old maintainer must email CRAN** confirming the change in
  writing; mention that email when submitting the first new version.
- rOpenSci's biweekly newsletter has a "Call For Contributors" section to match
  packages with new maintainers.

## Package evolution & lifecycle

Mature, widely-depended-on packages should change their user-facing API rarely and
carefully. The full protocols — the **two-stage deprecate → defunct** process,
renaming functions/arguments/datasets, and renaming packages — are in
`references/lifecycle-evolution.md`. Read it before changing or removing any
exported function, argument, or dataset.

## Archiving a package

When a package reaches end of life, follow the archiving procedure (README
rewrite with the right repostatus badge, close issues, archive and transfer to
`ropensci-archive`). The full steps and the minimal README template are in
`references/archiving.md`.

## Curation context

rOpenSci tags packages (`peer-reviewed`, `staff_maintained`, `incubator`,
`archived`, `legacy`) and reviews long-failing packages biannually/annually,
seeking new maintainers or archiving after ~1 month of unresponsiveness. Keep admin
access to your repo (email `[email protected]` if lost) and join the
`#package-maintenance` channel on rOpenSci Slack.

## Related skills

- Cutting a version → `package-release`.
- Initial standards/setup → `package-standards`.
- Announcing changes on the blog → `blog-post`.
