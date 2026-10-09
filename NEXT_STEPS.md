# NEXT STEPS

> 📦 **تنبيه الأرشفة (2026-10-09، الحل 1 للكومباكت)**: المهام القديمة (من «## DONE (2026-09-23)» فصاعداً) **نُقلت بلا حذف** إلى `NEXT_STEPS-ARCHIVE.md` — أقسام NOW الحالية وقائمة التفضيلات الحية تبقى هنا.

## NOW (2026-10-09) — حلول الكومباكت 1-4 مطبَّقة — أعد تشغيل OpenCode ⭐
- ✅ **الحلول الأربعة طُبِّقت فعلاً**: (1) أرشفة الذاكرة الأربعة بلا حذف + تحقق `ALL VERIFIED`، (2) `instructions` = 12 عنصراً، (3) `small_model`/`agent.arabic`/`build` ← `opencode/mimo-v2.6-flash-free`، (4) `tool_output.max_bytes = 20000`.
- ✅ **اختبار `provider.opencode` مغلق**: إدخال فارغ `{} يدمج` مع المورد المدمج (11 موديل) والمصادقة تعمل بلا `apiKey` → **حُذف الإدخال، لا حاجة له**.
- ✅ **أُعيد تشغيل OpenCode** (15:49) — كل التغييرات محمّلة (لا hot-reload).
- ⬜ **بانتظار قرارك**: (أ) حذف `D:\ai\portfolio\opencode.json` (إعداد مشروع قديم، 4 أسطر)، (ب) إقفال توثيق Kali Linux (مثبّت ومكتمل — أغلقه في `PROGRESS`؟)، (ج) نشر `winner-dev` (بانتظار «go» + فحص أمني).
- 📌 **الدروس 18-26 لم تعد في سياق LEARNING النشط** — تُقرأ من `LEARNING-ARCHIVE.md` أو `AGENT-REACH-REFERENCE.md` / `PROBLEM-SOLVING-PLAYBOOK.md`.

## NOW (2026-10-09) — إظهار سياق كل موديل في `/models` — أعد تشغيل OpenCode ⭐
- ✅ **طُبِّقت كل التعديلات فعلياً** في `C:\Users\RTX\.config\opencode\opencode.jsonc` — دُمج حجم السياق داخل حقل `name` لكل موديل دون تغيير أي معرّف `model` (التحقق: `VALID JSONC` + **51 موديل بـ`name` + 29 بلا `name`** — كلها مقصودة).
- ✅ **مزامنة المرآة مُقفلة (2026-10-09)**: `SRC(normalized CR->LF) == MIR: True` — الفرق الوحيد كان CR منفردين في المصدر تحوّلا إلى LF في المرآة (الطول متطابق 124247 بايت، والمحتوى متكافئ)؛ قِسم 2026-10-09 هو الأخير في المرآة (السطر 806–822)؛ حُذفت السكربتات المؤقتة الثلاثة (`check_learning.py`، `find_cjk.py`، `verify_mirror.py`) وتأكّد غيابها.
- ⬜ **الخطوة الوحيدة المطلوبة منك**: **أعد تشغيل OpenCode** — الإعداد يُحمَّل عند الإقلاع فقط (لا hot-reload). ستظهر عندك أمثلة: `Kimi K3 (200k)`، `nemotron-3-ultra-550b-a55b:free (1M)`، `DeepSeek V4 Flash (128k, free)`.
- 📌 **قاعدة الصياغة المتبعة**: `ctx >= 1_000_000` → `"1M"`، وإلا `round(ctx/1000) + "k"` (262144→262k، 131072→131k، 65536→66k). المصدر: `limit.context` في الإعداد أو `openrouter.ai/api/v1/models` — **لا تخمين**.
- ⚠️ **7 موديلات OpenRouter بلا سياق موثّق** (alias `openrouter/free` + 6 معرّفات أكد API غيابها: minimax-m3، minimax-m2.7، ling-3.0-flash-fin، ling-3.0-flash-sante، glm-5.2، deepseek-v4-flash) — **تُركت `{}`** بلا اسم التزاماً بقاعدة عدم التخمين.
- ⚠️ **مستثناة بلا تخمين أيضاً**: `lmstudio` (4 موديلات) + `ollama/gemma4:31b-cloud` — بلا مصدر سياق موثّق فبقيت `{}`.

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
