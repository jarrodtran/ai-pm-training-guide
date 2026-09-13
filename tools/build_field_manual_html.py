#!/usr/bin/env python3
"""Build field-manual.html — the FDE-PM Field Manual, Apple-design edition.

Markdown is the source of truth; the design system lives in assets/apple.css
and is inlined so the output page stays self-contained (offline, no CDN).
"""
import pathlib
import re

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "fde-pm-field-manual.md"
OUT = ROOT / "field-manual.html"
CSS = (ROOT / "assets" / "apple.css").read_text(encoding="utf-8")

md_text = SRC.read_text(encoding="utf-8")
mver = re.search(r"\*\*Version ([\d.]+)", md_text)
VERSION = mver.group(1) if mver else ""

lines = md_text.splitlines()
title = lines[0].lstrip("# ").strip()
subtitle = lines[1].lstrip("# ").strip()
body_md = "\n".join(lines[2:])

# the hero carries these two meta lines instead of the body flow
body_md = body_md.replace(
    "**Companion technical reference to the AI-PM Graduate Program · 5 modules · ~90 hours · self-paced**\n", "")
body_md = re.sub(r"\*\*Version [\d.]+ · sources verified [^*]+\*\*\n", "", body_md)

body_md = re.sub(r"^(\s*)- \[ \] ", r"\1- ☐ ", body_md, flags=re.M)
body_md = re.sub(r"^(\s*)- \[[xX]\] ", r"\1- ☑ ", body_md, flags=re.M)
body_md = re.sub(r"\n---\n", "\n\n---\n\n", body_md)
body_md = re.sub(r"\n{3,}", "\n\n", body_md)

md = markdown.Markdown(
    extensions=["tables", "fenced_code", "toc", "attr_list", "sane_lists", "md_in_html"],
    extension_configs={"toc": {"toc_depth": "1-3", "permalink": False}},
)
html_body = md.convert(body_md)

# --- grouped navigation -------------------------------------------------------
def strip_tags(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()

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
            nav_parts.append('<div class="navgroup"><span class="glabel">Overview</span>')
            group_open = True
        nav_parts.append(f'<a class="nava" href="#{hid}" data-nav="{hid}">{label}</a>')
    else:
        nav_parts.append(f'<a class="nava lvl3" href="#{hid}" data-nav="{hid}">{label}</a>')
if group_open:
    nav_parts.append("</div>")
nav_html = "\n".join(nav_parts)

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>__TITLE__</title>
<style>
__CSS__
</style>
</head>
<body>

<div class="topbar">
  <button class="iconbtn" id="navtoggle" aria-label="Contents">Contents</button>
  <a class="backlink" href="index.html">← AI-PM Training Guide</a>
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
      <div class="kicker">Field Manual · v__VERSION__</div>
      <h1>__TITLE__</h1>
      <p class="sub">__SUBTITLE__</p>
      <div class="meta">
        <span>5 modules</span><span>17 blueprints</span><span>~90 hours</span><span>Verified September 12, 2026</span>
      </div>
    </header>
__BODY__
    <div class="pagefoot">
      <a href="index.html">← Back to the program</a>
      <span>Markdown source: <code>fde-pm-field-manual.md</code></span>
    </div>
  </main>
</div>

<script>
(function(){
  var root=document.documentElement, sb=document.getElementById("sidebar");
  try{var saved=localStorage.getItem("fm-theme"); if(saved) root.setAttribute("data-theme",saved);}catch(e){}
  document.getElementById("themebtn").addEventListener("click",function(){
    var cur=root.getAttribute("data-theme");
    var dark=cur?cur==="dark":matchMedia("(prefers-color-scheme:dark)").matches;
    var next=dark?"light":"dark";
    root.setAttribute("data-theme",next);
    try{localStorage.setItem("fm-theme",next);}catch(e){}
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

html = (TEMPLATE
        .replace("__CSS__", CSS)
        .replace("__TITLE__", title)
        .replace("__SUBTITLE__", subtitle)
        .replace("__VERSION__", VERSION)
        .replace("__NAV__", nav_html)
        .replace("__BODY__", html_body))
OUT.write_text(html, encoding="utf-8")
n_nav = nav_html.count('class="nava')
print(f"wrote {OUT.name} ({len(html):,} bytes) · nav items: {n_nav}")
