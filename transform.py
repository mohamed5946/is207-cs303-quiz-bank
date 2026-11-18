#!/usr/bin/env python3
"""One-time adaptation of the CS 309 quiz-bank template (index.html) into the
IS 207 + CS 303 two-subject bank: subject menu home screen, per-subject
quiz view, Cairo font, floating pill bottom nav. Run once; afterwards
build.py only re-injects the QUESTIONS data."""
import json, pathlib, re, sys

work = pathlib.Path(__file__).parent
html = open(work / "index.html", encoding="utf-8").read()

def rep(old, new, required=True):
    global html
    if old not in html:
        if required:
            raise SystemExit("NOT FOUND: " + old[:90])
        return
    html = html.replace(old, new, 1)

# ---------- 1) Cairo font ----------
rep('family=Tajawal:wght@400;500;700;800;900', 'family=Cairo:wght@400;600;700;800;900')
rep('font-family:"Tajawal",system-ui,sans-serif;', 'font-family:"Cairo",system-ui,sans-serif;')

# ---------- 2) Title ----------
rep("<title>CS 309 Quiz Bank</title>", "<title>IS 207 + CS 303 Quiz Bank</title>")

# ---------- 3) Extra CSS (menu cards, pill nav, back button) ----------
rep("""      @media (prefers-reduced-motion: reduce){""",
"""      /* ---------- Subject menu ---------- */
      .menu-grid{display:grid;gap:16px;margin-top:20px}
      @media(min-width:640px){.menu-grid{grid-template-columns:1fr 1fr}}
      .subject-card{display:flex;flex-direction:column;align-items:flex-start;gap:9px;text-align:start;
        background:var(--surface);border:1.6px solid var(--line);border-radius:var(--radius);
        box-shadow:var(--shadow-sm);padding:22px 20px;min-height:210px;color:var(--ink);width:100%;
        animation:rise .6s var(--ease) both;
        transition:transform .25s var(--ease),border-color .25s var(--ease),box-shadow .25s var(--ease)}
      .subject-card:hover{border-color:var(--accent);transform:translateY(-3px);box-shadow:var(--shadow)}
      .subject-card:active{transform:scale(.98)}
      .sc-code{font-weight:900;font-size:23px;color:var(--accent-strong);font-variant-numeric:tabular-nums}
      .sc-name{font-weight:800;font-size:16.5px;line-height:1.55}
      .sc-meta{font-size:13.5px;font-weight:700;color:var(--ink-soft)}
      .sc-desc{font-size:14.5px;line-height:1.8;color:var(--ink-soft)}
      .sc-prog{font-size:13px;font-weight:800;color:var(--amber)}
      .sc-go{margin-top:auto;font-weight:900;color:var(--accent-strong);font-size:15px}
      .back-btn{border:1px solid var(--line);background:var(--surface);color:var(--accent-strong);
        border-radius:999px;padding:9px 16px;min-height:42px;font-weight:800;font-size:14px;
        box-shadow:var(--shadow-sm);margin-bottom:14px;transition:transform .18s var(--ease)}
      .back-btn:active{transform:scale(.96)}

      /* ---------- Floating pill bottom nav (transparent corners) ---------- */
      .pill-nav{position:fixed;bottom:16px;left:50%;transform:translateX(-50%);z-index:50;
        display:flex;gap:2px;background:var(--surface);border:1px solid var(--line);border-radius:999px;
        padding:5px;box-shadow:0 10px 28px rgba(31,41,55,.18);max-width:calc(100vw - 24px)}
      .pill-nav button{border:0;background:transparent;color:var(--ink-soft);font-weight:800;font-size:13.5px;
        padding:10px 12px;min-height:42px;border-radius:999px;white-space:nowrap;
        transition:background .25s var(--ease),color .25s var(--ease)}
      .pill-nav button:hover{background:var(--surface-2)}
      .pill-nav button:active{transform:scale(.95)}
      .pill-nav button.home{color:var(--accent-strong)}
      .pill-nav button.on{background:var(--accent-soft);color:var(--accent-strong)}
      @media (max-width:560px){.pill-nav button{padding:10px 9px;font-size:12.5px}}

      @media (prefers-reduced-motion: reduce){""")

# ---------- 4) Body: menu view + quiz view ----------
menu_html = """    <div class="wrap" id="menuWrap">
      <header>
        <h1>بنك أسئلة <span class="en">IS 207 + CS 303</span></h1>
        <p class="sub">ميدتيرم الخميس 19 نوفمبر — اختار المادة، وحل أسئلتها لوحدها: الإجابة النموذجية والشرح بالعربي بيظهروا تحت كل سؤال بعد ما تختار إجابة. الأسئلة بالإنجليزي زي ما هي في الكتاب والتدريب.</p>
      </header>
      <main class="menu-grid">
        <button class="subject-card" data-subject="is207" style="animation-delay:60ms">
          <span class="sc-code">IS 207</span>
          <span class="sc-name">Web Technology — تكنولوجيا الويب</span>
          <span class="sc-meta">79 سؤال · HTML · CSS · JavaScript · الويب</span>
          <span class="sc-desc">أسئلة الكتاب (Practice Sheets) — HTML و CSS وأول أجزاء JavaScript.</span>
          <span class="sc-prog" id="progIs207"></span>
          <span class="sc-go">ابدأ التدريب ←</span>
        </button>
        <button class="subject-card" data-subject="cs303" style="animation-delay:140ms">
          <span class="sc-code">CS 303</span>
          <span class="sc-name">Advanced Operating Systems — نظم التشغيل المتقدمة</span>
          <span class="sc-meta">20 سؤال · الجدولة · العمليات · Deadlock</span>
          <span class="sc-desc">تدريب الميدتيرم — 12 اختيارات + 8 صح/غلط، من غير مقالي.</span>
          <span class="sc-prog" id="progCs303"></span>
          <span class="sc-go">ابدأ التدريب ←</span>
        </button>
      </main>
      <footer>كل مادة ليها بنكها ونتيجتها لوحدها — الأسئلة مش مخلوطة ببعض. نتيجتك بتتحسب في الجلسة دي بس، ولو قفلت الصفحة وفتحتها هتبدأ من الأول.</footer>
    </div>
    <div class="wrap" id="quizWrap" style="display:none">"""
rep('    <div class="wrap">\n      <header>', menu_html + '\n      <header>', required=True)

# ---------- 5) Quiz header: back button + dynamic title/sub ----------
rep("""      <header>
        <h1>بنك أسئلة <span class="en">CS 309</span></h1>
        <p class="sub">المعالجات الدقيقة ولغة التجميع (8086) — اختار إجابة أي سؤال، وهيظهرلك على طول تحت نفس السؤال إذا كانت صح ولا غلط، مع الإجابة النموذجية وشرح تفصيلي بالعربي بيحافظ على المصطلحات الإنجليزية زي ما هي. أسئلة للتدريب على الميدتيرم من التدريب والـ Assignments والسلايدز.</p>""",
"""      <header>
        <button class="back-btn" id="backBtn">← قايمة المواد</button>
        <h1 id="quizTitle">بنك أسئلة <span class="en">IS 207</span> — تكنولوجيا الويب</h1>
        <p class="sub" id="quizSub">أسئلة الكتاب (Practice Sheets) — HTML و CSS وأول أجزاء JavaScript. اختار إجابة أي سؤال، وهيظهرلك على طول إذا كانت صح ولا غلط، مع الإجابة النموذجية وشرح بالعربي.</p>""")

# ---------- 6) Exam bar: drop the cheat-sheet link, scope text to the subject ----------
rep("""        <button class="exam-btn" id="exam20Btn">🎲 عشرين سؤال</button>
        <a class="exam-btn" href="cheat-sheet.html" style="text-decoration:none;display:inline-flex;align-items:center;background:var(--amber)">📋 دليل الكلمات المفتاحية</a>
        <p>كل ضغطة على الزرار بتجيبلك 20 سؤال عشوائي مختلفين من البنك كله، بترتيب عشوائي — حلّهم كأنك في امتحان مصغّر، وأول ما تخلّص العشرين هتظهر نتيجتك وتقدر تراجع غلطاتك أو تجيب عشرين جداد.</p>""",
"""        <button class="exam-btn" id="exam20Btn">🎲 عشرين سؤال</button>
        <p>كل ضغطة على الزرار بتجيبلك 20 سؤال عشوائي مختلفين من بنك المادة دي، بترتيب عشوائي — حلّهم كأنك في امتحان مصغّر، وأول ما تخلّص العشرين هتظهر نتيجتك وتقدر تراجع غلطاتك أو تجيب عشرين جداد.</p>""")

# ---------- 7) Remove the bank segmented control ----------
old_seg = '''        <div class="seg" role="tablist" aria-label="اختيار البنك">
          <button data-bank="all" class="on">الكل (110)</button>
          <button data-bank="drill">التدريب (20)</button>
          <button data-bank="a1">Assignment 1 (30)</button>
          <button data-bank="a3">Assignment 3 (14)</button>
          <button data-bank="expected">أسئلة متوقعة (16)</button>
          <button data-bank="past">الامتحان السابق (30)</button>
        </div>
'''
rep(old_seg, "")
# dead .seg CSS rules
rep("""      .seg{display:flex;flex-wrap:wrap;background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:4px;gap:4px;box-shadow:var(--shadow-sm)}
      .seg button{flex:1;border:0;background:transparent;color:var(--ink-soft);font-weight:700;font-size:14.5px;
        padding:10px 6px;min-height:44px;border-radius:10px;transition:background .3s var(--ease),color .3s var(--ease)}
      .seg button.on{background:var(--accent);color:#fff;box-shadow:0 4px 12px rgba(30,90,122,.35)}
""", "")

# ---------- 8) Replace the FAB stack with the floating pill nav ----------
old_fab = '''      <div class="fab-stack">
        <button class="fab" id="fabTop" aria-label="العودة لأعلى الصفحة" title="لأعلى الصفحة"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5"/><path d="m5 12 7-7 7 7"/></svg></button>
        <button class="fab last" id="fabLast" aria-label="الذهاب لآخر سؤال جاوبته" title="آخر سؤال جاوبته"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="m19 12-7 7-7-7"/></svg></button>
      </div>
'''
new_pill = '''      <nav class="pill-nav" id="pillNav" style="display:none" aria-label="التنقل السريع">
        <button class="home" id="navHome">🏠 الرئيسية</button>
        <button id="navShuffle">🔀 خلط</button>
        <button id="navWrong" style="display:none">الغلطات بس</button>
        <button id="navExam">🎲 عشرين</button>
        <button id="navTop">↑ لأعلى</button>
      </nav>
'''
rep(old_fab, new_pill)

# ---------- 9) Footer ----------
old_footer_start = "      <footer>الأسئلة والإجابات من تدريب الميدتيرم"
i = html.find(old_footer_start)
assert i != -1, "footer not found"
j = html.find("</footer>", i)
new_footer = ("      <footer>الأسئلة من أسئلة الكتاب (Practice Sheets) لمادة IS 207 — 79 سؤال (HTML و CSS وأول أجزاء JavaScript)، "
    "وتدريب ميدتيرم CS 303 — 20 سؤال (12 اختيارات + 8 صح/غلط). الشروح مكتوبة بالعربي للتدريب مع الحفاظ على المصطلحات الإنجليزية زي ما هي."
    "<br/>ملحوظة: سؤال 13 في IS 207 مفهومه الـ hypertext، والاختيارات مافيهاش الكلمة دي — الأقرب منها (c) HTML. والأسئلة 1–5 متكررة في 75–79 زي ما هي في الكتاب."
    "<br/>نتيجتك بتتحسب في الجلسة دي بس، ولو قفلت الصفحة وفتحتها هتبدأ من الأول.</footer>")
html = html[:i] + new_footer + html[j + len("</footer>"):]

# ---------- 10) JS: bank names ----------
rep('var BANK_NAMES = { drill: "التدريب", a1: "Assignment 1", a3: "Assignment 3", expected: "أسئلة متوقعة", past: "الامتحان السابق" };',
    'var BANK_NAMES = { is207: "IS 207", cs303: "CS 303" };')

# ---------- 11) JS: default bank ----------
rep('        bank: "all",', '        bank: "is207",')

# ---------- 12) JS: startExam20 scoped to current subject ----------
rep("        var pool = QUESTIONS.map(function(q){ return q.id; });",
    "        var pool = QUESTIONS.filter(function(q){ return q.bank === state.bank; }).map(function(q){ return q.id; });")
rep("""        state.onlyIds = set;
        state.examMode = true;
        state.bank = "all";
        state.topic = "all";""",
"""        state.onlyIds = set;
        state.examMode = true;
        state.topic = "all";
        // Fresh exam round for THIS subject only — keep the other subject's score.
        Object.keys(state.answers).forEach(function(id){
          if (byId[id] && byId[id].bank === state.bank) delete state.answers[id];
        });""")
rep("""        state.query = "";
        state.wrongOnly = false;
        state.answers = {};
        state.lastId = null;""",
"""        state.query = "";
        state.wrongOnly = false;
        state.lastId = null;""")
rep("""        state.order = picked.concat(pool.slice(picked.length));""",
"""        state.order = picked.concat(pool.slice(picked.length)).concat(QUESTIONS.filter(function(q){ return q.bank !== state.bank; }).map(function(q){ return q.id; }));""")
rep("""        document.getElementById("search").value = "";
        Array.prototype.forEach.call(document.querySelectorAll(".seg button"), function(x){
          x.classList.toggle("on", x.getAttribute("data-bank") === "all");
        });
        render();
        updateWrongBtn();
        var banner = document.getElementById("examBanner");""",
"""        document.getElementById("search").value = "";
        render();
        updateWrongBtn();
        var banner = document.getElementById("examBanner");""")

# ---------- 13) JS: resetAll scoped to current subject ----------
rep("""      function resetAll(){
        state.answers = {};""",
"""      function resetAll(){
        Object.keys(state.answers).forEach(function(id){
          if (byId[id] && byId[id].bank === state.bank) delete state.answers[id];
        });""")

# ---------- 14) JS: remove the seg click handler ----------
html, n = re.subn(
    r"      // ---- Controls ----\n      Array\.prototype\.forEach\.call\(document\.querySelectorAll\(\"\.seg button\"\), function\(b\)\{.*?\n      \}\);\n",
    "      // ---- Controls ----\n", html, count=1, flags=re.DOTALL)
assert n == 1, "seg handler block not found"

# ---------- 15) JS: navWrong sync in updateWrongBtn ----------
rep("""        btn.style.display = wrong.length ? "" : "none";
        btn.textContent = "الغلطات بس (" + wrong.length + ")";
        btn.classList.toggle("on", state.wrongOnly);""",
"""        btn.style.display = wrong.length ? "" : "none";
        btn.textContent = "الغلطات بس (" + wrong.length + ")";
        btn.classList.toggle("on", state.wrongOnly);
        var navWrong = document.getElementById("navWrong");
        if (navWrong){
          navWrong.style.display = wrong.length ? "" : "none";
          navWrong.textContent = "الغلطات بس (" + wrong.length + ")";
          navWrong.classList.toggle("on", state.wrongOnly);
        }""")

# ---------- 16) JS: replace the FAB section with menu + pill-nav logic ----------
new_section = """      // ---- Subject menu + floating pill nav ----
      var menuWrap = document.getElementById("menuWrap");
      var quizWrap = document.getElementById("quizWrap");
      var pillNav = document.getElementById("pillNav");
      var quizTitle = document.getElementById("quizTitle");
      var quizSub = document.getElementById("quizSub");
      var SUBJECTS = {
        is207: { code: "IS 207", ar: "تكنولوجيا الويب", count: 79,
          sub: "أسئلة الكتاب (Practice Sheets) — HTML و CSS وأول أجزاء JavaScript. اختار إجابة أي سؤال، وهيظهرلك على طول إذا كانت صح ولا غلط، مع الإجابة النموذجية وشرح بالعربي." },
        cs303: { code: "CS 303", ar: "نظم التشغيل المتقدمة", count: 20,
          sub: "تدريب الميدتيرم — 12 اختيارات + 8 صح/غلط، من غير مقالي. اختار إجابة أي سؤال، وهيظهرلك على طول إذا كانت صح ولا غلط، مع الإجابة النموذجية وشرح بالعربي." }
      };
      function subjectProgress(id){
        var total = QUESTIONS.filter(function(q){ return q.bank === id; }).length;
        var done = 0, good = 0;
        Object.keys(state.answers).forEach(function(aid){
          if (byId[aid] && byId[aid].bank === id){ done++; if (state.answers[aid] === byId[aid].answer) good++; }
        });
        return done ? ("جاوبت " + done + " من " + total + " — صح " + good) : ("لسه مبدأتش — " + total + " سؤال");
      }
      function showMenu(){
        quizWrap.style.display = "none";
        menuWrap.style.display = "";
        pillNav.style.display = "none";
        document.getElementById("progIs207").textContent = subjectProgress("is207");
        document.getElementById("progCs303").textContent = subjectProgress("cs303");
        window.scrollTo({ top: 0, behavior: "auto" });
      }
      function openSubject(id){
        var s = SUBJECTS[id];
        state.bank = id;
        state.topic = "all";
        state.onlyIds = null;
        state.examMode = false;
        state.wrongOnly = false;
        state.query = "";
        if (state.order.length !== QUESTIONS.length){
          state.order = QUESTIONS.map(function(q){ return q.id; });
        }
        document.getElementById("search").value = "";
        quizTitle.innerHTML = 'بنك أسئلة <span class="en">' + s.code + '</span> — ' + s.ar;
        quizSub.textContent = s.sub;
        menuWrap.style.display = "none";
        quizWrap.style.display = "";
        pillNav.style.display = "";
        render();
        updateWrongBtn();
        window.scrollTo({ top: 0, behavior: "auto" });
      }
      Array.prototype.forEach.call(document.querySelectorAll(".subject-card"), function(card){
        card.addEventListener("click", function(){ openSubject(card.getAttribute("data-subject")); });
      });
      document.getElementById("backBtn").addEventListener("click", showMenu);
      document.getElementById("navHome").addEventListener("click", showMenu);
      document.getElementById("navShuffle").addEventListener("click", function(){ document.getElementById("shuffleBtn").click(); });
      document.getElementById("navWrong").addEventListener("click", function(){ document.getElementById("wrongBtn").click(); });
      document.getElementById("navExam").addEventListener("click", startExam20);
      document.getElementById("navTop").addEventListener("click", function(){
        window.scrollTo({ top: 0, behavior: reduced ? "auto" : "smooth" });
      });
      function updateFabs(){
        if (!pillNav) return;
        pillNav.style.display = (quizWrap.style.display === "none") ? "none" : "";
      }
"""
html, n = re.subn(
    r"      // ---- Floating nav buttons \+ mobile filters toggle ----.*?      var controlsEl = document\.getElementById\(\"controls\"\);",
    new_section + "      var controlsEl = document.getElementById(\"controls\");",
    html, count=1, flags=re.DOTALL)
assert n == 1, "fab section not found"

# ---------- 17) Initial view is the menu ----------
rep("      render();\n    </script>", "      render();\n      showMenu();\n    </script>")

# ---------- Safety checks ----------
assert "CS 309" not in html, "CS 309 leaked"
assert "8088" not in html, "8088 leaked"
assert "cheat-sheet" not in html, "cheat-sheet link leaked"
assert ".seg" not in html, "seg remnants"
assert 'class="fab' not in html, "fab remnants"
assert "fabTop" not in html and "fabLast" not in html, "fab JS remnants"

open(work / "index.html", "w", encoding="utf-8").write(html)
print("transformed index.html:", len(html), "bytes")
