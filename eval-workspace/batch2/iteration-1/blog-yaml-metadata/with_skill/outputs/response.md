# rOpenSci Blog Post: YAML Frontmatter and Author Metadata

## Post YAML frontmatter

Every post's `index.Rmd`, `index.qmd`, or `index.md` needs a YAML block at the top:

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

### Field notes

- **`slug`** — used in the URL; keep it short and descriptive.
- **`title`** — title case; no Markdown formatting inside the title.
- **`package_version`** — required for posts about a package; omit otherwise.
- **`author`** — one or more full names, each matching the name in that author's metadata file exactly.
- **`date`** — ISO 8601 (`YYYY-MM-DD`), agreed with the Community Manager.
- **`tags`** — reuse existing tags from the tags page rather than inventing new ones. Posts about peer-reviewed packages must include `Software Peer Review`, `community`, `packages`, and the package name. Tech notes must add `tech notes`.
- **`description`**, **`socialImg`**, **`socialAlt`**, **`social`** — optional; delete any you are not using.
- **`editor`** — leave as `~` (null) until assigned.
- **Do not include a `categories` field** — the blogdown addin adds it automatically; remove it.
- An optional `preface: "some alert text"` field renders an alert box at the top of the post.

---

## Author metadata file

Each author needs a file at:

```
content/author/yourfirstname-yourlastname/_index.md
```

The folder name must use lowercase letters and hyphens (no spaces, no underscores).

```yaml
name: Author Name
link: https://yourwebsite.example.com
mastodon: https://mastodon.social/@yourhandle
twitter: yourtwitter
github: yourgithub
gitlab: yourgitlab
keybase: yourkeybase
orcid: 0000-0000-0000-0000
img: link-to-picture-in-themes/ropensci/static/img/community
```

### Minimum required

- **`name`** — required; must match what you put in the post's `author:` field.
- At least one of: `link`, `github`, `gitlab`, or another social/profile field.

### Username format

- GitHub, GitLab, Twitter, Keybase, ORCID: plain username or ID — no `@` prefix, no `https://` URL.
- Mastodon: the full profile URL (for example `https://fosstodon.org/@you`).

---

## Quick checklist before opening the PR

- [ ] Author metadata file exists at the correct path and `name` matches the post's `author:` list.
- [ ] `categories` field removed from YAML.
- [ ] Tags reuse existing tags; peer-review posts include `Software Peer Review`, `community`, `packages`, and the package name.
- [ ] `tech notes` tag added if this is a tech note.
- [ ] `package_version` set if the post is about a package release.
- [ ] Every image has alt text.
- [ ] `roblog::ro_lint_md()` and `roblog::ro_check_urls()` pass on `index.md`.
