# rOpenSci Skills

A collection of [Agent Skills](https://www.anthropic.com/news/skills) that help R developers follow [rOpenSci](https://ropensci.org/)'s guides and books — from writing a package that meets the standards, through peer review, release, and long-term maintenance, to blogging about it.

Each skill packages the relevant chapters of the rOpenSci [Developer Guide](https://devguide.ropensci.org/), [Statistical Software Guide](https://stats-devguide.ropensci.org/), and [Blog Guide](https://blogguide.ropensci.org/) into focused, on-demand guidance that an LLM agent (e.g. Claude) can load only when it's actually needed.

## The skills

| Skill                     | What it helps with                                                                                                                                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`package-standards`**   | Build or audit an R package against rOpenSci's package development standards: naming, `DESCRIPTION`/`Authors@R`, dependency choices, roxygen2 docs, README, testing & coverage, code style, CI, and security. The foundation the other skills build on.                  |
| **`peer-review-author`**  | Prepare and submit a package to rOpenSci software peer review: scope/fit and overlap policy, the pre-submission checklist, running `pkgcheck`, the submission template, and what to expect from `@ropensci-review-bot`.                                                  |
| **`package-review`**      | Conduct a review as a reviewer or editor: the official reviewer checklist and template, what to evaluate beyond the checkboxes, reviewer conduct/timing, `pkgreviewr`, and the editor checks.                                                                            |
| **`stats-standards`**     | Apply the Statistical Software peer-review standards to a package implementing a statistical method: standard categories, documenting standards with the `srr` package (`@srrstats` tags), running `srr`/`autotest`, and the graded badges. Extends `package-standards`. |
| **`package-release`**     | Release a new version the rOpenSci way: updating `NEWS.md`, semantic versioning, CRAN release checks, tagging, GitHub release notes, and announcing it.                                                                                                                  |
| **`package-maintenance`** | Maintain a package over its lifetime: community files (`CONTRIBUTING`, code of conduct), repo grooming, maintainer takeover, deprecating/renaming, lifecycle management, and archiving.                                                                                  |
| **`blog-post`**           | Write and submit a post (blog post or tech note) to the rOpenSci blog: drafting `index.Rmd`/`index.qmd` for `roweb3`, YAML frontmatter and author metadata, alt text and images, the `roblog` checks, and the submission PR workflow.                                    |

They're designed to compose. `package-standards` is the base; `stats-standards` layers the statistical standards on top; `peer-review-author` and `package-review` cover the two sides of review; `package-release`, `package-maintenance`, and `blog-post` cover what comes after.

## Layout

Each skill is a directory following the Agent Skills format:

```
package-standards/
├── SKILL.md          # frontmatter (name + when-to-use description) + body
└── references/       # detailed material loaded on demand
    ├── description-naming-deps.md
    ├── documentation.md
    ├── testing-style-ci.md
    └── security.md
```

`SKILL.md` carries the lightweight guidance that's always loaded once the skill triggers; the `references/` files hold the deeper detail the agent reads only when a task calls for it.

## Using the skills

With [Claude Code](https://docs.claude.com/en/docs/claude-code), copy (or symlink) the skill directories into your skills folder:

```bash
# user-level, available in every project
cp -r package-standards peer-review-author package-review \
      stats-standards package-release package-maintenance blog-post \
      ~/.claude/skills/
```

The skills then trigger automatically when your request matches their description — e.g. "is this package ready to submit to rOpenSci?" loads `peer-review-author`, "deprecate this function" loads `package-maintenance`.

## How these were validated

`eval-workspace/` contains the evaluation harness used while developing the skills: for each test prompt, an agent ran the task _with_ the skill and _without_ it, the two outputs were graded against assertions, and the results were aggregated into a benchmark (`grade*.py`, `aggregate.py`, and the `iteration-*` / `batch2` result sets). It documents how each skill earned its place.

## License & source

The guidance distilled here comes from rOpenSci's openly licensed guides and books. See [ropensci.org](https://ropensci.org/) and the [rOpenSci Dev Guide](https://devguide.ropensci.org/) for the authoritative, always-current source.
