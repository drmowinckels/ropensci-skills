# Blog Post Technical Requirements, YAML, and Checklists

Source: <https://blogguide.ropensci.org/authortechnical.html>

## Author metadata file (required)

Create `content/author/yourfirstname-yourlastname/_index.md`. Frontmatter fields:

```yaml
name: Author name
link: website URL or other online presence
mastodon: Mastodon full URL to profile
twitter: Twitter username
github: GitHub username
gitlab: GitLab username
keybase: Keybase ID
orcid: ORCID ID
img: link to picture saved in themes/ropensci/static/img/community
```

Minimum: `name` plus a `link` or one social/GitHub/GitLab username (no `@`, no
`https://` for usernames).

## Post YAML frontmatter

```yaml
slug: post-template
title: Post Title in Title Case
package_version: 0.1.0
author:
  - Author Name1
  - Author Name2
date: "2020-03-10"
tags:
  - Software Peer Review
  - packages
  - R
  - community
description: A very short summary of your post (~ 100 characters)
socialImg: blog/2019/06/04/post-template/name-of-image.png
socialAlt: Alternative description of the image
social: A post about blabla by @[email protected]!
editor: ~
```

- Optional `preface: "some alert"` adds an alert box.
- **Remove the `categories` field** the addin adds — use `tags` instead.
- Delete `description` / `socialImg` / `socialAlt` if unused.
- **Tags**: reuse existing tags (browse the tags page) instead of inventing new
  ones (e.g. `packages`, not `package`). Posts about peer-reviewed packages must
  include `Software Peer Review`, `community`, `packages`, and the package name.

## Images and alt text

- **Every image needs alternative text.**
- All images go in the post folder (`content/blog/YYYY-MM-DD-slug/`) — never link to
  external hosts.
- Keep images < 1 MB; prefer transparent backgrounds; compress with OptiPNG /
  minimage / TinyPNG.
- Markdown/external images use a Hugo shortcode with `alt=`:
  `{{< figure src="image-name.png" alt="informative description" >}}`
  (also `imgtxt` for text beside an image; classes `pull-left` / `center` /
  `pull-right`).
- **In `.Rmd` files, wrap shortcodes** in `<!--html_preserve-->` …
  `<!--/html_preserve-->`.
- For Rmd-generated figures, set alt text via the `hugoopts` chunk option:
  `hugoopts=list(alt="…", caption="…", width=300)`.
- Non-English image variants: name them `image.es.png`, etc.

## Citations, widgets, embeds

- Citations as footnotes (`[^1]`) listed at the bottom. Get them via
  `citation("pkg")`, `rcrossref::cr_cn(doi, format="text", style="apa")`, or Google
  Scholar APA.
- HTML widgets (DT, leaflet): include a screenshot and use the figure shortcode's
  `link` option to the live version.
- Social-media embeds are no longer recommended — use a block quote linking the
  post instead.

## Multilingual posts

- English default is `index.md`; translations are `index.<lang>.md` (e.g.
  `index.es.md`). A single non-English post omits `index.md`. Discuss language with
  the editors first.

## Author Checklist — posts about peer-reviewed packages (verbatim)

```markdown
- [ ] I have read the Content Guidelines.
- [ ] I have read the Technical Guidelines.
- [ ] I used or followed the R Markdown or Markdown template.
- [ ] I have followed the Style Guide.
- [ ] I created or updated my author metadata with correct folder name.
- [ ] I have added relevant tags after browsing existing tags (including "community" tag).
- [ ] I have added the "tech notes" tag if this is a technote.
- [ ] I ran `roblog::ro_lint_md()` on index.md (optional).
- [ ] I ran `roblog::ro_check_urls()` on index.md (optional).
- [ ] I ran a spell-check on index.md.
- [ ] I have added the tags - Software Peer Review, my-packagename.
- [ ] I have added the package-version YAML tag.
- [ ] I have added acknowledgement of the reviewers' work (with links to reviewers).
- [ ] I have added a link to the software peer review thread.
```

## Author Checklist — other posts (verbatim)

Same as above **minus** the last four peer-review-specific items (the
`Software Peer Review` / package tags, the `package-version` YAML tag, reviewer
acknowledgement, and the software-review thread link).

## Promotion (what rOpenSci does after publishing)

Source: <https://blogguide.ropensci.org/authorpromote.html>

rOpenSci posts from Mastodon + LinkedIn (tagging authors/reviewers and the review
thread), lists the post in the monthly newsletter, syndicates to R-bloggers / R
Weekly, and to **Rogue Scholar** (which assigns a **DOI**, archives in the Internet
Archive, and adds it to your ORCID if integrated). You may cross-post to your own
site if you link back to the rOpenSci version.
