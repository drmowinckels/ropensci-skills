#!/usr/bin/env python3
"""Grade rOpenSci skill eval runs by checking for required rOpenSci-specific facts.

Each assertion passes if ANY of its regex alternatives matches the response
(case-insensitive). Writes grading.json into each run dir (schema: expectations
array of {text, passed, evidence}) and writes the assertion list back into each
eval_metadata.json.
"""
import json, re, pathlib, sys

ITER = pathlib.Path(__file__).parent / (sys.argv[1] if len(sys.argv) > 1 else "iteration-1")

# eval_dir -> list of (assertion_text, [regex alternatives])
ASSERTIONS = {
    "pkgstd-new-package": [
        ("Recommends usethis to scaffold the package", [r"usethis"]),
        ("Recommends snake_case for function naming", [r"snake[_ ]?case"]),
        ("Says use Imports rather than Depends", [r"\bImports\b.*\bDepends\b|\bDepends\b.*\bImports\b|use\s+imports"]),
        ("Recommends modern HTTP/JSON deps (httr2/curl/jsonlite)", [r"httr2|jsonlite|\bcurl\b|crul"]),
        ("States the ~75% test coverage expectation", [r"75\s*%|75\s*percent|75[^\n]{0,25}cover|cover[^\n]{0,25}75"]),
        ("Specifies CI across release, oldrel and devel R", [r"oldrel|devel.*release|release.*devel"]),
        ("Mentions the rOpenSci repostatus README badge", [r"repostatus"]),
        ("Covers API-key security (env var / keyring / not printed)", [r"environment variable|\.renviron|renviron|keyring|never print"]),
        ("Recommends at least one vignette", [r"vignette"]),
        ("Recommends roxygen2 for documentation", [r"roxygen"]),
    ],
    "pkgstd-audit-description": [
        ("Flags package name should be lowercase", [r"lower\s?case|lowercase"]),
        ("Flags Title should drop 'in R' / be Title Case", [r"title case|drop[^\n]{0,20}\bin r\b|\bin r\b[^\n]{0,20}(redundant|drop|remove|unnecessary)"]),
        ("Flags missing Authors@R / ORCID", [r"authors@r|orcid"]),
        ("Flags Description starting with 'This package'", [r"this package"]),
        ("Flags Depends should be Imports", [r"depends[^\n]{0,40}imports|imports[^\n]{0,40}depends|move[^\n]{0,20}imports|use\s+imports"]),
        ("Flags RCurl/rjson as discouraged (httr2/curl/jsonlite)", [r"httr2|jsonlite|crul|RCurl|rjson"]),
        ("Flags missing/invalid license (CRAN/OSI)", [r"cran[^\n]{0,10}osi|osi[^\n]{0,10}cran|osi[- ]?approved|valid licen[sc]e"]),
        ("Flags missing URL / BugReports fields", [r"bugreports"]),
    ],
    "author-scope-readiness": [
        ("Addresses whether the package is in scope", [r"in scope|out of scope|within scope|fits[^\n]{0,25}scope|scope[^\n]{0,25}(categor|fit)"]),
        ("Mentions the overlap / significant-difference policy", [r"overlap|significant difference|duplicat"]),
        ("Recommends running pkgcheck before submitting", [r"pkgcheck"]),
        ("Mentions the ~2-year maintenance commitment", [r"2[- ]?year|two[- ]?year"]),
        ("Says submit before CRAN release / software paper", [r"before .*cran|before .*publi|prior to cran|before submitting .*paper"]),
        ("Notes README must let editor assess without installing", [r"without install|assess[^\n]{0,30}without"]),
        ("Mentions a pre-submission enquiry option", [r"pre[- ]?submission|presubmission"]),
    ],
    "author-submission-mechanics": [
        ("Says open an issue in ropensci/software-review", [r"software-review|software review"]),
        ("Mentions the submission template", [r"template"]),
        ("Mentions @ropensci-review-bot / pkgcheck on submission", [r"ropensci-review-bot|review-bot|pkgcheck"]),
        ("Says two reviewers are assigned", [r"two reviewers|2 reviewers"]),
        ("Mentions the ~3-week review window", [r"3[- ]?week|three[- ]?week|21[- ]?day"]),
        ("Mentions approval and transfer to the ropensci org", [r"transfer|ropensci org|ropensci github"]),
        ("Notes a statement of need is required", [r"statement of need"]),
    ],
    "review-reviewer-checklist": [
        ("Mentions checking for conflict of interest", [r"conflict of interest|conflict"]),
        ("States the 3-week review timeframe", [r"3[- ]?week|three[- ]?week"]),
        ("Includes Documentation checklist (statement of need)", [r"statement of need"]),
        ("Includes Functionality checklist (packaging guidelines/tests)", [r"functionality|packaging guidelines|automated tests"]),
        ("Recommends hands-on checks (devtools::check/test, install)", [r"devtools|R CMD check|install"]),
        ("Mentions respectful / non-adversarial conduct (CoC)", [r"respectful|non-adversarial|code of conduct|kind"]),
        ("Mentions the reviewer 'rev' role / being credited", [r"\brev\b|reviewer role|acknowledg"]),
        ("Mentions the pkgreviewr helper", [r"pkgreviewr"]),
    ],
    "review-editor-checks": [
        ("Notes docs should be assessable without installing", [r"without install|assess.*without"]),
        ("Mentions fit / overlap check", [r"overlap|fit[^\n]{0,15}scope|scope[^\n]{0,15}(criteria|overlap|fit)|meets[^\n]{0,15}scope"]),
        ("Mentions CRAN/OSI license check", [r"cran[^\n]{0,10}osi|osi[^\n]{0,10}cran|osi[- ]?approved|valid licen[sc]e"]),
        ("Mentions checking issue/PR tracker health", [r"tracker|project management|issue.*pr"]),
        ("Mentions assigning exactly two reviewers", [r"two reviewers|2 reviewers"]),
        ("Mentions the bot runs pkgcheck", [r"pkgcheck"]),
        ("Mentions the 21-day / 3-week reviewer default", [r"21[- ]?day|3[- ]?week|three[- ]?week"]),
        ("Mentions check srr for statistical packages", [r"\bsrr\b"]),
    ],
}

def grade_text(text, alts):
    for pat in alts:
        m = re.search(pat, text, re.IGNORECASE | re.DOTALL)
        if m:
            snippet = m.group(0)
            return True, snippet[:160]
    return False, ""

for eval_dir, asserts in ASSERTIONS.items():
    base = ITER / eval_dir
    # update eval_metadata.json with assertion texts
    meta_path = base / "eval_metadata.json"
    if meta_path.exists():
        meta = json.loads(meta_path.read_text())
        meta["assertions"] = [a[0] for a in asserts]
        meta_path.write_text(json.dumps(meta, indent=2) + "\n")
    for config in ("with_skill", "without_skill"):
        resp = base / config / "outputs" / "response.md"
        if not resp.exists():
            print(f"MISSING {resp}")
            continue
        text = resp.read_text()
        expectations = []
        for atext, alts in asserts:
            passed, evidence = grade_text(text, alts)
            expectations.append({"text": atext, "passed": passed, "evidence": evidence})
        grading = {"expectations": expectations,
                   "passed_count": sum(1 for e in expectations if e["passed"]),
                   "total": len(expectations)}
        (base / config / "grading.json").write_text(json.dumps(grading, indent=2) + "\n")
        print(f"{eval_dir}/{config}: {grading['passed_count']}/{grading['total']}")
