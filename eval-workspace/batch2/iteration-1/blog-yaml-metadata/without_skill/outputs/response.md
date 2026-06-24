# rOpenSci Blog Post YAML Frontmatter and Author Metadata

## Post YAML Frontmatter

Every rOpenSci blog post requires a YAML block at the top of the file. Here is the complete template:

```yaml
---
slug: "your-post-slug"
title: Post Title in Title Case
package_version: 0.1.0
author:
  - Author Name1
  - Author Name2
date: 2020-03-10
tags:
  - Software Peer Review
  - packages
  - R
  - community
description: "A very short summary of your post (~ 100 characters)"
socialImg: blog/YYYY/MM/DD/your-post-slug/name-of-image.png
socialAlt: "Alternative description of the image"
social: "A post about blabla by @handle@mastodon.social!"
editor:
---
```

### Field reference

| Field             | Required | Notes                                                                                      |
| ----------------- | -------- | ------------------------------------------------------------------------------------------ |
| `slug`            | Yes      | URL-friendly identifier; must be unique                                                    |
| `title`           | Yes      | Use title case                                                                             |
| `author`          | Yes      | List of author names exactly as they appear in author files                                |
| `date`            | Yes      | ISO format: `'YYYY-MM-DD'`                                                                 |
| `tags`            | Yes      | Subject tags for discoverability; do **not** use `categories`                              |
| `package_version` | Optional | Only include if the post focuses on a specific package version; delete the field otherwise |
| `description`     | Optional | ~100-character summary used in previews and SEO                                            |
| `socialImg`       | Optional | Path to image used in social media preview cards                                           |
| `socialAlt`       | Optional | Alt text for the social image                                                              |
| `social`          | Optional | Default text for social media sharing; falls back to post title if omitted                 |
| `editor`          | Optional | Left blank until the rOpenSci editor is assigned; do not fill in yourself                  |

**Notes:**

- The `categories` field is deprecated — use `tags` instead.
- The file is saved at `/content/blog/YYYY-MM-DD-slug/index.md`.

---

## Author Metadata File

Each author needs a file at `/content/authors/firstname-lastname/_index.md`. If you are a new contributor, you must create this file as part of your submission.

### Complete author file template

```yaml
---
name: Author Name
link: https://your-website.com
mastodon: https://mastodon.social/@yourhandle
twitter: yourtwitter
github: yourgithub
gitlab: yourgitlab
keybase: yourkeybase
orcid: 0000-0000-0000-0000
img: themes/ropensci/static/img/community/firstname-lastname.jpg
bio: "Optional short biography shown on your author page."
---
```

### Field reference

| Field      | Required | Notes                                                                                                 |
| ---------- | -------- | ----------------------------------------------------------------------------------------------------- |
| `name`     | Yes      | Full display name                                                                                     |
| `link`     | Minimum  | Personal website or other online presence; at least `link` or one social/GitHub field must be present |
| `github`   | Minimum  | GitHub username without `@`; used to pull your profile picture if `img` is absent                     |
| `gitlab`   | Optional | GitLab username without `@`                                                                           |
| `twitter`  | Optional | Twitter/X username without `@`                                                                        |
| `mastodon` | Optional | Full profile URL (e.g. `https://fosstodon.org/@handle`)                                               |
| `keybase`  | Optional | Keybase ID without `@`                                                                                |
| `orcid`    | Optional | ORCID identifier                                                                                      |
| `img`      | Optional | Custom profile picture path; if omitted the system uses your GitHub profile picture                   |
| `bio`      | Optional | Short professional description; shown on author pages for staff, editors, and leadership              |

**Minimum requirement:** Provide `name` plus at least one of `link`, `github`, `gitlab`, or a social handle so that an author page can be generated.

---

## Sources

- [rOpenSci Blog Guide — Technical Guidelines](https://blogguide.ropensci.org/authortechnical.html)
- [rOpenSci Blog Guide — Post Template (md)](https://blogguide.ropensci.org/templatemd.html)
- [rOpenSci Blog Guide — Author File Template](https://blogguide.ropensci.org/authortemplate.html)
