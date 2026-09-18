#!/usr/bin/env python3
"""Refresh the `★ N` badges in README.md from the GitHub API.

Updates counts in place and never reorders or rewrites entries. Pass --check to
report drift without writing (used on pull requests, where the token is read-only).
"""
import argparse, json, os, re, sys, urllib.error, urllib.request

README = "README.md"
API = "https://api.github.com/graphql"
# `- [owner/name](https://github.com/owner/name) — text `★ 1.2k``
ENTRY = re.compile(r"^(- \[(?P<repo>[\w.-]+/[\w.-]+)\]\(https://github\.com/(?P=repo)\).*?)`★ [^`]*`\s*$")
# `| 12 | [owner/name](https://github.com/owner/name) | 5.1k | 2.9 | 86.8 |`
ROW = re.compile(r"^(\|\s*\d+\s*\|\s*\[(?P<repo>[\w.-]+/[\w.-]+)\]\(https://github\.com/(?P=repo)\)\s*\|\s*)(?P<stars>[^|]+?)(\s*\|)")


def fmt(n):
    """Match the list's existing style: 5093 -> 5.1k, 2000 -> 2k, 862 -> 862."""
    return f"{n / 1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


def fetch(repos, token):
    """One GraphQL call per 100 repos. Returns {repo: (stars, canonical_name)}."""
    out = {}
    for i in range(0, len(repos), 100):
        chunk = repos[i:i + 100]
        query = "query{" + " ".join(
            f'r{j}: repository(owner:"{r.split("/")[0]}", name:"{r.split("/")[1]}")'
            "{nameWithOwner stargazerCount}" for j, r in enumerate(chunk)
        ) + "}"
        req = urllib.request.Request(
            API, json.dumps({"query": query}).encode(),
            {"Authorization": f"bearer {token}", "Content-Type": "application/json"})
        try:
            body = json.load(urllib.request.urlopen(req, timeout=60))
        except urllib.error.HTTPError as e:
            sys.exit(f"GitHub API error {e.code}: {e.read()[:300].decode(errors='replace')}")
        for j, repo in enumerate(chunk):
            node = (body.get("data") or {}).get(f"r{j}")
            if node:
                out[repo] = (node["stargazerCount"], node["nameWithOwner"])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="report drift, write nothing")
    args = ap.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN is not set")

    lines = open(README, encoding="utf-8").read().split("\n")
    repos = sorted({m.group("repo") for line in lines
                    for m in [ENTRY.match(line) or ROW.match(line)] if m})
    print(f"found {len(repos)} repositories in {README}")

    stars = fetch(repos, token)
    missing = [r for r in repos if r not in stars]
    renamed = {r: new for r, (_, new) in stars.items() if new != r}

    changed, out = [], []
    for line in lines:
        m = ENTRY.match(line)
        if m and m.group("repo") in stars:
            n = fmt(stars[m.group("repo")][0])
            new = f"{m.group(1)}`★ {n}`"
            if new != line:
                changed.append((m.group("repo"), line.rsplit("`★ ", 1)[-1].rstrip("`"), n))
            out.append(new)
            continue
        m = ROW.match(line)
        if m and m.group("repo") in stars:
            n = fmt(stars[m.group("repo")][0])
            new = ROW.sub(lambda x: f"{x.group(1)}{n}{x.group(4)}", line)
            if new != line:
                changed.append((m.group("repo"), m.group("stars").strip(), n))
            out.append(new)
            continue
        out.append(line)

    seen = set()
    unique = [c for c in changed if c[0] not in seen and not seen.add(c[0])]
    for repo, old, new in unique:
        print(f"  {repo}: {old} -> {new}")
    for repo in missing:
        print(f"  !! {repo}: not found (404) — left unchanged, check manually")
    for old, new in renamed.items():
        print(f"  ~~ {old}: renamed to {new} — link still works, consider updating")

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as f:
            f.write(f"### Star refresh\n\n{len(unique)} project(s) changed, "
                    f"{len(missing)} unreachable, {len(renamed)} renamed.\n\n")
            for repo, old, new in unique[:40]:
                f.write(f"- `{repo}` {old} → **{new}**\n")
            for repo in missing:
                f.write(f"- :warning: `{repo}` returned 404\n")
            for old, new in renamed.items():
                f.write(f"- :pencil2: `{old}` is now `{new}`\n")

    if args.check:
        print(f"\ncheck mode: {len(unique)} project(s) would change")
        return
    if changed:
        open(README, "w", encoding="utf-8").write("\n".join(out))
        print(f"\nwrote {README} ({len(unique)} project(s) updated)")
    else:
        print("\nno changes")


if __name__ == "__main__":
    main()
