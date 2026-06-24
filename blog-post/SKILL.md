---
name: blog-post
description: >-
  Help an author write and submit a post to the rOpenSci blog (a long-form blog
  post or a shorter tech note) following the rOpenSci Blog Guide
  (blogguide.ropensci.org). Use this whenever someone wants to write an rOpenSci
  blog post or tech note, announce a package on the rOpenSci blog, draft the
  index.Rmd/index.qmd for roweb3, set up the YAML frontmatter or author metadata,
  add alt text / images correctly, run the roblog checks, or follow the
  blog-submission PR workflow. Triggers on "write an rOpenSci blog post", "tech
  note", "blog about my package release", "submit a post to roweb3", or "rOpenSci
  blog YAML". For the package release mechanics themselves use package-release.
---

# Writing an rOpenSci Blog Post or Tech Note

This skill walks an author through drafting and submitting a post to the rOpenSci
blog, which lives in the **roweb3** repository. Get the structure, YAML, images,
and review protocol right and the PR will sail through.

Primary sources: <https://blogguide.ropensci.org/authorcontent.html>,
<https://blogguide.ropensci.org/authortechnical.html>,
<https://blogguide.ropensci.org/authorreview.html>,
<https://blogguide.ropensci.org/authorpromote.html>.

## Choose the post type

- **Blog post** — long form, broad readership. Publishes weekly on **Tuesdays**.
- **Tech note** — shorter, for a technical audience; for releases with major new
  features, breaking changes, or significant new docs. Must give something a reader
  **could not glean from the documentation itself**. Can publish any weekday. Tag
  it with the **"tech notes"** tag.

Both get the same promotion. "Post" refers to either.

## Submission process (overview)

1. Get a go-ahead and tentative publication date from the Community Manager.
2. **Fork roweb3** and work on a new branch (`usethis::pr_push()` helps).
3. Draft in R Markdown / Quarto / Markdown; create/update your author metadata.
4. Preview and refine locally (`blogdown::serve_site()` / `hugo serve`, or the
   Netlify PR preview).
5. Open a **draft PR**; paste the matching author checklist into the first comment.
6. A blog editor reviews; **mark ready for review ≥ 1 week before** the target date.
7. Revise in response to review.

## File structure and technical requirements

- Post lives in `content/blog/YYYY-MM-DD-slug/`.
- Source file: `index.Rmd` (R Markdown), `index.qmd` (Quarto), or `index.md`
  (Markdown). **Never** use the `.RMarkdown` format.
- For `.Rmd`/`.qmd` you must **knit/render and commit BOTH the source and the
  generated `index.md`.**
- Tooling: `blogdown` (≥ 1.6.0) with its "New Post" RStudio addin; install the Hugo
  version pinned in `netlify.toml` (e.g. `blogdown::install_hugo("0.133.0")`);
  optional `roblog` package
  (`install.packages("roblog", repos = "https://dev.ropensci.org")`).

When you're actually drafting the post's files, the exact YAML schema,
author-metadata file, image/alt-text rules, and the verbatim author checklists are
in `references/technical-and-yaml.md` — follow it closely then, as these are the
things reviewers check. For a higher-level "how do I write/submit a post" question,
the body here is enough.

## Style essentials

- Have a clear take-away; share something not already in the docs; use your own
  voice (professional, not academic).
- Define a target audience but stay broadly understandable; open with a short
  summary and a compelling example (explain code before it, interpret figures
  after).
- Write **'rOpenSci'** (never 'ROpenSci').
- **Title in title case; headings in sentence case**; no markdown in the title.
  Headings use `##` / `###` / `####`.
- **Put each sentence on its own line** (cleaner diffs and review suggestions).
- Use **relative URLs** for rOpenSci links (`/blog/...`); link rOpenSci packages via
  their `docs.ropensci.org` URL.
- Avoid Latin abbreviations ("e.g.", "i.e.") — use plain phrases.
- **Every image needs alternative text.**
- Thank reviewers by full name linked to their author page and link the
  software-review thread (for posts about peer-reviewed packages).

## Gotchas reviewers always catch

These are the small, grounded details a generic answer tends to get wrong — worth
getting right even before you open the YAML reference:

- Author metadata lives at `content/author/<firstname-lastname>/_index.md` —
  **`author`, singular**, lowercase-hyphenated folder. The `name` there must match
  the post's `author:` field exactly.
- **Remove the `categories` field** the blogdown "New Post" addin inserts — rOpenSci
  uses `tags`, and you should **reuse existing tags** from the tags page rather than
  invent new ones (`packages`, not `package`).
- Peer-review posts need the `Software Peer Review` tag and a `package_version`
  field; tech notes need the `tech notes` tag.
- Social preview fields are `socialImg` / `socialAlt` / `social`.

## After publishing

rOpenSci promotes every post (Mastodon/social, the community newsletter, R Weekly /
R-bloggers syndication, and a Rogue Scholar DOI). You don't arrange this yourself —
the editor handles it on publication. For your own release-announcement channels
beyond the blog, see `package-release`.

## Pre-submission checks

```r
roblog::ro_lint_md()    # alt text, relative links, Hugo shortcodes
roblog::ro_check_urls() # broken URLs
```

Also run a spell-check on `index.md` and preview the rendered post.

## Responding to review

- React to **every inline comment** with a 👍/👎 emoji so the editor knows you saw
  it (you may explain a disagreement).
- **Resolve conversations** once addressed.
- **Tag the editor** when you're done; they confirm when it's ready to publish.

## Related skills

- The release itself (NEWS, versioning, CRAN, GitHub release) → `package-release`.
- Marketing channels beyond the blog → `package-release` (Marketing section).
