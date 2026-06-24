# How to Write and Submit a Blog Post to the rOpenSci Blog

Congratulations on passing peer review! Here is a complete walkthrough of the process.

## Step 1: Contact the Community Manager first

Before writing anything, reach out to the rOpenSci Community Manager to get a go-ahead and a tentative publication date.
Do not open a PR cold — the editor needs to schedule your post.

## Step 2: Choose your post type

For a package that just passed peer review, you have two options:

- **Blog post** — long-form, broad readership, publishes on Tuesdays.
  Good for a narrative about why you built the package, what problem it solves, and what you learned from review.
- **Tech note** — shorter, technical audience, can publish any weekday.
  Use this if the focus is on a major new feature or significant new documentation.
  Tag it with the **"tech notes"** tag.

Both get the same promotion.
For a peer-review announcement, a full blog post is most common.

## Step 3: Fork roweb3 and set up your branch

The rOpenSci blog lives in the [roweb3](https://github.com/ropensci/roweb3) repository.

```r
# Fork and create a branch
usethis::pr_push()  # after forking on GitHub
```

Install the Hugo version pinned in `netlify.toml`:

```r
blogdown::install_hugo("0.133.0")  # use the version in netlify.toml
```

Optionally install the `roblog` linting package:

```r
install.packages("roblog", repos = "https://dev.ropensci.org")
```

## Step 4: Create the post file

Posts live at `content/blog/YYYY-MM-DD-slug/`.
Use the blogdown "New Post" RStudio addin to scaffold the folder, or create it manually.

Your source file must be one of:

- `index.Rmd` (R Markdown)
- `index.qmd` (Quarto)
- `index.md` (plain Markdown)

Never use `.RMarkdown`.

If you write in `.Rmd` or `.qmd`, you must **knit/render it and commit both the source file and the generated `index.md`**.

## Step 5: Set up your author metadata

If this is your first rOpenSci post, you need to create an author metadata file.
The exact schema is documented in the roweb3 contributing guide.
Your author file goes in `content/author/your-name/`.

## Step 6: Write the post

### What to include (for a peer-review post)

- A short summary at the top — what the package does and who it is for.
- A compelling example early on — show the code, explain it before and interpret results after.
- Something the reader could not glean from the documentation alone (your motivation, design decisions, what changed during review).
- A thank-you to your reviewers by full name, linked to their rOpenSci author page, with a link to the software-review thread.

### Style rules

- Write **'rOpenSci'** (never 'ROpenSci').
- **Title in title case; headings in sentence case.**
- No markdown formatting in the title.
- Use `##` / `###` / `####` for headings.
- **Put each sentence on its own line** — this makes review diffs and inline suggestions much cleaner.
- Use relative URLs for rOpenSci links (for example, `/blog/2024/01/my-post/`).
- Link your package via its `docs.ropensci.org` URL.
- Avoid Latin abbreviations — write "for example" instead of "e.g.", "that is" instead of "i.e.".
- **Every image must have alternative text.**
- Use your own voice — professional but not academic.

## Step 7: Preview locally

```r
blogdown::serve_site()
# or
# hugo serve
```

The Netlify PR preview will also render once you open the PR.

## Step 8: Run pre-submission checks

```r
roblog::ro_lint_md()    # checks alt text, relative links, Hugo shortcodes
roblog::ro_check_urls() # checks for broken URLs
```

Also run a spell-check on `index.md`.

## Step 9: Open a draft PR

Open a **draft** pull request on roweb3.
Paste the rOpenSci author checklist (from the blog guide) into your first PR comment so the editor can track your progress.

## Step 10: Mark ready for review at least one week before your target date

Switch the PR from draft to ready for review no later than one week before the scheduled publication date.
The editor will review and leave inline comments.

## Step 11: Respond to review

- React to **every inline comment** with a 👍 or 👎 so the editor knows you saw it.
  If you disagree, explain why — do not just ignore it.
- **Resolve conversations** once you have addressed them.
- **Tag the editor** when you have finished your revisions.
  They will confirm when the post is ready to publish.

## Summary timeline

| Step                 | Action                                                                             |
| -------------------- | ---------------------------------------------------------------------------------- |
| Before writing       | Contact Community Manager, get a date                                              |
| Writing              | Fork roweb3, create post in `content/blog/YYYY-MM-DD-slug/index.Rmd`               |
| Before PR            | Knit/render, run `roblog::ro_lint_md()` and `roblog::ro_check_urls()`, spell-check |
| PR                   | Open as draft, paste author checklist                                              |
| ≥ 1 week before date | Mark ready for review                                                              |
| After review         | Respond to every comment, resolve, tag editor                                      |

## Useful links

- [rOpenSci Blog Guide — content](https://blogguide.ropensci.org/authorcontent.html)
- [rOpenSci Blog Guide — technical setup](https://blogguide.ropensci.org/authortechnical.html)
- [rOpenSci Blog Guide — review process](https://blogguide.ropensci.org/authorreview.html)
- [rOpenSci Blog Guide — promotion](https://blogguide.ropensci.org/authorpromote.html)
- [roweb3 repository](https://github.com/ropensci/roweb3)
