# Writing and Submitting a Blog Post to the rOpenSci Blog

Congratulations on passing peer review! rOpenSci welcomes blog posts from authors whose packages have passed peer review. The full process is documented in the [rOpenSci Blog Guide for Authors and Editors](https://blogguide.ropensci.org/).

---

## Step 1: Contact the Community Manager First

Before writing anything, propose your post idea to the rOpenSci Community Manager via the [contact form on the rOpenSci website](https://ropensci.org/contact/). This aligns expectations and ensures a publication slot.

---

## Step 2: Choose a Post Format

rOpenSci publishes two types of content:

- **Blog post** — Long-form, broad readership. Published on Tuesdays.
- **Tech note** — Shorter, more technical. Published on any weekday.

For a package announcement after peer review, a blog post is the natural fit, but a tech note is also acceptable if the content is narrow and technical.

---

## Step 3: Write the Post

### Content to cover

Your post should offer insight that goes beyond the package documentation. Typical elements for a peer-reviewed package announcement:

- Why you created the package (the problem it solves)
- How it works technically, with real examples
- Code snippets paired with plain-language explanation and illustrative visuals
- Lessons learned or challenges overcome during development
- Acknowledgement of your reviewers with links to their GitHub profiles
- A link to the peer review thread on GitHub
- A call to action (e.g., issues tagged `help wanted` or `good first issue`, a forum thread for feedback)

### Tone

Professional but approachable — less formal than an academic paper, not casual. Use your own voice.

### Structure

- Open with a concise summary of the package's purpose
- Use short headings to break up longer posts
- Close by reinforcing the core message so readers can easily share it

---

## Step 4: Set Up the Post Files

### Fork and branch

Fork the [rOpenSci website repository](https://github.com/ropensci/roweb3) and create a new branch for your post.

### Create the post folder

Under `/content/blog/`, create a folder named:

```
YYYY-MM-DD-your-package-slug/
```

Place all post files and images inside this folder.

### Choose a template/format

| Format         | Files to commit                                     |
| -------------- | --------------------------------------------------- |
| R Markdown     | `index.Rmd` (source) + `index.md` (knitted output)  |
| Quarto         | `index.qmd` (source) + `index.md` (rendered output) |
| Plain Markdown | `index.md` only                                     |

Templates are available in the blog guide appendix: [Markdown template](https://blogguide.ropensci.org/templatemd.html) and [R Markdown template](https://blogguide.ropensci.org/templatermd.html).

### Required YAML front matter

```yaml
slug: your-package-name
title: "Title in Title Case"
author: Your Name
date: YYYY-MM-DD
tags:
  - Software Peer Review
  - your-package-name
  - community
description: "~100 character summary of the post"
package_version: 1.0.0
```

The `Software Peer Review` tag and your package name tag are mandatory for peer-review posts. Add the `tech notes` tag if writing a tech note instead of a blog post.

### Author metadata

Create or update your author file at:

```
content/author/firstname-lastname/_index.md
```

Use the [author file template](https://blogguide.ropensci.org/authortemplate.html) for the required fields (name, links, social handles).

### Images

- Store images in the post folder
- Reference them with relative paths using Hugo shortcodes, not raw HTML
- Keep each image under 1 MB
- Add alt text to every image

### Optional quality checks

```r
roblog::ro_lint_md("index.md")   # style/lint check
roblog::ro_check_urls("index.md") # broken URL check
```

Run a spell-check on `index.md` before submitting.

---

## Step 5: Submit a Pull Request

1. Open a **draft pull request** from your fork to the main `roweb3` repository.
2. In the PR's first comment, paste the [Author Checklist for peer-reviewed packages](https://blogguide.ropensci.org/authorchecklistpeer.html). The required items include:
   - Confirming you read the Content and Technical Guidelines
   - Used the correct template
   - Created/updated your author metadata
   - Added the `Software Peer Review` and package name tags
   - Added the `package_version` YAML field
   - Acknowledged reviewers with links
   - Linked to the peer review thread
   - Ran spell-check (and optionally the `roblog` linting tools)
3. Netlify will automatically build a preview — check it for rendering issues.
4. Mark the PR ready for review **at least one week before** your desired publication date.

---

## Step 6: Respond to Editorial Feedback

An rOpenSci editor will review the PR and leave inline comments and suggestions via GitHub's review interface.

- Acknowledge every comment with a thumbs-up or thumbs-down emoji so the editor knows you saw it.
- Address all requested changes and resolve conversations as you go.
- If you disagree with a suggestion, explain why — constructive discussion is welcome.
- Tag the editor once all feedback has been addressed.

The editor confirms publication readiness when the review loop is complete.

---

## Step 7: Publication and Promotion

Once published, rOpenSci will:

- Post to its Mastodon and LinkedIn accounts, tagging you
- Feature the post in its monthly newsletter (1,000+ subscribers)
- Syndicate to R-bloggers and R Weekly for broader reach
- Archive the post on Rogue Scholar, giving it a permanent DOI (linkable from your ORCID)

You may cross-post the content to your own website as long as you link back to the rOpenSci version.

---

## Key Links

- [rOpenSci Blog Guide](https://blogguide.ropensci.org/) — complete author and editor documentation
- [roweb3 repository](https://github.com/ropensci/roweb3) — fork this to submit your post
- [Author Checklist for peer-reviewed packages](https://blogguide.ropensci.org/authorchecklistpeer.html)
- [Markdown post template](https://blogguide.ropensci.org/templatemd.html)
- [R Markdown post template](https://blogguide.ropensci.org/templatermd.html)
- [Author file template](https://blogguide.ropensci.org/authortemplate.html)
- [rOpenSci contact form](https://ropensci.org/contact/)

---

Sources:

- [rOpenSci Blog Guide for Authors and Editors](https://blogguide.ropensci.org/)
- [Content Guidelines](https://blogguide.ropensci.org/authorcontent.html)
- [Technical Guidelines](https://blogguide.ropensci.org/authortechnical.html)
- [Author Checklist – Peer-reviewed packages](https://blogguide.ropensci.org/authorchecklistpeer.html)
- [Respond to Feedback](https://blogguide.ropensci.org/authorreview.html)
- [Publication and Promotion](https://blogguide.ropensci.org/authorpromote.html)
- [rOpenSci Community Contributing Guide](https://contributing.ropensci.org/)
