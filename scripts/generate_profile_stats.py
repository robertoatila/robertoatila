# Generates self-hosted SVG cards from the official GitHub API.
import json
import os
import urllib.request
from collections import Counter
from pathlib import Path

USERNAME = os.environ.get("GITHUB_REPOSITORY_OWNER", "robertoatila")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = Path("assets/stats")
OUT.mkdir(parents=True, exist_ok=True)

CARD_WIDTH = 470
STATS_HEIGHT = 220
LANGUAGES_HEIGHT = 245

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
    return (
        str(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


def write_stats(user, repos):
    own_repos = [repo for repo in repos if not repo.get("fork")]
    metrics = [
        ("Repositórios públicos", user.get("public_repos", len(own_repos))),
        ("Seguidores", user.get("followers", 0)),
        ("Estrelas recebidas", sum(repo.get("stargazers_count", 0) for repo in own_repos)),
        ("Forks", sum(repo.get("forks_count", 0) for repo in own_repos)),
    ]

    columns = []
    positions = ((24, 85), (250, 85), (24, 160), (250, 160))
    for (x, y), (label, value) in zip(positions, metrics):
        columns.append(
            f'<text x="{x}" y="{y}" class="label">{esc(label)}</text>'
            f'<text x="{x}" y="{y + 33}" class="value">{esc(value)}</text>'
        )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{CARD_WIDTH}" height="{STATS_HEIGHT}" viewBox="0 0 {CARD_WIDTH} {STATS_HEIGHT}" role="img" aria-label="Estatísticas públicas do GitHub de {esc(USERNAME)}">
<title>Atividade pública no GitHub</title>
<desc>Resumo de repositórios, seguidores, estrelas e forks de {esc(USERNAME)}.</desc>
<style>
  .card {{ fill: #0d1117; stroke: #30363d; }}
  .title {{ font: 600 18px -apple-system,BlinkMacSystemFont,Segoe UI,sans-serif; fill: #58a6ff; }}
  .label {{ font: 500 14px -apple-system,BlinkMacSystemFont,Segoe UI,sans-serif; fill: #8b949e; }}
  .value {{ font: 700 28px -apple-system,BlinkMacSystemFont,Segoe UI,sans-serif; fill: #f0f6fc; }}
  .rule {{ stroke: #21262d; }}
</style>
<rect class="card" x="0.5" y="0.5" width="469" height="219" rx="14"/>
<text x="24" y="36" class="title">Atividade pública no GitHub</text>
<line class="rule" x1="24" y1="55" x2="446" y2="55"/>
{''.join(columns)}
<line class="rule" x1="235" y1="68" x2="235" y2="204"/>
<line class="rule" x1="24" y1="135" x2="446" y2="135"/>
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

    if languages:
        largest_amount = languages[0][1] or 1
        for index, (language, amount) in enumerate(languages):
            y = 76 + index * 28
            pct = amount / total_bytes * 100
            width = max(4, int(250 * amount / largest_amount))
            rows.append(f'<text x="24" y="{y}" class="label">{esc(language)}</text>')
            rows.append(f'<rect x="128" y="{y - 9}" width="{width}" height="6" rx="3" class="bar"/>')
            rows.append(f'<text x="446" y="{y}" text-anchor="end" class="pct">{pct:.1f}%</text>')
    else:
        rows.append('<text x="24" y="110" class="empty">Nenhum dado público de linguagem disponível.</text>')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{CARD_WIDTH}" height="{LANGUAGES_HEIGHT}" viewBox="0 0 {CARD_WIDTH} {LANGUAGES_HEIGHT}" role="img" aria-label="Linguagens dos repositórios públicos de {esc(USERNAME)}">
<title>Linguagens dos repositórios públicos</title>
<desc>Distribuição proporcional das seis linguagens mais usadas nos repositórios públicos de {esc(USERNAME)}.</desc>
<style>
  .card {{ fill: #0d1117; stroke: #30363d; }}
  .title {{ font: 600 18px -apple-system,BlinkMacSystemFont,Segoe UI,sans-serif; fill: #58a6ff; }}
  .label {{ font: 500 14px -apple-system,BlinkMacSystemFont,Segoe UI,sans-serif; fill: #f0f6fc; }}
  .pct {{ font: 500 12px -apple-system,BlinkMacSystemFont,Segoe UI,sans-serif; fill: #8b949e; }}
  .empty {{ font: 400 13px -apple-system,BlinkMacSystemFont,Segoe UI,sans-serif; fill: #8b949e; }}
  .bar {{ fill: #58a6ff; }}
  .rule {{ stroke: #21262d; }}
</style>
<rect class="card" x="0.5" y="0.5" width="469" height="244" rx="14"/>
<text x="24" y="36" class="title">Linguagens dos repositórios públicos</text>
<line class="rule" x1="24" y1="55" x2="446" y2="55"/>
{''.join(rows)}
</svg>'''
    (OUT / "top-languages.svg").write_text(svg, encoding="utf-8")


user = get_json(f"https://api.github.com/users/{USERNAME}")
repos = get_json(f"https://api.github.com/users/{USERNAME}/repos?per_page=100&type=owner&sort=updated")
write_stats(user, repos)
write_languages(repos)
