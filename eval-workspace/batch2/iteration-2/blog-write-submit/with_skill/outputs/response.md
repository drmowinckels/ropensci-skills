Congratulations on passing peer review! Here is how to write and submit a blog post to the rOpenSci blog.

## Choose your post type

For a package that just passed peer review you have two options:

- **Blog post** — long-form, broad readership, publishes on Tuesdays.
- **Tech note** — shorter, aimed at a technical audience; appropriate if your package has major new features or breaking changes worth highlighting beyond the docs. Tech notes can publish any weekday and must carry the `tech notes` tag.

Both get the same promotion pipeline (Mastodon/social, community newsletter, R Weekly, R-bloggers, Rogue Scholar DOI) — the editor handles all of that on publication.

## Step 1: Get a go-ahead first

Before writing anything, contact the rOpenSci Community Manager to get a go-ahead and a tentative publication date.
You need that date to work backwards to your review deadline.

## Step 2: Fork roweb3 and set up tooling

Fork the [roweb3 repository](https://github.com/ropensci/roweb3) and create a new branch.
`usethis::pr_push()` is a convenient way to manage this.

Install the Hugo version pinned in `netlify.toml`, for example:

```r
blogdown::install_hugo("0.133.0")
```

Optionally install the `roblog` linting package:

```r
install.packages("roblog", repos = "https://dev.ropensci.org")
```

## Step 3: Create the post file

Your post lives at:

```
content/blog/YYYY-MM-DD-your-slug/index.Rmd   # or .qmd or .md
```

Use the **blogdown "New Post" RStudio addin** to scaffold this correctly.
Never use the `.RMarkdown` format.

If you write in R Markdown or Quarto, you must knit/render the file and commit **both** the source (`index.Rmd`/`index.qmd`) and the generated `index.md`.

## Step 4: Create or update your author metadata

Your author metadata file lives at:

```
content/author/firstname-lastname/_index.md
```

Note: the folder name uses `author` (singular) and lowercase-hyphenated names.
The `name` field there must match exactly what you put in the post's `author:` YAML field.

## Step 5: Write the post

A few style points reviewers always check:

- Write **'rOpenSci'** (never 'ROpenSci').
- **Title in title case; headings in sentence case** (`##` / `###` / `####`).
- No markdown in the title.
- Put **each sentence on its own line** — this makes review comments and diffs much cleaner.
- Open with a short summary and a compelling example; explain code before it appears, interpret figures after.
- Use **relative URLs** for rOpenSci links (for example `/blog/...`); link your package via its `docs.ropensci.org` URL.
- Avoid Latin abbreviations — write "for example" instead of "e.g.", "that is" instead of "i.e.".
- **Every image needs alt text.**
- Thank your reviewers by full name, linked to their rOpenSci author page, and link the software-review thread.

For tags, **reuse existing tags** from the rOpenSci tags page — do not invent new ones.
Use `packages` (not `package`).
Peer-review posts need the `Software Peer Review` tag and a `package_version` field in the YAML frontmatter.
**Remove the `categories` field** that the blogdown addin inserts — rOpenSci uses `tags` instead.

## Step 6: Pre-submission checks

```r
roblog::ro_lint_md()    # checks alt text, relative links, Hugo shortcodes
roblog::ro_check_urls() # checks for broken URLs
```

Also run a spell-check on `index.md` and preview the rendered post locally with `blogdown::serve_site()` or `hugo serve`.
The Netlify PR preview will also show you a rendered version once you open the PR.

## Step 7: Open a draft PR

Open a **draft PR** on roweb3.
Paste the matching author checklist into the first comment of the PR.
A blog editor will be assigned to review your post.

**Mark the PR ready for review at least one week before your target publication date.**

## Step 8: Respond to review

- React to every inline comment with a 👍 or 👎 so the editor knows you saw it (you can explain a disagreement).
- Resolve conversations once you have addressed them.
- Tag the editor when you are done with revisions; they confirm when the post is ready to publish.

## Summary checklist

1. Get a go-ahead and publication date from the Community Manager.
2. Fork roweb3, create a branch, install pinned Hugo.
3. Create `content/blog/YYYY-MM-DD-slug/index.Rmd` (or `.qmd`/`.md`).
4. Create/update your author metadata file.
5. Write in your own voice, follow style rules, add alt text to images.
6. Use correct tags (`Software Peer Review`, `packages`); remove `categories`; add `package_version`.
7. Run `roblog::ro_lint_md()` and `roblog::ro_check_urls()`.
8. Commit source + rendered `index.md`, open a draft PR with the author checklist.
9. Mark ready for review ≥ 1 week before publication; respond to all editor comments.
