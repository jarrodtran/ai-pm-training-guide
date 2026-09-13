/* Course-page structure helper: builds the "On this page" bar, module anchors,
   section anchors, and next-module links. Loaded by every course page. */
(function(){
  function ready(fn){
    if(document.readyState !== "loading"){ fn(); }
    else { document.addEventListener("DOMContentLoaded", fn); }
  }
  ready(function(){
    var mods = Array.prototype.slice.call(document.querySelectorAll(".mod"));
    if(!mods.length){ return; }

    /* give every module an id from its number (M1 → #m1) */
    mods.forEach(function(m){
      if(!m.id){
        var no = m.querySelector(".no");
        if(no){
          var t = no.textContent.trim().toLowerCase();
          if(/^m\d+$/.test(t)){ m.id = t; }
        }
      }
    });

    /* tag sections by their overline label */
    function tagSection(re, id){
      var secs = Array.prototype.slice.call(document.querySelectorAll("section"));
      for(var i=0;i<secs.length;i++){
        var ov = secs[i].querySelector(".overline");
        if(ov && re.test(ov.textContent)){ secs[i].id = id; return true; }
      }
      return false;
    }
    tagSection(/^Deliverables/i, "deliverables");
    tagSection(/^Assessment/i, "assessment");
    tagSection(/^Final/i, "final");

    /* "On this page" bar, inserted under the header */
    var toc = document.createElement("div");
    toc.className = "toc";
    var html = "<span class='tl'>On this page:</span>";
    mods.forEach(function(m){ html += "<a href='#"+m.id+"'>"+m.id.toUpperCase()+"</a>"; });
    if(document.getElementById("deliverables")){ html += "<a href='#deliverables'>Deliverables</a>"; }
    if(document.getElementById("assessment")){ html += "<a href='#assessment'>Assessment</a>"; }
    if(document.getElementById("final")){ html += "<a href='#final'>Final</a>"; }
    toc.innerHTML = html;
    var header = document.querySelector("header.chead");
    if(header && header.parentNode){ header.parentNode.insertBefore(toc, header.nextSibling); }

    /* "Next: M# →" link at the foot of every module but the last */
    for(var i=0;i<mods.length-1;i++){
      var nx = mods[i+1];
      var mt = nx.querySelector(".mt");
      var a = document.createElement("div");
      a.className = "nextm";
      a.innerHTML = "<a href='#"+nx.id+"'>Next: "+(mt ? mt.textContent : nx.id.toUpperCase()) + " →</a>";
      mods[i].appendChild(a);
    }
  });
})();
