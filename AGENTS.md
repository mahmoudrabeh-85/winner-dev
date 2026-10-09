## Session Start Rule

At the start of every session, read `INDEX.md` first — it contains the master file index, project paths, server ports, and next steps. Then read `PROGRESS.md`, `NEXT_STEPS.md`, `DECISIONS.md` for details. This saves time vs. reading every file separately.

## Precision Rule

Only change exactly what the user asks for. Do not modify, add, or remove anything beyond the explicit request. Every edit must be strictly scoped to the user's exact words.

## Preview Rule (after every important edit)

After any significant UI/content/design edit: open the preview in the browser immediately (for this site: open the local `portfolio.html` or a version file). Then iterate based on user feedback — do not move to the next step before the user sees the result.

## Security Rule (before every push)

Run the mandatory security scan before any push: grep token patterns, check git status, review .gitignore, audit git history. Show results to the user and get "go" before pushing.

## Testing Rule (2026-09-23)

When the user says **"اختبر قبل الرفع"**: run the DEFAULT test group from `TESTING.md` (A1 + A2 + D1-D4) plus type-specific additions (UI→C1,C2,C6; flow→C3; deploy→D5,E1-E4; API/data→B4,F1-F3), show a ✅/❌ results table, and never commit before the user's "go".

## Delegation Rule (long tasks)

For long/heavy tasks, delegate as a **swarm of 2-3 small subagents in parallel** — proven winning pattern (2026-09-20): `fast` + `coder` with small scoped tasks → fast success + live preview on http://127.0.0.1:8767/. Avoid single heavy `implementer` alone (risk 504 timeout on free provider). Agents live in `~/.config/opencode/agent/` (implementer / inspector / planner / fast / coder / researcher / arabic). Keep at most 2-3 parallel agents (429 risk at 4+). Always preview after swarm completes.
