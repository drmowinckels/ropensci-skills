# Security Best Practices

Source: <https://devguide.ropensci.org/pkg_security.html>

These are the checkable security practices rOpenSci expects. Apply them to any
package that handles credentials, makes network requests, or records HTTP fixtures.

## Secrets and credentials

- Store API keys in **environment variables**; consider removing the option to
  pass a key as a function argument entirely.
- Support **keyring** (OS credential store) as an alternative to `.Renviron`.
- **Never print the API key** — not in any message, warning, or error, even in
  verbose mode.
- Guide users so credentials never land in `.Rhistory` or committed scripts; point
  them to startup-file docs and `usethis::edit_r_environ()`.

## Recorded requests / test fixtures

- When using **vcr** or **httptest/httptest2**, make sure recorded requests and
  fixtures **do not contain secrets**.
- Follow vcr's security guidance and httptest's "Redacting and Modifying Recorded
  Requests"; **inspect fixtures before the first commit**.

## CI secrets

- Repository secrets are available only to Actions running in the repo itself —
  **not** in forks or external pull requests.
- Skip secret-dependent tests based on the presence of an env var, and rely on
  mocked/cached responses instead.
- Document this behavior in `CONTRIBUTING.md` so contributors know why some tests
  skip.

## CRAN compliance with credentials

- Skip credential-requiring tests (`skip_on_cran()`) and examples (`\dontrun{}`).
- Pre-compute vignettes that need credentials, or use vcr.

## GitHub account hygiene

- 2FA is recommended and **compulsory** for all rOpenSci GitHub org members and
  outside collaborators.
- Periodically prune repo access for former collaborators.

## Issue templates and protocol

- In issue templates, tell users **not to share any credentials**.
- If a credential is leaked, explicitly ask the user to **revoke the key**.
- If the wrapped web service offers both http and https, **opt for https**.
