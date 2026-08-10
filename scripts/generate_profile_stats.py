import json
import os
import urllib.request
from collections import Counter
from pathlib import Path

USERNAME = os.environ.get("GITHUB_REPOSITORY_OWNER", "robertoatila")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = Path("assets/stats")
OUT.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "github-profile-stats",
    "X-GitHub-Api-Version": "2022-11-28",
}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"


def get_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def esc(value):
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def write_stats(user, repos):
    own_repos = [repo for repo in repos if not repo.get("fork")]
    stars = sum(repo.get("stargazers_count", 0) for repo in own_repos)
    forks = sum(repo.get("forks_count", 0) for repo in own_repos)
    repos_count = user.get("public_repos", len(own_repos))
    followers = user.get("followers", 0)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="470" height="185" viewBox="0 0 470 185" role="img" aria-label="Estatísticas públicas do GitHub de {esc(USERNAME)}">
<style>
  .title {{ font: 600 18px -apple-system,BlinkMacSystemFont,Segoe UI,sans-serif; fill: #58a6ff; }}
  .label {{ font: 500 13px -apple-system,BlinkMacSystemFont,Segoe UI,sans-serif; fill: #8b949e; }}
  .value {{ font: 700 22px -apple-system,BlinkMacSystemFont,Segoe UI,sans-serif; fill: #c9d1d9; }}
  .foot {{ font: 400 11px -apple-system,BlinkMacSystemFont,Segoe UI,sans-serif; fill: #8b949e; }}
</style>
<rect x="0.5" y="0.5" width="469" height="184" rx="10" fill="#0d1117" stroke="#30363d"/>
<text x="24" y="34" class="title">GitHub — estatísticas públicas</text>
<text x="24" y="72" class="label">Repositórios públicos</text><text x="24" y="99" class="value">{repos_count}</text>
<text x="145" y="72" class="label">Seguidores</text><text x="145" y="99" class="value">{followers}</text>
<text x="255" y="72" class="label">Estrelas recebidas</text><text x="255" y="99" class="value">{stars}</text>
<text x="375" y="72" class="label">Forks</text><text x="375" y="99" class="value">{forks}</text>
<line x1="24" y1="125" x2="446" y2="125" stroke="#21262d"/>
<text x="24" y="151" class="foot">Gerado automaticamente via GitHub Actions usando a API oficial do GitHub.</text>
<text x="24" y="169" class="foot">Sem dependência de servidores públicos de cards.</text>
</svg>'''
    (OUT / "github-stats.svg").write_text(svg, encoding="utf-8")


def write_languages(repos):
    totals = Counter()
    for repo in repos:
        if repo.get("fork"):
            continue
        try:
            data = get_json(repo["languages_url"])
        except Exception:
            continue
        totals.update(data)

    total_bytes = sum(totals.values()) or 1
    languages = totals.most_common(6)

    rows = []
    y = 68
    for language, amount in languages:
        pct = amount / total_bytes * 100
        width = max(2, int(300 * pct / 100))
        rows.append(f'<text x="24" y="{y}" class="label">{esc(language)}</text>')
        rows.append(f'<text x="430" y="{y}" text-anchor="end" class="pct">{pct:.1f}%</text>')
        rows.append(f'<rect x="125" y="{y-10}" width="300" height="8" rx="4" fill="#21262d"/>')
        rows.append(f'<rect x="125" y="{y-10}" width="{width}" height="8" rx="4" fill="#58a6ff"/>')
        y += 27

    height = max(120, y + 10)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="470" height="{height}" viewBox="0 0 470 {height}" role="img" aria-label="Linguagens dos repositórios públicos de {esc(USERNAME)}">
<style>
  .title {{ font: 600 18px -apple-system,BlinkMacSystemFont,Segoe UI,sans-serif; fill: #58a6ff; }}
  .label {{ font: 500 12px -apple-system,BlinkMacSystemFont,Segoe UI,sans-serif; fill: #c9d1d9; }}
  .pct {{ font: 500 11px -apple-system,BlinkMacSystemFont,Segoe UI,sans-serif; fill: #8b949e; }}
</style>
<rect x="0.5" y="0.5" width="469" height="{height-1}" rx="10" fill="#0d1117" stroke="#30363d"/>
<text x="24" y="34" class="title">Linguagens — repositórios públicos</text>
{''.join(rows)}
</svg>'''
    (OUT / "top-languages.svg").write_text(svg, encoding="utf-8")


user = get_json(f"https://api.github.com/users/{USERNAME}")
repos = get_json(f"https://api.github.com/users/{USERNAME}/repos?per_page=100&type=owner&sort=updated")
write_stats(user, repos)
write_languages(repos)
