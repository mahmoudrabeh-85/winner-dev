# NEXT STEPS

> 📦 **تنبيه الأرشفة (2026-10-09، الحل 1 للكومباكت)**: المهام القديمة (من «## DONE (2026-09-23)» فصاعداً) **نُقلت بلا حذف** إلى `NEXT_STEPS-ARCHIVE.md` — أقسام NOW الحالية وقائمة التفضيلات الحية تبقى هنا.

## NOW (2026-10-18) — نُشر على main (0bc0b38) ✅
- ✅ **الفرع والライブ**: commit `0bc0b38` مرفوع — الحي محدث على GitHub Pages (`Content-Length: 156607`) + Vercel (`Age: 0`)
- ✅ **رسالة تيليجرام**: أُرسلت للرابط الحي عبر @mahmoudoc26_bot (`message_id: 141`)

## NOW (2026-10-18) — صفحة التطبيقات حيّة + متجاوبة ✅
- ✅ **apps.html مرفوع**: commit `6fcdd02` — حيّ على GitHub Pages + Vercel + Cloudflare (`/apps.html`) + متجاوب (0 فيضان).
- ✅ **رسالة تيليجرام**: أُرسلت رسالة الإصلاح (`message_id: 144`).
- ⬜ **بانتظارك**: (1) تدوير توكن البوت في `73d1949` عبر BotFather، (2) قرار تنظيف سجل git، (3) تشغيل `cleanup-opencode-db.bat`.
- ⬜ **مؤجَّل**: زر `apps.html` الفاتح (تباين 2.81:1) · ثيمات فاتحة لـ4 تطبيقات · رفع `vercel.json`+`.vercelignore`.

## NOW (2026-10-11) — منشور وحيّ (ad84566) — المتبقي تدوير التوكن وتنظيف القاعدة ⭐
- ✅ **منشور ومتحقق (2026-10-10، بعد «go»)**: commit `ad84566` على `main` — إصلاح honeypot (11398px←1521) + فحمي `#1B2440` + قائمة موبايل — حيّ (E1-E3).
- ⬜ **بانتظارك**: (1) تدوير توكن البوت المكشوف في `73d1949` عبر BotFather، (2) قرار تنظيف سجل git، (3) تشغيل `cleanup-opencode-db.bat` (القاعدة 2.08GB).
- 📌 **لا عمل كود معلق** — أي مهمة قادمة تبدأ من هنا.

## NOW (2026-10-09) — حلول الكومباكت 1-4 مطبَّقة — أعد تشغيل OpenCode ⭐
- ✅ **الحلول الأربعة طُبِّقت فعلاً**: (1) أرشفة الذاكرة الأربعة بلا حذف + تحقق `ALL VERIFIED`، (2) `instructions` = 12 عنصراً، (3) `small_model`/`agent.arabic`/`build` ← `opencode/mimo-v2.6-flash-free`، (4) `tool_output.max_bytes = 20000`.
- ✅ **اختبار `provider.opencode` مغلق**: إدخال فارغ `{} يدمج` مع المورد المدمج (11 موديل) والمصادقة تعمل بلا `apiKey` → **حُذف الإدخال، لا حاجة له**.
- ✅ **أُعيد تشغيل OpenCode** (15:49) — كل التغييرات محمّلة (لا hot-reload).
- ✅ **اكتمل الثلاث (2026-10-09)**: (أ) حُذف `D:\ai\portfolio\opencode.json` ✅، (ب) أُقفل توثيق Kali Linux في `PROGRESS` ✅، (ج) **نُشر winner-dev** — commit `70f52a4` على `main` + تحقّق حيّ (E1-E3 + honeypot) ✅.
- 📌 **الدروس 18-26 لم تعد في سياق LEARNING النشط** — تُقرأ من `LEARNING-ARCHIVE.md` أو `AGENT-REACH-REFERENCE.md` / `PROBLEM-SOLVING-PLAYBOOK.md`.

## NOW (2026-10-09) — تقصير أسماء النماذج + تصغير خط Windows Terminal — أعد تشغيل OpenCode ⭐
- ✅ **تقصير الأسماء منجَز**: استبدال `img, think` → `i, t` و `, img)` → `, i)` و `, think)` → `, t)` في `opencode.jsonc` — 66 موديلاً. مثال: `Exo Free (1M, i, t)`.
- ✅ **تصغير الخط منجَز**: `"fontSize": 8` في `profiles.defaults` بملف `settings.json` الخاص بـ Windows Terminal.
- ✅ **التحقق**: JSONC سليم + CLI يعرض الأسماء الجديدة. نسخة احتياطية: `opencode.jsonc.bak-shortnames`.
- ⬜ **الخطوة الوحيدة المطلوبة منك**: **أعد تشغيل OpenCode** — الإعداد يُحمَّل عند الإقلاع فقط (لا hot-reload). ستظهر أمثلة: `Exo Free (1M, i, t)`، `Kimi K3 (1M, i, t)`، `Big Pickle (200k, t)`.
- 📌 **قاعدة الصياغة**: `ctx >= 1_000_000` → `"1M"`، وإلا `round(ctx/1000) + "k"`، والوسوم المختصرة بعد السياق داخل القوس: `i` = img، `t` = think. **لا وسم `web`**.
- 📌 **ملاحظة**: `deepseek-flash` و`deepseek-v4-pro` (مكتشفان من API) بلا سياق في الاسم — بطاقة V4 الرسمية تقول 1M لكن المعرّف المعلن V4.1 ← وسوم فقط حتى مصدر موثّق لـV4.1.
- ✅ **مزامنة المرآة مُقفلة (2026-10-09)**: `SRC(normalized CR->LF) == MIR: True` (الطول 124247 بايت كلاهما).

## NOW (2026-10-07) — قرار أدوات «وصول الإنترنت» ⭐
- ⛔ **لا تثبّت Agent-Reach كاملاً** — 73% من منصاته صينية، وOpenCLI = Node + متصفح على جهاز يعاني ضغط ذاكرة موثّق.
- ⬜ **الخيار 1 (الموصى به): لا شيء** — أنت تملك Firecrawl + Composio + vidscribe = تغطية 70%+ مجاناً.
- ⬜ **الخيار 2 (خفيف):** `winget install GitHub.cli` — يفتح قناة GitHub كاملة بلا أي ثقل إضافي.
- ⬜ **الخيار 3 (عند طلب Twitter/Reddit فعلاً):** `npm install -g opencli` فقط — بلا طبقة التوجيه.
- 📌 **الملف المرجعي:** `C:\Users\RTX\.config\opencode\AGENT-REACH-REFERENCE.md` (كل الروابط + الأرقام + ما لديك + الفجوة + 4 سيناريوهات جاهزة).
- 📌 **قاعدة 19 الجديدة:** رابط `mcporter` في README ذلك المشروع يشير لـ Fork بـ 4 نجوم — افحص حقل `parent` في GitHub API قبل أي رابط من README.
- ✅ **تم 2026-10-07:** الملفان (`AGENT-REACH-REFERENCE.md` + `AGENT-REACH-PREFERENCES.md`) منسوخان إلى `~/.config/opencode/` **ومضافان إلى `instructions`** (17 ملفاً) — الترتيب: PREFERENCES قبل REFERENCE. الكلفة 30.4KB لكل جلسة. ⛔ **يلزم إعادة تشغيل opencode** لتفعيل التحميل.
- ✅ **تصحيح 2026-10-07 (المهم):** Reddit **ليس** بلا pathway مجاني. القياس الأوسع كشف **`arctic-shift.photon-reddit.com`** و**`api.fxtwitter.com`** — كلاهما يعمل **بلا حساب ولا Cookie**. التُفِّا في `D:\ai\tools\web-read.py`. **لن تحتاج حساباً ثانوياً لما هو مُغطّى الآن.** ومثلها `gh` CLI 2.102.0 مثبّت.
- ⚠️ **ما زال ينقص فعلاً:** **بحث Twitter/X** (لا مجاني — $200/شهر للـ API) و**تايم‌لاين** (syndication = 429) و**تعليقات Reddit** (الأرشيف لا يوفّرها). للحاجة الحقيقية لهذه الثلاثة: حساب ثانوي + OpenCLI.
- 📌 **قاعدة 25 (الأهم في هذه الجلسة):** الحكم العمومي السلبي («X غير موجود / لا حل») يحتاج **بحثاً** لا N محاولات فاشلة. 3 فشل يثبتون فشل 3 أشياء فقط ولا يثبتون شيئاً عن الرابعة.

## NOW (2026-10-07) — تثبيت أداة Android بعد موافقتك ⭐
- ⬜ **1) ثبّت `agent-device`**: `npm install -g agent-device@latest` ثم `agent-device doctor` (يتطلب Node 22.12+ وعندنا 24.15 ✓). **أخبرني «ثبّت» لأنفّذه**.
- ⬜ **2) ثم أضيفه في `opencode.jsonc`** بـ `"enabled": false` ← تعيد تشغيل opencode ← تختبره ← عندها نفعّله.
- ⬜ **3) اختياري لمشروع `winner-parental-control` فقط**: `@us-all/android-mcp` (76 أداة + 5 prompts تشخيص: `crash-investigation`, `memory-leak-detection`, `app-startup-profile`).
- 📌 **لا تثبّت ثالثاً** — 3 خوادم MCP = ثقل إقلاع (درس 2026-09-16: إبطاء ~27 ث).
- 📌 **الملف المرجعي**: `C:\Users\RTX\.config\opencode\ANDROID-TOOLS-REFERENCE.md` (TOP 4 + 9 مرفوضات بسببها).

## NOW (2026-10-07) — إنهاء علاج تجميد شاشة OpenCode ⭐
- ⬜ **خطوة واحدة منك**: أغلق OpenCode ← شغّل `C:\Users\RTX\Desktop\cleanup-opencode-db.bat` ← انتظر 2-5 دقائق. النتيجة المتوقعة: القاعدة من 2.08GB إلى ≈ 400MB، والنسخة الاحتياطية في `~\.local\share\opencode\_backup\`.
- ✅ **تم بالفعل**: قتل 27 عملية MCP يتيمة (تحرير 1.61GB) + قمع تجمّد System UI في المحاكي + حارس تنظيف تلقائي عند كل تسجيل دخول.
- 📌 **لمنع التكرار**: ابدأ جلسة جديدة كل ~500 رسالة (الجلسات الضخمة هي السبب)، أو أعد تشغيل السكربت كل شهرين.
- 📌 **موفّر إضافي**: إغلاق محاكي Android يوفّر ~3.5GB من الذاكرة (قيمة `qemu-system-x86_64`).
- ⛔ **لا تحاول `schtasks`/`Register-ScheduledTask`** — يرفض بـ Access denied بلا صلاحيات مسؤول. الحل المعتمد هو ملف VBS في مجلد Startup.

## DONE (2026-10-06) — قالب Fullstack ⭐
- ✅ **43 ملفاً في 4 فئات** — `fullstack\react-express-mono` جديد ومُختبَر بالكامل (install + build + CRUD حيّ + proxy) — النظام مكتمل الآن.
- 📌 **أقصر مسار لمشروع جديد**: `cp -r templates\fullstack\react-express-mono my-app` → `npm install` → `npm run dev` → `localhost:5173`.
- ⬜ (اختياري) قالب fullstack ثانٍ `react-fastapi` لمحبي Python.

## DONE (2026-10-06) — نظام القوالب + فحص APIs ⭐
- ✅ **28 قالباً جاهزاً** في `D:\ai\MY-PREFERENCES\templates\` (React+shadcn / UX / Backend FastAPI+Express / عقود API / مخطط DB) — **مُختبرة بالكامل**: build ناجح + CRUD حيّ.
- ✅ **كل الـ APIs تعمل** (OpenRouter + Ollama + Composio + Firecrawl + الخوادم المحلية) — تقرير «الخطأ → الإصلاح» مُسلَّم.
- ✅ **MCP `shadcn-ui-local`** يعمل بعد إعادة التشغيل (قوالب موارده ظاهرة).
- 📌 **كيف تستخدم القوالب**: افتح `templates\README.md` → جدول القرار → انسخ للمشروع → اتبع السلاسلة الذهبية (contract → schema → backend → frontend → UX audit → نشر).

## قائمة دائمة (2026-09-27) — ملفات التفضيلات الحية ⭐
- 📌 **فوراً عند أي تفضيل جديد**: سجّله في `D:\ai\MY-PREFERENCES\MY-PREFERENCES.md` (تفضيلات عامة + خاصة) — لا تنتظر نهاية الجلسة.
- 📌 **نهاية كل جلسة**: حدّث `C:\Users\RTX\.config\opencode\LEARNING.md` (المصدر) أولاً ثم أعد نسخه إلى `D:\ai\MY-PREFERENCES\LEARNING.md` (مزامنة المرآة بـ Copy-Item + التحقق SHA256).
- 📌 **اقرأ الملفين في بداية أي جلسة** في هذا المشروع أو غيره (MY-PREFERENCES = تطبيق، LEARNING = دروس).
