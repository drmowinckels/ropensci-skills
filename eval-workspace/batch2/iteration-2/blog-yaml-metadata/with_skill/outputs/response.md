# rOpenSci Blog Post: YAML Frontmatter and Author Metadata

## Post YAML frontmatter

Every post (`index.Rmd`, `index.qmd`, or `index.md`) needs a YAML block at the top. Here is the full schema:

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

- **`slug`** — the URL slug; matches the post folder name (without the date prefix).
- **`title`** — title case; no Markdown formatting inside the title.
- **`package_version`** — required only for posts about a peer-reviewed package; omit otherwise.
- **`author`** — a list of names that must match the `name` field in each author's `_index.md` exactly.
- **`date`** — publication date as `"YYYY-MM-DD"`.
- **`tags`** — reuse existing tags from the rOpenSci tags page rather than inventing new ones (use `packages`, not `package`). Posts about peer-reviewed packages must include `Software Peer Review`, `community`, `packages`, and the package name. Tech notes must include the `tech notes` tag.
- **`description`**, **`socialImg`**, **`socialAlt`**, **`social`** — social-preview fields; delete any you are not using.
- **`editor`** — leave as `~` (null) when submitting.
- **`preface`** — optional; if present, its value appears as an alert box at the top of the post.
- **Remove `categories`** — the blogdown "New Post" addin inserts this field, but rOpenSci does not use it. Delete it entirely.

---

## Author metadata file

Each author needs a file at:

```
content/author/firstname-lastname/_index.md
```

The folder name must be lowercase and hyphen-separated. The frontmatter inside it:

```yaml
name: Author Name
link: https://yourwebsite.example.com
mastodon: https://mastodon.social/@yourhandle
twitter: yourhandle
github: yourgithubusername
gitlab: yourgitlabusername
keybase: yourkeybaseid
orcid: 0000-0000-0000-0000
img: link to picture saved in themes/ropensci/static/img/community
```

### Minimum required

At minimum you need:

- `name` — this must match the post's `author:` list exactly.
- At least one of: `link`, `github`, `gitlab`, or another social handle.

For usernames (`twitter`, `github`, `gitlab`, `keybase`): no `@` prefix, no `https://`. For `mastodon`: provide the full profile URL.

---

## Quick checklist before opening your PR

- [ ] `categories` field removed from post YAML.
- [ ] Tags reuse existing tags from the tags page.
- [ ] `Software Peer Review` tag and `package_version` field present (peer-review posts only).
- [ ] `tech notes` tag present (tech notes only).
- [ ] Author folder name is lowercase-hyphenated and matches `name` in `_index.md`.
- [ ] `name` in `_index.md` matches the post's `author:` field exactly.
- [ ] Every image has alternative text.
