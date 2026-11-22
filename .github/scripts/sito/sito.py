#!/usr/bin/env python3
"""Genera docs/index.html (EN) e docs/it/index.html (IT) del sito PatchPilot da un'unica struttura."""
import json, sys, html
from pathlib import Path

REPO = Path(sys.argv[1])
CSS = Path(__file__).with_name("style.css").read_text().replace(
    "</style>",
    ".steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin:8px 0}\n"
    ".step{background:var(--panel);border:1px solid var(--line);border-radius:18px;padding:20px;position:relative}\n"
    ".step .n{position:absolute;top:14px;right:18px;font-size:46px;font-weight:800;color:var(--gold);opacity:.35;line-height:1}\n"
    ".step h3{margin:0 0 .4em;color:var(--text);font-size:21px}.step p{margin:0;color:var(--muted)}\n"
    ".say{display:inline-block;background:#ffb5471f;border:1px solid #ffb54755;border-radius:12px;padding:2px 10px;margin:3px 2px;font-style:italic;color:var(--text)}\n"
    ".new{display:inline-block;font-size:12px;font-weight:700;border-radius:999px;padding:0 8px;margin-left:4px;background:#ffb54722;color:var(--gold);border:1px solid #ffb54766;vertical-align:middle}\n"
    ".safe{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px}.safe div{background:var(--panel2);border:1px solid var(--line);border-radius:14px;padding:12px 14px}\n"
    "</style>")

BASE = "https://francescorizzo-cyber.github.io/patchpilot/"
GH = "https://github.com/francescorizzo-cyber/patchpilot"
STRIPE = "https://buy.stripe.com/00w6oG96j0DqcBG5DX63K01"
PAYPAL = "https://paypal.me/AutoFonicMixer/4.99EUR"
MAIL = "autofonic.mixer@gmail.com"

N = '<span class="new">0.9.1</span>'

L = {}
L["en"] = dict(
    url=BASE, pre="", other=("it/", "Italiano"), lib="libreria/",
    title="PatchPilot – say the sound, it sets your Zoom pedal: AI tone assistant for 30 Zoom pedals, Boss, Valeton, NUX · Windows, Mac, Linux",
    desc="PatchPilot recognises your multi-effects pedal by itself and builds the sound you describe right on the pedal: AI tone assistant and coach, sound from a song, automatic backup, setlist and stage mode. 30 Zoom pedals (MS-50G, MS-70CDR+, G1on, G3, G1 FOUR, G2 FOUR, G6, G11, B6…), Boss Katana, GT-100, GT-1000, Valeton GP-200, NUX. Windows, Mac, Linux; Android coming soon.",
    keywords="Zoom pedal editor, AI guitar tone assistant, Zoom MS-50G editor, MS-70CDR+ editor Mac, Zoom G1on editor, Zoom G3 editor Linux, G1 FOUR editor, Guitar Lab alternative, Guitar Lab Linux, Boss Katana editor Linux, GT-1000 editor, Valeton GP-200 editor, NUX Mighty Lite editor, tone from a song, Zoom patch backup, guitar setlist app, stage mode, patch volume LUFS",
    og="img/patchpilot-zoom-pedal-editor-windows-mac-linux.jpg",
    nav=[("#how", "How it works"), ("#features", "Features"), ("#pedals", "Pedals"), ("#screens", "Screens"), ("#android", "Android"), ("#full", "Price"), ("#faq", "FAQ"), ("libreria/", "Patch library")],
    kicker="Multi-effects pedals made simple",
    h1="Plug in your pedal. Say the sound you want. PatchPilot sets it up for you.",
    lead="No menus, no manual, no guessing which knob to turn. PatchPilot <strong>recognises your pedal by itself</strong>, and when you write <em>“warm blues crunch”</em> it chooses the effects and <strong>sets the knobs on your pedal</strong>. For <strong>37 pedals</strong> — 30 Zoom plus Boss, Valeton, NUX and Line 6 — and any MIDI pedal, on <strong>Windows, Mac and Linux</strong> — Android coming soon.",
    b_dl="Download for Windows · Mac · Linux", b_play="Android: coming soon on Google Play", b_full="Full version · €4.99", b_test="5-minute test guide", testurl="TEST.md#english",
    shot_alt="PatchPilot: the pedal-shaped main screen for MS-50G+, G2 FOUR and G11",
    stats=[("37", "pedals: 30 Zoom + 7 Boss, Valeton, NUX, Line 6"), ("+", "any MIDI pedal for the setlist"), ("€4.99", "one time only")],
    ver=f"📦 <strong>Today's download is 0.9.0.</strong> Everything marked {N} — automatic connection, the AI that sets the sound on the pedal, the coach, sound from a song, variants, 10 languages and the new pedals — comes with <strong>0.9.1</strong>, the next update.",
    beta=f"🧪 <strong>Beta.</strong> Tested on a real <strong>Zoom MS-50G</strong>; on the other models everything works the same way, with a <em>“Model in testing”</em> notice and a <strong>“Send the log…”</strong> button. Got one? <a href=\"{GH}/blob/main/TEST.md#english\">Help us in 5 minutes</a>.",
    how_h="How it works: three steps", how_lead="You don't need to know what a compressor is, which knob is which, or how your model's menus work.",
    steps=[
        ("🔌 Plug in", f"PatchPilot <strong>recognises the pedal</strong> and connects as soon as you plug in the cable. It reads <strong>all your patches</strong> and saves a <strong>dated backup</strong> before touching anything. No ports to choose, no boxes to tick. {N}"),
        ("💬 Ask for a sound", f"Press <strong>Ask for a sound</strong> and write it your way: <span class=say>warm blues crunch</span> <span class=say>80s clean with chorus</span>. The AI builds it with your pedal's real effects and <strong>PatchPilot puts it on the pedal</strong> — effects, on/off, knobs. Or load <strong>20–30 seconds of a song</strong>. {N}"),
        ("🎯 Fine-tune by talking", f"<span class=say>too muddy</span> <span class=say>like before, less distorted</span> <span class=say>you do it</span>. The <strong>sound coach</strong> changes only what is needed and explains it in one line. Every step is a <strong>variant</strong>: one click takes you back. {N}"),
    ],
    then="Then you play: <strong>setlist, stage mode and songs that follow the tempo</strong> tell you which sound comes next.",
    safe_h="Your saved sounds are never overwritten",
    safe=[
        ("🎚️ Patch in use only", "PatchPilot changes the sound like you do when you turn the pedal's knobs. It never saves over your patches: like it? save it; don't? change patch and it's back."),
        ("💾 Backup first", "On pedals that allow it, all your patches are saved to a file with date and time before the first change — never overwritten."),
        ("⛔ Blocked forever", "Factory reset and deleting files in the pedal are blocked in the code. Saving to memory and sending whole patches stay off until a model is tested."),
    ],
    feat_h="Everything it does",
    groups=[
        ("Sound, without the manual", [
            ("💬", "Ask for a sound", f"Describe it, PatchPilot builds it on the pedal. On the old MultiStomp family it can even add effects the patch doesn't have. {N}"),
            ("🎯", "Sound coach", f"Keep talking: it changes 1–3 things at a time, says what it touched, and every step can be undone. {N}"),
            ("🎵", "Sound from a song", f"20–30 s from a file or the microphone: distortion, tone, delay repeats, reverb tail and modulation measured on your computer — audio never leaves it. {N}"),
            ("🎓", "The teacher", f"<em>Explain this patch</em>: what each effect and knob does, how they work together, and a small experiment to try. {N}"),
            ("🎛️", "Knobs turned for you", f"Move a knob in the editor and it moves on the pedal. {N}"),
            ("📝", "Variants", f"<em>clean verse</em>, <em>solo with more gain</em>: several versions of the same patch, kept on your computer. {N}"),
        ]),
        ("Look inside your pedal", [
            ("🔌", "Connects by itself", f"Plug in and it is connected; unplug and it lets go. {N}"),
            ("📋", "Every patch with its name", "The full list at a glance, the current one highlighted."),
            ("🏷️", "Real names", "Effects and knobs with their real names and limits, in knob or fader view."),
            ("🎸", "Needle tuner", "Big on the screen, readable from across the room."),
            ("🖼️", "Your pedal on the screen", "The main page draws your model, with display, knobs and switches."),
            ("🌍", "10 languages", f"English, Italiano, Français, Español, Deutsch, Português, Svenska, Dansk, Slovenščina, Hrvatski. {N}"),
        ]),
        ("Keep your sounds safe", [
            ("💾", "Automatic backup", "Every patch to a dated file, to reopen even without the pedal."),
            ("📄", "Sound sheets", "A readable card for each patch, to print or share."),
            ("🔎", "Search by effect", "“Where did I use that delay?”"),
            ("⚖️", "Compare", "Two patches side by side, only the differences."),
        ]),
        ("On stage", [
            ("🎶", "Setlist", "A patch for every song, one per pedal if you use several; capo and notes."),
            ("⏭️", "Song bar", "Mouse wheel, arrows, space bar or a USB/Bluetooth page-turner pedal; search by name."),
            ("🌙", "Stage mode", "Dark screen, big letters: what to play now and what comes next."),
            ("🥁", "Songs that follow the tempo", "Sections with their bars, count-in and a “GET READY” warning before every change; delay times for the tempo."),
            ("🌊", "Gradual transitions", "The sound changes little by little, like a virtual expression pedal."),
        ]),
        ("Volume and community", [
            ("🔊", "Every patch at the same volume", "Play the same riff with each patch: PatchPilot measures loudness as the ear hears it (LUFS) and tells you the level to set."),
            ("📈", "Level meter and MIDI faders", "See the signal level; send volume and expression to a MIDI pedal."),
            ("📚", "Patch library", "Patches shared by users, free (CC0), by song, artist, genre and pedal. Share yours with one click."),
            ("🙋", "Tester page", "Pedal not listed? A guided, listen-only recording helps us add it."),
        ]),
    ],
    ped_h="Supported pedals: 37 + any MIDI pedal",
    ped_cols=("Pedals", "Recognised by itself", "Reads the patches", "PatchPilot sets the sound", "Status"),
    peds=[
        ("<strong>Zoom MS-50G</strong>", "✅", "✅ all 50 + backup", "✅ in one go, effects included", "✅ <strong>tested on a real pedal</strong>"),
        (f"Zoom MS-60B · MS-70CDR · G1on · G1Xon · B1on · B1Xon · G3 · G3X · B3 {N}", "✅", "✅ + backup", "✅ in one go, effects included", "🧪 in test"),
        ("Zoom MS-50G+ · MS-60B+ · MS-70CDR+ · MS-80IR+ · MS-200D+ · MS-90LP+", "✅", "✅ + tuner", f"✅ one change at a time {N}", "🧪 in test"),
        ("Zoom G2 FOUR · G2X FOUR · B2 FOUR", "✅", "✅ + tuner", f"✅ one change at a time {N}", "🧪 in test"),
        ("Zoom G1 FOUR · G1X FOUR · B1 FOUR · B1X FOUR · G3n · G3Xn · G5n · B3n", "✅", "✅", f"✅ one change at a time {N}", "🧪 in test"),
        ("Zoom G6 · G11 · B6", "choose it once", "✅", f"✅ one change at a time {N}", "🧪 not yet tried on a real pedal"),
        (f"Boss Katana MkII · GT-100 · GT-1000 / GT-1000CORE · Valeton GP-200 {N}", "✅", "✅ patch in use", "✅ one change at a time", "🧪 in test"),
        (f"Boss Katana MkI · NUX Mighty Lite BT MkII {N}", "choose it once", "✅ patch in use", "✅ one change at a time", "🧪 in test"),
        (f"Line 6 HX Stomp {N} · any MIDI pedal, any brand", "–", "–", "patch change for each song, MIDI controls", "standard MIDI"),
    ],
    tester=f"🙋 <strong>Your pedal is not in the list? Become a tester.</strong> The computer program has a <strong>Tester</strong> page: a guided recording that only listens. It sends nothing but the standard MIDI identity request, then records what the pedal sends while you change patch and turn a knob. Email the file to <a href=\"mailto:{MAIL}\">{MAIL}</a> with brand and model.",
    scr_h="What it looks like", scr_lead="Screens from the computer program (version 0.9.0).",
    shots=[("img/patchpilot-effects-parameters-editor.jpg", 1100, 800, "Editor: effects and parameters, knob or fader view"),
           ("img/patchpilot-tuner.jpg", 1100, 800, "Needle tuner"),
           ("img/patchpilot-connect-model-language.jpg", 1100, 800, "Connect page and language"),
           ("img/patchpilot-midi-faders-audio-level.jpg", 1100, 800, "Same volume for every patch: level meter and MIDI faders"),
           ("img/patchpilot-patch-variants.jpg", 1250, 800, "Variants of a patch (0.9.1)")],
    and_h="📱 Android app", and_tag="coming soon on Google Play",
    and_lead="The same PatchPilot on your phone or tablet, with a USB-C or OTG cable: no computer in the rehearsal room or on stage. It will be released <strong>on Google Play only</strong>.",
    and_cards=[("👆", "One finger", "Swipe on the pedal: left/right changes model, up/down changes song."),
               ("💬", "Ask for a sound", "Describe the sound, the AI prepares it and explains it in a few words."),
               ("🌙", "Setlist and stage mode", "Tempo sections, “GET READY” warning, Bluetooth page-turner pedals."),
               ("🔑", "Full version", "Bought inside the app with Google Play: €4.99, one time only.")],
    and_img_alt="PatchPilot for Android: drawings of the Zoom MS-50G+, G1X FOUR, G2 FOUR, G6, G11 and B6 pedals", and_cap="The pedals as the Android app draws them",
    inst_h="Install in a minute",
    inst=[("Windows 10/11", "<code>…-windows-x64-setup.exe</code> or the portable <code>.zip</code>. SmartScreen: <em>More info → Run anyway</em>."),
          ("macOS", "<code>…-macos-arm64.dmg</code> (M1–M4) or <code>…-macos-x64.dmg</code> (Intel). First time: <em>System Settings → Privacy &amp; Security → Open Anyway</em>."),
          ("Linux", "<code>…-linux-x64.deb</code> (<code>sudo apt install ./PatchPilot-….deb</code>) or <code>.tar.gz</code>."),
          ("Then", "Plug the pedal in with its USB cable. That's all. Close Guitar Lab first: the pedal talks to one program at a time.")],
    price_h="Free and full version",
    price_lead=f"{N} 7 days with everything on, AI included (5 trial requests). After that, what you need to use your pedal <strong>stays free forever</strong>.",
    price_cols=("", "Free forever", "Full version"),
    prices=[("Recognition, patch list, editor, knobs from the computer, tuner", "✅", "✅"),
            ("Backup inside the program, log, Tester page, patch library", "✅", "✅"),
            ("Setlist", "3 songs", "unlimited + stage mode"),
            ("Backup export, sound sheets, search, compare", "—", "✅"),
            ("Variants", "—", "✅"),
            ("AI: ask for a sound, coach, sound from a song, teacher", "7-day trial", "✅ 100 requests a month")],
    full_h="Full version: €4.99, one time only",
    full_steps=[f"In PatchPilot open the <em>Support ♥</em> page and copy your device code (<code>PP-ABCD-EFGH</code>).",
                f"<strong>Card, Google Pay or Apple Pay</strong>: <a href=\"{STRIPE}\">pay €4.99 with Stripe</a>, paste the device code: the <strong>unlock code appears right after the payment</strong>.",
                f"<strong>PayPal</strong>: <a href=\"{PAYPAL}\">pay €4.99</a>, then write to <a href=\"mailto:{MAIL}\">{MAIL}</a>: the unlock code arrives by email, usually within a day."],
    b_card="Pay €4.99 by card", b_pp="Pay €4.99 with PayPal",
    full_small="One code per computer (Windows, macOS, Linux). On Android the full version is bought inside the app, with Google Play.",
    faq_h="Frequently asked questions",
    faq=[("Do I need to know how my pedal works?", "No. You plug it in and describe the sound in your own words: PatchPilot chooses the effects and sets the knobs on the pedal, then tells you in one line what it did. If you want to learn, “Explain this patch” explains every effect and knob."),
         ("Can PatchPilot ruin my patches?", "PatchPilot works on the patch in use, like turning the pedal's own knobs, and never saves over your patches. Before the first change it saves a dated backup of all patches (on pedals that allow it). Factory reset and file deletion are blocked forever."),
         ("Which pedals does it support?", "30 Zoom pedals — MS-50G, MS-60B, MS-70CDR, the MultiStomp+ series, G1on/B1on, G3/B3, G1/B1 FOUR, G2/B2 FOUR, G3n, G5n, G6, G11, B6 — plus Boss Katana MkI/MkII, GT-100, GT-1000, Valeton GP-200, NUX Mighty Lite BT MkII, Line 6 HX Stomp and any MIDI pedal for patch changes. Tested on a real MS-50G; the others are in test."),
         ("Can it copy the sound of a song?", "With 0.9.1: load 20–30 seconds of a song or play it to the microphone. PatchPilot measures distortion, tone, delay, reverb and modulation on your computer and the AI builds a close patch with your pedal's effects. It works best with the guitar alone. The audio never leaves your computer."),
         ("Is there an Android app for Zoom MultiStomp pedals?", "Zoom's Guitar Lab apps for these pedals are mostly for iPhone. PatchPilot's Android app is coming soon on Google Play; today PatchPilot runs on Windows, macOS and Linux."),
         ("Is PatchPilot an alternative to Guitar Lab?", "Yes, and it also runs on Linux and works with older models such as the MS-50G, G1on and G3 that have no app. It doesn't install Zoom's effect files: for those you still need Zoom's software."),
         ("What does the AI send over the internet?", "Only your request and the patch values (numbers). Never audio: songs and microphone are measured on your computer. Everything else works offline."),
         ("How much does it cost?", "Download is free. From 0.9.1: 7 days with everything on, then recognition, patch reading, editor, tuner and a 3-song setlist stay free forever. The full version is €4.99, once per device."),
         ("Is PatchPilot made by Zoom?", "No. PatchPilot is an independent project, not affiliated with Zoom, Boss/Roland, Valeton, NUX or Line 6.")],
    foot=(f"<a href=\"{GH}\">Project page and downloads on GitHub</a> · <a href=\"{GH}/blob/main/PRIVACY.md\">Privacy</a> · <a href=\"{GH}/issues/new/choose\">Report a problem</a> · Contact: <a href=\"mailto:{MAIL}\">{MAIL}</a>",
          "PatchPilot is an independent project, not affiliated with ZOOM Corporation, Boss/Roland, Valeton, NUX or Line 6. Brand and model names are trademarks of their owners.<br>Made by Francesco Rizzo."),
)

L["it"] = dict(
    url=BASE + "it/", pre="../", other=("../", "English"), lib="libreria/",
    title="PatchPilot – di' il suono e lo imposta sul tuo pedale Zoom: assistente AI per 30 pedali Zoom, Boss, Valeton, NUX · Windows, Mac, Linux",
    desc="PatchPilot riconosce da solo il tuo multieffetto e costruisce sul pedale il suono che descrivi: assistente AI e coach del suono, suono preso da un brano, backup automatico, scaletta e modalità palco. 30 pedali Zoom (MS-50G, MS-70CDR+, G1on, G3, G1 FOUR, G2 FOUR, G6, G11, B6…), Boss Katana, GT-100, GT-1000, Valeton GP-200, NUX. Windows, Mac, Linux; Android in arrivo.",
    keywords="editor pedali Zoom, assistente AI suono chitarra, editor Zoom MS-50G, editor MS-70CDR+ Mac, editor Zoom G1on, editor Zoom G3 Linux, editor G1 FOUR, alternativa Guitar Lab, Guitar Lab Linux, editor Boss Katana Linux, editor GT-1000, editor Valeton GP-200, editor NUX Mighty Lite, suono da una canzone, backup patch Zoom, scaletta chitarra, modalità palco, stesso volume patch LUFS",
    og="img/patchpilot-editor-pedali-zoom-windows-mac-linux.jpg",
    nav=[("#come", "Come funziona"), ("#funzioni", "Funzioni"), ("#pedali", "Pedali"), ("#schermate", "Schermate"), ("#android", "Android"), ("#full", "Prezzo"), ("#faq", "Domande"), ("libreria/", "Libreria patch")],
    kicker="I multieffetto, resi semplici",
    h1="Collega il pedale. Di' che suono vuoi. Al resto pensa PatchPilot.",
    lead="Niente menu, niente manuale, niente tentativi su quale manopola girare. PatchPilot <strong>riconosce il pedale da solo</strong> e quando scrivi <em>«crunch blues caldo»</em> sceglie gli effetti e <strong>imposta le manopole sul tuo pedale</strong>. Per <strong>37 pedali</strong> — 30 Zoom più Boss, Valeton, NUX e Line 6 — e qualsiasi pedale MIDI, su <strong>Windows, Mac e Linux</strong> — Android in arrivo.",
    b_dl="Scarica per Windows · Mac · Linux", b_play="Android: in arrivo su Google Play", b_full="Versione completa · 4,99 €", b_test="Guida di prova in 5 minuti", testurl="TEST.md#italiano",
    shot_alt="PatchPilot: la schermata principale a forma di pedale per MS-50G+, G2 FOUR e G11",
    stats=[("37", "pedali: 30 Zoom + 7 Boss, Valeton, NUX, Line 6"), ("+", "qualsiasi pedale MIDI per la scaletta"), ("4,99 €", "una volta sola")],
    ver=f"📦 <strong>Il download di oggi è la 0.9.0.</strong> Tutto quello che è segnato {N} — collegamento automatico, l'AI che imposta il suono sul pedale, il coach, il suono preso da un brano, le varianti, le 10 lingue e i nuovi pedali — arriva con la <strong>0.9.1</strong>, il prossimo aggiornamento.",
    beta=f"🧪 <strong>Beta.</strong> Provata su uno <strong>Zoom MS-50G</strong> vero; sugli altri modelli funziona tutto allo stesso modo, con l'avviso <em>«Modello in prova»</em> e il pulsante <strong>«Manda il registro…»</strong>. Ne hai uno? <a href=\"{GH}/blob/main/TEST.md#italiano\">Aiutaci in 5 minuti</a>.",
    how_h="Come funziona: tre passi", how_lead="Non serve sapere cos'è un compressore, quale manopola è quale o come funzionano i menu del tuo modello.",
    steps=[
        ("🔌 Collega", f"PatchPilot <strong>riconosce il pedale</strong> e si collega appena attacchi il cavo. Legge <strong>tutte le tue patch</strong> e salva un <strong>backup con data e ora</strong> prima di toccare qualsiasi cosa. Niente porte da scegliere, niente caselle da spuntare. {N}"),
        ("💬 Chiedi un suono", f"Premi <strong>Chiedi un suono</strong> e scrivilo a modo tuo: <span class=say>crunch blues caldo</span> <span class=say>pulito anni '80 con chorus</span>. L'AI lo costruisce con gli effetti veri del tuo pedale e <strong>PatchPilot lo mette sul pedale</strong> — effetti, acceso/spento, manopole. Oppure carica <strong>20–30 secondi di una canzone</strong>. {N}"),
        ("🎯 Rifinisci parlando", f"<span class=say>troppo impastato</span> <span class=say>come prima ma meno distorto</span> <span class=say>fallo tu</span>. Il <strong>coach del suono</strong> cambia solo quello che serve e lo spiega in una riga. Ogni passo è una <strong>variante</strong>: con un clic torni indietro. {N}"),
    ],
    then="Poi suoni: <strong>scaletta, modalità palco e brani che seguono il tempo</strong> ti dicono qual è il suono successivo.",
    safe_h="I suoni che hai salvato non vengono mai sovrascritti",
    safe=[
        ("🎚️ Solo la patch in uso", "PatchPilot cambia il suono come fai tu quando giri le manopole del pedale. Non salva mai sopra le tue patch: ti piace? la salvi; non ti piace? cambi patch e torna com'era."),
        ("💾 Prima il backup", "Sui pedali che lo permettono, tutte le patch vengono salvate in un file con data e ora prima della prima modifica — mai sovrascritto."),
        ("⛔ Vietati per sempre", "Ripristino di fabbrica e cancellazione di file nel pedale sono bloccati nel codice. Salvataggio in memoria e invio di patch intere restano spenti finché un modello non è provato."),
    ],
    feat_h="Tutto quello che fa",
    groups=[
        ("Il suono, senza il manuale", [
            ("💬", "Chiedi un suono", f"Lo descrivi, PatchPilot lo costruisce sul pedale. Sulla famiglia dei vecchi MultiStomp può anche aggiungere effetti che la patch non ha. {N}"),
            ("🎯", "Coach del suono", f"Continui a parlare: cambia 1–3 cose alla volta, dice cosa ha toccato e ogni passo si può annullare. {N}"),
            ("🎵", "Suono preso da un brano", f"20–30 s da file o dal microfono: distorsione, timbro, ripetizioni del delay, coda del riverbero e modulazione misurati sul tuo computer — l'audio non esce mai. {N}"),
            ("🎓", "Il maestro", f"<em>Spiegami questa patch</em>: a cosa serve ogni effetto e ogni manopola, come lavorano insieme e un piccolo esperimento da provare. {N}"),
            ("🎛️", "Manopole girate per te", f"Muovi una manopola nell'editor e si muove sul pedale. {N}"),
            ("📝", "Varianti", f"<em>strofa pulita</em>, <em>assolo con più gain</em>: più versioni della stessa patch, tenute sul tuo computer. {N}"),
        ]),
        ("Guarda dentro il pedale", [
            ("🔌", "Si collega da solo", f"Attacchi il cavo ed è collegato; lo stacchi e si scollega. {N}"),
            ("📋", "Tutte le patch con il nome", "L'elenco completo in un colpo d'occhio, quella in uso in evidenza."),
            ("🏷️", "Nomi veri", "Effetti e manopole con i loro nomi e limiti, a manopole o a fader."),
            ("🎸", "Accordatore a lancetta", "Grande sullo schermo, si legge anche da lontano."),
            ("🖼️", "Il tuo pedale sullo schermo", "La pagina principale disegna il tuo modello, con display, manopole e interruttori."),
            ("🌍", "10 lingue", f"Italiano, English, Français, Español, Deutsch, Português, Svenska, Dansk, Slovenščina, Hrvatski. {N}"),
        ]),
        ("Suoni al sicuro", [
            ("💾", "Backup automatico", "Tutte le patch in un file con data, da riaprire anche senza pedale."),
            ("📄", "Schede suono", "Una scheda leggibile per ogni patch, da stampare o condividere."),
            ("🔎", "Ricerca per effetto", "«Dove ho usato quel delay?»"),
            ("⚖️", "Confronto", "Due patch una accanto all'altra, solo le differenze."),
        ]),
        ("Sul palco", [
            ("🎶", "Scaletta", "Una patch per ogni brano, una per pedale se ne usi più di uno; capotasto e note."),
            ("⏭️", "Barra dei brani", "Rotella del mouse, frecce, barra spaziatrice o pedale volta-pagina USB/Bluetooth; ricerca per nome."),
            ("🌙", "Modalità palco", "Schermo scuro, caratteri grandi: cosa suonare adesso e cosa viene dopo."),
            ("🥁", "Brani che seguono il tempo", "Sezioni con le loro battute, conteggio iniziale e avviso «PREPARA» prima di ogni cambio; tempi del delay per il tempo."),
            ("🌊", "Passaggi graduali", "Il suono cambia piano piano, come con un pedale d'espressione virtuale."),
        ]),
        ("Volume e comunità", [
            ("🔊", "Tutte le patch allo stesso volume", "Suoni lo stesso giro con ogni patch: PatchPilot misura il volume come lo sente l'orecchio (LUFS) e ti dice il livello da impostare."),
            ("📈", "Livello audio e fader MIDI", "Vedi il livello del segnale; mandi volume ed espressione a un pedale MIDI."),
            ("📚", "Libreria di patch", "Patch condivise da chi usa PatchPilot, libere (CC0), per brano, artista, genere e pedale. Condividi la tua con un clic."),
            ("🙋", "Pagina Tester", "Il tuo pedale non c'è? Una registrazione guidata che ascolta soltanto ci aiuta ad aggiungerlo."),
        ]),
    ],
    ped_h="Pedali supportati: 37 + qualsiasi pedale MIDI",
    ped_cols=("Pedali", "Riconosciuto da solo", "Legge le patch", "PatchPilot imposta il suono", "Stato"),
    peds=[
        ("<strong>Zoom MS-50G</strong>", "✅", "✅ tutte le 50 + backup", "✅ in un colpo solo, effetti compresi", "✅ <strong>provato su un pedale vero</strong>"),
        (f"Zoom MS-60B · MS-70CDR · G1on · G1Xon · B1on · B1Xon · G3 · G3X · B3 {N}", "✅", "✅ + backup", "✅ in un colpo solo, effetti compresi", "🧪 in prova"),
        ("Zoom MS-50G+ · MS-60B+ · MS-70CDR+ · MS-80IR+ · MS-200D+ · MS-90LP+", "✅", "✅ + accordatore", f"✅ una modifica alla volta {N}", "🧪 in prova"),
        ("Zoom G2 FOUR · G2X FOUR · B2 FOUR", "✅", "✅ + accordatore", f"✅ una modifica alla volta {N}", "🧪 in prova"),
        ("Zoom G1 FOUR · G1X FOUR · B1 FOUR · B1X FOUR · G3n · G3Xn · G5n · B3n", "✅", "✅", f"✅ una modifica alla volta {N}", "🧪 in prova"),
        ("Zoom G6 · G11 · B6", "lo scegli una volta", "✅", f"✅ una modifica alla volta {N}", "🧪 non ancora provati su un pedale vero"),
        (f"Boss Katana MkII · GT-100 · GT-1000 / GT-1000CORE · Valeton GP-200 {N}", "✅", "✅ patch in uso", "✅ una modifica alla volta", "🧪 in prova"),
        (f"Boss Katana MkI · NUX Mighty Lite BT MkII {N}", "lo scegli una volta", "✅ patch in uso", "✅ una modifica alla volta", "🧪 in prova"),
        (f"Line 6 HX Stomp {N} · qualsiasi pedale MIDI, di qualsiasi marca", "–", "–", "cambio patch per ogni brano, comandi MIDI", "MIDI standard"),
    ],
    tester=f"🙋 <strong>Il tuo pedale non è in elenco? Diventa tester.</strong> Il programma per computer ha la pagina <strong>Tester</strong>: una registrazione guidata che ascolta soltanto. Al pedale manda solo la richiesta di identità MIDI standard, poi registra quello che il pedale invia mentre cambi patch e giri una manopola. Manda il file a <a href=\"mailto:{MAIL}\">{MAIL}</a> con marca e modello.",
    scr_h="Com'è fatto", scr_lead="Schermate del programma per computer (versione 0.9.0).",
    shots=[("img/patchpilot-editor-effetti-parametri.jpg", 1100, 800, "Editor: effetti e parametri, a manopole o a fader"),
           ("img/patchpilot-accordatore.jpg", 1100, 800, "Accordatore a lancetta"),
           ("img/patchpilot-scaletta-barra-brani.jpg", 1100, 800, "Scaletta e barra dei brani"),
           ("img/patchpilot-fader-midi-livello-audio.jpg", 1100, 800, "Stesso volume per tutte le patch: livello audio e fader MIDI"),
           ("img/patchpilot-varianti-patch.jpg", 1250, 800, "Varianti di una patch (0.9.1)")],
    and_h="📱 App Android", and_tag="in arrivo su Google Play",
    and_lead="Lo stesso PatchPilot sul telefono o sul tablet, con un cavo USB-C o OTG: niente computer in sala prove o sul palco. Uscirà <strong>solo su Google Play</strong>.",
    and_cards=[("👆", "Un dito solo", "Scorri sul pedale: sinistra/destra cambia modello, su/giù cambia brano."),
               ("💬", "Chiedi un suono", "Descrivi il suono, l'AI lo prepara e te lo spiega in poche parole."),
               ("🌙", "Scaletta e palco", "Sezioni a tempo, avviso «PREPARA», pedali volta-pagina Bluetooth."),
               ("🔑", "Versione completa", "Si compra dentro l'app con Google Play: 4,99 €, una volta sola.")],
    and_img_alt="PatchPilot per Android: i disegni dei pedali Zoom MS-50G+, G1X FOUR, G2 FOUR, G6, G11 e B6", and_cap="I pedali come li disegna l'app Android",
    inst_h="Si installa in un minuto",
    inst=[("Windows 10/11", "<code>…-windows-x64-setup.exe</code> oppure lo <code>.zip</code> senza installazione. SmartScreen: <em>Ulteriori informazioni → Esegui comunque</em>."),
          ("macOS", "<code>…-macos-arm64.dmg</code> (M1–M4) oppure <code>…-macos-x64.dmg</code> (Intel). La prima volta: <em>Impostazioni di Sistema → Privacy e sicurezza → Apri comunque</em>."),
          ("Linux", "<code>…-linux-x64.deb</code> (<code>sudo apt install ./PatchPilot-….deb</code>) oppure <code>.tar.gz</code>."),
          ("Poi", "Collega il pedale con il suo cavo USB. Basta così. Chiudi prima Guitar Lab: il pedale parla con un programma alla volta.")],
    price_h="Gratis e versione completa",
    price_lead=f"{N} 7 giorni con tutto acceso, AI compresa (5 richieste di prova). Poi quello che serve per usare il pedale <strong>resta gratis per sempre</strong>.",
    price_cols=("", "Gratis per sempre", "Versione completa"),
    prices=[("Riconoscimento, elenco patch, editor, manopole dal computer, accordatore", "✅", "✅"),
            ("Backup nel programma, registro, pagina Tester, libreria di patch", "✅", "✅"),
            ("Scaletta", "3 brani", "senza limiti + modalità palco"),
            ("Esportazione del backup, schede suono, ricerca, confronto", "—", "✅"),
            ("Varianti", "—", "✅"),
            ("AI: chiedi un suono, coach, suono da un brano, maestro", "7 giorni di prova", "✅ 100 richieste al mese")],
    full_h="Versione completa: 4,99 €, una volta sola",
    full_steps=[f"In PatchPilot apri la pagina <em>Sostieni ♥</em> e copia il codice dispositivo (<code>PP-ABCD-EFGH</code>).",
                f"<strong>Carta, Google Pay o Apple Pay</strong>: <a href=\"{STRIPE}\">paga 4,99 € con Stripe</a>, incolla il codice dispositivo: il <strong>codice di sblocco appare subito dopo il pagamento</strong>.",
                f"<strong>PayPal</strong>: <a href=\"{PAYPAL}\">paga 4,99 €</a>, poi scrivi ad <a href=\"mailto:{MAIL}\">{MAIL}</a>: il codice di sblocco arriva per email, di solito entro un giorno."],
    b_card="Paga 4,99 € con carta", b_pp="Paga 4,99 € con PayPal",
    full_small="Un codice per ogni computer (Windows, macOS, Linux). Su Android la versione completa si compra dentro l'app, con Google Play.",
    faq_h="Domande frequenti",
    faq=[("Devo sapere come funziona il mio pedale?", "No. Lo colleghi e descrivi il suono con parole tue: PatchPilot sceglie gli effetti e imposta le manopole sul pedale, poi ti dice in una riga cosa ha fatto. Se vuoi imparare, «Spiegami questa patch» ti spiega ogni effetto e ogni manopola."),
         ("PatchPilot può rovinare le mie patch?", "PatchPilot lavora sulla patch in uso, come quando giri le manopole del pedale, e non salva mai sopra le tue patch. Prima della prima modifica salva un backup con data di tutte le patch (sui pedali che lo permettono). Ripristino di fabbrica e cancellazione di file sono vietati per sempre."),
         ("Quali pedali supporta?", "30 pedali Zoom — MS-50G, MS-60B, MS-70CDR, la serie MultiStomp+, G1on/B1on, G3/B3, G1/B1 FOUR, G2/B2 FOUR, G3n, G5n, G6, G11, B6 — più Boss Katana MkI/MkII, GT-100, GT-1000, Valeton GP-200, NUX Mighty Lite BT MkII, Line 6 HX Stomp e qualsiasi pedale MIDI per il cambio patch. Provato su un MS-50G vero; gli altri sono in prova."),
         ("Può copiare il suono di una canzone?", "Con la 0.9.1: carichi 20–30 secondi di una canzone o la fai sentire al microfono. PatchPilot misura sul tuo computer distorsione, timbro, delay, riverbero e modulazione e l'AI costruisce una patch simile con gli effetti del tuo pedale. Funziona meglio con la chitarra da sola. L'audio non esce mai dal computer."),
         ("C'è un'app Android per i pedali Zoom MultiStomp?", "Le app Guitar Lab di Zoom per questi pedali sono quasi tutte per iPhone. L'app Android di PatchPilot è in arrivo su Google Play; oggi PatchPilot funziona su Windows, macOS e Linux."),
         ("PatchPilot è un'alternativa a Guitar Lab?", "Sì, e funziona anche su Linux e con modelli più vecchi come MS-50G, G1on e G3 che un'app non ce l'hanno. Non installa i file degli effetti Zoom: per quelli serve ancora il programma di Zoom."),
         ("Cosa manda l'AI su internet?", "Solo la tua richiesta e i valori della patch (numeri). Mai l'audio: canzoni e microfono vengono misurati sul tuo computer. Tutto il resto funziona senza internet."),
         ("Quanto costa?", "Il download è gratis. Dalla 0.9.1: 7 giorni con tutto acceso, poi riconoscimento, lettura delle patch, editor, accordatore e scaletta di 3 brani restano gratis per sempre. La versione completa costa 4,99 €, una volta per dispositivo."),
         ("PatchPilot è fatto da Zoom?", "No. PatchPilot è un progetto indipendente, non affiliato a Zoom, Boss/Roland, Valeton, NUX o Line 6.")],
    foot=(f"<a href=\"{GH}\">Pagina del progetto e download su GitHub</a> · <a href=\"{GH}/blob/main/PRIVACY.md\">Privacy</a> · <a href=\"{GH}/issues/new/choose\">Segnala un problema</a> · Contatti: <a href=\"mailto:{MAIL}\">{MAIL}</a>",
          "PatchPilot è un progetto indipendente, non affiliato a ZOOM Corporation, Boss/Roland, Valeton, NUX o Line 6. I nomi di marche e modelli sono marchi dei rispettivi proprietari.<br>Realizzato da Francesco Rizzo."),
)

ID = {"en": dict(how="how", feat="features", ped="pedals", scr="screens"), "it": dict(how="come", feat="funzioni", ped="pedali", scr="schermate")}


def strip(s):
    import re
    return html.unescape(re.sub(r"<[^>]+>", "", s)).replace("  ", " ").strip()


def page(lang):
    d, i, p = L[lang], ID[lang], L[lang]["pre"]
    app = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "PatchPilot",
           "operatingSystem": "Windows, macOS, Linux, Android", "applicationCategory": "MultimediaApplication",
           "applicationSubCategory": "Guitar multi-effects pedal editor with AI tone assistant",
           "description": d["desc"], "image": BASE + d["og"], "downloadUrl": GH + "/releases/latest",
           "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR", "description": "Free download; full version 4.99 EUR one-time per device"},
           "author": {"@type": "Person", "name": "Francesco Rizzo"}, "softwareVersion": "0.9.0", "url": d["url"],
           "inLanguage": ["en", "it", "fr", "es", "de", "pt", "sv", "da", "sl", "hr"],
           "featureList": [strip(t) for _, items in d["groups"] for _, t, _ in items],
           "screenshot": [BASE + s[0] for s in d["shots"]]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]}
    o = []
    w = o.append
    w(f'<!doctype html>\n<html lang="{lang}">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">')
    w(f'<title>{html.escape(d["title"])}</title>\n<meta name="description" content="{html.escape(d["desc"])}">')
    w('<meta name="robots" content="index,follow,max-image-preview:large">')
    w(f'<meta name="keywords" content="{html.escape(d["keywords"])}">')
    w(f'<link rel="canonical" href="{d["url"]}">')
    w(f'<link rel="alternate" hreflang="en" href="{BASE}">\n<link rel="alternate" hreflang="it" href="{BASE}it/">\n<link rel="alternate" hreflang="x-default" href="{BASE}">')
    w(f'<link rel="icon" href="{p}img/icona.png">')
    w(f'<meta property="og:type" content="website">\n<meta property="og:title" content="{html.escape(d["title"])}">\n<meta property="og:description" content="{html.escape(d["desc"])}">')
    w(f'<meta property="og:image" content="{BASE}{d["og"]}">\n<meta property="og:site_name" content="PatchPilot">\n<meta property="og:url" content="{d["url"]}">\n<meta name="twitter:card" content="summary_large_image">')
    w('<script type="application/ld+json">\n' + json.dumps(app, ensure_ascii=False, indent=1) + '\n</script>')
    w('<script type="application/ld+json">\n' + json.dumps(faq, ensure_ascii=False, indent=1) + '\n</script>')
    w(CSS.strip())
    w('</head>\n<body>')
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in d["nav"])
    w(f'<nav><div class="in"><img src="{p}img/icona.png" width="30" height="30" alt=""><b>PATCHPILOT</b>{nav}<span class="sp"></span><a href="{d["other"][0]}">{d["other"][1]}</a></div></nav>')
    w('<div class="hero"><div class="in">')
    w(f'<p class="k">{d["kicker"]}</p>\n<h1>{html.escape(d["h1"])}</h1>\n<p class="lead">{d["lead"]}</p>')
    w(f'<div class="btns">\n<a class="btn" href="{GH}/releases/latest">{d["b_dl"]}</a>\n<span class="btn o">{d["b_play"]}</span>\n<a class="btn p" href="#full">{d["b_full"]}</a>\n<a class="btn o" href="{GH}/blob/main/{d["testurl"]}">{d["b_test"]}</a>\n</div>')
    w(f'<img class="shot" src="{p}{d["og"]}" width="1100" height="800" alt="{html.escape(d["shot_alt"])}" fetchpriority="high">')
    w('<div class="stats">' + "".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in d["stats"]) + '</div>')
    w('</div></div>\n<main>')
    w(f'<p class="note">{d["ver"]}</p>')
    w(f'<p class="note" style="border-left-color:var(--green)">{d["beta"]}</p>')
    w(f'<h2 id="{i["how"]}">{d["how_h"]}</h2>\n<p class="lead">{d["how_lead"]}</p>\n<div class="steps">')
    for k, (h, t) in enumerate(d["steps"], 1):
        w(f'<div class="step"><span class="n">{k}</span><h3>{h}</h3><p>{t}</p></div>')
    w(f'</div>\n<p>{d["then"]}</p>')
    w(f'<h3>🛡️ {d["safe_h"]}</h3>\n<div class="safe">' + "".join(f'<div><strong>{a}</strong><br><small>{b}</small></div>' for a, b in d["safe"]) + '</div>')
    w(f'<h2 id="{i["feat"]}">{d["feat_h"]}</h2>')
    for g, items in d["groups"]:
        w(f'<h3>{g}</h3>\n<div class="grid">')
        for ic, t, x in items:
            w(f'<div class="card f"><div class="ico" aria-hidden="true">{ic}</div><p><strong>{t}.</strong> {x}</p></div>')
        w('</div>')
    w(f'<h2 id="{i["ped"]}">{d["ped_h"]}</h2>\n<div class="tw"><table>')
    w("<tr>" + "".join(f"<th>{c}</th>" for c in d["ped_cols"]) + "</tr>")
    for r in d["peds"]:
        w("<tr>" + "".join(f'<td{" class=c" if 0 < j < 4 and len(strip(c)) < 6 else ""}>{c}</td>' for j, c in enumerate(r)) + "</tr>")
    w(f'</table></div>\n<p class="note">{d["tester"]}</p>')
    w(f'<h2 id="{i["scr"]}">{d["scr_h"]}</h2>\n<p class="lead">{d["scr_lead"]}</p>\n<div class="gal">')
    for src, wd, ht, cap in d["shots"]:
        w(f'<figure><a href="{p}{src}"><img src="{p}{src}" width="{wd}" height="{ht}" loading="lazy" alt="PatchPilot – {html.escape(cap)}"></a><figcaption>{cap}</figcaption></figure>')
    w('</div>')
    w(f'<h2 id="android">{d["and_h"]} <span class="tag n">{d["and_tag"]}</span></h2>\n<p class="lead">{d["and_lead"]}</p>\n<div class="grid">')
    for ic, t, x in d["and_cards"]:
        w(f'<div class="card f"><div class="ico" aria-hidden="true">{ic}</div><p><strong>{t}.</strong> {x}</p></div>')
    w(f'</div>\n<figure style="max-width:520px;margin:16px auto 0"><img src="{p}img/patchpilot-app-android-pedali-zoom.jpg" width="900" height="1149" loading="lazy" alt="{html.escape(d["and_img_alt"])}"><figcaption>{d["and_cap"]}</figcaption></figure>')
    w(f'<h2 id="install">{d["inst_h"]}</h2>\n<div class="tw"><table>' + "".join(f"<tr><td><strong>{a}</strong></td><td>{b}</td></tr>" for a, b in d["inst"]) + "</table></div>")
    w(f'<h2>{d["price_h"]}</h2>\n<p>{d["price_lead"]}</p>\n<div class="tw"><table>')
    w(f'<tr><th>{d["price_cols"][0]}</th><th class="c">{d["price_cols"][1]}</th><th class="c">{d["price_cols"][2]}</th></tr>')
    for a, b, c in d["prices"]:
        w(f'<tr><td>{a}</td><td class="c">{b}</td><td class="c">{c}</td></tr>')
    w('</table></div>')
    w(f'<h2 id="full">{d["full_h"]}</h2>\n<div class="price">\n<ol>' + "".join(f"<li>{s}</li>" for s in d["full_steps"]) + "</ol>")
    w(f'<div class="btns"><a class="btn" href="{STRIPE}">{d["b_card"]}</a> <a class="btn p" href="{PAYPAL}">{d["b_pp"]}</a></div>\n<small>{d["full_small"]}</small>\n</div>')
    w(f'<h2 id="faq">{d["faq_h"]}</h2>')
    for q, a in d["faq"]:
        w(f'<details><summary>{q}</summary><p>{a}</p></details>')
    w(f'\n<footer>\n<p>{d["foot"][0]}</p>\n<p>{d["foot"][1]}</p>\n</footer>\n</main>\n</body>\n</html>\n')
    return "\n".join(o)


(REPO / "docs/index.html").write_text(page("en"))
(REPO / "docs/it/index.html").write_text(page("it"))
print("ok")
