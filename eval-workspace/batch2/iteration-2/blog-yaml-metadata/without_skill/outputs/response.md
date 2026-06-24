For an rOpenSci blog post you need to set up two separate pieces of metadata: the post's own YAML frontmatter, and a per-author profile file.

## Post frontmatter

Save your post at `content/blog/YYYY-MM-DD-your-slug/index.md`. The YAML at the top of that file should look like this:

```yaml
---
slug: "your-post-slug"
title: Post Title in Title Case
package_version: 0.1.0 # delete this line if the post is not about a package
author:
  - Author Name One
  - Author Name Two
date: 2024-06-01
tags:
  - Software Peer Review
  - packages
  - community
description: "A short summary of your post (~100 characters)"
socialImg: blog/2024/06/01/your-post-slug/name-of-image.png
socialAlt: "Alt text describing the social sharing image"
social: "A post about X by @handle@mastodon.social!"
editor:
---
```

Field notes:

| Field             | Required    | Notes                                                                        |
| ----------------- | ----------- | ---------------------------------------------------------------------------- |
| `slug`            | Yes         | Becomes the URL path segment                                                 |
| `title`           | Yes         | Title case                                                                   |
| `author`          | Yes         | List of full names matching author profile files                             |
| `date`            | Yes         | `YYYY-MM-DD`                                                                 |
| `tags`            | Recommended | Browse existing tags first to avoid near-duplicates; do not use `categories` |
| `description`     | Recommended | ~100 characters; used in listings and social previews                        |
| `package_version` | Conditional | Only for posts about a specific package release; delete otherwise            |
| `socialImg`       | Optional    | Path relative to `static/`; enables a rich social card                       |
| `socialAlt`       | Optional    | Required if `socialImg` is set                                               |
| `social`          | Optional    | Default tweet/toot text; defaults to post title if omitted                   |
| `editor`          | Leave blank | Filled in by the rOpenSci editorial team during review                       |

## Author profile file

Each author listed in the post frontmatter needs a corresponding file at:

```
content/authors/firstname-lastname/_index.md
```

The file contains only a YAML block (no body text is needed):

```yaml
---
name: Your Full Name
link: https://your-website.example.com
mastodon: https://mastodon.social/@yourhandle
twitter: yourhandle
github: yourgithubusername
gitlab: yourgitlabusername
keybase: yourkeybaseid
orcid: 0000-0000-0000-0000
img: link-to-photo-in-themes/ropensci/static/img/community
---
```

Field notes:

- At minimum you must supply `name` and at least one of: `link`, `github`, `gitlab`, or a social handle — so there is somewhere to link from your author page.
- Usernames go in without the `@` prefix or full URL (except `mastodon`, which takes the full profile URL).
- `img` is optional; if omitted, the site falls back to your GitHub profile picture automatically.
- The file path uses a hyphenated slug of your name: `firstname-lastname`.

## Checklist before submitting

- [ ] Post file is at `content/blog/YYYY-MM-DD-slug/index.md`
- [ ] `slug` in frontmatter matches the directory name
- [ ] Every name in `author` has a matching `content/authors/firstname-lastname/_index.md`
- [ ] `tags` checked against existing site tags
- [ ] `package_version` removed if the post is not about a package
- [ ] `socialImg` and `socialAlt` both present if you want a social card
- [ ] `editor` field left empty

Sources:

- [Technical Guidelines – rOpenSci Blog Guide](https://blogguide.ropensci.org/authortechnical.html)
- [Template – Post (md) – rOpenSci Blog Guide](https://blogguide.ropensci.org/templatemd.html)
- [Template – Author file – rOpenSci Blog Guide](https://blogguide.ropensci.org/authortemplate.html)
- [rOpenSci Blog Guide for Authors and Editors](https://blogguide.ropensci.org/)
