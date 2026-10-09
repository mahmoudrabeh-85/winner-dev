# فهرس مرجعي سريع — كل ما تحتاجه في مكان واحد
> آخر تحديث: 2026-09-19
> اقرأه في بداية كل جلسة — وفّر وقتك

---

## 🚀 أوامر تشغيل سريعة

| الأمر | الوظيفة |
|-------|---------|
| `http://127.0.0.1:8767/` | واجهة الوظائف الموحدة (401 وظيفة + فجوات مهارات + تتبع) |
| `http://127.0.0.1:8781/` | داشبورد التطوير الشخصي (فجوات + موارد تعلم) |
| `http://127.0.0.1:8765/` | CLI Launcher (22 أداة) |
| `python D:\ai\job-hunt\app\job_app.py` | تشغيل خادم الوظائف على 8767 |
| `python D:\ai\supervisor\dev_dashboard_server.py` | تشغيل داشبورد التطوير على 8781 |
| `python D:\ai\supervisor\supervisor_bot.py` | تشغيل بوت المراقب |

---

## 📂 مسارات المشاريع

```
D:\ai\portfolio\
├── portfolio.html              ← الموقع الحي (v4)
├── bot\bot.py                  ← بوت الموقع (@mahmoudagent26_bot)
├── bot\knowledge.json          ← معرفة البوت
├── AGENTS.md                   ← قواعد العمل
├── PROGRESS.md                 ← ما تم إنجازه
├── NEXT_STEPS.md               ← ما يتبقى
├── DECISIONS.md                ← القرارات المهمة
└── VERSIONS.md                 ← سجل الإصدارات

D:\ai\job-hunt\
├── frontend\
│   ├── index.html              ← الواجهة الموحدة (8767) ⭐
│   ├── app.js                  ← SPA router + logic
│   └── style.css               ← التصميم (dark/light)
├── app\
│   ├── job_app.py              ← الخادم (8767) ⭐
│   └── main.py                 ← FastAPI (بديل)
├── tools\
│   ├── job_aggregator.py       ← مجمع الوظائف CLI
│   ├── job_analyzer.py         ← محلل ذكي
│   └── job_swot.py             ← أداة SWOT
├── data\
│   ├── jobs.db                 ← قاعدة البيانات (401 وظيفة)
│   └── .env                    ← مفاتيح Adzuna
├── cv\
│   ├── mahmoud_rabeh_AR.pdf    ← السيرة بالعربي
│   ├── mahmoud_rabeh_EN.pdf    ← السيرة بالإنجليزي
│   └── mahmoud_rabeh_EN.txt    ← نص مستخرج
├── PROGRESS.md
├── NEXT_STEPS.md
└── DECISIONS.md

D:\ai\supervisor\
├── supervisor_bot.py           ← بوت المراقب (@mahmoudoc26_bot)
├── dev_dashboard_server.py     ← داشبورد التطوير (8781)
├── dev_dashboard.html          ← واجهة الداشبورد
├── profile.json                ← ملف المستخدم
├── start_services.bat          ← تشغيل الخوادم
├── watchdog.vbs                ← حارس إعادة التشغيل
├── skill_progress.json         ← تتبع تقدم المهارات
└── .env                        ← توكن البوت

D:\ai\media-buying\
├── docs\marketing\
│   ├── LINKEDIN-POSTS.md       ← 10 منشورات جاهزة
│   ├── LINKEDIN-PROFILE-COPY.md ← بروفايل للنسخ
│   ├── AFFILIATE-ROADMAP.md    ← خارطة أفلييت
│   ├── ACCOUNTS-SETUP.md       ← قائمة إعداد الحسابات
│   └── SOCIAL-CONTENT-PLAN.md  ← خطة السوشيال
├── AGENTS.md
├── PROGRESS.md
├── NEXT_STEPS.md
└── DECISIONS.md

D:\ai\tools\
├── cli_launcher_server.py      ← خادم CLI (8765)
├── cli_launcher.html           ← واجهة الأدوات
├── make_apps.py                ← مولّد ملفات apps
└── apps\                       ← 21 أداة (app.json لكل واحدة)
```

---

## 📊 حالة المشاريع (ملخص سريع)

| المشروع | الحالة | الرابط |
|---------|--------|--------|
| البورتفوليو | ✅ v4 حي | `mahmoudrabeh-85.github.io/winner-dev/portfolio.html` |
| job-hunt | ✅ 401 وظيفة + واجهة موحدة | `127.0.0.1:8767` |
| بوت المراقب | ✅ يعمل + حارس | `@mahmoudoc26_bot` |
| التسويق | ⏸ ملفات جاهزة — بانتظارك | `D:\ai\media-buying\` |
| CLI Launcher | ✅ 22 أداة | `127.0.0.1:8765` |

---

## 🔑 معلومات أساسية

| البند | القيمة |
|-------|--------|
| الاسم الصحيح | **محمود رابح** (وليس ربيع أو رباح) |
| حساب Gmail | mah4allah@gmail.com |
| LinkedIn | linkedin.com/in/mahmoud-rabeh-7102071a3 |
| بوت الموقع | @mahmoudagent26_bot |
| بوت المراقب | @mahmoudoc26_bot |
| حساب Adzuna | APP_ID=48386322 (Europe) |
| Munster | WINNER_DEV仓库 mahmoudrabeh-85/winner-dev |

---

## ⏭️ الخطوات التالية (من NEXT_STEPS.md)

1. **⭐** اختر أول وظيفة للتقديم (GiveDirectly 61 أو Oracle Fusion 56)
2. **⭐** أكمل بروفايل لينكدإن (6 خطوات — 20 دقيقة)
3. **⭐** جرّب تلخيص فيديو (أرسل رابط يوتيوب للبوت)
4. **⭐** جرّب /search و /assist من الهاتف
5. ⬜ ثبّت Docker/WSL (PowerShell كمسؤول: `wsl --install -d Ubuntu`)

---

## 📋 قواعد مختصرة

| القاعدة | التفاصيل |
|---------|----------|
| لا رفع من media-buying | مشروع محلي 100% — لا git إطلاقاً |
| فحص أمني قبل push | grep أنماط توكنات + مراجعة git status + .gitignore |
| معاينة بعد كل تعديل | افتح المتصفح فوراً — لا تنتقل قبل رؤية النتيجة |
| الاسم = محمود رابح | في كل الملفات والبروفايلات والمنشورات |
| لا أسعار في البروفايلات |_negotiable — بعد discovery call فقط |
| +20M EGP فقط | مبيعاته الفعلية — لا أرقام غير مؤكدة |

---

*انسخ هذا الملف أو اقرأه في بداية كل جلسة — يوفّر عليك تصفح PROGRESS/NEXT_STEPS/DECISIONS*
