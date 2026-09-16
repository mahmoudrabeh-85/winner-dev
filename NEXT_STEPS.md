# NEXT STEPS

## Today (2026-09-16) — Firecrawl MCP + Composio — RESTART opencode ⭐
- ✅ **مثبّتان**: `firecrawl` (remote — scrape/search/parse بلا مفتاح) + `composio` (remote — بوابة 1000+ تكامل) في `opencode.jsonc` — 12 خادماً (5 مفعّلة).
- ⬜ **أعد تشغيل opencode الآن** لتحميل الخادمين → ثم `opencode mcp auth composio` للمصادقة → جرّب: "ابحث في الويب عن..." (firecrawl) و"اربط Gmail" (composio).
- ⬜ اختياري لاحقاً: مفتاح `FIRECRAWL_API_KEY` (يفتح crawl/map/agent) — يُضاف في User env ثم header في الإعداد.

## Today (2026-09-16) — داشبورد job-hunt + تحسين سرعة الإقلاع — RESTART opencode ⭐
- ✅ **داشبورد موحد** `D:\ai\job-hunt\dashboard.html` — صفحة واحدة بـ 4 تبويبات (المحلل الذكي + تحليل الوظائف + SWOT + 130 وظيفة) via iframes + lazy loading. خادم ثابت على 8768 لخدمة ملفات data/.
- ✅ **صفحة إعدادات** `D:\ai\job-hunt\setup.html` — تظهر قبل النتائج: تحميل CV + LinkedIn + اختيار 8 مصادر + نوع العمل + 7 أسئلة تصفية + 4 deal breakers. تُحفظ في localStorage → dashboard.
- ✅ **تعطيل 5 خوادم MCP** (context7 + github + mcp-ui + magic-ui + shadcn-ui) → يبقى 3 (playwright + chrome-devtools + uiux-pro). قُتلت 12 عملية زومبي. GITHUB_TOKEN موجود فعلاً في env.
- ✅ **إصلاح الداشبورد** — إزالة `src=""` من iframes (كان يسبب تحميل الصفحة نفسها بدلاً من البيانات). كل 4 التبويبات تعمل الآن.
- ✅ **API تصفية جديد** `/api/search` — يقبل: source, work_type, min_score, q, skills, location, limit. أُضيف try/except + `dict(j)` لتحويل sqlite3.Row.
- ✅ **صفحة فلتر ذكية** `setup.html` — تحوّلت من صفحة إعدادات إلى فلتر + نتائج مباشرة (150 وظيفة مطابقة). أزرار تصنيف + بحث نصي + رابط العودة للداشبورد.
- ⬜ **أعد تشغيل opencode الآن** لتطبيق تعطيل MCP وتحسين الإقلاع.
- ⬜ المستخدم: إضافة Felix/Ultrawork/FreelanceUp إلى job-aggregator. شهادة Oracle SCM (ملغاة مؤقتاً — 2026-09-16). تنظيف ذاكرة completed projects.

## Today (2026-09-15) — أدوات التصميم جاهزة — RESTART opencode ⭐
- ✅ **14 مهارة تصميم** مثبتة في `C:\Users\RTX\.config\opencode\skills\selected\` (585KB) عبر `skills.paths` (9 من Google Stitch الرسمي + 5 Anti-slop).
- ✅ **MCP chrome-devtools (52K⭐) مُفعّل** + **ملف مرجعي** `C:\Users\RTX\.config\opencode\DESIGN-REFERENCES.md` في instructions.
- ✅ التحقق: 188/188 قوساً + `opencode run` ردّ "تمام".
- ⬜ **أعد تشغيل opencode الآن** لتحميل المهارات و MCP الجديد → ثم جربها: "صمم كارت خدمة بمعايير frontend-design".
- ⬜ **بانتظار المستخدم**: تفعيل Stitch MCP (`npx @_davideast/stitch-mcp init` — 10-15 دقيقة، يحتاج حساب Google Cloud).
- ⬜ **بانتظار المستخدم**: معاينة v4 والموافقة → انسخ → الجذر + فحص أمني → push.

## Today (2026-09-15/16) — MCP/UI-UX على المشاريع المنفذة — جاري الإغلاق
- ✅ **داشبورد المشاريع** (`D:\ai\tools\dashboard\generate_dashboard.py`) — يقرأ ملفات الذاكرة + فحص حي → dashboard.html بتصميم Industrial. 134 منجز، 53 معلّق، 4 نشطة.
- ✅ **CLI Launcher موحّد** — `cli_launcher.html` بهوية Industrial + dashboard card (22 أداة، 21/22 مثبتة).
- ✅ **job-hunt index.html** — تدقيق WCAG: `:focus-visible` + `prefers-reduced-motion` + back-to-top + modal scroll fix. أقواس 194/194.
- ⬜ **أعد تشغيل opencode الآن** لتحميل الـ 14 مهارة + chrome-devtools MCP.
- ⬜ المستخدم: إضافة Felix/Ultrawork/FreelanceUp إلى job-aggregator + شهادة Oracle SCM (ملغاة مؤقتاً) + تنظيف ذاكرة completed projects.

## Today (2026-09-15) — CLI Launcher v2: كل أداة بمجلدها + واجهة منفصلة (انتهت)
- ✅ **النقل**: كل ملفات الـ Launcher انتقلت من `D:\ai\portfolio\tools\` → **`D:\ai\tools\`** (أدوات النظام لا تنتمي لريبو الموقع العام) — `start_bots.vbs` حُدّث + الخادم يعمل من الموقع الجديد.
- ✅ **v2**: كل أداة لها **مجلدها الخاص** `D:\ai\tools\apps\<id>\app.json` (21 أداة) + **واجهة HTML مستقلة** `/app/<id>` (أوامر سريعة + تنفيذ بتقاط الناتج `/exec` + فتح طرفية `/run`).
- ✅ **مولّد مركزي**: `D:\ai\tools\make_apps.py` — إضافة أداة = مجلد + JSON فقط.
- ✅ **تحسينات**: أوامر `start` تعود فوراً + فحص Rust عبر `rustc` → كلها 21/21 مثبتة. مُختبَر بصرياً في المتصفح ✅
- ⬜ **المستخدم**: يكمل بروفايل LinkedIn (الخطوات 2-7 — 20 دقيقة) ثم ينشر المنشورات 10.
- ⬜ **المستخدم**: يراجع تقرير الوظائف ويرسل أفضل 3-5 وظائف يتقدم لها.

## Today (2026-09-13) — Subagents + memory updated, RESTART opencode
- ✅ **RESTART opencode now** to load the 3 new custom subagents (arabic/coder/fast) + GitHub MCP.
- ✅ After restart, test parallel agents: "أطلق coder و arabic في مهمتين متوازيتين".
- ⬜ USER works in `D:\ai\media-buying\` (LOCAL-ONLY, never push): configure LinkedIn (LINKEDIN-PROFILE-COPY.md → personal profile) → post the 10 posts → create social accounts per checklist.
- ⬜ MCP: playwright + context7 installed; github MCP needs the restart too (GITHUB_TOKEN set & verified).

## Today (2026-09-13) — Marketing files MOVED to private project
- ✅ **SPLIT COMPLETE**: all marketing/learning files moved to `D:\ai\media-buying\` (own AGENTS/PROGRESS/NEXT_STEPS/DECISIONS). Portfolio repo = site code only (`eeedd7f` pushed).

## Pending decisions from today (2026-09-13)
- ⬜ **Hardware decision**: user asked which dependable local coding model + required specs. Answer delivered (Qwen3-Coder-30B-A3B @ 24GB VRAM — used RTX 3090 best value ~16-20k EGP, total ~32-42k; or economic 16GB path = Qwen3-Coder-14B w/ RTX 4060 Ti ~24-28k). **Awaiting user's choice** between the two levels (or final build parts list).
- ⬜ **openrouter stays enabled** in opencode.jsonc (`disabled_providers` excludes it — its `:free` models work without key). When user adds keys for other providers, remove that provider from `disabled_providers` (comment in file explains).
- ✅ small_model switched to `opencode/mimo-v2.5-free` (user approved; old `opencodefree/deepseek-v4-flash-free` was 429 rate-limited).
- ✅ **v3 activated as active version** + responsive fixed + user-approved ("ممتاز ظبطت"). Test method saved in docs/RESPONSIVE-TESTING.md.
- ✅ **Deploy #8 COMPLETE**: security scan passed → pushed `30d4994` → **LIVE**: `https://mahmoudrabeh-85.github.io/winner-dev/` (GitHub Pages was already enabled; redirects `/portfolio.html`; verified v3+responsive-fix+assets 200). Optional: Vercel/Cloudflare Pages connection later for custom domain/branch previews.
- ✅ **Supervisor bot token was actually the one rotated** (not site bot) — new token in `supervisor/.env`, bot restarted (PID 3008), test msg delivered. Old site token in git history is 401/dead (cosmetic leftover) — optional git history cleanup later.

## Tomorrow (2026-09-14) — Resume Here ⭐
- الجلسة انتهت 2026-09-13 **بوضع "كل شيء مكتمل"** (user confirmed: "جرّبت البوت — كل شيء يعمل").
- ✅ **Smart-reply tests PASSED on user's phone**: مرحبا → greeting رد ترحيب؛ المشاريع → قائمة؛ اعرض هيكل المشروع في portfolio → task انطلق؛ رسالة صوتية → فهمت ونفذت. **المنطق الجديد مُختبَر 11/11 محلياً + فعلياً من الهاتف.**
- ✅ Supervisor bot: نسخة واحدة نظيفة (PID 2468) + توكن جديد `8703195403:AAF3Js3T...` + auto-start VBS في Startup.
- ⬜ USER (أي وقت): add API keys to supervisor/.env (OPENROUTER/OPENAI/ANTHROPIC) — optional, mimo works without them
- ⬜ USER: إعادة تسمية البوت عبر BotFather (Rabeh Consultant Bot) — 5 ثوانٍ
- ⬜ USER (اختياري): git history cleanup of dead 401 token from api/telegram.js — cosmetic, needs force-push + "go"
- ⬜ لاحقاً: حزمة التسويق (من قائمة مهام سابقة: LinkedIn/Facebook/affiliate/SEO)

## Today — Supervisor Bot (built, needs user actions)
- ✅ Supervisor bot built + running (D:\ai\supervisor\, PID 16696 → current PID 26468)
- ✅ /task with model: selection + voice tasks + notifications
- ✅ Chat with @mahmoudoc26_bot established (user pressed START, MSG_ID=9 delivered)
- ⬜ USER: add API keys to supervisor/.env (OPENROUTER/OPENAI/ANTHROPIC) — cloud models only; local models confirmed NOT viable for opencode
- ⬜ Test end-to-end: /projects → /models → /task portfolio اعرض هيكل المشروع → notification
- ⬜ Test voice task from phone
- ⬜ Long-term: both bots as Windows services (auto-start on boot)

## Today — Versioning System (awaiting decision)
- ✅ v1 archived (current design) — versions/v1-2026-09-08/
- ✅ v2 added (Google Stitch design) — versions/v2-2026-09-10/
- ✅ v3 added (Stitch + local images + Telegram bot) — versions/v3-2026-09-10/
- ✅ VERSIONS.md registry created with switching methods
- ✅ Telegram bot: @mahmoudagent26_bot (chat_id: 184519943)
- ✅ API endpoint: api/telegram.js (Vercel Serverless Function)
- ⬜ Review v3 locally (open versions/v3-2026-09-10/portfolio.html in browser)
- ⬜ DECISION: make v3 the active version? (if yes: copy its files to root + push)
- ⬜ If v3 goes live: test form submission end-to-end on Vercel
- ⬜ Rename bot via BotFather: /setname → "Rabeh Consultant Bot"

## Today — Media Buyer Learning (in progress)
- ✅ 90-day marketing plan (PLAN-90DAYS.md) — DONE
- ✅ Media buyer roadmap (MEDIA-BUYER-ROADMAP.md) — DONE
- ✅ Word reference doc (Media-Buyer-Reference.docx) — DONE, updates on "حدّث المرجع"
- ⬜ Practice: install Meta Business account + Pixel (step 1 of floor 3)
- ⬜ First real campaign with 100-150 EGP/day (after Pixel setup)

## Tomorrow — Marketing Package (awaiting approval to start)
1. Build 90-day marketing plan (Egypt + Gulf + USA, per-platform strategy).
2. Write LinkedIn posts (Arabic + English, ~10 posts) — configure profile first.
3. Write Facebook/Instagram/TikTok/YouTube content (Egypt).
4. Build affiliate roadmap (specialty + general products + mix, Egyptian networks: Noon/Jumia/Amazon).
5. SEO audit of portfolio.html: meta tags, JSON-LD (Person + Service), keywords, sitemap, robots.
6. Setup checklist file for accounts (LinkedIn, FB page, TikTok, YouTube, Instagram, WhatsApp Business, Upwork).

## Web (optional polish later)
- Test live deployment on Cloudflare Pages + Vercel after language-toggle changes.
- Verify language toggle works on mobile (single button visible).

## Completed This Session (2026-09-08)
- ✅ Created PLAN-90DAYS.md (90-day marketing plan)
- ✅ Created MEDIA-BUYER-ROADMAP.md (5-phase learning roadmap)
- ✅ Created Media-Buyer-Reference.docx (Word reference, updates on request)
- ✅ Removed Knowledge Center section (all "Coming Soon" items)
- ✅ Moved social bar icons to left side (left:14px fixed)
- ✅ Unified language toggle: single button "Change Language" / "تغيير اللغة" in nav
- ✅ Portfolio size reduced: 95KB → ~74KB, 15 sections → 14
- ✅ Removed pricing from services (negotiable only)
- ✅ Started marketing plan discussion (Egypt + Gulf + USA, LinkedIn-first, affiliate learning)

## Session 2026-09-07 (completed)