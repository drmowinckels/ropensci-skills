Congratulations on passing rOpenSci peer review! Writing a blog post about your package is encouraged — rOpenSci actively supports package authors in publishing an announcement post. Here is how to do it from start to finish.

## The official guide

Everything is documented in the [rOpenSci Blog Guide for Authors and Editors](https://blogguide.ropensci.org/). The two chapters you must read are:

- [Content Guidelines](https://blogguide.ropensci.org/content.html)
- [Technical Guidelines](https://blogguide.ropensci.org/authortechnical.html)

---

## 1. Decide on format: blog post vs. tech note

rOpenSci publishes two formats, both promoted equally:

- **Blog post** — long-form, broad readership, typically published on Tuesdays.
- **Tech note** — shorter, more technical, targeted audience, can be published any weekday. Suitable if you are announcing a major update, breaking changes, or significant documentation rather than a first introduction.

For a package that just passed peer review, a blog post is the natural choice.

---

## 2. Plan your content

The key question to answer: _what can readers get from this post that they cannot get from the package documentation?_

Good angles for a peer-review announcement post:

- Why you created the package and what problem it solves
- What you learned during the peer review process
- How the reviewers improved the package
- A compelling worked example that goes beyond the README
- Your development plans and how people can contribute

Structural tips:

- Open by assuming readers have never heard of your package — give a brief orientation.
- Use short headings so readers can scan and decide whether to continue.
- For each code example: explain the objective in plain language, show the code with context, then interpret the output — do not leave the conclusion implicit.
- **Acknowledge your reviewers by first and last name**, linked to their rOpenSci author page, and link to the software review thread on GitHub.
- Close with a call to action: links to "help wanted" or "good first issue" labels, the rOpenSci forum, or wherever you want feedback.

---

## 3. Set up the repository

Posts are submitted via pull request to the rOpenSci website repository.

```bash
# Fork and clone the website repo
# https://github.com/ropensci/roweb3
git clone https://github.com/YOUR-USERNAME/roweb3
cd roweb3
git checkout -b my-package-post
```

You will also need Hugo 0.133.0 (the version pinned in `netlify.toml`) and blogdown:

```r
install.packages("blogdown")
blogdown::install_hugo(version = "0.133.0")
```

---

## 4. Create your post file

Posts live at `content/blog/YYYY-MM-DD-slug/`. Use a date close to when you expect to publish.

The easiest way is the blogdown RStudio addin: **Addins → New Post**. It creates the folder and populates the YAML front matter automatically.

Alternatively, create the folder and file manually. Choose your format:

| Format     | File name   | What to commit                     |
| ---------- | ----------- | ---------------------------------- |
| R Markdown | `index.Rmd` | both `.Rmd` and the knitted `.md`  |
| Quarto     | `index.qmd` | both `.qmd` and the rendered `.md` |
| Markdown   | `index.md`  | just `index.md`                    |

---

## 5. Fill in the YAML front matter

```yaml
slug: "your-package-name-peer-review"
title: "Your Post Title in Title Case"
author:
  - Your Name
date: 2025-01-15
tags:
  - Software Peer Review
  - your-package-name
  - community
description: "A ~100-character summary of the post shown in previews."
```

Key points:

- Remove the auto-generated `categories` field; use `tags` only.
- Always include the tags `Software Peer Review` and your package name for review announcement posts.
- Browse existing tags at [ropensci.org/tags](https://ropensci.org/tags/) and reuse them rather than inventing new ones.

---

## 6. Create or update your author profile

Add a file at `content/author/firstname-lastname/_index.md` if you do not already have one. Required fields: your name and at least one link (website, GitHub, etc.). You can also add Mastodon, ORCID, and a profile image.

---

## 7. Write and preview locally

Store all images inside your post folder (`content/blog/YYYY-MM-DD-slug/`). Use Hugo shortcodes for images and always include alt text:

```
{{< figure src="my-plot.png" alt="A bar chart showing..." >}}
```

Style conventions to follow:

- Write "rOpenSci" (not "ROpenSci").
- Use relative URLs for links within the rOpenSci site (e.g., `/blog/` not `https://ropensci.org/blog/`).
- Add a new line at the end of each sentence to keep diffs readable.
- Avoid Latin abbreviations — write "for instance" instead of "e.g."

Preview your post:

```r
blogdown::serve_site()
# or from the terminal:
hugo serve
```

Visit `http://localhost:1313` to see it rendered.

---

## 8. Run the automated checks

The `roblog` package provides two helpful checks:

```r
# install if needed: install.packages("roblog")
roblog::ro_lint_md("content/blog/YYYY-MM-DD-slug/index.md")
roblog::ro_check_urls("content/blog/YYYY-MM-DD-slug/index.md")
```

Also run a spell check before submitting.

If you used R Markdown, knit the file to generate the `.md` before opening the PR.

---

## 9. Submit via pull request

1. Push your branch to your fork.
2. Open a **draft** pull request against `ropensci/roweb3`.
3. In the **first comment** of the PR, paste the checklist for peer-reviewed package posts (found in the [Technical Guidelines](https://blogguide.ropensci.org/authortechnical.html)) and check off each item.
4. Netlify will automatically build a preview of your post — use the preview URL to do a final visual check.
5. Push any fixes, then mark the PR as **Ready for Review** at least **one week before** your intended publication date.

An rOpenSci editor will review your draft, leave suggestions in the PR, and work with you on a publication date.

---

## Quick checklist summary

- [ ] Post is in `content/blog/YYYY-MM-DD-slug/index.(R)md`
- [ ] Author profile exists in `content/author/firstname-lastname/_index.md`
- [ ] YAML includes `Software Peer Review` and package name tags
- [ ] Reviewers acknowledged by name with links
- [ ] Link to the software review thread included
- [ ] R Markdown knitted to `.md` (if applicable)
- [ ] `roblog::ro_lint_md()` and `roblog::ro_check_urls()` pass
- [ ] Images have alt text and are under 1 MB
- [ ] Post previews correctly locally
- [ ] Draft PR opened with the peer-review checklist in the first comment

---

## Useful links

- [rOpenSci Blog Guide](https://blogguide.ropensci.org/)
- [roweb3 repository](https://github.com/ropensci/roweb3) (where you submit the PR)
- [Existing blog posts](https://ropensci.org/blog/) for examples
- [rOpenSci tags](https://ropensci.org/tags/)
- [roblog package](https://docs.ropensci.org/roblog/)
