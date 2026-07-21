# Leetcode Stats Dashboard

A single-file HTML dashboard for [`bhushan1010/Leetcode`](https://github.com/bhushan1010/Leetcode) — solved count, difficulty breakdown, topic frequency, an activity heatmap, streak, and the full solve list.

## How it works

`leetcode-dashboard.html` has no build step and no backend. On open, it fetches three things straight from GitHub in the browser:

| Source | Used for |
|---|---|
| `raw.githubusercontent.com/.../stats.json` | Solved count, easy/medium/hard split, per-problem difficulty |
| `raw.githubusercontent.com/.../README.md` | Topic tag cloud (parses the `## Topic` tables) |
| `api.github.com/repos/.../commits` | Activity heatmap + current streak (counts commits starting with `Time:`, which LeetHub writes on every accepted solve) |

Since LeetHub already commits to `main` every time you solve a problem, the dashboard is current as of your last solve — no separate sync step needed. If GitHub can't be reached (offline, or the browser hits GitHub's unauthenticated rate limit), it falls back to a cached snapshot baked into the file so it never shows blank, and flags itself as **cached** instead of **live** in the footer.

## Using it

- **Locally:** just open `leetcode-dashboard.html` in a browser.
- **Re-sync:** click "↻ re-sync now" in the footer to re-fetch without reloading the page.
- **Host it:** drop it in a GitHub Pages repo (or the `Leetcode` repo itself, e.g. `docs/index.html` with Pages enabled) to get a public URL. It stays live since it always reads from the API/raw endpoints at load time, not from data baked in at deploy time.

## Rate limits

The commits fetch hits `api.github.com` unauthenticated, capped at **60 requests/hour per IP**, shared by anyone on that network. Fine for occasional personal checking; if you embed this somewhere with real traffic, you'll hit that ceiling.

## Optional: daily history workflow

Not required for the dashboard to work — it's only useful if you want a **trend line over time** (e.g. "solved per week") rather than just current totals, or want to avoid the live API rate limit by having the dashboard read a file in your own repo instead of calling `api.github.com` directly.

If you want it, here's what it would do:

```yaml
# .github/workflows/snapshot-stats.yml
name: Snapshot LeetCode stats
on:
  schedule:
    - cron: "0 18 * * *"   # once daily, ~11:30pm IST
  workflow_dispatch: {}

jobs:
  snapshot:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Append today's stats to history.json
        run: |
          python3 - <<'EOF'
          import json, datetime, pathlib

          stats = json.loads(pathlib.Path("stats.json").read_text())["leetcode"]
          history_path = pathlib.Path("history.json")
          history = json.loads(history_path.read_text()) if history_path.exists() else []

          today = datetime.date.today().isoformat()
          if not history or history[-1]["date"] != today:
              history.append({
                  "date": today,
                  "solved": stats["solved"],
                  "easy": stats["easy"],
                  "medium": stats["medium"],
                  "hard": stats["hard"],
              })
              history_path.write_text(json.dumps(history, indent=2))
          EOF
      - name: Commit if changed
        run: |
          git config user.name "github-actions"
          git config user.email "actions@github.com"
          git add history.json
          git diff --cached --quiet || git commit -m "Snapshot stats"
          git push
```

Say the word and I'll add this file to your repo plan and wire the dashboard to plot `history.json` as a trend line instead of (or alongside) the live heatmap.
