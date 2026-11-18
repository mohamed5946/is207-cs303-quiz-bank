#!/usr/bin/env python3
"""Generate quiz-data.json for IS 207 + CS 303 quiz bank.
IS 207: textbook Practice Sheets Q1-79 (photos sent 2026-11-18), answers per the
answer key delivered in chat. CS 303: midterm drill (20 Qs) from
cs303-midterm-drill-2026-11-19.md."""
import json, pathlib

Q = []

def add(id_, bank, topic, q, options, answer, explanation):
    Q.append({"id": id_, "bank": bank, "topic": topic, "q": q,
              "options": options, "answer": answer, "explanation": explanation})

# ================= IS 207 (bank is207) =================
T_HTML = "HTML"
T_CSS = "CSS"
T_JS = "JavaScript"
T_WEB = "الويب والبروتوكولات"

add("I01", "is207", T_WEB, "Common application layer protocols include:.......",
    ["HTTP", "DNS", "FTP", "A,b,c"], 3,
    "الـ HTTP والـ DNS والـ FTP التلاتة بروتوكولات طبقة التطبيقات، فالإجابة A,b,c.")
add("I02", "is207", T_HTML, "....... Is not an Inline element in HTML.",
    ["<h1>", "<i>", "<u>", "None of the Previous"], 0,
    "الـ <h1> عنصر block مش inline، أما <i> و <u> فـ inline.")
add("I03", "is207", T_WEB, "... opens link in a new window tab.",
    ['src="_blank"', 'alt="_blank"', 'target="_self"', 'target="_blank"'], 3,
    "الـ target=\"_blank\" بيفتح اللينك في تاب جديد، أما target=\"_self\" فبيفتحه في نفس التاب.")
add("I04", "is207", T_WEB, "... maintains and maps the name of the website.",
    ["HTTP", "DNS", "HTML", "Browsers"], 1,
    "الـ DNS هو اللي بيحوّل اسم الموقع (الـ domain) لعنوان IP.")
add("I05", "is207", T_HTML, "..... is used for creating clickable links.",
    ["<link>", "<http>", "<cl>", "<a>"], 3,
    "التاج <a> هو اللي بيعمل اللينك، أما <link> فبيربط ملفات زي الـ CSS.")
add("I06", "is207", T_CSS, "... defines an internal style sheet.",
    ["<script>", "<link>", "<class>", "<style>"], 3,
    "الـ <style> بيعرّف internal stylesheet جوّه الصفحة، أما <link> فبيربط ملف CSS خارجي.")
add("I07", "is207", T_CSS, "img[src] uses ... CSS selector",
    ["class selector", "universe selector", "Id selector", "Attribute selector"], 3,
    "الـ img[src] بيختار الصور اللي عندها attribute اسمه src، فده attribute selector.")
add("I08", "is207", T_CSS, "Background-attachment is used to..",
    ["control the scrolling of an image", "set the background color", "repeat the background image", "set the position of background"], 0,
    "الـ background-attachment بيتحكم في سكرول صورة الخلفية: fixed بتثبتها و scroll بتتحرك مع الصفحة.")
add("I09", "is207", T_CSS, "How can you include an external CSS file in an HTML document?",
    ['<style src="styles.css">', '<link rel="stylesheet" href="styles.css">', '<css href="styles.css">', '<import stylesheet="styles.css">'], 1,
    "الملف الخارجي بيتربط بـ <link rel=\"stylesheet\" href=\"...\"> جوّه الـ <head>.")
add("I10", "is207", T_CSS, "The list-style-image specifies...",
    ["background-image", "image position", "arrange images", "marker image"], 3,
    "الـ list-style-image بيحدد صورة الـ marker بتاع عناصر القايمة بدل النقطة أو الرقم.")
add("I11", "is207", T_WEB, "........ is the address of a given unique resource on the Web.",
    ["DNS", "HTTP", "URL", "Scheme"], 2,
    "الـ URL هو عنوان أي مورد على الويب، زي https://example.com/page.")
add("I12", "is207", T_WEB, "....... Is the type of category in which the owner domain is registered",
    ["Scheme", "Domain", "Sub Domain", "Top level Domain"], 3,
    "الـ Top level Domain هو فئة الدومين (.com و .edu و .org) اللي بيتسجل تحتها الدومين.")
add("I13", "is207", T_WEB, "........ refers to the way in which Web pages (HTML documents) are linked together",
    ["HTTP", "Text", "HTML", "Mark Up"], 2,
    "المفهوم الصح هو الـ hypertext — الصفحات مترابطة بلينكات — بس الاختيارات مافيهاش الكلمة دي، والأقرب منها (c) HTML لأن اللينكات بتتعمل بتاج <a> في الـ HTML.")
add("I14", "is207", T_HTML, "........Does not have a closing tag or any contents",
    ["<P>", "<h1>", "<Img>", "<HTML>"], 2,
    "الـ <img> عنصر void: مالهوش closing tag ولا محتوى جوّاه، أما <p> و <h1> و <html> فلازم يتقفلوا.")
add("I15", "is207", T_HTML, "........ is not a block level element in HTML.",
    ["<h1>", "<i>", "<p>", "None of the previous"], 1,
    "الـ <i> عنصر inline، أما <h1> و <p> فـ block level.")
add("I16", "is207", T_HTML, "...is the largest heading in HTML",
    ["h1", "hr", "h6", "head"], 0,
    "أكبر heading هو <h1>، و <h6> هو أصغر واحد.")
add("I17", "is207", T_CSS, "... is styling HTML5 layout",
    ["PhP", "Jquery", "Css", "All of the above"], 2,
    "الـ CSS هو اللي بيعمل styling وتنسيق الصفحة، مش PHP ولا jQuery.")
add("I18", "is207", T_HTML, "Metadata is contained in.....",
    ["HTML tag", "Head tag", "Body tag", "Title tag"], 1,
    "الـ metadata (زي <meta> و <title>) بتتحط جوّه الـ <head>.")
add("I19", "is207", T_HTML, ".....is used to insert an image in html pages.",
    ['<img url="htmllogo.jpg" />', '<img alt="htmllogo.jpg" />', '<img src="htmllogo.jpg" />', '<img link="htmllogo.jpg" />'], 2,
    "الصورة بتتدرج بـ <img src=\"...\">، والـ src هو اللي فيه مسار الصورة.")
add("I20", "is207", T_HTML, "...is used to create a text area in html.",
    ["<Text>", "<textarea>", '<input type="text">', '<input type="textarea">'], 1,
    "الـ <textarea> للنص الطويل متعدد الأسطر، أما <input type=\"text\"> فسطر واحد بس.")
add("I21", "is207", T_HTML, "Which tag is used to create a numbered list in HTML?",
    ["<Nl>", "<ol>", "<ul>", "<dl>"], 1,
    "الـ <ol> هي الـ ordered list (مرقمة)، و <ul> نقط، و <dl> قايمة تعريفات.")
add("I22", "is207", T_CSS, "...is used to link an external style sheet in the HTML file.",
    ['<link rel="stylesheet" href="style.css" />', '<link rel="stylesheet" src="style.css" />', '<style rel="stylesheet" src="style.css" />', '<style rel="stylesheet" link="style.css"/>'], 0,
    "الملف الخارجي بيتربط بـ <link rel=\"stylesheet\" href=\"style.css\"> — والـ href مش src.")
add("I23", "is207", T_CSS, "...is used to embed css in html page",
    ["<inline>", "<internal>", "<css>", "<style>"], 3,
    "الـ CSS جوّه الصفحة بيتكتب بين <style>...</style> في الـ <head>.")
add("I24", "is207", T_HTML, "....creates a dropdown list.",
    ["<dropdown>", "<select>", "<input>", "<downlist>"], 1,
    "الـ dropdown list بتتعمل بتاج <select>، والاختيارات جوّاها بتاج <option>.")
add("I25", "is207", T_WEB, "The .com at the URL represents....",
    ["Top-level domain", "Scheme", "Domain name", "Sub-domain"], 0,
    "الـ .com ده top-level domain — فئة الدومين، مش اسم الدومين نفسه.")
add("I26", "is207", T_WEB, "Relative URLs are used to ...",
    ["link other pages within the same site", "link the same page with other sites", "link other pages with other sites", "does not link"], 0,
    "الـ relative URL بيربط صفحات جوّه نفس الموقع من غير ما يكتب الدومين كامل.")
add("I27", "is207", T_JS, "...Can Change HTML Content.",
    ["window.write", "getElementById", "console.log", "html.write"], 1,
    "الـ document.getElementById(...) بيوصل للعنصر وبعدين تقدر تغيّر محتواه بـ innerHTML — أما console.log فبيطبع في الـ console بس.")
add("I28", "is207", T_JS, "....is used to access HTML elements",
    ["getElementById()", "getElementbyId()", "getElementByid()", "None"], 0,
    "الاسم بالظبط getElementById() — كابيتال I وكابيتال B و d صغيرة، أي تغيير في الكابيتال يبوّظها.")
add("I29", "is207", T_JS, 'What is the output: var x = 55;   var y = "0";   console.log(x + y);',
    ["55", '55"0"', '"5" "5" "0"', '"550"'], 3,
    "الـ 55 + \"0\" = \"550\": الجمع مع نص بيحوّل الرقم لنص ويلزقهم، فالناتج نص مش رقم.")
add("I30", "is207", T_WEB, "....are form's method.",
    ["GET,PULL", "GET,Post", "Get,Pop", "Get,Push"], 1,
    "الـ form ليها طريقتين: GET و POST.")
add("I31", "is207", T_HTML, "... define options in a drop-down list.",
    ["<drop-down>", "<select>", "<option>", "<datalist>"], 2,
    "الاختيارات جوّه الـ <select> بتتعرف بتاج <option>.")
add("I32", "is207", T_CSS, "...is the CSS selector in the following sentence:   p, li, h1 { color: red;}",
    ["P, li,h1", "color", "Red", "Color: Red"], 0,
    "الـ selector هو الجزء اللي قبل القوس: p, li, h1 — أما color: red فدي الـ declaration.")
add("I33", "is207", T_CSS, "...uses the ID selector",
    ["#para1", ".center", "*{p}", "All of the above"], 0,
    "الـ #para1 ده ID selector (الـ # للـ id)، أما .center فده class selector.")
add("I34", "is207", T_CSS, "...is a grouping content element.",
    ["hr", "br", "h1", "div"], 3,
    "الـ <div> هو عنصر تجميع المحتوى (block container)، أما <hr> فخط أفقي و <br> سطر جديد.")
add("I35", "is207", T_JS, "Which one is a true syntax:",
    ["let person={Name:'John',age: 30};", "var person={Name:John, age: 30};", 'var person={"Name":John,age: 30}', "Al of the above"], 0,
    "الصح بس (a): الـ 'John' لازم تبقى بين كوتس لأنها نص، وفي (b) و (c) الـ John من غير كوتس فالـ JavaScript هتدور على متغير اسمه John ومش هتلاقيه.")
add("I36", "is207", T_HTML, '..is an alphabetic list starts with "D"',
    ['<ol type = "A" start = "4">', '<nl type = "A" start = "4">', '<ul type = "A" start = "4">', '<ol type = "A" start = "D">'], 0,
    "الـ start رقم مش حرف: 4 يعني الحرف الرابع في الأبجدية = D، والتاج الصح هو <ol> مش <ul> ولا <nl>.")
add("I37", "is207", T_JS, "To delete a color property of car object",
    ["delete color.car", "pop car.color", "delete car.color", "pop color.car"], 2,
    "الحذف من الـ object بـ delete object.property: delete car.color — أما pop فدي للمصفوفات بس.")
add("I38", "is207", T_JS, "To access an object method use...keyword to refer object.",
    ["method", "this", "object", "Function"], 1,
    "الـ this بتشاور على الـ object نفسه جوّه الـ method بتاعه.")
add("I39", "is207", T_HTML, "....tag is used to specify page expiry, page author, list of keywords, and page description.",
    ["Title", "Head", "Meta", "Style"], 2,
    "تاج <meta> هو اللي بيحدد الـ expiry والـ author والـ keywords ووصف الصفحة.")
add("I40", "is207", T_JS, "... attribute of the <script> tag refers to the external script file path.",
    ["<a>", "<link>", "<href>", "<src>"], 3,
    "الـ src بتاع <script> هو اللي بيشاور على مسار ملف الـ JavaScript الخارجي.")
add("I41", "is207", T_CSS, "To add more space outside of field text ,use......",
    ["padding", "margin", "border", "width"], 1,
    "الـ margin مسافة برّه العنصر، أما الـ padding فمسافة جوّه العنصر بين حدوده ومحتواه.")
add("I42", "is207", T_JS, "JavaScript code can be placed in .....",
    ["<body>, </body>", "<meta>, </meta>", "<title>, </title>", "None"], 0,
    "كود الـ JavaScript بيتحط في <script> جوّه الـ <body> (أو الـ <head>)، مش في <meta> ولا <title>.")
add("I43", "is207", T_JS, "To display javascript output in a box, use....",
    ["Console.log", "Box.log", "Window.alert", "console.alert"], 2,
    "الـ window.alert() بيعرض الناتج في صندوق منبثق، أما console.log فبيطبع في الـ console بس.")
add("I44", "is207", T_HTML, "Which HTML tag is used to define a hyperlink?",
    ["<link>", "<a>", "<hyperlink>", "<url>"], 1,
    "الـ hyperlink بيتعمل بتاج <a> مع href، أما <link> فبيربط ملفات خارجية زي الـ CSS.")
add("I45", "is207", T_HTML, "Which HTML tag defines a large heading?",
    ["<header>", "<h1>", "<main>", "<big>"], 1,
    "أكبر heading هو <h1>، أما <header> فده تاج بنية مش heading.")
add("I46", "is207", T_HTML, "What does the <hr /> element represent in HTML?",
    ["Horizontal rule", "Header", "Hyperlink reference", "Heading row"], 0,
    "الـ <hr> يعني horizontal rule — خط أفقي بيفصل بين أجزاء الصفحة.")
add("I47", "is207", T_HTML, "What are the two required attributes of the <img> tag?",
    ["title and caption", "href and alt", "src and alt", "link and description"], 2,
    "الـ <img> لازم ليه src (مسار الصورة) و alt (نص بديل لو الصورة مظهرتش).")
add("I48", "is207", T_HTML, "How can an image be used as a link in HTML?",
    ['<a src="image.jpg">Link</a>', '<a> <img src="image.jpg" alt="Link"> </a>', '<a href="image.jpg">Link</a>', '<img href="image.jpg" alt="Link">'], 1,
    "الصورة تبقى لينك لما تحط <img> جوّه <a>: <a><img src=\"image.jpg\" alt=\"Link\"></a>.")
add("I49", "is207", T_HTML, "What does the <a> tag's target attribute define in HTML?",
    ["Font size", "Location to open the linked document", "Color of the linked text", "Width of the linked image"], 1,
    "الـ target بيحدد مكان فتح اللينك: _blank في تاب جديد و _self في نفس التاب.")
add("I50", "is207", T_HTML, "How do you represent the first item in an ordered list?",
    ["<il>", "<li>", "<ol>", "<ul>"], 1,
    "كل item في أي قايمة بيتعمل بتاج <li>، والـ <ol> هو القايمة نفسها.")
add("I51", "is207", T_HTML, "What tag is used to define a table row in HTML?",
    ["<row>", "<tr>", "<td>", "<th>"], 1,
    "صف الجدول <tr> (table row)، والخلية <td>، وعنوان العمود <th>.")
add("I52", "is207", T_HTML, "What tag is used to define a table cell in HTML?",
    ["<tc>", "<td>", "<cell>", "<th>"], 1,
    "خلية الجدول <td> (table data)، أما <th> فخلية عنوان (header cell).")
add("I53", "is207", T_HTML, "What HTML tag is used to create a text input field?",
    ["<textfield>", '<input type="text">', "<textinput>", "<textbox>"], 1,
    "حقل النص بيتعمل بـ <input type=\"text\">.")
add("I54", "is207", T_HTML, "How is a password input field created in an HTML form?",
    ['<input type="password">', "<password>", "<secret>", '<input type="secret">'], 0,
    "حقل الباسورد بيتعمل بـ <input type=\"password\"> — الحروف بتظهر نقط.")
add("I55", "is207", T_CSS, "Which selector is used to select all elements with a specific class?",
    ["#class", ".class", "*class*", "class:"], 1,
    "الـ class selector بيبدأ بنقطة: .class — أما # فدي للـ id.")
add("I56", "is207", T_CSS, "Which value of the `background-repeat` property will repeat an image both horizontally and vertically?",
    ["repeat-x", "repeat-y", "no-repeat", "repeat"], 3,
    "الـ repeat بتكرر الصورة أفقي وعمودي، أما repeat-x فأفقي بس و repeat-y فعمودي بس.")
add("I57", "is207", T_HTML, "The ........ is the ideal way to present a glossary, list of terms and the description of each term.",
    ["dt", "dl", "ul", "ol"], 1,
    "قايمة المصطلحات والتعريفات بتتعمل بـ <dl> (description list)، وجوّاها <dt> للمصطلح و <dd> للوصف.")
add("I58", "is207", T_HTML, "The ..........attribute defines space between table cells.",
    ["cellpadding", "cellborder", "cellspacing", "none"], 2,
    "الـ cellspacing = المسافة بين الخلايا وبعضها — متلخبطهاش مع الـ cellpadding اللي جوّه الخلية.")
add("I59", "is207", T_HTML, "The ........... attribute represents the distance between cell borders and the content within a cell.",
    ["cellpadding", "cellborder", "cellspacing", "none"], 0,
    "الـ cellpadding = المسافة بين حدود الخلية والمحتوى اللي جوّاها — عكس الـ cellspacing اللي بين الخلايا.")
add("I60", "is207", T_HTML, "...........attribute merge two or more columns into a single column in html tables.",
    ["Colmerge", "colspan", "rowmerge", "rowspan"], 1,
    "الـ colspan بيدمج أعمدة (col = column)، أما rowspan فبيدمج صفوف.")
add("I61", "is207", T_HTML, "...........attribute merge two or more rows in html tables.",
    ["Colmerge", "colspan", "rowmerge", "rowspan"], 3,
    "الـ rowspan بيدمج صفوف (row = صف)، أما colspan فبيدمج أعمدة.")
add("I62", "is207", T_HTML, "...................element is used to insert a scrolling area of text.",
    ["textarea", "scrollarea", "marquee", "none"], 2,
    "الـ <marquee> هو اللي بيعمل نص متحرك (scrolling)، أما <textarea> فحقل إدخال نص.")
add("I63", "is207", T_HTML, "................is not considered as a form control.",
    ["Check box", "Radio button", "Clickable button", "Clickable link"], 3,
    "الـ clickable link مش form control — أما الـ checkbox والـ radio والـ button فكلهم form controls.")
add("I64", "is207", T_HTML, "............... is used to get input long text content.",
    ["Check box", "Data list", "Text area", "Reset button"], 2,
    "النص الطويل بيتاخد بـ <textarea>، أما <input type=\"text\"> فسطر واحد بس.")
add("I65", "is207", T_CSS, "background-repeat property will repeat ......... vertically by default.",
    ["paragraph", "heading", "form", "image"], 3,
    "الـ background-repeat بيكرر صورة الخلفية (image) — والقيمة الافتراضية repeat بتكررها أفقي وعمودي.")
add("I66", "is207", T_CSS, "The ............attribute specifies an image for the marker rather than a bullet point or number.",
    ["marker", "image", "list-style-image", "bullet"], 2,
    "الـ list-style-image بيحدد صورة للـ marker بتاع عناصر القايمة بدل النقطة أو الرقم.")
add("I67", "is207", T_JS, "The javascript code is inserted between ............tags.",
    ["<java>..</java>", "<javascript>...</javascript>", "<script>...</script>", "<js>...</js>"], 2,
    "كود الـ JavaScript بيتكتب بين <script> و </script> — مفيش تاج اسمه <javascript>.")
add("I68", "is207", T_JS, "To add an element to the end of an array, you use the ............ method",
    ["Unshift()", "Pop()", "Shift()", "push()"], 3,
    "الـ push() بيضيف في الآخر، و unshift() بيضيف في الأول — احفظهم: push آخر، unshift أول.")
add("I69", "is207", T_JS, "To add an element to the beginning of an array, you use the........ method",
    ["Unshift()", "Pop()", "Shift()", "push()"], 0,
    "الـ unshift() بيضيف في الأول، أما push() فبيضيف في الآخر.")
add("I70", "is207", T_JS, "To remove an element from the end of an array, you use ........method.",
    ["Unshift()", "Pop()", "Shift()", "push()"], 1,
    "الـ pop() بيشيل من الآخر، و shift() بيشيل من الأول — pop آخر، shift أول.")
add("I71", "is207", T_JS, "To remove an element from the beginning of an array, you use the .........method.",
    ["Unshift()", "Pop()", "Shift()", "push()"], 2,
    "الـ shift() بيشيل من الأول، أما pop() فبيشيل من الآخر.")
add("I72", "is207", T_JS, "let x = 5;  let z = x ** 2;  x ** y produces the same result as ..........",
    ["Math.pow(x,y)", "X multiply by Y", "X by 2Y", "none"], 0,
    "الـ ** هو operator الأس، و x ** y = Math.pow(x,y) — مش ضرب ولا ضرب في 2.")
add("I73", "is207", T_JS, "For debugging purposes, you can call the ......... method in the browser to display data.",
    ["Window.alert", "console.log", "inner.HTML", "getElementById"], 1,
    "الـ console.log() بيطبع الداتا في الـ console للـ debugging، أما window.alert فبيطلع صندوق منبثق.")
add("I74", "is207", T_JS, "...................allows you to add interactivity to a web page.",
    ["html", "css", "javscript", "none"], 2,
    "الـ JavaScript هي اللي بتضيف التفاعلية للصفحة — الـ HTML بنية والـ CSS تنسيق بس.")
add("I75", "is207", T_WEB, "Common application layer protocols include:.......",
    ["HTTP", "DNS", "FTP", "A,b,c"], 3,
    "الـ HTTP والـ DNS والـ FTP التلاتة بروتوكولات طبقة التطبيقات.")
add("I76", "is207", T_HTML, "....... Is not an Inline element in HTML.",
    ["<h1>", "<i>", "<u>", "None of the Previous"], 0,
    "الـ <h1> عنصر block مش inline.")
add("I77", "is207", T_WEB, "... opens link in a new window tab.",
    ['src="_blank"', 'alt="_blank"', 'target="_self"', 'target="_blank"'], 3,
    "الـ target=\"_blank\" بيفتح اللينك في تاب جديد.")
add("I78", "is207", T_WEB, "... maintains and maps the name of the website.",
    ["HTTP", "DNS", "HTML", "Browsers"], 1,
    "الـ DNS هو اللي بيحوّل اسم الموقع لعنوان IP.")
add("I79", "is207", T_HTML, "..... is used for creating clickable links.",
    ["<link>", "<http>", "<cl>", "<a>"], 3,
    "التاج <a> هو اللي بيعمل اللينك.")

# ================= CS 303 (bank cs303) =================
T_SCHED = "الجدولة"
T_PROC = "حالات العمليات"
T_FORK = "العمليات: fork و exec"
T_CS = "الأقسام الحرجة"
T_AMDAHL = "قانون أمدال"
T_DEAD = "الجمود (Deadlock)"
T_CONC = "التزامن"

add("C01", "cs303", T_SCHED, "P1 (arrival 0, burst 8), P2 (arrival 1, burst 4), P3 (arrival 2, burst 9), P4 (arrival 3, burst 5). What is the average waiting time under SRTF?",
    ["5.5", "6.5", "7.25", "8"], 1,
    "الـ Gantt: P1 0–1، P2 1–5، P4 5–10، P1 10–17، P3 17–26. أوقات الانتظار: 9 و 0 و 15 و 2، المتوسط = 26/4 = 6.5.")
add("C02", "cs303", T_SCHED, "Round Robin, quantum = 2. P1 (arrival 0, burst 5), P2 (arrival 0, burst 3). What is the average waiting time?",
    ["2.5", "3", "3.5", "4"], 2,
    "الـ Gantt: P1 0–2، P2 2–4، P1 4–6، P2 6–7، P1 7–8. الانتظار: P1 = 3 و P2 = 4، المتوسط = 7/2 = 3.5.")
add("C03", "cs303", T_SCHED, "Which scheduling algorithm can cause starvation of long processes?",
    ["FCFS", "SJF", "Round Robin", "None of them"], 1,
    "الـ SJF بيفضّل العمليات القصيرة، فالعملية الطويلة ممكن تستنى للأبد لو العمليات القصيرة بتتابع — وده الـ starvation.")
add("C04", "cs303", T_SCHED, "A job arrives at 0, first runs at 3, finishes at 12, and has a burst of 6. What is its response time?",
    ["3", "6", "9", "12"], 0,
    "الـ response time = أول مرة يشتغل − وقت الوصول = 3 − 0 = 3. متلخبطهاش مع الـ waiting (turnaround − burst = 12 − 6 = 6) ولا الـ turnaround (12).")
add("C05", "cs303", T_SCHED, "Which algorithm suffers most from the convoy effect?",
    ["FCFS", "SJF", "Round Robin", "SRTF"], 0,
    "في الـ FCFS العملية الطويلة اللي في الأول بتوقف كل اللي وراها — وده الـ convoy effect.")
add("C06", "cs303", T_PROC, "A process in the Blocked state is:",
    ["Executing on the CPU", "Waiting for an event such as I/O", "Waiting to be assigned to a processor", "Terminated"], 1,
    "الـ Blocked يعني مستني حدث زي الـ I/O يخلص. اللي مستني processor بس هو الـ Ready، واللي شغال على الـ CPU هو الـ Running.")
add("C07", "cs303", T_FORK, 'A program calls fork() twice in a row, then prints "X". How many "X" lines appear?',
    ["2", "3", "4", "6"], 2,
    "كل fork بيضاعف عدد العمليات: 2^2 = 4 عمليات، وكل واحدة بتطبع X.")
add("C08", "cs303", T_PROC, "When a process finishes its I/O wait, it moves to the:",
    ["Running", "Ready", "Terminated", "New"], 1,
    "بعد ما الـ I/O يخلص بيرجع Ready، وعمره ما يروح Running على طول — الـ Running بتيجي من الـ Ready بس عن طريق الـ dispatcher.")
add("C09", "cs303", T_CS, "Which is NOT a requirement for a solution to the critical-section problem?",
    ["Mutual exclusion", "Progress", "Bounded waiting", "Preemption"], 3,
    "الشروط التلاتة هي mutual exclusion و progress و bounded waiting — والـ preemption مش منهم.")
add("C10", "cs303", T_CS, "A race condition occurs when:",
    ["Two processes run on different CPUs", "The result depends on the timing or order of process execution", "A process waits for I/O", "The memory is full"], 1,
    "الـ race condition يعني النتيجة بتعتمد على ترتيب وتوقيت تنفيذ العمليات — لأنهم بيشاركوا نفس الداتا من غير حماية.")
add("C11", "cs303", T_AMDAHL, "50% of a program is serial. What is the speedup (Amdahl's law) with 4 cores?",
    ["1.6", "2", "2.5", "4"], 0,
    "قانون أمدال: 1 / (0.5 + 0.5/4) = 1 / 0.625 = 1.6. الجزء الـ serial هو اللي بيحدّ السرعة.")
add("C12", "cs303", T_DEAD, "Imposing a fixed order on all resources breaks which deadlock condition?",
    ["Mutual exclusion", "Hold and wait", "Circular wait", "No preemption"], 2,
    "ترتيب ثابت للموارد بيمنع الـ circular wait — مفيش دايرة طلبات تتكون لو الكل بيطلب بنفس الترتيب.")
add("C13", "cs303", T_SCHED, "SJF is optimal because it gives the minimum average turnaround time.",
    ["True", "False"], 1,
    "غلط — الـ SJF هو الـ optimal لأنه بيدي أقل average WAITING time، مش turnaround.")
add("C14", "cs303", T_SCHED, "Increasing the Round Robin time quantum always decreases the average waiting time.",
    ["True", "False"], 1,
    "غلط — كل ما الـ quantum يكبر الـ RR بيقرب من الـ FCFS، والانتظار ممكن يزيد مش يقل.")
add("C15", "cs303", T_SCHED, "Under preemptive SJF (SRTF), a newly arriving process with a shorter remaining time preempts the running process.",
    ["True", "False"], 0,
    "صح — دي فكرة الـ preemptive SJF: أي عملية جديدة بوقت متبقّي أقل بتوقف اللي شغالة وتاخد الـ CPU.")
add("C16", "cs303", T_FORK, "A zombie process is still running and consuming CPU.",
    ["True", "False"], 1,
    "غلط — الـ zombie مات خلاص ومش بيستهلك CPU، اللي فاضل بس مدخله في جدول العمليات لحد ما الأب يعمل wait(). احفظها: zombie = ابن ميت.")
add("C17", "cs303", T_FORK, "After a successful exec, the next line of the old program runs.",
    ["True", "False"], 1,
    "غلط — الـ exec الناجح مبييرجعش أبدًا: نفس الـ PID بيكمل بالبرنامج الجديد، والسطر اللي بعد الـ exec مبيتنفذش.")
add("C18", "cs303", T_CS, "Two threads incrementing a shared counter without a lock can lose updates because the increment is not atomic.",
    ["True", "False"], 0,
    "صح — الـ increment تلات خطوات (اقرأ، زوّد، اكتب)، و thread تاني ممكن يدخل في النص ويضيّع تحديث.")
add("C19", "cs303", T_CONC, "Concurrency means tasks execute at exactly the same instant.",
    ["True", "False"], 1,
    "غلط — ده الـ parallelism. الـ concurrency يعني المهام بتتقدم بالتناوب، مش لازم في نفس اللحظة.")
add("C20", "cs303", T_DEAD, "Deadlock can occur only if all four conditions hold at the same time: mutual exclusion, hold-and-wait, no preemption, circular wait.",
    ["True", "False"], 0,
    "صح — لازم الشروط الأربعة تتجمع مع بعض عشان يحصل deadlock، وكسر أي شرط منهم بيمنعه.")

# ================= validate + dump =================
assert len(Q) == 99, f"expected 99 questions, got {len(Q)}"
ids = [q["id"] for q in Q]
assert len(set(ids)) == len(ids), "duplicate ids!"
for q in Q:
    assert len(q["options"]) == 4 or len(q["options"]) == 2, q["id"]
    assert 0 <= q["answer"] < len(q["options"]), q["id"]
    assert q["q"].strip() and q["explanation"].strip(), q["id"]
    assert all(o.strip() for o in q["options"]), q["id"]
is207 = [q for q in Q if q["bank"] == "is207"]
cs303 = [q for q in Q if q["bank"] == "cs303"]
assert len(is207) == 79 and len(cs303) == 20, (len(is207), len(cs303))

out = pathlib.Path(__file__).parent / "quiz-data.json"
out.write_text(json.dumps(Q, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote {out}: {len(Q)} questions (IS 207: {len(is207)}, CS 303: {len(cs303)})")
