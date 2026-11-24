"""Pagine per Google: una per ogni pedale (inglese e italiano), una per lingua (es, fr, de, pt) e la sitemap.

Uso:  python3 tools/pagine_seo.py        (dalla cartella principale del repository)
Scrive docs/pedals/<pedale>/, docs/it/pedali/<pedale>/, docs/pedals/, docs/it/pedali/, docs/es|fr|de|pt/ e docs/sitemap.xml.
Lo stile è quello di docs/index.html.  Le pagine si rifanno ogni volta da qui: non modificarle a mano.
"""
import datetime, html, json, os, re

SITE = "https://francescorizzo-cyber.github.io/patchpilot/"
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs")
TODAY = datetime.date.today().isoformat()
RELEASES = "https://github.com/francescorizzo-cyber/patchpilot/releases/latest"

STYLE = re.search(r"<style>.*?</style>", open(os.path.join(ROOT, "index.html"), encoding="utf-8").read(), re.S).group(0)

# nome, tipo, basso
PEDALS = [
    ("Zoom MS-50G", "classic_t", False),
    ("Zoom MS-60B", "classic", True), ("Zoom MS-70CDR", "classic", False),
    ("Zoom G1on", "classic", False), ("Zoom G1Xon", "classic", False), ("Zoom B1on", "classic", True), ("Zoom B1Xon", "classic", True),
    ("Zoom G3", "classic", False), ("Zoom G3X", "classic", False), ("Zoom B3", "classic", True),
    ("Zoom MS-50G+", "plus", False), ("Zoom MS-60B+", "plus", True), ("Zoom MS-70CDR+", "plus", False),
    ("Zoom MS-80IR+", "plus", False), ("Zoom MS-200D+", "plus", False), ("Zoom MS-90LP+", "plus", False),
    ("Zoom G2 FOUR", "four", False), ("Zoom G2X FOUR", "four", False), ("Zoom B2 FOUR", "four", True),
    ("Zoom G1 FOUR", "fourc", False), ("Zoom G1X FOUR", "fourc", False), ("Zoom B1 FOUR", "fourc", True), ("Zoom B1X FOUR", "fourc", True),
    ("Zoom G3n", "fourc", False), ("Zoom G3Xn", "fourc", False), ("Zoom G5n", "fourc", False), ("Zoom B3n", "fourc", True),
    ("Zoom G6", "g", False), ("Zoom G11", "g", False), ("Zoom B6", "g", True),
    ("Boss Katana MkII", "brand", False), ("Boss GT-100", "brand", False), ("Boss GT-1000 / GT-1000CORE", "brand", False),
    ("Valeton GP-200", "brand", False), ("Boss Katana MkI", "brand_m", False), ("NUX Mighty Lite BT MkII", "brand_m", False),
    ("Line 6 HX Stomp", "midi", False),
]


def slug(name):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", name.lower().replace("+", " plus").replace("/", " "))).strip("-")


def short(name):
    return name.split(" / ")[0]


# ------------------------------------------------------------------ testi per tipo di pedale

CAP = {
    "en": {
        "classic_t": dict(rec="✅", read="✅ all 50 patches", backup="✅ all patches, at every connection", sets="✅ effects, switches and knobs in one go — it can also add or swap effects", tuner="—", status="✅ tested on a real pedal (firmware 3.10)"),
        "classic": dict(rec="✅", read="✅ all patches", backup="✅ all patches, at every connection", sets="✅ effects, switches and knobs in one go — it can also add or swap effects", tuner="—", status="🧪 in test: works like the MS-50G, with a “send the log” button"),
        "plus": dict(rec="✅", read="✅ all patches", backup="✅ all patches, at first connection", sets="✅ knobs, switches and effects, one change at a time", tuner="✅", status="🧪 in test"),
        "four": dict(rec="✅", read="✅ all patches", backup="✅ all patches, at first connection", sets="✅ knobs, switches and effects, one change at a time", tuner="✅", status="🧪 in test"),
        "fourc": dict(rec="✅", read="✅ all patches", backup="✅ all patches, at first connection", sets="✅ knobs, switches and effects, one change at a time", tuner="—", status="🧪 in test"),
        "g": dict(rec="choose it once", read="✅ all patches", backup="✅ all patches, at first connection", sets="✅ knobs, switches and effects, one change at a time", tuner="—", status="🧪 not yet tried on a real pedal"),
        "brand": dict(rec="✅", read="✅ the patch in use", backup="✅ the patch in use", sets="✅ knobs and switches, one change at a time", tuner="—", status="🧪 in test"),
        "brand_m": dict(rec="choose it once", read="✅ the patch in use", backup="✅ the patch in use", sets="✅ knobs and switches, one change at a time", tuner="—", status="🧪 in test"),
        "midi": dict(rec="—", read="—", backup="—", sets="patch change for each song of the setlist (standard MIDI)", tuner="—", status="standard MIDI"),
    },
    "it": {
        "classic_t": dict(rec="✅", read="✅ tutte le 50 patch", backup="✅ tutte le patch, a ogni collegamento", sets="✅ effetti, interruttori e manopole in un colpo — può anche aggiungere o sostituire effetti", tuner="—", status="✅ provato su un pedale vero (firmware 3.10)"),
        "classic": dict(rec="✅", read="✅ tutte le patch", backup="✅ tutte le patch, a ogni collegamento", sets="✅ effetti, interruttori e manopole in un colpo — può anche aggiungere o sostituire effetti", tuner="—", status="🧪 in prova: funziona come l'MS-50G, con il pulsante «invia il registro»"),
        "plus": dict(rec="✅", read="✅ tutte le patch", backup="✅ tutte le patch, al primo collegamento", sets="✅ manopole, interruttori ed effetti, un cambio alla volta", tuner="✅", status="🧪 in prova"),
        "four": dict(rec="✅", read="✅ tutte le patch", backup="✅ tutte le patch, al primo collegamento", sets="✅ manopole, interruttori ed effetti, un cambio alla volta", tuner="✅", status="🧪 in prova"),
        "fourc": dict(rec="✅", read="✅ tutte le patch", backup="✅ tutte le patch, al primo collegamento", sets="✅ manopole, interruttori ed effetti, un cambio alla volta", tuner="—", status="🧪 in prova"),
        "g": dict(rec="si sceglie una volta", read="✅ tutte le patch", backup="✅ tutte le patch, al primo collegamento", sets="✅ manopole, interruttori ed effetti, un cambio alla volta", tuner="—", status="🧪 non ancora provato su un pedale vero"),
        "brand": dict(rec="✅", read="✅ la patch in uso", backup="✅ la patch in uso", sets="✅ manopole e interruttori, un cambio alla volta", tuner="—", status="🧪 in prova"),
        "brand_m": dict(rec="si sceglie una volta", read="✅ la patch in uso", backup="✅ la patch in uso", sets="✅ manopole e interruttori, un cambio alla volta", tuner="—", status="🧪 in prova"),
        "midi": dict(rec="—", read="—", backup="—", sets="cambio patch per ogni brano della scaletta (MIDI standard)", tuner="—", status="MIDI standard"),
    },
}

T = {
    "en": dict(
        lang="en", home=SITE, list_url=SITE + "pedals/", list_dir="pedals", other="it",
        title="{m} editor for Android, Windows, Mac & Linux – AI tone coach, patch backup | PatchPilot",
        desc="Free {m} editor: PatchPilot recognises your {m}, backs up your patches and sets the sound you describe — “warmer”, “more reverb”, “80s delay” — right on the pedal. AI coach, offline for simple things and online for complex ones, in 10 languages, tone from a song. Android, Windows, macOS, Linux.",
        h1="{m} editor and AI tone coach",
        lead="Plug your <strong>{m}</strong> into your phone or computer with the USB cable: PatchPilot recognises it, <strong>saves a backup</strong> and lets you <strong>describe the sound</strong> — <span class=say>warmer</span> <span class=say>more reverb</span> <span class=say>80s delay</span> — then sets it on the pedal. No menus, no manual.",
        lead_midi="PatchPilot changes the patch of your <strong>{m}</strong> for every song of your setlist, with standard MIDI messages: in stage mode you see the song in big letters and the pedal follows.",
        bass=" A bass multi-effects pedal: the coach talks about lows, mids and highs just the same.",
        what="What PatchPilot does on the {m}",
        rows=["Recognised by itself", "Reads the patches", "Automatic backup", "PatchPilot sets the sound", "Tuner", "Status"],
        talk="Talk to it",
        talk_p="With the AI coach, write the way you'd talk to a guitarist friend: <span class=say>70s crunch</span> <span class=say>bright clean for arpeggios</span> <span class=say>too muddy</span> <span class=say>like before but cleaner</span>. Simple things are done by the <strong>offline AI</strong> on the phone, with no internet and for free; complex ones by the <strong>online AI</strong>. In 10 languages: <span class=say>more distorted</span> <span class=say>delay at 120 bpm, dotted eighths</span> <span class=say>turn off the chorus</span> <span class=say>delay mix to 30%</span>.",
        safe="Your saved sounds are never overwritten: PatchPilot changes the patch in use, like turning the pedal's own knobs. Factory reset and file deletion are blocked forever.",
        dl="Download for Windows · Mac · Linux", android="Android: coming soon on Google Play", more="Everything PatchPilot does",
        others="Other supported pedals", all="All 37 supported pedals",
        faq=[("Is there an Android app for the {m}?", "Yes: PatchPilot for Android recognises the {m} as soon as you plug in the USB-C / OTG cable, with the AI sound coach (offline for simple things, online for complex ones) and tone from a song. It is coming soon on Google Play; today PatchPilot runs on Windows, macOS and Linux."),
             ("Can I back up my {m} patches?", "Yes. {backup}. The backup is a file with date and time that you can export and share."),
             ("Is PatchPilot made by the pedal maker?", "No. PatchPilot is an independent project, not affiliated with Zoom, Boss/Roland, Valeton, NUX or Line 6.")],
        list_title="Supported pedals: Zoom, Boss, Valeton, NUX, Line 6 – editor and AI tone coach | PatchPilot",
        list_desc="All 37 pedals PatchPilot supports: Zoom MultiStomp, MultiStomp+, G1on, G3, G1/B1 FOUR, G2 FOUR, G3n, G5n, G6, G11, B6, Boss Katana, GT-100, GT-1000, Valeton GP-200, NUX Mighty Lite, Line 6 HX Stomp. Editor, backup and AI tone coach.",
        list_h1="Supported pedals", list_lead="Choose your pedal to see what PatchPilot does with it.",
        home_name="PatchPilot", indep="PatchPilot is an independent project, not affiliated with ZOOM Corporation, Boss/Roland, Valeton, NUX or Line 6. Brand and model names are trademarks of their owners.",
    ),
    "it": dict(
        lang="it", home=SITE + "it/", list_url=SITE + "it/pedali/", list_dir="it/pedali", other="en",
        title="Editor {m} per Android, Windows, Mac e Linux – coach del suono AI, backup patch | PatchPilot",
        desc="Editor gratuito per {m}: PatchPilot riconosce il tuo {m}, fa il backup delle patch e imposta il suono che descrivi — «più caldo», «più riverbero», «delay anni '80» — direttamente sul pedale. Coach AI offline per le cose semplici e online per quelle complesse, in 10 lingue, suono da un brano. Android, Windows, macOS, Linux.",
        h1="Editor {m} e coach del suono con l'AI",
        lead="Collega il tuo <strong>{m}</strong> al telefono o al computer con il cavo USB: PatchPilot lo riconosce, <strong>salva il backup</strong> e ti lascia <strong>descrivere il suono</strong> — <span class=say>più caldo</span> <span class=say>più riverbero</span> <span class=say>delay anni '80</span> — poi lo imposta sul pedale. Niente menu, niente manuale.",
        lead_midi="PatchPilot cambia la patch del tuo <strong>{m}</strong> per ogni brano della scaletta, con i messaggi MIDI standard: in modalità palco vedi il brano a caratteri grandi e il pedale segue.",
        bass=" È un multieffetto per basso: il coach parla di bassi, medi e alti allo stesso modo.",
        what="Cosa fa PatchPilot sul {m}",
        rows=["Si riconosce da solo", "Legge le patch", "Backup automatico", "PatchPilot imposta il suono", "Accordatore", "Stato"],
        talk="Parlagli",
        talk_p="Con il coach AI scrivi come parleresti a un amico chitarrista: <span class=say>crunch anni '70</span> <span class=say>pulito brillante per arpeggi</span> <span class=say>troppo impastato</span> <span class=say>come prima ma più pulito</span>. Le cose semplici le fa l'<strong>AI offline</strong> sul telefono, senza internet e gratis; quelle complesse l'<strong>AI online</strong>. In 10 lingue: <span class=say>più distorto</span> <span class=say>delay a 120 bpm ottavi puntati</span> <span class=say>spegni il chorus</span> <span class=say>Mix del delay al 30%</span>.",
        safe="I suoni che hai salvato non vengono mai sovrascritti: PatchPilot cambia la patch in uso, come girare le manopole del pedale. Ripristino di fabbrica e cancellazione di file sono bloccati per sempre.",
        dl="Scarica per Windows · Mac · Linux", android="Android: presto su Google Play", more="Tutto quello che fa PatchPilot",
        others="Altri pedali supportati", all="Tutti i 37 pedali supportati",
        faq=[("Esiste un'app Android per il {m}?", "Sì: PatchPilot per Android riconosce il {m} appena colleghi il cavo USB-C / OTG, con il coach del suono AI (offline per le cose semplici, online per quelle complesse) e il suono da un brano. Arriva presto su Google Play; oggi PatchPilot funziona su Windows, macOS e Linux."),
             ("Posso fare il backup delle patch del {m}?", "Sì. {backup}. Il backup è un file con data e ora che puoi esportare e condividere."),
             ("PatchPilot è fatto dal produttore del pedale?", "No. PatchPilot è un progetto indipendente, non collegato a Zoom, Boss/Roland, Valeton, NUX o Line 6.")],
        list_title="Pedali supportati: Zoom, Boss, Valeton, NUX, Line 6 – editor e coach del suono AI | PatchPilot",
        list_desc="Tutti i 37 pedali supportati da PatchPilot: Zoom MultiStomp, MultiStomp+, G1on, G3, G1/B1 FOUR, G2 FOUR, G3n, G5n, G6, G11, B6, Boss Katana, GT-100, GT-1000, Valeton GP-200, NUX Mighty Lite, Line 6 HX Stomp. Editor, backup e coach del suono AI.",
        list_h1="Pedali supportati", list_lead="Scegli il tuo pedale per vedere cosa fa PatchPilot.",
        home_name="PatchPilot", indep="PatchPilot è un progetto indipendente, non collegato a ZOOM Corporation, Boss/Roland, Valeton, NUX o Line 6. I nomi di marchi e modelli appartengono ai rispettivi proprietari.",
    ),
}

BACKUP_SENTENCE = {
    "en": {"classic_t": "PatchPilot reads all 50 patches and saves a backup at every connection", "classic": "PatchPilot reads all the patches and saves a backup at every connection",
           "plus": "At the first connection PatchPilot reads all the patches and saves a backup", "four": "At the first connection PatchPilot reads all the patches and saves a backup",
           "fourc": "At the first connection PatchPilot reads all the patches and saves a backup", "g": "At the first connection PatchPilot reads all the patches and saves a backup",
           "brand": "PatchPilot saves the patch in use before changing it", "brand_m": "PatchPilot saves the patch in use before changing it", "midi": "This pedal only receives patch changes, so there is nothing to back up"},
    "it": {"classic_t": "PatchPilot legge tutte le 50 patch e salva il backup a ogni collegamento", "classic": "PatchPilot legge tutte le patch e salva il backup a ogni collegamento",
           "plus": "Al primo collegamento PatchPilot legge tutte le patch e salva il backup", "four": "Al primo collegamento PatchPilot legge tutte le patch e salva il backup",
           "fourc": "Al primo collegamento PatchPilot legge tutte le patch e salva il backup", "g": "Al primo collegamento PatchPilot legge tutte le patch e salva il backup",
           "brand": "PatchPilot salva la patch in uso prima di cambiarla", "brand_m": "PatchPilot salva la patch in uso prima di cambiarla", "midi": "Questo pedale riceve solo i cambi patch, quindi non c'è niente da salvare"},
}

E = html.escape


def head(lang, title, desc, url, alternates, ld):
    alt = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{u}">' for l, u in alternates)
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{url}">
{alt}
<link rel="icon" href="{SITE}img/icona.png">
<meta property="og:type" content="website">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="{SITE}img/patchpilot-zoom-pedal-editor-windows-mac-linux.jpg">
<meta property="og:site_name" content="PatchPilot">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=1)}
</script>
{STYLE}
</head>
<body>
"""


def nav(t, other_url, other_label):
    return (f'<nav><div class="in"><img src="{SITE}img/icona.png" width="30" height="30" alt=""><b>PATCHPILOT</b>'
            f'<a href="{t["home"]}">{"Home"}</a><a href="{t["list_url"]}">{t["list_h1"]}</a>'
            f'<a href="{t["home"]}#senza-ai">{"Coach"}</a><span class="sp"></span><a href="{other_url}">{other_label}</a></div></nav>\n')


def foot(t):
    return (f'<footer><p><a href="https://github.com/francescorizzo-cyber/patchpilot">GitHub</a> · <a href="{SITE}privacy.html">Privacy</a> · '
            f'<a href="mailto:autofonic.mixer@gmail.com">autofonic.mixer@gmail.com</a> · '
            f'<a href="{SITE}">English</a> · <a href="{SITE}it/">Italiano</a> · <a href="{SITE}es/">Español</a> · <a href="{SITE}fr/">Français</a> · '
            f'<a href="{SITE}de/">Deutsch</a> · <a href="{SITE}pt/">Português</a></p><p>{t["indep"]}<br>Made by Francesco Rizzo.</p></footer>\n</main>\n</body>\n</html>\n')


def app_ld(t, url, name_extra):
    return {"@type": "SoftwareApplication", "name": "PatchPilot", "url": url,
            "operatingSystem": "Android, Windows, macOS, Linux", "applicationCategory": "MultimediaApplication",
            "applicationSubCategory": f"{name_extra} editor and AI tone coach",
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
            "downloadUrl": RELEASES, "author": {"@type": "Person", "name": "Francesco Rizzo"},
            "inLanguage": ["en", "it", "es", "fr", "de", "pt", "sv", "da", "sl", "hr"]}


def write(rel, text):
    path = os.path.join(ROOT, rel, "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(text)


def pedal_page(lang, name, kind, bass):
    t, cap = T[lang], CAP[lang][kind]
    m = short(name)
    s = slug(name)
    url = SITE + ("pedals/" if lang == "en" else "it/pedali/") + s + "/"
    other = SITE + ("it/pedali/" if lang == "en" else "pedals/") + s + "/"
    faqs = [(q.format(m=m), a.format(m=m, backup=BACKUP_SENTENCE[lang][kind])) for q, a in t["faq"]]
    ld = {"@context": "https://schema.org", "@graph": [
        app_ld(t, url, m),
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "PatchPilot", "item": t["home"]},
            {"@type": "ListItem", "position": 2, "name": t["list_h1"], "item": t["list_url"]},
            {"@type": "ListItem", "position": 3, "name": name, "item": url}]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
    ]}
    alts = [("en", SITE + "pedals/" + s + "/"), ("it", SITE + "it/pedali/" + s + "/"), ("x-default", SITE + "pedals/" + s + "/")]
    out = [head(lang, t["title"].format(m=m), t["desc"].format(m=m), url, alts, ld),
           nav(t, other, "Italiano" if lang == "en" else "English"),
           '<div class="hero"><div class="in">',
           f'<p class="k"><a href="{t["list_url"]}">{t["list_h1"]}</a> › {E(name)}</p>',
           f'<h1>{E(t["h1"].format(m=name))}</h1>',
           f'<p class="lead">{(t["lead_midi"] if kind == "midi" else t["lead"]).format(m=E(m))}{t["bass"] if bass else ""}</p>',
           f'<div class="btns"><a class="btn" href="{RELEASES}">{t["dl"]}</a><span class="btn o">{t["android"]}</span><a class="btn o" href="{t["home"]}">{t["more"]}</a></div>',
           '</div></div>\n<main>',
           f'<h2>{E(t["what"].format(m=m))}</h2>',
           '<div class="tw"><table>']
    for label, key in zip(t["rows"], ["rec", "read", "backup", "sets", "tuner", "status"]):
        out.append(f'<tr><td><strong>{label}</strong></td><td>{cap[key]}</td></tr>')
    out.append('</table></div>')
    if kind != "midi":
        out += [f'<h2>{t["talk"]}</h2>', f'<p>{t["talk_p"]}</p>', f'<p class="note">🛡️ {t["safe"]}</p>']
    out.append('<h2>FAQ</h2>')
    for q, a in faqs:
        out.append(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>')
    out.append(f'<h2>{t["others"]}</h2><p>' + " · ".join(
        f'<a href="{t["list_url"]}{slug(n)}/">{E(n)}</a>' for n, _, _ in PEDALS if n != name) + "</p>")
    out.append(foot(t))
    write(("pedals/" if lang == "en" else "it/pedali/") + s, "\n".join(out))
    return url


def list_page(lang):
    t = T[lang]
    url = t["list_url"]
    other = SITE + ("it/pedali/" if lang == "en" else "pedals/")
    ld = {"@context": "https://schema.org", "@graph": [app_ld(t, url, "Zoom, Boss, Valeton, NUX"),
          {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "url": url + slug(n) + "/"} for i, (n, _, _) in enumerate(PEDALS)]}]}
    alts = [("en", SITE + "pedals/"), ("it", SITE + "it/pedali/"), ("x-default", SITE + "pedals/")]
    out = [head(lang, t["list_title"], t["list_desc"], url, alts, ld), nav(t, other, "Italiano" if lang == "en" else "English"),
           f'<div class="hero"><div class="in"><h1>{t["list_h1"]}</h1><p class="lead">{t["list_lead"]}</p></div></div>\n<main>',
           '<div class="tw"><table>', f'<tr><th>{t["list_h1"]}</th><th>{t["rows"][3]}</th><th>{t["rows"][5]}</th></tr>']
    for n, kind, _ in PEDALS:
        c = CAP[lang][kind]
        out.append(f'<tr><td><a href="{url}{slug(n)}/"><strong>{E(n)}</strong></a></td><td>{c["sets"]}</td><td>{c["status"]}</td></tr>')
    out += ['</table></div>', foot(t)]
    write(t["list_dir"], "\n".join(out))
    return url


# ------------------------------------------------------------------ pagine per lingua (dalla scheda dello store)

LANG_PAGES = {
    "es": dict(name="Español", h="Editor para pedales multiefectos con IA", dl="Descargar para Windows · Mac · Linux", android="Android: muy pronto en Google Play", pedals="Pedales compatibles",
               title="PatchPilot – editor de pedales Zoom, Boss, Valeton, NUX con IA: di el sonido y se ajusta en el pedal", sec="Español"),
    "fr": dict(name="Français", h="Éditeur de pédales multi-effets avec IA", dl="Télécharger pour Windows · Mac · Linux", android="Android : bientôt sur Google Play", pedals="Pédales compatibles",
               title="PatchPilot – éditeur pour pédales Zoom, Boss, Valeton, NUX avec IA : décris le son, il se règle sur la pédale", sec="Français"),
    "de": dict(name="Deutsch", h="Editor für Multieffektpedale mit KI", dl="Download für Windows · Mac · Linux", android="Android: bald bei Google Play", pedals="Unterstützte Pedale",
               title="PatchPilot – Editor für Zoom-, Boss-, Valeton- und NUX-Pedale mit KI: Sound beschreiben, das Pedal stellt sich ein", sec="Deutsch"),
    "pt": dict(name="Português", h="Editor de pedaleiras multiefeitos com IA", dl="Baixar para Windows · Mac · Linux", android="Android: em breve no Google Play", pedals="Pedaleiras compatíveis",
               title="PatchPilot – editor de pedaleiras Zoom, Boss, Valeton, NUX com IA: diga o som e ele se ajusta na pedaleira", sec="Português"),
}


def store_text(code):
    """Descrizione breve e completa della scheda Play in quella lingua (docs/play/SCHEDA_STORE_LINGUE.md del progetto sorgente, copiata in tools/)."""
    src = open(os.path.join(os.path.dirname(__file__), "scheda_store_lingue.md"), encoding="utf-8").read()
    head_word = {"es": "## Español", "fr": "## Français", "de": "## Deutsch", "pt": "## Português"}[code]
    sec = src.split(head_word, 1)[1].split("\n---", 1)[0]
    short_d = re.search(r"\(m[aá]x\.? 80\)\s*:?\s*\n`([^`]*)`", sec).group(1)
    full = re.split(r"\*\*[^*]+\*\*\s*:?\s*\n", sec)[-1].strip()
    return short_d, full


def md_to_html(text):
    out, items = [], []
    def flush():
        if items:
            out.append("<ul>" + "".join(f"<li>{E(i)}</li>" for i in items) + "</ul>")
            items.clear()
    for line in text.split("\n"):
        l = line.strip()
        if not l:
            flush(); continue
        if l.startswith("•"):
            items.append(l[1:].strip()); continue
        flush()
        if re.match(r"^[^\w\s«»\"'(]{1,3}\s+[A-ZÀ-ÜÄÖ0-9]", l) and l.upper() == l:
            out.append(f"<h2>{E(l)}</h2>")
        else:
            out.append(f"<p>{E(l)}</p>")
    flush()
    return "\n".join(out)


def lang_page(code):
    d = LANG_PAGES[code]
    short_d, full = store_text(code)
    url = SITE + code + "/"
    alts = [("en", SITE), ("it", SITE + "it/")] + [(c, SITE + c + "/") for c in LANG_PAGES] + [("x-default", SITE)]
    ld = {"@context": "https://schema.org", **app_ld(None, url, "Zoom, Boss, Valeton, NUX"), "description": short_d, "inLanguage": code}
    t = dict(home=url, list_url=SITE + "pedals/", list_h1=d["pedals"], indep="Zoom, Boss, Valeton, NUX, Line 6: trademarks of their owners. PatchPilot is an independent project.")
    out = [head(code, d["title"], short_d, url, alts, ld), nav(t, SITE, "English"),
           f'<div class="hero"><div class="in"><p class="k">{d["h"]}</p><h1>{E(short_d)}</h1>',
           f'<div class="btns"><a class="btn" href="{RELEASES}">{d["dl"]}</a><span class="btn o">{d["android"]}</span><a class="btn o" href="{SITE}pedals/">{d["pedals"]}</a></div>',
           f'<img class="shot" src="{SITE}img/patchpilot-zoom-pedal-editor-windows-mac-linux.jpg" width="1100" height="800" alt="PatchPilot"></div></div>\n<main>',
           md_to_html(full), foot(t)]
    write(code, "\n".join(out))
    return url


def sitemap(urls):
    rows = "\n".join(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls)
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{rows}\n</urlset>\n')


if __name__ == "__main__":
    urls = [SITE, SITE + "it/"]
    urls += [lang_page(c) for c in LANG_PAGES]
    for lang in ("en", "it"):
        urls.append(list_page(lang))
        urls += [pedal_page(lang, n, k, b) for n, k, b in PEDALS]
    urls += [SITE + "libreria/", SITE + "it/libreria/", SITE + "privacy.html"]
    sitemap(urls)
    print(len(urls), "pagine nella sitemap")
