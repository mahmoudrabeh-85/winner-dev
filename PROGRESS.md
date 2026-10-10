# PROGRESS

> 📦 **تنبيه الأرشفة (2026-10-09، الحل 1 للكومباكت)**: الأقسام القديمة (من «## Section 2026-10-06» فصاعداً) **نُقلت بلا حذف** إلى `PROGRESS-ARCHIVE.md` — هذا الملف يحتفظ بالأقسام الحديثة فقط (2026-10-09 وما قبلها في الأعلى).

## Section 2026-10-09 (توحيد الألوان على الفحمي + قائمة موبايل + إصلاحات responsive) ⭐
- ✅ **الخلفية**: `#0B0F17` ← `#3B4763` ← `#333F59` ← `#2B354D` ← `#252F47` ← `#202A42` ← **`#1B2440`** (درجة جديدة `obsidian-500` في اللوحة) — 6 تكرارات بتوجيه المستخدم حتى الرضا.
- ✅ **التناسق**: رُفعت كل الأسطح (بطاقات زجاجية 72 + أشرطة أقسام 5+1 + هيدر + حقول + رقائق + فوتر + تدرج البطل + تراكبه) من 900/950 إلى عائلة 600/700 — لا أسود فاحم إلا فوق الصور. خُفّض تعتيم صورة الخلفية (0.50→0.22 ديسكتوب).
- ✅ **قائمة الموبايل**: زر hamburger (`lg:hidden`) + لوحة روابط sticky (8 روابط بنفس `data-ar/data-en` ليعمل مبدّل اللغة) + JS فتح/إغلاق تلقائي عند النقر. صياغة JS مُتحقق `node --check` ✅.
- ✅ **responsive إضافي**: عدّادات `text-4xl` ← `text-3xl sm:text-4xl` (4) + إخفاء الشريط الاجتماعي العائم تحت 480px (كان يغطي المحتوى — نفس نهج `qr-float` القائم).
- ✅ **التحقق الستاتيكي (12/12)**: زر/لوحة/JS/روابط8/عدّادات/إخفاء/خلفية/توازن p,a,header,button.
- ✅ **التحقق الحي مكتمل (2026-10-10، عادت أدوات المتصفح)**: إصلاح الـ honeypot مؤكد — `scrollWidth` ديسكتوب 1521 ≤ 1536 (كان 11398) · موبايل 390px: 375 ≤ 390 · تابلت 768: 753 ≤ 768 · C1 لقطات (ديسكتوب/موبايل/تابلت/قائمة مفتوحة) بلا بقعة بيضاء وألوان متناسقة · C2 صفر أخطاء كونسول · C4 رحلة كاملة: منع الإرسال الفارغ + إرسال صالح فتح تيليجرام بالبيانات الصحيحة والـ honeypot فارغ · C6 المقاسات الثلاثة سليمة.
- ✅ **D2 حي**: `/.git/config` و`/.env` على `mahmoudrabeh.vercel.app` = 404 (الـ 200 كان على خادم المعاينة المؤقت فقط — أُوقف).
- ⚠️ **D4 كشف سراً في السجل القديم**: commit `73d1949` يحوي توكن بوت تيليجرام في `api/telegram.js` — **محذوف من HEAD الحالية** (git grep على HEAD = صفر) لكنه باقٍ في السجل. يتطلب: تدوير التوكن عبر BotFather + قرار تنظيف السجل. **لم يُرفع شيء بعد — بانتظار «go»**.

## Section 2026-10-09 (إصلاح التوسع الأفقي 11398px — honeypot كان يكسر الموبايل) ⭐
- ✅ **البلاغ**: بقعة بيضاء على الديسكتوب + الموقع لا يملأ الشاشة على الموبايل (المحتوى محشور يميناً مع فراغ أسود يساراً) — النسخة الحية `mahmoudrabeh.vercel.app`.
- ✅ **السبب الجذري (مقاس بـ Playwright)**: حقل honeypot للسبام بـ `position:absolute;left:-9999px` وسّع المستند إلى **11398px** (الشاشة 1536px). في RTL التوسع يمتد يساراً ⇒ الموبايل يعرض شريحة يمينية فقط + فراغ أسود، والديسكتوب يظهر مناطق فارغة/بيضاء + تمرير أفقي.
- ✅ **الإصلاح**: `position:fixed;top:0;left:0;width:1px;height:1px;opacity:0;pointer-events:none` — الـ fixed لا يؤثر على `scrollWidth` إطلاقاً. تحقق ستاتيكي: لا `-9999` متبقية + العنصران الزخرفيان (`-left-40`/`-right-40`) داخل آباء `overflow-hidden`.
- ✅ **فحوص TESTING الافتراضية (جزئية)**: A2 متوازن فعلياً (p:100/100، a:22/22 — سكربت الفحص الأول كان معطوباً والعد المباشر أثبت التوازن) · D1 بلا أسرار · D3 حالة git سليمة.
- ⬜ **مؤجَّل (أدوات المتصفح غير متاحة هذه الجلسة)**: C1/C2/C6 — إعادة القياس الحي (`scrollWidth` + لقطة موبايل 390px) + اختبار النموذج (C4) قبل أي رفع. **لم يُرفع شيء بعد**.
- 📌 **فجوة UX منفصلة**: لا توجد قائمة موبايل (الـ nav مخفي تحت `lg` بلا hamburger) — التنقل غير متاح على الهاتف. تُنفَّذ كخطوة تالية بعد تأكيد الإصلاح.

## Section 2026-10-09 (تقصير أسماء النماذج + تصغير خط Windows Terminal) ⭐
- ✅ **المشكلة**: أسماء النماذج الطويلة (`Exo Free (1M, img, think)`) تظهر مقطوعة في قائمة `/models` + حجم الخط الافتراضي كبير.
- ✅ **الحل الأول — تصغير الخط**: إضافة `"fontSize": 8` في `profiles.defaults` بملف `settings.json` الخاص بـ Windows Terminal. ينعكس فوراً على OpenCode.
- ✅ **الحل الثاني — تقصير الأسماء**: استبدال `img, think` → `i, t` و `, img)` → `, i)` و `, think)` → `, t)` في `opencode.jsonc` — 66 موديلاً. مثال: `Exo Free (1M, img, think)` → `Exo Free (1M, i, t)`.
- ✅ **التحقق**: JSONC سليم + CLI يعرض الأسماء الجديدة. نسخة احتياطية: `opencode.jsonc.bak-shortnames`.
- ⬜ **يتطلب إعادة تشغيل OpenCode** لرؤية النتيجة في الواجهة.

## Section 2026-10-09 (وسوم القدرات img/think في أسماء الموديلات) ⭐
- ✅ **المهمة**: المستخدم طلب إظهار حدود الكونتكست + الرؤية + التفكير + البحث بجوار كل اسم موديل في `/models` (بلا تخمين — مصدر موثّق فقط).
- ✅ **التنفيذ** في `opencode.jsonc`: **65 موديلاً باسم + 50 منها موسومة** `img`/`think` + 28 بلا اسم (معتمدة عمداً). الوسم داخل القوس القائم: `(128k, img, think)` — بلا وسم `web` إطلاقاً (لا خاصية بحث على مستوى الموديل في أي مصدر؛ websearch = أداة متاحة للأدوات toolcall فعلاً لكنها ليست خاصية موديل تُوسَّم).
- ✅ **مصادر القدرات (رسمية)**: Zen 11 من `opencode models opencode --verbose` (حقل `capabilities.input.image` + `reasoning`) · OpenRouter من `openrouter.ai/api/v1/models` · Ollama من `ollama show` · DuckAI/DeepSeek/Kimi/GLM من وثائق المورّدين (api-docs.deepseek.com/vision + HF model card + NVIDIA NIM).
- ✅ **كتلة `"opencode"` جديدة** (11 موديلاً، name فقط + limit مدمج): أول اختبار فعلي لإضافة مورد مدمج بالكامل — الدمج يعمل (built-in تبقى وتُطبَّق الأسماء).
- ✅ **تصحيحات قياس Ollama**: 9 موديلات سياقها القديم في الإعداد كان مخالفاً لـ`ollama show` (qwen3-fast 2k→40k، llama-3.1-8b 8k→131k، إلخ) + اسم `gemma4:31b-cloud` الجديد (262k, img, think).
- ✅ **تصحيحات بعد التحقق**: إزالة `img` من `Mistral-Small-24B-Instruct-2501` (2501 = نصّي، الرؤية أُضيفت في 3.1/2503 — دليل Mistral الرسمي) ومن `deepseek-chat/reasoner` (الدليل يوثّق `deepseek-flash` فقط) — الوسم الصحيح = دليل موثّق لا استنتاج عائلي.
- ✅ **الموديلان المكتشفان من API** أُضيف لهما اسم: `deepseek-flash` → «DeepSeek V4.1 Flash (img, think)» و`deepseek-v4-pro` → «DeepSeek V4 Pro (think)» — **وسوم فقط بلا سياق** (بطاقة الرسمية تغطي V4 لا V4.1).
- ✅ **التحقق**: JSONC سليم (255 أقواس متطابقة) + `opencode models opencode/deepseek/ollama --verbose` تُظهر الأسماء الجديدة فعلاً. نسخة احتياطية: `opencode.jsonc.bak-caps-2026-10-09`.
- ⬜ **يبقى: إعادة تشغيل OpenCode** لرؤية كل الأسماء في `/models` (الإعداد يُحمَّل عند الإقلاع فقط).

## Section 2026-10-09 (حلول الكومباكت 1-4 + اختبار `provider.opencode`) ⭐
- ✅ **الحل 1 (الأرشفة — نقل لا حذف، «دون كسر أي شيء»)**: 4 ملفات ذاكرة قُسّمت عند حدود مقيسة وأُنشئت لها أرشيفات: `LEARNING-ARCHIVE.md` (557 سطراً) + `PROGRESS-ARCHIVE.md` (232) + `DECISIONS-ARCHIVE.md` (63) + `NEXT_STEPS-ARCHIVE.md` (171). المحتفظ: LEARNING = 1-246 + **804-824 (جلسة اليوم كاملة)**، PROGRESS = 1-58، DECISIONS = 1-11، NEXT_STEPS = 1-52 (NOW الحالية).
- ✅ **التحقق الشامل `ALL VERIFIED`**: جسم كل أرشيف = الشريحة الأصلية حرفياً؛ المحتفظ = الأصلي − المنقول + سطور الإشارة فقط (PEEK)؛ لا نمو لتلوّث CJK/Cyrillic/FFFD. نسخ `.bak` الأربعة محفوظة في `%TEMP%\opencode\`.
- ✅ **سطور إشارة عربية** أُضيفت أعلى الأرشفات الأربعة + ملاحظة داخل جلسة 2026-10-09 في LEARNING بأن **الدروس 18-26 صارت في `LEARNING-ARCHIVE.md`**.
- ✅ **مرآة `MY-PREFERENCES` مُزامنة byte-for-byte**: SHA256 متطابق للملفين (LEARNING.md + LEARNING-ARCHIVE.md).
- ✅ **الحل 2**: `instructions` من 18 إلى **12 عنصراً** (إخراج WORK-INDEX/HARNESS_* ×3/AGENT-REACH ×2/`harness/README` — تُفتح عند الحاجة).
- ✅ **الحل 3**: `small_model` + `agent.arabic.model` + موكّل `build` ← **`opencode/mimo-v2.6-flash-free`** (الأفضل عربياً).
- ✅ **الحل 4**: `"tool_output": { "max_bytes": 20000 }` أعلى المستوى (قمع ناتج الأدوات العملاق).
- ✅ **اختبار `provider.opencode` (المعلّق)**: إدخال فارغ صريح `"opencode": {}` **يدمج ولا يستبدل** — `opencode models opencode` أعاد نفس الـ11 موديلاً، واستدعاء حيّ `opencode run --model opencode/mimo-v2.6-flash-free` رد `OK` بلا `apiKey` (المصادقة من `auth.json`). **حُذف الإدخال بعد الاختبار** (لا فائدة منه). الدرس: اختبار الإعداد ممكن من خارج الجلسة عبر CLI.
- ✅ **أُعيد تشغيل OpenCode** (2026-10-09، 15:49 — سجل `opencode_restart.log`: RELAUNCHED/DONE) — كل التغييرات محمّلة الآن.
- ✅ **نُشر winner-dev** (2026-10-09، commit `70f52a4` على `main`): قسم «أدوات بنيتها» (6 أدوات + 3 صور في `assets/tools/`) + honeypot لنموذج التواصل (D6) + الأرشيفات الثلاثة + `INDEX.md`/`TESTING.md` + حذف `opencode.json`. **التحقق الحيّ**: الصفحة 200 · `ToolkitSection` ورابط التنقل نشطان · الصور الثلاث 200 · honeypot ظاهر. المستبعد عمداً: `_diag.html` + `vercel.json` + لقطات التطوير (بلا رفع).

## Section 2026-10-09 (إظهار سياق كل موديل في `/models` عبر حقل `name`) ⭐
- ✅ **الهدف المُنجز**: جعل حجم «الكونتكست» يظهر بجوار اسم كل موديل في قائمة `/models` — التنفيذ بتضمين القيمة داخل حقل العرض `name` في `C:\Users\RTX\.config\opencode\opencode.jsonc` **دون تغيير أي معرّف `model`** (التزاماً بقاعدة الدقة).
- ✅ **الآلية المؤكدة (مهارة `customize-opencode`)**: قائمة `/models` تعرض حقل `name` فقط ولا تعرض `limit.context`؛ إضافة الحقل لا تعني تغيير المعرّف. الإعداد يُحمَّل عند الإقلاع فقط ⇒ **لا hot-reload** ⇒ يجب إعادة تشغيل OpenCode لرؤية النتيجة.
- ✅ **قرار الصيغة**: للموديلات التي تملك `name` أصلاً → دمج السياق داخل الأقواس الحالية، مثال: `DeepSeek V4 Flash (128k, free)` و`Qwen2.5 0.5B (fast, 16k)`. للموديلات بلا `name` → تعيين `name = "<model-id> (<ctx>)"` لإبقاء المعرّف + السياق. **قاعدة الصياغة**: `ctx >= 1_000_000` → `"1M"`، وإلا `round(ctx/1000) + "k"` (262144→262k، 131072→131k، 65536→66k).
- ✅ **المصدر الوحيد للقيم**: `limit.context` في الإعداد أو `openrouter.ai/api/v1/models` — **لا تخمين** لأي قيمة غير موثّقة.
- ✅ **كل التعديلات طُبِّقت فعلياً**: openrouter (18 موديل موثّق) + duckai (6) + freellmapi inline (4) + opencodefree (5) + freellmpool (5) + deepseek (2) + kimi (2) + ollama (إلحاق 5 + تسمية 2). الموفّر المدمج `opencode` لم يُعدّل.
- ✅ **التحقق نجح**: بارسر JSONC يحترم السلاسل → `VALID JSONC`؛ النتيجة **51 موديل بـ`name` + 29 بلا `name`** (كلها مقصودة). حُذف السكربت المؤقت بعد التحقق.
- 📌 **الـ29 بلا اسم (مقصودة)**: openrouter(7 = alias free + 6 معرّفات أكد API غيابها) · lmstudio(4) · ollama/gemma4:31b-cloud(1) · والبقية موفّرون معطّلون لا يظهرون في `/models` (google 4 + groq 3 + cerebras 2 + nim 1 + aiand 7).
- ✅ **مرآة LEARNING مُقفلة**: `SRC(normalized CR->LF) == MIR: True` (الطول 124247 بايت كلاهما؛ الفارق كان CR منفردَين في المصدر فقط طُبِّعا إلى LF) — أُضيف درس «تطبيع نهايات الأسطر» إلى اللفين معاً، وحُذفت السكربتات المؤقتة الثلاثة (`check_learning.py`، `find_cjk.py`، `verify_mirror.py`) وتأكّد غيابها.
- ⬜ **الخطوة المتبقية**: **أعد تشغيل OpenCode** لرؤية السياق بجوار الأسماء (مثال: `Kimi K3 (200k)`، `nemotron-3-ultra-550b-a55b:free (1M)`).

## Section 2026-10-09 (Kali Linux على WSL 2 — مُثبَّت بالكامل + دروس) ⭐
- ✅ **Kali GNU/Linux Rolling 2026.2** مثبّت عبر `wsl --install kali-linux` (WSL 2، الافتراضي `docker-desktop` ما زال موجوداً). التثبيت تجاوز مهلة 600 ثانية لكنه نجح في الخلفية — التحقق الحقيقي بـ `wsl -d kali-linux echo ALIVE` + `cat /etc/os-release` وليس بانتهاء الأوامر.
- ✅ **مستخدم UNIX أُنشئ**: `mahmoud` (أُجري عبر أول تشغيل). طول الاسم ≤ 32 بايت؛ لا تُلصق أوامر في `Enter new UNIX username:`.
- ✅ **تمييز البيئتين حُسم**: سطر يبدأ بـ `PS` = أوامر ويندوز؛ سطر `┌──(mahmoud㉿...)` = أوامر Kali. خلط الأمرين سبّب خطأين متتاليين (`sudo` مرفوض من ويندوز + أمر مكرر أوّل مرتين).
- ✅ **أزمة المرايا حُلّت** (2G تحميل): (1) `IPv6 unreachable` → ملف `/etc/apt/apt.conf.d/99force-ipv4` بقيمة `Acquire::ForceIPv4 "true";`؛ (2) مرآتا `mirror1.sox.rs` و`mirrors.netix.net` ميتتان → الفحص بـ `curl -sI` كشف أن `mirrors.ocf.berkeley.edu` تعطي `200` بينما `mirror.fcix.net` و`mirror.kumi.systems` لا تدعمان `kali-last-snapshot` (404)؛ (3) **الملف الصحيح للمرآة هو `/etc/apt/sources.list.d/kali.sources` (بصيغة deb822) لا `sources.list`** — أمر `sed` على `sources.list` لم يؤثر إطلاقاً.
- ✅ **`DNS` نطاقي محجوب**: ملقم WSL `10.255.255.254` لا يحل `mirrors.wikimedia.org` (NXDOMAIN) رغم ضبط ForceIPv4 — فحص `nslookup` لكل مرشح قبل اعتماده.
- ✅ **`kali-linux-default` (~2GB) ثبّت كاملاً** بعد اختيارات إعداد: لوحة مفاتيح `English (US)`، `macchanger=No`، `kismet setuid=No`، `wireshark dumpcap=No`، `sslh=standalone`. الترقية الأمنية `apt upgrade` مكتملة + `autoremove` حرّر 74MB.
- ✅ **درس الإعدادات المؤكدة**: نافذة السؤال (`Yes/No`) خلال التثبيت تُجاب بـ `No` دائماً في WSL (لا كرت لاسلكي/لا خدمات كلاسيكية) — و`Yes` لسؤال إعادة تشغيل الخدمات أثناء `libc6`.
- 📌 **الحزم الزائدة** (`perl/python3.13-minimal/openssh-client-gssapi`) أُزيلت بـ `autoremove` — متوقع بعد ترقية libc.
- ✅ **أُقفل هذا التوثيق (2026-10-09)**: Kali مثبّت ومكتمل ولا مهام متبقية — أي عمل مستقبلي عليه يبدأ من هنا كمرجع فقط.

## Section 2026-10-07 (سَدّ الفجوات: gh + web-read.py — مُختبَر حيّاً) ⭐
- ✅ **تصحيح مهم لادعاء خاطئ سابق**: كنت كتبت «Reddit بلا pathway مجاني» — القياس أثبت **خطأ**. بحث أوسع كشف **`api.fxtwitter.com`** (Twitter) و**`arctic-shift.photon-reddit.com`** (Reddit) — كلاهما يعمل **بلا حساب ولا Cookie ولا API key**.
- ✅ **11 طريقة مقاسة** لا 3: Twitter (6 طرق) · Reddit (7 طرق). النتيجة: `fxtwitter` ✅ · `Arctic Shift` ✅ · والباقي ❌/429.
- ✅ **الأداة المبنية:** `D:\ai\tools\web-read.py` (~250 سطر · **صفر تبعيات** · urllib فقط) بأوامر `tweet`/`user`/`reddit`/`doctor`/`raw`. **مُختبَر حيّاً**: تغريدة بالـ ID ✓ · بالرابط ✓ · Reddit بـ backoff ✓ · `--json` ✓ · `raw` ✓.
- ✅ **درس 26 مُطبَّق**: `doctor` أول مرة أعاد 1 OK/3 DEAD لأن Arctic Shift يرد **422 «بطيء»** عند التكرار — أضفت **retry-with-backoff** على (422/429/5xx) فأصبح **2 OK**. الدرس: DEAD من طلب واحد ليس حكماً؛ افصل الدائم (401/403/404) عن المؤقت (422/429).
- ✅ **`gh` CLI 2.102.0** مثبّت winget ومسجّل على `mahmoudrabeh-85` عبر `GITHUB_TOKEN` القائم. **مُختبَر**: `gh api user` → `mahmoudrabeh-85` · `gh search repos` ✓ · `gh repo view` ✓. تحذير: `gh auth status` يطبع «Token scopes: none» — **مCosmetic**، والدليل طلب حي ناجح.
- ✅ **الملفان محدَّثان v3** (454 + 162 سطراً) — تصُحيح جدول Reddit، توثيق الأداة، سجل التحديثات، **وتحديث قاعدة 8 في البرومبت** لتذكر `web-read.py` بدل تركه يقول Reddit بلا pathway. CJK/Cyr/FFFD/AR-underscore = **0** في الأربعة. SHA256 متطابق مع مرآة `MY-PREFERENCES`.
- ✅ **درس 25 (الأهم):** الحكم العمومي السلبي («X غير موجود / لا حل») يحتاج **دليل بحث** لا N محاولات فاشلة. 3 فشل يثبتون فشل 3 أشياء فقط ولا يثبتون شيئاً عن الرابع.

## Section 2026-10-07 (مرجع Agent-Reach + قواعد اختيار أدوات جديدة) ⭐
- ✅ **بحث موثّق** عن `Panniantong/Agent-Reach` (93,146 نجمة، MIT، Python، آخر دفعة اليوم) و **5 بدائل** بأرقام GitHub API حقيقية: **OpenCLI** (29,905 · Apache · JavaScript · 2026-09-24) + **mcporter** (5,053 · `openclaw` · TypeScript) + **autocli-skill** (916 · بلا رخصة · 17KB غلاف فقط) + Jina Reader/yt-dlp/gh/feedparser/Exa.
- ✅ **القياس الجانبي كشف 3 مصائد**: (1) رابط `mcporter` في README يشير لـ **Fork بـ 4 نجوم وآخر تحديث 2025-11** بينما الأصلي `openclaw/mcporter` بـ 5,053 نجمة، (2) النجوم ضجيج ترند صيني — 93K في شهرين، (3) **73% من منصاته صينية** = قيمة صفرية لمستخدم عربي.
- ✅ **فحص التوافق على الجهاز فعلياً**: Python 3.12.7 ✅ · Node 24.15 ✅ · Jina Reader **200 بلا تثبيت** ✅ · `gh` CLI ❌ · `agent-reach` ❌ · `mcporter` ❌.
- ✅ **التغطية القائمة = 70%+**: Firecrawl + Composio (LinkedIn متصل!) + vidscribe/yt-dlp + playwright + Jina. **الفجوة الوحيدة: Twitter/X + Reddit** → الحل = OpenCLI فقط.
- ✅ **ملف مرجعي جديد**: `C:\Users\RTX\.config\opencode\AGENT-REACH-REFERENCE.md` (295 سطراً · 20 رابطاً · **CJK=0 / Cyrillic=0 / FFFD=0**) — الجداول + الروابط الجاهزة + 4 سيناريوهات + ترتيب أولويات.
- ✅ **3 قواعد جديدة** في LEARNING.md: (19) افحص حقل `parent` قبل أي رابط داخل README، (20) النجوم قد تكون ضجيج ترند — اقرأ جدول المنصات، (21) التوصية تحتاج **3** فحوص لا 2: يحل الفجوة؟ يناسب الجهاز؟ يناسب اللغة؟
- ⛔ **التوصية النهائية: لا تثبّت** — إمّا OpenCLI فقط عند طلب Twitter/Reddit، أو `winget install GitHub.cli` فقط (خفيف، يفعّل قناة GitHub كاملة). Agent-Reatch كاملاً = عبء على جهاز يعاني ضغط ذاكرة موثّق.
- 📌 **ملف مرجعي بدون تثبيت — لم يُنفَّذ أي أمر**، بانتظار قرار المستخدم.

## Section 2026-10-07 (قالب Android + مرجع أدوات أندرويد — مُختبَر) ⭐
- ✅ **قالب `compose-mono`** (22 ملفاً / 18.6KB بعد التنظيف) في `D:\ai\MY-PREFERENCES\templates\android\` — **مبنيّ فعلاً** بنفس إصدارات الجهاز المخزَّنة (Gradle 8.5 + AGP 8.2.2 + Kotlin 1.9.22 + Compose BOM 2024.02.00 + SDK 34 / minSdk 26). **البناء الأول فشل** (`Unresolved reference: AppViewModel` — حزمة خاطئة في الملف: `package com.template.app.ui` بدل `com.template.app`) → **أُصلح** → `BUILD SUCCESSFUL` → APK ‏9.7MB. البناء الثاني (بعد الإصلاح) = 1م24ث.
- ✅ **قرارات القالب**: وحدة واحدة (`:app`) بلا Hilt/Retrofit (OkHttp 4.12 + kotlinx-serialization 1.6.2)، `TokenStore` بـ suspend (درس شاشة الإقلاع البيضاء)، `ApiClient` يرجع `Result<T>`، `network_security_config.xml` يسمح بـ`10.0.2.2`، `supportsRtl` + عربية افتراضية، `build.bat` يبني بـgradle.bat المحلي.
- ✅ **مرجع أدوات Android** `C:\Users\RTX\.config\opencode\ANDROID-TOOLS-REFERENCE.md` (143 سطراً، 12 مرشحاً بأرقام GitHub API حقيقية) — **الاختيار: `agent-device`** (4,903⭐، تحديث اليوم، Node 24.15 ✓، accessibility snapshots موفّرة للتوكنات + Evidence/Replay) + **`@us-all/android-mcp`** (76 أداة تشخيص) لمشروع winner-parental-control. **جدول المرفوضات** يوثّق 9 أدوات: `mikechambers/adb-mcp` (721⭐ لكنه لأدوات Adobe لا أندرويد!) · `CursorTouch/Android-MCP` (يحتاج Python 3.13) · `minhalvp` (مهجور 2025) · `OGAM` (تطبيق لا أداة) · وغيرها.
- ✅ **قاعدة 18 جديدة**: لا تثق في اسم الأداة — اقرأ README + أرقام API + اسم حزمة npm الصحيح (اكتُشف أن `mobile-mcp` على npm = package قديم v0.0.7، الصحيح `@mobilenext/mobile-mcp`).
- ✅ **فحص تلوّث لغوي**: القالب والملف المرجعي وDECISIONS = CJK 0 / Cyrillic 0 / FFFD 0 (أُصلح تلوّث في README و DECISIONS و ANDROID-TOOLS-REFERENCE).
- ✅ **`agent-device@0.21.23` مُثبّت ويعمل** (2026-10-09): `npm install -g agent-device@latest` نجح. **ثلاثة patches محلية** لتشغيله على ويندوز: (1) `ftruncate EPERM` — دالة `B` في `daemon-registration-owner.js` كانت تفتح بـ `'a'` ثم تقصّ؛ غيّرناها إلى `'r+'` مع fallback. (2) أداة `ps` POSIX غير موجودة على ويندوز → بنينا `ps.cmd` shim في `D:\ai\tools\agent-device-ps-shim\` + نسخناه إلى npm bin. (3) `owner-identity.js` كان يستدعي `ps` مباشرة بدون shell — عدّلناه ليستخدم `cmd /c ps` على win32 + رفعنا المهلة من 1ث إلى 8ث. **النتيجة**: `agent-device doctor` يخرج بـ code=0 والـ daemon يسجل `startTime` غير null. **ملاحظة**: agent-device **CLI فقط** (لا يدعم MCP مباشرة) — يُستدعى من داخل OpenCode عبر bash.

## Section 2026-10-07 (تشخيص تجميد شاشة OpenCode — السبب الجذري + أدوات علاج) ⭐
- ✅ **السبب الجذري أكّد بالقياس**: قاعدة `opencode.db` = **2.08GB** في `~\.local\share\opencode\` — منها **1.70GB** في جدول `event` (228,784 صف × 7.8KB متوسط)، و**162,499** حدث من نوع `message.part.updated.1` فقط. أكبر جلسة (**4,431 رسالة**) وحدها فيها **49,098** حدث. الآلية: كل تحديث streaming يُخزَّن حدثاً يحمل **نص الجزء كامل** (لا chunk فقط)، فتنمو القاعدة بلا سقف ويصير فتح/رسم الجلسة = تجميد دقيقة.
- ✅ **تصحيح خطئي ضمن الجلسة**: ظننتُ وجود «3 نسخ OpenCode» منفصلة — الفحص كشف أنها **عملية Electron واحدة** (main 21624 + children: renderer/GPU/utility). الاعتماد على `ParentProcessId` هو الفيصل.
- ✅ **27 عملية MCP يتيمة قُتلت** (آباء ميتون من جلسات مغلقة) → تحرير **1.61GB** (node RAM من 1,725MB → 116MB)، RAM المتاح من 3.0GB → 3.7GB، والعمليات من 30 → 3. حُفظت عمليات الـ API (NestJS على 3000) وتحققت: `/api/v1/health` = ok بعد التنظيف.
- ✅ **أدوات علاج جاهزة**: (1) `~\.local\share\opencode\opencode-db-cleanup.py` (dry-run ناجح: 92 جلسة = 1,590MB؛ ينسخ نسخة احتياطية + يحذف على دفعات 400 + VACUUM)، (2) `C:\Users\RTX\Desktop\cleanup-opencode-db.bat` (يشتغل بعد إغلاق OpenCode)، (3) `D:\ai\tools\cleanup-opencode-junk.ps1` (يقتل عمليات MCP يتيمة + يكتب سجلاً في `D:\ai\tools\logs\cleanup-junk.log`)، (4) `cleanup_opencode_junk.vbs` في Startup ليعمل تلقائياً عند كل تسجيل دخول.
- ⛔ **`schtasks`/Register-ScheduledTask = Access denied** بلا صلاحيات مسؤول — تكرّر الدرس (محاولة ثالثة تفشل بنفس السبب). الحل المعتمد: VBS في Startup.
- ⬜ **الخطوة المتبقية للمستخدم**: إغلاق OpenCode ← تشغيل `cleanup-opencode-db.bat` من سطح المكتب ← تحرير ~1.6GB (القاعدة ≈ 400MB) ← ختام التجميد.
