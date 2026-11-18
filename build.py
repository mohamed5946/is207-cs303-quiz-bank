#!/usr/bin/env python3
"""Build index.html for the IS 207 + CS 303 quiz bank:
embed quiz-data.json into the QUESTIONS array and revision-data.json
into the REVISION object in index.html."""
import json, pathlib

WORK = pathlib.Path(__file__).parent

data = json.loads((WORK / "quiz-data.json").read_text(encoding="utf-8"))
assert len(data) == 159, len(data)
assert sum(1 for q in data if q["bank"] == "is207") == 79
assert sum(1 for q in data if q["bank"] == "cs303") == 80
for q in data:
    assert len(q["options"]) in (2, 4) and 0 <= q["answer"] < len(q["options"])
    assert q["q"].strip() and q["explanation"].strip()
    assert q["id"].strip()

rev = json.loads((WORK / "revision-data.json").read_text(encoding="utf-8"))
assert set(rev) == {"is207", "cs303"}
assert len(rev["is207"]) == 5 and len(rev["cs303"]) == 4
for bank, secs in rev.items():
    for s in secs:
        assert s["title"].strip() and s["html"].strip()
        assert "</script" not in s["html"].lower()

html = (WORK / "index.html").read_text(encoding="utf-8")

lines = html.split("\n")
found_q = found_r = False
for i, line in enumerate(lines):
    if line.strip().startswith("var QUESTIONS = ["):
        # Escape "</" so a literal "</script>" inside a question/option
        # (e.g. "<script>...</script>") can't terminate the <script> block.
        # In JS "<\/" === "/" so the data is unchanged.
        js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
        lines[i] = "var QUESTIONS = " + js + ";"
        found_q = True
    elif line.strip().startswith("var REVISION = "):
        js = json.dumps(rev, ensure_ascii=False).replace("</", "<\\/")
        lines[i] = "var REVISION = " + js + ";"
        found_r = True
if not found_q:
    raise SystemExit("QUESTIONS line not found")
if not found_r:
    raise SystemExit("REVISION line not found")

html = "\n".join(lines)
assert "CS 309" not in html and "8088" not in html and "cheat-sheet" not in html
assert 'data-bank' not in html and 'class="seg' not in html
(WORK / "index.html").write_text(html, encoding="utf-8")
print(f"built index.html: {len(data)} questions (IS 207: 79, CS 303: 80) + revision (IS 207: 5 sections, CS 303: 4 sections)")
