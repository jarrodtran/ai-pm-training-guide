#!/usr/bin/env python3
"""Build the site's HTML pages from the markdown sources.

  field-manual.html            <- fde-pm-field-manual.md        (this script's sibling builds it)
  ai-pm-training-guide.html    <- ai-pm-training-guide.md
  case-packets.html            <- case-packets.md
  exams.html                   <- exams.md
  interview-bank.html          <- interview-bank.md
  answer-guide.html            <- answer-guide.md
  audit-report.html            <- audit-report.md
  templates/index.html         <- templates/README.md

Design lives in assets/apple.css and is inlined, so every output page
remains self-contained (works offline, no CDN, no build step at runtime).
"""
import pathlib
import re

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
CSS = (ROOT / "assets" / "apple.css").read_text(encoding="utf-8")

# markdown source -> output html (relative to repo root)
DOCS = [
    ("ai-pm-training-guide.md", "ai-pm-training-guide.html", "Master syllabus", "Twenty modules"),
    ("case-packets.md", "case-packets.html", "Case packet", "Four cases, exhibits and teaching notes"),
    ("exams.md", "exams.html", "Exam book", "Midterm, capstone thesis, defense, rubrics"),
    ("interview-bank.md", "interview-bank.html", "Interview question bank", "Questions mapped to the course that builds each answer"),
    ("answer-guide.md", "answer-guide.html", "Midterm answer guide", "Self-grading frameworks"),
    ("audit-report.md", "audit-report.html", "Program audit", "Read-only audit of the program files"),
    ("templates/README.md", "templates/index.html", "Template library", "Fill-in-the-blank templates"),
]

# pages that get a rendered counterpart — used to rewrite links
RENDERED = {
    "ai-pm-training-guide.md": "ai-pm-training-guide.html",
    "case-packets.md": "case-packets.html",
    "exams.md": "exams.html",
    "interview-bank.md": "interview-bank.html",
    "answer-guide.md": "answer-guide.html",
    "audit-report.md": "audit-report.html",
    "fde-pm-field-manual.md": "field-manual.html",
    "templates/README.md": "templates/index.html",
}

SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>__TITLE__ · AI-PM Training Guide</title>
<style>
__CSS__
</style>
</head>
<body>

<div class="topbar">
  <button class="iconbtn" id="navtoggle" aria-label="Contents">Contents</button>
  <a class="backlink" href="__HOME__">← AI-PM Training Guide</a>
  <span class="spacer"></span>
  <button class="iconbtn nowrap" id="themebtn" aria-label="Toggle appearance">Appearance</button>
  <button class="iconbtn nowrap" id="printbtn">Print</button>
</div>

<div class="shell">
  <nav class="sidebar" id="sidebar" aria-label="Contents">
    <input class="navsearch" id="navsearch" type="search" placeholder="Filter sections" autocomplete="off" aria-label="Filter sections">
    __NAV__
  </nav>

  <main class="main">
    <header class="hero">
      <div class="kicker">__KICKER__</div>
      <h1>__TITLE__</h1>
      <p class="sub">__SUB__</p>
    </header>
__BODY__
    <div class="pagefoot">
      <a href="__HOME__">← Back to the program</a>
      <span>Markdown source: <code>__SOURCE__</code></span>
    </div>
  </main>
</div>

<script>
(function(){
  var root=document.documentElement, sb=document.getElementById("sidebar");
  var KEY="fm-theme";
  try{var saved=localStorage.getItem(KEY); if(saved) root.setAttribute("data-theme",saved);}catch(e){}
  document.getElementById("themebtn").addEventListener("click",function(){
    var cur=root.getAttribute("data-theme");
    var dark=cur?cur==="dark":matchMedia("(prefers-color-scheme:dark)").matches;
    var next=dark?"light":"dark";
    root.setAttribute("data-theme",next);
    try{localStorage.setItem(KEY,next);}catch(e){}
  });
  document.getElementById("printbtn").addEventListener("click",function(){window.print();});
  document.querySelectorAll(".main table").forEach(function(t){
    if(t.parentElement.classList.contains("tablewrap"))return;
    var w=document.createElement("div");w.className="tablewrap";
    t.parentNode.insertBefore(w,t);w.appendChild(t);
  });
  document.getElementById("navtoggle").addEventListener("click",function(){sb.classList.toggle("open");});
  sb.addEventListener("click",function(e){if(e.target.tagName==="A")sb.classList.remove("open");});
  var search=document.getElementById("navsearch");
  search.addEventListener("input",function(){
    var q=search.value.trim().toLowerCase();
    document.querySelectorAll(".navgroup").forEach(function(g){
      var shown=0;
      g.querySelectorAll(".nava").forEach(function(a){
        var hit=!q||a.textContent.toLowerCase().indexOf(q)>-1;
        a.style.display=hit?"":"none"; if(hit)shown++;
      });
      var gl=g.querySelector(".glabel");
      var glhit=!q||(gl&&gl.textContent.toLowerCase().indexOf(q)>-1);
      g.style.display=(shown||glhit)?"":"none";
    });
  });
  var links={};
  document.querySelectorAll(".nava").forEach(function(a){links[a.getAttribute("data-nav")]=a;});
  var targets=[].slice.call(document.querySelectorAll(".main h1[id],.main h2[id],.main h3[id]"));
  var current=null;
  function activate(id){
    if(current===id)return;
    if(links[current])links[current].classList.remove("active");
    current=id;
    var el=links[id];
    if(el){
      el.classList.add("active");
      var r=el.getBoundingClientRect(), sr=sb.getBoundingClientRect();
      if(r.top<sr.top||r.bottom>sr.bottom){ sb.scrollTop+=(r.top-sr.top)-sr.height/2+r.height/2; }
    }
  }
  if("IntersectionObserver" in window){
    var io=new IntersectionObserver(function(entries){
      entries.forEach(function(en){ if(en.isIntersecting) activate(en.target.id); });
    },{rootMargin:"-52px 0px -72% 0px",threshold:0});
    targets.forEach(function(t){io.observe(t);});
  }
  document.addEventListener("keydown",function(e){
    if(e.key==="/"&&document.activeElement!==search){e.preventDefault();search.focus();}
    if(e.key==="Escape"&&document.activeElement===search){search.value="";search.dispatchEvent(new Event("input"));search.blur();}
  });
})();
</script>
</body>
</html>
"""


def strip_tags(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


def rewrite_links(text: str, depth: str) -> str:
    """Point links at rendered pages (and fix depth for nested sources)."""
    for src, out in RENDERED.items():
        for prefix in ("", "./", "../"):
            text = text.replace(f"]({prefix}{src})", f"]({depth}{out})")
        text = text.replace(f"href=\"{src}\"", f"href=\"{depth}{out}\"")
    # markdown links that point at a directory (e.g. templates/) -> index
    text = re.sub(r"\]\(\.?/?templates/?\)", f"]({depth}templates/index.html)", text)
    return text


def build(src_rel: str, out_rel: str, kicker: str, sub: str) -> tuple[str, int]:
    src = ROOT / src_rel
    text = src.read_text(encoding="utf-8")
    depth = "../" if "/" in out_rel else ""

    lines = text.splitlines()
    h1 = re.match(r"^#\s+(.*)", lines[0]) if lines else None
    title = h1.group(1).strip() if h1 else src.stem
    body_md = "\n".join(lines[1:]) if h1 else text

    body_md = re.sub(r"^(\s*)- \[ \] ", r"\1- ☐ ", body_md, flags=re.M)
    body_md = re.sub(r"^(\s*)- \[[xX]\] ", r"\1- ☑ ", body_md, flags=re.M)
    body_md = re.sub(r"\n---\n", "\n\n---\n\n", body_md)
    body_md = re.sub(r"\n{3,}", "\n\n", body_md)

    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "attr_list", "sane_lists", "md_in_html"],
        extension_configs={"toc": {"toc_depth": "1-3", "permalink": False}},
    )
    html_body = md.convert(body_md)
    html_body = rewrite_links(html_body, depth)

    heads = re.findall(r'<(h[123])\s+id="([^"]+)"[^>]*>(.*?)</\1>', html_body, re.S)
    nav_parts, group_open = [], False
    for tag, hid, raw in heads:
        label = strip_tags(raw)
        if tag == "h1":
            if group_open:
                nav_parts.append("</div>")
            nav_parts.append(f'<div class="navgroup"><a class="glabel" href="#{hid}">{label}</a>')
            group_open = True
        elif tag == "h2":
            if not group_open:
                nav_parts.append('<div class="navgroup"><span class="glabel">Contents</span>')
                group_open = True
            nav_parts.append(f'<a class="nava" href="#{hid}" data-nav="{hid}">{label}</a>')
        else:
            nav_parts.append(f'<a class="nava lvl3" href="#{hid}" data-nav="{hid}">{label}</a>')
    if group_open:
        nav_parts.append("</div>")
    nav_html = "\n".join(nav_parts) or '<div class="navgroup"><span class="glabel">Contents</span></div>'

    page = (SHELL.replace("__CSS__", CSS)
                 .replace("__TITLE__", title)
                 .replace("__KICKER__", kicker)
                 .replace("__SUB__", sub)
                 .replace("__HOME__", f"{depth}index.html")
                 .replace("__SOURCE__", src_rel)
                 .replace("__NAV__", nav_html)
                 .replace("__BODY__", html_body))
    out = ROOT / out_rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    return out_rel, len(page)


if __name__ == "__main__":
    total = 0
    for src_rel, out_rel, kicker, sub in DOCS:
        name, size = build(src_rel, out_rel, kicker, sub)
        total += size
        print(f"  {name:34} {size:>9,} bytes")
    print(f"built {len(DOCS)} pages · {total:,} bytes total")
