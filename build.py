# -*- coding: utf-8 -*-
"""Genera el lloc estàtic a ./site a partir de pages.py i home_main.html.

Ús:  python3 build.py
Per editar textos: modifica pages.py (subpàgines) o home_main.html (portada) i torna a executar.
"""
import os, re
from pages import PAGES, NEWSLETTER

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
LOGO = "https://www.parroquiasarria.net/wp-content/uploads/2016/09/logo-parroquia-v.png"
FAVICON = "https://www.parroquiasarria.net/wp-content/uploads/2016/07/cropped-STVICENÇ_favicon-270x270.png"
SITE = "Parròquia de Sant Vicenç de Sarrià"

# Menú (text idèntic a l'original). href local = slug.html; externs amb http.
MENU = [
    ("Actualitat", "index.html#actualitat", None),
    ("Parròquia", "parroquia.html", [
        ("Benvingut", "benvingut"), ("Història i Art", "historia-i-art"),
        ("SANT VICENÇ", "sant-vicenc"), ("SANTA EULÀLIA", "santa-eulalia"),
        ("Memorial Pere Tarrés", "https://www.causaperetarres.com")]),
    ("Sagraments", "sagraments.html", [
        ("Catecumenat", "catecumenat"), ("Catecumenat Adults", "catecumenat-adults"),
        ("Baptisme", "baptisme"), ("Eucaristia", "eucaristia"), ("Confirmació", "confirmacio"),
        ("Matrimoni", "matrimoni"), ("Unció de malalts", "uncio-de-malalts")]),
    ("Grups", "grups.html", [
        ("Catequesis Infants", "catequesis-infants"), ("Catequesis Confirmació", "catequesis-confirmacio"),
        ("Postconfirmació", "postconfirmacio"), ("Cercle Estudis", "cercle-estudis"),
        ("Esplai", "esplai"), ("Càritas", "caritas")]),
    ("Entitats", "#", [
        ("Capella Música", "http://www.cordyapason.cat/"),
        ("Assís Centre d’acollida", "http://www.assis.cat/"),
        ("Centre de Sarrià", "http://www.centredesarria.entitatsbcn.net/"),
        ("CP Sarrià", "http://www.cpsarria.cat/"),
        ("Teatre de Sarrià", "http://teatredesarria.barcelona.ppe.entitats.diba.cat/")]),
    ("Horaris", "horaris.html", None),
    ("Contacte", "contacte.html", None),
    ("Donatius", "donatius.html", None),  # CTA
]
SECTIONS = {m[1].replace(".html", ""): (m[0], m[2]) for m in MENU if m[2] and m[1] != "#"}


def href(target):
    return target if target.startswith(("http", "#", "index.html")) else target + ".html"


def ext_attrs(target):
    return ' target="_blank" rel="noopener"' if target.startswith("http") else ""


def nav(current, section):
    out = []
    for label, link, sub in MENU:
        slug = link.replace(".html", "")
        top_active = current == slug or section == slug
        cls = []
        if sub: cls.append("has-sub")
        if label == "Donatius": cls.append("cta")
        li = f'<li{" class=%s" % chr(34) + " ".join(cls) + chr(34) if cls else ""}>'
        a = f'<a href="{link}"{" class=\"active\"" if top_active else ""}>{label}</a>'
        if sub:
            items = "".join(
                f'<li><a href="{href(t)}"{ext_attrs(t)}{" class=\"active\"" if t == current else ""}>{l}</a></li>'
                for l, t in sub)
            out.append(f'{li}{a}\n<ul class="sub">{items}</ul></li>')
        else:
            out.append(f"{li}{a}</li>")
    return "\n".join(out)


def head(title, desc=""):
    d = f'\n<meta name="description" content="{desc}">' if desc else ""
    return f"""<!doctype html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>{d}
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
"""


def header(current, section):
    return f"""<div class="topbar">
  <div class="wrap">
    <div class="contact-mini">
        <span>TEL. 932 030 907</span>
<span>santvicenc181@arqbcn.cat</span>
</div>
    <form class="search" role="search" action="https://www.google.com/search" method="get">
      <label for="s">Cerca:</label>
      <input id="s" type="search" name="q">
      <input type="hidden" name="sitesearch" value="parroquiasarria.net">
    </form>
  </div>
</div>
<header class="site">
  <div class="wrap">
    <a class="logo" href="index.html"><img src="{LOGO}" alt="{SITE}"></a>
    <button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="main" aria-label="Menú principal"><ul>
{nav(current, section)}
    </ul></nav>
  </div>
</header>
"""


FOOTER = f"""<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="logo-f" href="index.html"><img src="{LOGO}" alt="{SITE}"></a>
        <p>C/Rector Voltà 5, 08034 BARCELONA<br><a href="tel:932030907">TEL. 932 030 907</a><br><a href="mailto:santvicenc181@arqbcn.cat">santvicenc181@arqbcn.cat</a></p>
      </div>
      <div><h5>Parròquia</h5><ul>
        <li><a href="benvingut.html">Benvingut</a></li><li><a href="historia-i-art.html">Història i Art</a></li>
        <li><a href="horaris.html">Horaris</a></li><li><a href="donatius.html">Donatius</a></li><li><a href="contacte.html">Contacte</a></li></ul></div>
      <div><h5>Sagraments</h5><ul>
        <li><a href="baptisme.html">Baptisme</a></li><li><a href="eucaristia.html">Eucaristia</a></li>
        <li><a href="confirmacio.html">Confirmació</a></li><li><a href="matrimoni.html">Matrimoni</a></li><li><a href="uncio-de-malalts.html">Unció de malalts</a></li></ul></div>
      <div><h5>Grups</h5><ul>
        <li><a href="catequesis-infants.html">Catequesis Infants</a></li><li><a href="postconfirmacio.html">Postconfirmació</a></li>
        <li><a href="cercle-estudis.html">Cercle Estudis</a></li><li><a href="esplai.html">Esplai</a></li><li><a href="caritas.html">Càritas</a></li></ul></div>
    </div>
    <div class="copy">
      <span>Parròquia de Sarrià, 2016. © Tots els drets reservats</span>
      <a class="to-top" href="#" aria-label="Amunt">↑</a>
    </div>
  </div>
</footer>
<script src="assets/main.js"></script>
</body>
</html>
"""

SIDEBAR = f"""<aside class="side">
  <div class="side-news">
    <h2>Full Parroquial Digital</h2>
    <p>Vols rebre la newsletter per estar al corrent de les notícies, celebracions i activitats de la parròquia? Fes clic a la imatge del "Full Parroquial" que tens a sobre i inscriu-t'hi!</p>
    <a class="btn" href="{NEWSLETTER}" target="_blank" rel="noopener">Full Parroquial</a>
  </div>
  <div class="card">
    <h2>CONTACTE</h2>
    <p>OBERTURA ESGLÉSIA<br>Dilluns a Divendres 7.30 a 21h<br>Dissabtes 7.30 a 14h i 17 a 20.30h<br>Diumenges 9 a 14h i 17 a 21h</p>
    <p>C/Rector Voltà 5, 08034 BARCELONA</p>
    <a class="tel" href="tel:932030907">TEL. 932 030 907</a>
    <a class="mail" href="mailto:santvicenc181@arqbcn.cat">santvicenc181@arqbcn.cat</a>
  </div>
  <div class="card">
    <h2>MISSES</h2>
    <p><strong>Feiners:</strong> 8 (8.30 festius civils), 10 i 20.15h (vigilies de solemnitat no coincideix amb dissabte)</p>
    <p><strong>Dissabtes:</strong> 8, 10 i 19.15h</p>
    <p><strong>Diumenges:</strong> 10, 11.30, 13 i 20.15h (cast)</p>
    <p><strong>Diumenges juliol i agost:</strong> 10, 11.30 i 20.15h (cast)</p>
    <p><strong>Feiners agost:</strong> 10 i 20.15h</p>
  </div>
  <div class="card">
    <h2>CONFESSIONS</h2>
    <p><strong>Feiners:</strong> de 8.30 a 10h i de 19.45 a 20.15h</p>
    <p><strong>Diumenges i festius:</strong> 1/4h abans de cada Missa</p>
  </div>
  <div class="card">
    <h2>DESPATX PARROQUIAL</h2>
    <p><strong>Dilluns, dimecres i divendres:</strong><br>de 17.30 a 20h, <em>excepte vigílies i festius</em></p>
    <p><strong>JULIOL i AGOST, dimecres:</strong><br>de 17.30 a 20h, <em>excepte vigílies i festius</em></p>
  </div>
</aside>"""


def child_grid(section, current=None):
    _, items = SECTIONS[section]
    cards = []
    for label, t in items:
        cls = "child"
        if t.startswith("http"): cls += " ext"
        if t == current: cls += " current"
        cards.append(f'<a class="{cls}" href="{href(t)}"{ext_attrs(t)}>{label}</a>')
    return '<div class="child-grid">' + "".join(cards) + "</div>"


def render_page(slug, p):
    section = p.get("section")
    idx = p.get("index")
    crumbs = ['<a href="index.html">Inici</a>']
    if section:
        crumbs.append(f'<a href="{section}.html">{SECTIONS[section][0]}</a>')
    crumbs.append(f'<span aria-current="page">{p["title"]}</span>')
    crumbs_html = ' <span aria-hidden="true">/</span> '.join(crumbs)

    blocks = []
    if p["body"].strip():
        blocks.append(f'<article class="prose reveal">{p["body"]}</article>')
    if idx:
        blocks.append(f'<div class="reveal">{child_grid(idx)}</div>')
    if section:
        blocks.append(f'<div class="related reveal"><h2>{SECTIONS[section][0]}</h2>{child_grid(section, slug)}</div>')

    html = head(f"{p['title']} - {SITE}")
    html += header(slug, section)
    html += f"""<div class="page-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Ruta">{crumbs_html}</nav>
    <h1>{p['title']}</h1>
  </div>
</div>
<div class="wrap layout">
  <main>
{chr(10).join(blocks)}
  </main>
  {SIDEBAR}
</div>
"""
    html += FOOTER
    return html


def render_home():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "home_main.html"), encoding="utf-8") as f:
        main = f.read()
    html = head(f"{SITE} | {SITE}",
                "La parròquia de Sant Vicenç de Sarrià,lloc de pregària, en el qual s’aplega per a l’Eucaristia i els altres sagraments la comunitat cristiana d’avui.")
    html += header("index", None) + main + "\n" + FOOTER
    return html


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_home())
    for slug, p in PAGES.items():
        with open(os.path.join(OUT, slug + ".html"), "w", encoding="utf-8") as f:
            f.write(render_page(slug, p))
    print(f"{len(PAGES) + 1} pàgines generades a {OUT}")
