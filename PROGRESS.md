# PROGRESS

## Section 2026-09-16 (5 مهام: سرعة + مهارات + Stitch + v4 + شهادة — DONE)
- ✅ **السرعة**: `npx --no-install --help` أثبت الـ cache دافئاً (playwright 6s + chrome-devtools 6s + uiux-pro 3s = ~15s أرضية لـ 3 خوادم محلية). الباقي من الـ 60s هو opencode نفسه. firecrawl/composio البعيدان = صفر عمليات جديدة (21 node ثابتة).
- ✅ **إزالة Oracle/ERP من المهارات**: حُذفت من `job_aggregator.py` + `smart_scorer.py` + KEYWORDS + وسوم setup.html (43 → 38 مهارة). التحقق: `COMPILE OK` + البروفايل يعرض 38 مهارة.
- ✅ **سؤال كارت GCP**: بحث رسمي — التسجيل يشترط كارت (تحقق هوية فقط) + 300$ رصيد 90 يوم + **لا سحب إلا بترقية يدوية**. التوصية: إبقاء Stitch معطلاً (احتياجات التصميم مغطاة).
- ✅ **معاينة v4**: خادم 8771 + Playwright — العنوان سليم + 0 أخطاء console + لقطة شاشة مأخوذة. بانتظار موافقة المستخدم للتفعيل.
- ✅ **شهادة Oracle SCM أُلغيت مؤقتاً**: حُدّثت كل الإشارات في portfolio + job-hunt (NEXT_STEPS/DECISIONS/PROGRESS).
- ⬜ المستخدم: إعادة تشغيل opencode + `opencode mcp auth composio` + الموافقة على v4.

## Section 2026-09-16 (تثبيت Firecrawl MCP + Composio — DONE)
- ✅ **بحث ويب موثق**: Firecrawl الرسمي `firecrawl/firecrawl-mcp-server` (7,413⭐ — `npx -y firecrawl-mcp` + `FIRECRAWL_API_KEY`) + طبقة مستضافة بلا مفتاح `https://mcp.firecrawl.dev/v2/mcp`؛ Composio عبر `https://connect.composio.dev/mcp` + مصادقة `opencode mcp auth composio`.
- ✅ **التثبيت**: خادمان بعيدان (remote) في `opencode.jsonc` — `firecrawl` + `composio` (مفعّلان). لا عمليات node جديدة. التحقق: JSONC سليم (12 خادماً — 5 مفعّلة) + الوصول حي (405/401 كما هو متوقع).
- ✅ ملف `customize-opencode` skill حُمّل قبل التعديل (حسب القاعدة) + DECISIONS.md/NEXT_STEPS.md/LEARNING.md حُدّثت.
- ⬜ المستخدم: إعادة تشغيل opencode + `opencode mcp auth composio` + مفتاح Firecrawl اختياري لاحقاً.

## Section 2026-09-16 (إصلاح الداشبورد + صفحة فلتر ذكية — DONE)
- ✅ **إصلاح قاتل في الداشبورد**: `dashboard.html` — الـ iframes كانت تشير لنفسها (`src=""` → المتصفح يفسّره كعنوان الصفحة الحالية). **الحل:** إزالة `src=""` بالكامل والاستخدام فقط `data-src` مع تعيين `src` عند النقر (lazy loading). كل 4 التبويبات تعمل الآن ✅.
- ✅ **API تصفية جديد**: أُضيف `/api/search` في `job_app.py` — يقبل: source, work_type, min_score, q (بحث نصي), skills, location, limit. يُرجع وظائف مع تحليل CV. **إضافة حاسمة:** `dict(j)` لتحويل `sqlite3.Row` → dict (كان يسبب 500 error).
- ✅ **صفحة فلتر ذكية** `setup.html`: بدل صفحة إعدادات تحوّلت لصفحة فلتر + نتائج مباشرة — حقل بحث نصي + بطاقات مصادر قابلة للتحديد + فلترة حسب المصدر ونوع العمل + عرض النتائج في الوقت الحقيقي (AJAX) + أزرار تصنيف (الكل/عالٍ/متوسط/منخفض) + رابط العودة للداشبورد. **مُختبَر**: 150 وظيفة مطابقة تظهر ✅.
- ⬜ المستخدم: إضافة Felix/Ultrawork/FreelanceUp إلى job-aggregator. شهادة Oracle SCM (ملغاة مؤقتاً — 2026-09-16). تنظيف ذاكرة completed projects.

## Section 2026-09-15/16 (MCP/UI-UX على المشاريع المنفذة — جاري الإغلاق)
- ✅ **داشبورد المشاريع (Command Center)**: `D:\ai\tools\dashboard\generate_dashboard.py` يقرأ 10 مشاريع + ملفات الذاكرة (استخراج ✅/⬜ تلقائي + أوقات متوقعة) + فحص حي (HTTP 200 / عمليات Python / منافذ). Dashboard v1: 134 منجز، 53 معلّق، 4 نشطة. **مُختبَر**: خادم 8800 + Playwright DOM (10 بطاقات، portfolio 76%， job-hunt 73%， الموقع 200 OK ✅， بايثون يعمل 4 عمليات ✅).
- ✅ **CLI Launcher موحّد بالهوية الموحدة**: `D:\ai\tools\cli_launcher.html` — مرساة **Industrial** (أسود `#0B0C0A` + mono + حدود 1px + acid `#C6FF4A`) مع توكنز uiux-pro. بطاقة dashboard مُضافة. **مُختبَر**: 22 أداة، 21/22 مثبتة ✅.
- ✅ **job-hunt index.html تدقيق WCAG**: أُضيف `:focus-visible` (WCAG 2.4.7) + `@media (prefers-reduced-motion: reduce)` (WCAG 2.3.3) + زر back-to-top + `modal.scrollTop=0` عند الفتح. الأقواس: 194/194. **مُختبَر**: 142 وظيفة محمّلة، مودال ring يعمل ✅.
- ✅ **نظام تصميم موحّد**: مرساة Industrial (frontend-design skill) + لوحة uiux-pro (`#440154/#21918C/#FDE725/#1A1A2E/#F5F5F5`) — مستخدمة في Dashboard + Launcher. job-hunt تحتفظ بتوكنزها الخاصة (مطابقة أصلاً).
- ⬜ المستخدم: إضافة Felix/Ultrawork/FreelanceUp إلى job-aggregator. شهادة Oracle SCM (ملغاة مؤقتاً — 2026-09-16). تنظيف ذاكرة completed projects.

## Section 2026-09-15 (Search: Design/Frontend MCPs + Google Stitch + Skills — DONE)
- ✅ **بحث توثيقي عبر GitHub API**: أفضل 10 MCP تصميم/فرونت إند = chrome-devtools (52,051⭐) / playwright (37,144⭐) / Figma-Context (15,864⭐) / magic-mcp (5,871⭐) / executeautomation (5,644⭐) / design-extract (4,101⭐) / shadcn-ui (2,991⭐) / fetcher-mcp (1,085⭐) / penpot (503⭐) / better-design (233⭐) — الأرقام فعلية اليوم.
- ✅ **Google Stitch اكتُشف بالكامل**: الرسمي `google-labs-code/stitch-skills` (8,260⭐ — 16 مهارة تدعم OpenCode يدوياً) + MCP عبر `stitch.googleapis.com/mcp` (يتطلب إعداد GCP: gcloud auth + تفعيل Stitch API عبر `npx @_davideast/stitch-mcp init`).
- ✅ **14 مهارة تصميم منتقاة + مثبتة** في `C:\Users\RTX\.config\opencode\skills\selected\` (585KB) عبر `skills.paths` — 9 من Stitch + 5 Anti-slop (superdesign/brandkit/frontend-design/audit/extract-design).
- ✅ **MCP جديد مفعّل**: `chrome-devtools` (npx) + **MCP معطّل بانتظار GCP**: `stitch` (remote).
- ✅ **ملف مرجعي شامل**: `C:\Users\RTX\.config\opencode\DESIGN-REFERENCES.md` — جدول اختيار + كل MCPs/mهارات/CLI + أفضل 10 سوق — أُضيف إلى instructions (auto-load كل جلسة).
- ✅ التحقق: 188/188 قوساً + `opencode run` رد "تمام" بعد تحميل الإعداد الجديد.
- ⬜ **إعادة تشغيل opencode** لتحميل المهارات و MCP الجديد.
- ⬜ المستخدم: تفعيل Stitch MCP لاحقاً (`npx @_davideast/stitch-mcp init` — 10-15 دقيقة).

## Section 2026-09-15 (v4 — تحسينات UI/UX MCP — جاهزة للمعاينة)
- ✅ **نسخة v4 أُنشئت** في `versions/v4-2026-09-15/` (نسخة كاملة من v3 الحالية + تحسينات).
- ✅ **التحسينات المطبقة** (معايير uiux-pro + shadcn + magic-ui): توكنز نظامية (4px/radius/elevation/z-index/motion) + شريط تقدم القراءة أعلى الصفحة + **توست بدل alert** في نموذج التواصل (رسالة عربية/إنجليزية حسب اللغة) + `:focus-visible` (WCAG 2.4.7) + `prefers-reduced-motion` (WCAG 2.3.3) + رفع بطاقات glass عند hover + ضغط أزرار عند النقر.
- ✅ **مُختبَر في المتصفح** (عبر خادم محلي 8770): شريط التقدم يعمل (53.97% عند منتصف الصفحة) + التوست يظهر بأنيميشن toastIn + توازن 14/14 قسم + 0 أخطاء JS + 207 زوج ترجمة سليم.
- ✅ VERSIONS.md حُدّث (سجل v4 + خطوات التفعيل) + DECISIONS.md (قرار v4 معلّق على موافقة المستخدم).
- ⬜ **بانتظار المستخدم**: معاينة v4 والموافقة → ثم: انسخ v4 → الجذر → فحص أمني (قاعدة 13) → push → تحقق حي.

## Section 2026-09-13 (Subagents + LOCAL-ONLY protection — DONE)
- ✅ **Multi-project management from ONE chat confirmed**: direct paths + parallel subagents + opencode-delegate + reading any project's memory files. Limit: 2-3 parallel agents max (free provider 429 risk at 4+).
- ✅ **Custom subagents added to global config** (`~/.config/opencode/opencode.jsonc`, braces 177/177 verified): `arabic` (opencode/mimo-v2.5-free — best Arabic), `coder` (opencode/nemotron-3-ultra-free — heavy analysis), `fast` (opencode/ling-3.0-flash-fin-free — light checks). Each agent = own model.
- ✅ **media-buying project = LOCAL-ONLY (user explicit decision)**: no .git, no remote; `.gitignore` safety net blocks everything by default; AGENTS.md + DECISIONS.md contain hard block rules.

## Section 2026-09-13 (Marketing/learning SPLIT into private project — DONE)
- ✅ All `docs/marketing/*` files moved to new private project `D:\ai\media-buying\` (own AGENTS/PROGRESS/NEXT_STEPS/DECISIONS).
- ✅ Portfolio repo cleaned: `eeedd7f` pushed — repo now = site code + site docs only (privacy fix: strategy files were public on winner-dev).
- ⬜ USER now works in `D:\ai\media-buying\` for: LinkedIn profile copy-paste, 10 posts, affiliate, ads learning.
- Related decision: LinkedIn = personal profile (linkedin.com/in/mahmoud-rabeh-7102071a3).

## Section 2026-09-13 (Marketing package + SEO — DONE, live)
- ✅ **SEO audit + fix** (from marketing package list): added meta description/keywords/author/robots, canonical → live domain, favicon link (svg existed but unlinked), 8 OG + 4 Twitter cards, **2 JSON-LD blocks (Person w/ LinkedIn + Service)**. Fixed **robots.txt + sitemap.xml pointing to wrong domain** (mahmoud-rabeh.com → mahmoudrabeh-85.github.io/winner-dev). Committed `5c78390` → **verified LIVE** (HTTP 200, JSON-LD present in served copy, size 104631). Lessons: GitHub Pages deploy has ~1min delay (verify via raw.githubusercontent instantly, then re-check after 60s).
- ✅ **Marketing package files** (committed `756afd7`):
  - `docs/marketing/LINKEDIN-POSTS.md` — 10 posts ready (5 AR + 5 EN), posting schedule tips, forbidden numbers noted.
  - `docs/marketing/SOCIAL-CONTENT-PLAN.md` — Egypt FB/IG/TikTok/YouTube weekly columns, 30-day quick start, Meta Pixel later.
  - `docs/marketing/AFFILIATE-ROADMAP.md` — Noon/Jumia/Amazon start steps (5 products, test 100-150 EGP/day, scale +30-40% rule).
  - `docs/marketing/ACCOUNTS-SETUP.md` — 7-platform checklist (LinkedIn first, then FB/TikTok/YT/IG/WA Business/Upwork), no prices in profiles rule.
- ⬜ USER actions from checklist: configure LinkedIn profile → then post the 10 posts; create FB page + accounts per checklist.

## Section 2026-09-13 (Supervisor bot smart replies + auto-start — DONE, user-verified from phone)
- ✅ **Smart reply logic** (`D:\ai\supervisor\supervisor_bot.py`): project detection ANYWHERE in sentence via `_match_project` (priority: first word, then multi-word phrases, then word-token match) + `PROJECT_SYNONYMS` (بورتفوليو/وينر/ذكاء الاعمال/الدماغ الثاني... for all 6 projects) + `_strip_project` + `_smart_reply` (المشاريع/النماذج/المهام/مرحبا/شكراً natural commands, no slash needed). **11/11 unit tests PASS locally + user tested from phone: "كل شيء يعمل"**.
- ✅ **Voice handler upgraded**: same smart detection (previously first-word-only — "اعرض هيكل المشروع في portfolio" would have failed).
- ✅ **Auto-start on logon**: `%APPDATA%\...\Startup\start_bots.vbs` starts supervisor_bot.py + portfolio bot/bot.py hidden with Win32_Process duplicate-guard (schtasks failed: Access denied without admin).
- ✅ Supervisor bot running as ONE clean instance (PID 2468), current token `[REDACTED]` (getMe OK, test msg msg_id=45 delivered).
- ✅ Help text fixed: default model now shows mimo (was outdated qwen3:8b).

## Section 2026-09-13 (v3 DEPLOYED — LIVE on GitHub Pages ✅)
- ✅ **Security scan (rule 13) passed**: git status clean-except-expected; rg scan of tracked files = 0 secrets; bot/.py reads token from env; .gitignore hardened (added versions/v1-2026-09-13-backup/ + assistant.exe).
- ✅ **CRITICAL security finding handled**: old token `[REDACTED]` was in git history (api/telegram.js commit 73d1949) **but is now REVOKED/401** (rotated long ago) — no live risk. Current site-bot token (`bot/.env` = `[REDACTED]`) was **never** in git history. **User actually rotated the SUPERVISOR bot** (`@mahmoudoc26_bot`) — new token `[REDACTED]` verified (getMe OK) → saved to `supervisor/.env` → bot restarted (PID 3008) → delivered test message to user (msg_id=45). Old supervisor token was 401 (revoked).
- ✅ **Pushed**: commit `30d4994` → `origin/main` (winner-dev repo, 7 files: portfolio.html, docs/RESPONSIVE-TESTING.md, memory files, bot/bot.py admin alerts, .gitignore).
- ✅ **LIVE VERIFIED**: `https://mahmoudrabeh-85.github.io/winner-dev/` → HTTP 200 redirects to `/portfolio.html` → live copy = 102k chars, contains `responsive-fix` + media-768 CSS + QR asset (HTTP 200 on assets) + `mahmoudagent26_bot` form link. **Deploy #8 COMPLETE** (GitHub Pages was already enabled — no Vercel/Cloudflare needed).
- ⬜ Optional later: clean git history (old dead token text from api/telegram.js) — cosmetic only, token is 401.

## Section 2026-09-13 (v3 activated + responsive fix — DONE, user-approved)
- ✅ **v3 = active version now**: copied `versions/v3-2026-09-10/` → root (portfolio.html 118KB, identity verified). Backup of previous v1 kept at `versions/v1-2026-09-13-backup/`.
- ✅ **Responsive gap found & fixed**: v3 had ONLY background media queries — v1's full responsive CSS (css/input.css lines 144-203) was MISSING in v3 → that's why mobile/tablet looked broken. Added `<style data-purpose="responsive-fix">` (37 rules, ≤768px tablet + ≤480px mobile, RTL/LTR aware): social bar 44→36→32px icons, QR hidden on ≤480px, section padding 48/32px, glass-panel padding, compact #langToggle, modal padding.
- ✅ User tested via DevTools (390×844 + 768×1024) and confirmed: **"ممتاز ظبطت"**.
- ✅ Added `docs/RESPONSIVE-TESTING.md` — quick mobile/tablet test method (F12 → Ctrl+Shift+M → presets).
- ✅ small_model switched: `opencodefree/deepseek-v4-flash-free` (429) → `opencode/mimo-v2.5-free` (works, no proxy needed).
- ⬜ NEXT: user "go" → security scan (rule 13) → push → test live on Vercel/Cloudflare (#8).

## Section 2026-09-13 (Model list filter + openrouter restore — DONE, verified)
- ✅ Added `disabled_providers` to global opencode.jsonc (12 providers without keys) → /models shrunk 576 → 43.
- ✅ **openrouter restored immediately** after user feedback: its `:free` models DO work without key (was the device default model). Now 414 models (371 openrouter incl. 23 `:free`).
- ✅ Verified keys untouched: `OPENROUTER_API_KEY` in User env (len 73) + `openrouter` in `%USERPROFILE%\.local\share\opencode\auth.json` + `{env:OPENROUTER_API_KEY}` intact in config line 69.
- ✅ Runtime check: `opencode run --model opencode/big-pickle` → replied OK (config valid, default model works).
- ✅ Hardware consult delivered (Qwen3-Coder-30B-A3B = the dependable local coding model; needs 24GB VRAM e.g. used RTX 3090 ~16-20k; economic 16GB option = Qwen3-Coder-14B) — awaiting user's final choice.

## Section 2026-09-13 (Free AI proxy providers — DONE, tested)
- ✅ Added free proxy providers to global opencode.jsonc: duckai (3000), opencodefree (6446), freellmpool (8080), freellmapi (3001, manual), freeinference + free models in groq/google/openrouter/nim/mistral/cerebras/sambanova/github-models.
- ✅ Created launcher `~/free-ai-proxies/start-proxies.ps1/.bat/.sh` (port checks, auto-install git-clone/zip, bun/uv/npm installs, logs) — UTF-8 BOM fixed for PS 5.1.
- ✅ Test results: duckai → geo-blocked (ECONNRESET, needs VPN); opencodefree → 429 rate-limit (temporary); freellmpool → Pollinations shared budget exhausted; mimo built-in remains the only practical free option. Documented in DECISIONS.md + LEARNING.md.

## Session 2026-09-13 (Supervisor bot — multi-model support DONE)
- ✅ Created `D:\ai\supervisor\` — Telegram remote-control bot for OpenCode across ALL projects.
- ✅ New bot via BotFather (token in supervisor/.env, ADMIN_ID=184519943, .gitignore protects secrets).
- ✅ projects.json: portfolio, winner-druge, ai-studio, lead-intel, lead-intel-v2, second-brain.
- ✅ Commands: /start /help /projects /models /task /status /log /cancel + voice messages (OGG→WAV→Google STT ar/en).
- ✅ Model selection: `/task <proj> model:<alias> <prompt>` + bare alias + voice ("portfolio model claude ...").
- ✅ MODEL_ALIASES: local qwen3/llama3 + OpenRouter gpt4o/gpt4/claude/claude35/claude3/gemini/deepseek/mistral.
- ✅ _run_task passes --model + provider keys (OPENROUTER/OPENAI/ANTHROPIC) as subprocess env; warns if key missing.
- ✅ Task notifications + /status + /log show the model used.
- ✅ Both bots RUNNING: portfolio bot (bot.py) + supervisor bot (PID 26468, polling 200 OK).
- ✅ qwen3 speed fix: created `qwen3-fast` (Modelfile: num_ctx 2048) — 8.4 → 17.9 tok/s on GTX 1660 Ti 6GB (was ~60s/reply with 40k ctx + thinking).
- ✅ Registered `qwen3-fast` in global opencode.jsonc ollama provider (tool_call:true, ctx 2k) + `fast` alias in supervisor bot.
- ⚠️ opencode+ollama local models still impractical: qwen3 unregistered→server error; registered→timeout (thinking per agentic step × slow tokens). Bot stays on mimo (cloud, fast, Arabic-capable).
- ⚠️ qwen3 Arabic quality is weak (answers English to Arabic prompts) — cloud models better for Arabic.
- ✅ Downloaded `qwen2.5-coder:1.5b` (986MB) — 73 tok/s direct API (4x qwen3-fast). Registered in opencode.jsonc + `coder` alias in bot.
- ⚠️ opencode+local still hangs even for 1.5b (weak tool-calling in small model + slow prefill on Ryzen 3750H). Direct `ollama run` is the fast path; bot tasks stay on mimo.
- ✅ FINAL DECISION: no more local model downloads — local models are NOT viable for coding with opencode. Local use = direct `ollama run qwen2.5-coder:1.5b` (quick Q&A/code only). opencode + supervisor bot = cloud only (mimo default, OpenRouter/Anthropic/OpenAI when keys added). Documented in DECISIONS.md.
- ✅ Chat with @mahmoudoc26_bot established (user pressed START, test message delivered MSG_ID=9).
- ⬜ User must /start the new bot (chat not found until first contact).
- ⬜ User must add API keys to supervisor/.env for cloud models (local qwen3:8b works now).
- ⬜ Long-term: run both bots as Windows services (die if PC off).

## Session 2026-09-10 (Versioning system — DONE)
- ✅ Created versions system: `versions/v1-2026-09-08/` (current design, full copy HTML+CSS+JS+assets) + `versions/v2-2026-09-10/` (new Google Stitch design, self-contained).
- ✅ Created VERSIONS.md — version registry with dates + 3 switching methods (manual copy, local preview, temp subpath deploy).
- ✅ v2 verified: 14 sections preserved, 208 data-en/data-ar pairs, langToggle present, balanced tags, self-contained JS (bilingual + FAQ + QR modal), Tailwind via CDN.
- ✅ v2 uses Obsidian dark + Gold premium theme, fonts Sora/Inter/Tajawal (better Arabic), QR modal instead of project modal.
- ✅ Stitch prompt saved at stitch_modern_animated_portfolio_redesign/STITCH-PROMPT.md.

## Session 2026-09-08 (Media buying learning — DONE)
- ✅ Created docs/marketing/PLAN-90DAYS.md (90-day marketing plan, Egypt + Gulf + USA).
- ✅ Created docs/marketing/MEDIA-BUYER-ROADMAP.md (5-phase learning roadmap).
- ✅ Created docs/marketing/Media-Buyer-Reference.docx — Word reference doc (49 paragraphs, 9 tables) that gets updated continuously; user says "حدّث المرجع" to update.
- ✅ User choosing strategy: learn media buying for self first → then sell as service. Budget: start small (100-150 EGP/day), scale 30-40% based on results.
- ✅ Mentoring Mode verified active (PROTOCOL.md Level 5 + build agent prompt + LEARNING.md auto-explain rule).

## Session 2026-09-08 (Web changes — DONE, committed & pushed to GitHub)
- ✅ Removed Knowledge Center section (all "Coming Soon") + all nav/footer/menu links to it.
- ✅ Moved social bar icons to left side (fixed left:14px instead of inset-inline-start).
- ✅ Unified language toggle: single button, text matches current language ("Change Language" / "تغيير اللغة"), removed langToggleMobile.
- ✅ Portfolio size reduced: 95KB → ~74KB, 15 sections → 14.
- ✅ Responsive CSS for whole page: hero text, grids, fonts, padding, cards, social bar, QR badge (tablet ≤768px / mobile ≤480px).
- ✅ Rebuilt css/style.css + committed + pushed to https://github.com/mahmoudrabeh-85/portfolio (commit 3f87440).

## Session 2026-09-08 (Marketing — DISCUSSED, not yet started)
- Decisions taken (awaiting execution tomorrow):
  - Targets: Egypt + Gulf + USA.
  - Channels: LinkedIn (all) + Facebook/TikTok/YouTube/Instagram/WhatsApp (Egypt) + Upwork (USA).
  - Affiliate marketing: wants all tracks (specialty + general products + mix).
  - LinkedIn URL: https://www.linkedin.com/in/mahmoud-rabeh-7102071a3
  - REAL number to use: monthly sales > 20M EGP (trading/distribution model).
  - Numbers NOT confirmed ($50M+, 500+ suppliers) → do NOT use.
  - Services prices: NOT shown in site/marketing — "negotiable, decided after discovery call".

## Session 2026-09-07 (Global setup — DONE)
- Added all 19 free OpenRouter models + openai/gpt-oss-120b/20b to global opencode.jsonc.
- Added session handover instructions + auto-create missing files to build agent prompt.
- Created PROGRESS.md, NEXT_STEPS.md, DECISIONS.md in D:\ai\portfolio.
- Created PROTOCOL.md + global LEARNING.md (cumulative memory).