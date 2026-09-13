#!/usr/bin/env python3
"""Build field-manual.html — Apple-grade design system.

Editorial reference layout: frosted top bar, sticky grouped sidebar with
scroll-spy, large display typography, hairline tables, soft-radius code
blocks, light/dark, print. Markdown stays the source of truth.
"""
import pathlib
import re

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "fde-pm-field-manual.md"
OUT = ROOT / "field-manual.html"

md_text = SRC.read_text(encoding="utf-8")
mver = re.search(r"\*\*Version ([\d.]+)", md_text)
VERSION = mver.group(1) if mver else ""

lines = md_text.splitlines()
title = lines[0].lstrip("# ").strip()
subtitle = lines[1].lstrip("# ").strip()
body_md = "\n".join(lines[2:])

# lift the two meta lines out of the flow — the hero carries them instead
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
:root{
  --bg:#ffffff; --bg-2:#f5f5f7; --bg-3:#fbfbfd;
  --text:#1d1d1f; --text-2:#6e6e73; --text-3:#86868b;
  --sep:rgba(0,0,0,.10); --sep-2:rgba(0,0,0,.06);
  --accent:#0071e3; --accent-soft:rgba(0,113,227,.09);
  --mono:ui-monospace,"SF Mono",SFMono-Regular,Menlo,Monaco,Consolas,monospace;
  --sans:-apple-system,BlinkMacSystemFont,"SF Pro Text","SF Pro Display","Helvetica Neue",Helvetica,Arial,sans-serif;
  --r:18px; --r-sm:12px; --bar:52px;
  --shadow:0 1px 3px rgba(0,0,0,.04),0 8px 24px rgba(0,0,0,.04);
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --bg:#000000; --bg-2:#1d1d1f; --bg-3:#161617;
  --text:#f5f5f7; --text-2:#a1a1a6; --text-3:#86868b;
  --sep:rgba(255,255,255,.14); --sep-2:rgba(255,255,255,.08);
  --accent:#2997ff; --accent-soft:rgba(41,151,255,.14);
  --shadow:0 1px 3px rgba(0,0,0,.5),0 8px 24px rgba(0,0,0,.4);
}}
html[data-theme="dark"]{
  --bg:#000000; --bg-2:#1d1d1f; --bg-3:#161617;
  --text:#f5f5f7; --text-2:#a1a1a6; --text-3:#86868b;
  --sep:rgba(255,255,255,.14); --sep-2:rgba(255,255,255,.08);
  --accent:#2997ff; --accent-soft:rgba(41,151,255,.14);
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important;animation:none!important}}
body{
  font-family:var(--sans);background:var(--bg);color:var(--text);
  font-size:17px;line-height:1.6;letter-spacing:-.011em;
  -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;
}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
:focus-visible{outline:4px solid var(--accent-soft);outline-offset:2px;border-radius:6px}

/* ── top bar ───────────────────────────────────────────────── */
.topbar{
  position:fixed;top:0;left:0;right:0;height:var(--bar);z-index:60;
  display:flex;align-items:center;gap:14px;padding:0 22px;
  background:color-mix(in srgb,var(--bg) 72%,transparent);
  -webkit-backdrop-filter:saturate(180%) blur(20px);backdrop-filter:saturate(180%) blur(20px);
  border-bottom:1px solid var(--sep);
}
.topbar .mark{font-size:14px;font-weight:600;letter-spacing:-.01em;color:var(--text);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.topbar .spacer{flex:1}
.iconbtn{
  font:500 13px var(--sans);color:var(--text-2);background:transparent;border:1px solid var(--sep);
  border-radius:980px;padding:6px 13px;cursor:pointer;white-space:nowrap;transition:background .2s,color .2s,border-color .2s;
}
.iconbtn:hover{background:var(--bg-2);color:var(--text);border-color:var(--sep-2)}
.nowrap{white-space:nowrap}
#navtoggle{display:none}

/* ── shell ─────────────────────────────────────────────────── */
.shell{display:grid;grid-template-columns:286px minmax(0,1fr);max-width:1440px;margin:0 auto;padding-top:var(--bar)}
.sidebar{
  position:sticky;top:var(--bar);height:calc(100vh - var(--bar));overflow-y:auto;
  padding:26px 18px 80px 22px;border-right:1px solid var(--sep);overscroll-behavior:contain;
}
.sidebar::-webkit-scrollbar{width:8px}
.sidebar::-webkit-scrollbar-thumb{background:var(--sep);border-radius:4px}
.navsearch{
  width:100%;padding:8px 12px;margin-bottom:20px;border:1px solid var(--sep);border-radius:10px;
  background:var(--bg-2);color:var(--text);font:500 13.5px var(--sans);letter-spacing:-.01em;
}
.navsearch::placeholder{color:var(--text-3)}
.navsearch:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 4px var(--accent-soft);background:var(--bg)}
.navgroup{margin-bottom:20px}
.glabel{
  display:block;font-size:11px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;
  color:var(--text-3);margin:0 0 7px 10px;text-decoration:none;
}
a.glabel:hover{color:var(--accent);text-decoration:none}
.nava{
  display:block;font-size:13.5px;line-height:1.34;letter-spacing:-.01em;
  padding:5px 10px;border-radius:8px;color:var(--text-2);text-decoration:none;
  transition:background .15s,color .15s;
}
.nava:hover{background:var(--bg-2);color:var(--text);text-decoration:none}
.nava.lvl3{padding-left:22px;font-size:12.5px;color:var(--text-3)}
.nava.active{background:var(--accent-soft);color:var(--accent);font-weight:600}

/* ── article ───────────────────────────────────────────────── */
.main{padding:0 56px 140px;max-width:calc(820px + 112px)}
.hero{padding:76px 0 44px;border-bottom:1px solid var(--sep);margin-bottom:46px}
.kicker{font-size:12px;font-weight:600;letter-spacing:.09em;text-transform:uppercase;color:var(--accent);margin-bottom:14px}
.hero h1{font-size:clamp(36px,5.2vw,58px);line-height:1.05;letter-spacing:-.028em;font-weight:700}
.hero .sub{font-size:clamp(19px,2.2vw,24px);line-height:1.32;letter-spacing:-.017em;color:var(--text-2);margin-top:16px;max-width:30ch;font-weight:400}
.hero .meta{display:flex;flex-wrap:wrap;gap:10px;margin-top:26px}
.hero .meta span{
  font-size:12.5px;color:var(--text-2);background:var(--bg-2);
  border-radius:980px;padding:5px 13px;letter-spacing:-.01em;white-space:nowrap;
}
.main h1{
  font-size:clamp(30px,3.6vw,42px);line-height:1.08;letter-spacing:-.024em;font-weight:700;
  margin:70px 0 10px;scroll-margin-top:calc(var(--bar) + 20px);
}
.main h1:first-of-type{margin-top:10px}
.main h2{
  font-size:clamp(22px,2.5vw,29px);line-height:1.16;letter-spacing:-.019em;font-weight:700;
  margin:46px 0 14px;scroll-margin-top:calc(var(--bar) + 20px);
}
.main h3{
  font-size:19px;line-height:1.28;letter-spacing:-.013em;font-weight:600;
  margin:32px 0 10px;scroll-margin-top:calc(var(--bar) + 20px);
}
.main p{font-size:17px;line-height:1.62;margin:0 0 15px;max-width:74ch}
.main ul,.main ol{margin:0 0 17px 23px;font-size:17px;line-height:1.6}
.main li{margin-bottom:7px}
.main li>ul,.main li>ol{margin-top:7px}
.main strong{font-weight:600}
.main em{font-style:italic}
.main hr{border:none;border-top:1px solid var(--sep);margin:60px 0}

/* tables — hairline, no vertical rules */
.tablewrap{overflow-x:auto;margin:20px 0 26px;border:1px solid var(--sep);border-radius:var(--r-sm);-webkit-overflow-scrolling:touch}
.main table{width:100%;border-collapse:collapse;font-size:14.5px;letter-spacing:-.006em;min-width:540px;background:var(--bg)}
.main th{
  text-align:left;font-size:11.5px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;
  color:var(--text-2);background:var(--bg-2);padding:12px 15px;white-space:nowrap;
  position:sticky;top:0;z-index:1;border-bottom:1px solid var(--sep);
}
.main td{padding:12px 15px;border-top:1px solid var(--sep-2);vertical-align:top;line-height:1.5}
.main tbody tr:first-child td{border-top:none}
.main td strong{font-weight:600;color:var(--text)}

/* code + blueprint diagrams */
.main pre{
  background:var(--bg-2);border-radius:var(--r-sm);padding:20px 22px;margin:20px 0 26px;
  overflow-x:auto;font-family:var(--mono);font-size:12.5px;line-height:1.52;letter-spacing:0;
  color:var(--text);-webkit-overflow-scrolling:touch;
}
.main pre code{background:none;padding:0;font-size:inherit}
.main code{font-family:var(--mono);font-size:.88em;background:var(--bg-2);padding:2px 6px;border-radius:6px;letter-spacing:0}

/* callouts */
.main blockquote{
  background:var(--bg-2);border-radius:var(--r);padding:20px 24px;margin:22px 0 28px;
  max-width:74ch;
}
.main blockquote p{font-size:16px;line-height:1.58;margin:0;color:var(--text-2)}
.main blockquote p+p{margin-top:10px}
.main blockquote strong{color:var(--text);font-weight:600}

@media (max-width:980px){
  .shell{grid-template-columns:1fr}
  #navtoggle{display:inline-flex;align-items:center}
  .sidebar{
    position:fixed;top:var(--bar);left:0;right:0;bottom:0;height:auto;width:100%;max-width:none;
    background:var(--bg);border-right:none;z-index:55;padding:20px 22px 80px;
    transform:translateX(-100%);transition:transform .34s cubic-bezier(.32,.72,0,1);
  }
  .sidebar.open{transform:none}
  .main{padding:0 22px 110px;max-width:none}
  .hero{padding:44px 0 32px;margin-bottom:34px}
  .main h1{margin-top:52px}
}
@media print{
  .topbar,.sidebar,.navsearch{display:none!important}
  .shell{display:block;padding-top:0;max-width:none}
  .main{max-width:none;padding:0}
  body{font-size:10.5pt;background:#fff;color:#000}
  .hero{padding-top:0;border-color:#ccc}
  .main h1{page-break-before:always;page-break-after:avoid;font-size:20pt}
  .main h1:first-of-type{page-break-before:avoid}
  .main h2,.main h3{page-break-after:avoid}
  .main pre,.tablewrap,.main blockquote{page-break-inside:avoid}
  .main pre,.main blockquote,.main th{background:#f2f2f2}
  a{color:#000;text-decoration:none}
  .hero .meta span{border:1px solid #ddd;background:none}
}
</style>
</head>
<body>

<div class="topbar">
  <button class="iconbtn" id="navtoggle" aria-label="Contents">Contents</button>
  <span class="mark">__TITLE__</span>
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
  </main>
</div>

<script>
(function(){
  var root=document.documentElement;

  /* appearance: system → explicit choice once the reader makes one */
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

  /* wide tables scroll, never break the measure */
  document.querySelectorAll(".main table").forEach(function(t){
    if(t.parentElement.classList.contains("tablewrap"))return;
    var w=document.createElement("div");w.className="tablewrap";
    t.parentNode.insertBefore(w,t);w.appendChild(t);
  });

  /* mobile contents */
  var sb=document.getElementById("sidebar");
  document.getElementById("navtoggle").addEventListener("click",function(){sb.classList.toggle("open");});
  sb.addEventListener("click",function(e){if(e.target.tagName==="A")sb.classList.remove("open");});

  /* filter */
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

  /* scroll-spy */
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
      if(r.top<sr.top||r.bottom>sr.bottom){
        sb.scrollTop+=(r.top-sr.top)-sr.height/2+r.height/2;
      }
    }
  }
  if("IntersectionObserver" in window){
    var io=new IntersectionObserver(function(entries){
      entries.forEach(function(en){ if(en.isIntersecting) activate(en.target.id); });
    },{rootMargin:"-"+52+"px 0px -72% 0px",threshold:0});
    targets.forEach(function(t){io.observe(t);});
  }

  /* keyboard: / focuses the filter */
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
        .replace("__TITLE__", title)
        .replace("__SUBTITLE__", subtitle)
        .replace("__VERSION__", VERSION)
        .replace("__NAV__", nav_html)
        .replace("__BODY__", html_body))
OUT.write_text(html, encoding="utf-8")
n_nav = nav_html.count('class="nava')
n_grp = nav_html.count("navgroup")
print(f"wrote {OUT} ({len(html):,} bytes) · nav items: {n_nav} · groups: {n_grp}")
