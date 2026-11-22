#!/usr/bin/env python3
"""
Libreria della comunità di PatchPilot: controllo e archiviazione delle patch mandate con il modulo
".github/ISSUE_TEMPLATE/4_libreria.yml".

  python3 libreria.py controlla   -> legge la segnalazione (GITHUB_EVENT_PATH), controlla la patch, risponde con un commento
  python3 libreria.py aggiungi    -> (etichetta "approvata") salva la patch in docs/libreria/patch/ e aggiorna l'elenco
  python3 libreria.py elenco      -> rifà docs/libreria/index.json da tutti i file
  python3 libreria.py prova FILE  -> controlla un file sul computer, senza GitHub

Il testo della segnalazione è scritto da chiunque: qui si tratta SOLO come dati (JSON letto e controllato),
non viene mai eseguito né passato alla shell. Si salvano solo i campi previsti, con limiti di lunghezza.
Gli stessi limiti stanno nell'app (android/app/src/main/java/it/rizzo/haguitar/midi/Community.kt, repository HaGuitar).
"""
import hashlib
import json
import os
import re
import sys
import unicodedata
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LIB = os.path.join(ROOT, "docs", "libreria")
PATCH_DIR = os.path.join(LIB, "patch")
INDEX = os.path.join(LIB, "index.json")
SITE = "https://francescorizzo-cyber.github.io/patchpilot/libreria/"

FORMAT = "patchpilot-libreria"
# Stesso elenco dell'app (Profiles.all senza i profili solo-MIDI: Community.models, repository HaGuitar).
ZOOM_MODELS = ["MS-50G+", "MS-60B+", "MS-70CDR+", "MS-80IR+", "MS-200D+", "MS-90LP+",
               "G2 FOUR", "G2X FOUR", "B2 FOUR", "G1 FOUR", "G1X FOUR", "B1 FOUR", "B1X FOUR",
               "G3n", "G3Xn", "G5n", "B3n", "G6", "G11", "B6",
               "MS-50G", "MS-60B", "MS-70CDR", "G1on", "G1Xon", "B1on", "B1Xon", "G3", "G3X", "B3"]
OTHER_MODELS = ["Katana MkII", "Katana MkI", "GT-100", "GT-1000", "GP-200 (Valeton)", "Mighty Lite BT MkII (NUX)"]
MODELS = ZOOM_MODELS + OTHER_MODELS
MAX_NAME, MAX_TEXT, MAX_NOTES, MAX_SYSEX_HEX, MAX_SLOTS, MAX_PARAMS = 40, 80, 500, 24000, 10, 32
MAX_FILE = 200_000
HEX_RE = re.compile(r"^[0-9A-Fa-f]{2}( [0-9A-Fa-f]{2})*$")
ATTACH_RE = re.compile(r"https://github\.com/user-attachments/files/\d+/[A-Za-z0-9._-]+\.json")


def slug(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if not unicodedata.combining(c)).replace("+", "plus")
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:40] or "patch"


def text(o, key, limit, required=False, errors=None):
    v = o.get(key, "")
    if not isinstance(v, str):
        errors.append(f"«{key}» deve essere un testo")
        return ""
    v = " ".join(v.split()) if key != "notes" else v.strip()
    v = "".join(c for c in v if c == "\n" or ord(c) >= 32)
    if required and not v:
        errors.append(f"manca «{key}»")
    if len(v) > limit:
        errors.append(f"«{key}» troppo lungo (massimo {limit} caratteri)")
    return v


def check(o):
    """(errori, patch pulita). Si tengono SOLO i campi previsti."""
    errors = []
    if not isinstance(o, dict):
        return ["il contenuto non è un oggetto JSON"], None
    if o.get("format") != FORMAT:
        errors.append("non è una patch della libreria di PatchPilot (format)")
    if o.get("version") != 1:
        errors.append("versione del file non supportata")
    model = o.get("model")
    if model not in MODELS:
        errors.append(f"modello non riconosciuto: {model!r}")
    clean = {
        "format": FORMAT, "version": 1, "model": model,
        "name": text(o, "name", MAX_NAME, True, errors),
        "author": text(o, "author", MAX_NAME, True, errors),
        "song": text(o, "song", MAX_TEXT, False, errors),
        "artist": text(o, "artist", MAX_TEXT, False, errors),
        "genre": text(o, "genre", MAX_TEXT, False, errors),
        "notes": text(o, "notes", MAX_NOTES, False, errors),
        "license": "CC0-1.0",
        "app": text(o, "app", MAX_TEXT, False, errors),
        "date": text(o, "date", 20, False, errors),
    }
    if o.get("license") != "CC0-1.0":
        errors.append("licenza diversa da CC0-1.0")
    p = o.get("patch")
    if not isinstance(p, dict):
        errors.append("manca la patch")
        return errors, None
    cp = {"index": 0, "bank": 0, "program": 0, "name": text(p, "name", MAX_NAME, True, errors)}
    sysex = p.get("sysex")
    if sysex is not None:
        if not isinstance(sysex, str) or len(sysex) > MAX_SYSEX_HEX or not HEX_RE.match(sysex.strip()):
            errors.append("messaggio della patch (sysex) non valido o troppo grande")
        elif not sysex.upper().startswith("F0") or not sysex.upper().rstrip().endswith("F7"):
            errors.append("il messaggio della patch non è un messaggio SysEx (F0 … F7)")
        elif model in ZOOM_MODELS and not sysex.upper().startswith("F0 52"):
            errors.append("il messaggio della patch non è un messaggio Zoom (F0 52 … F7)")
        else:
            cp["sysex"] = sysex.strip().upper()
    vol = p.get("volume")
    if vol is not None and (not isinstance(vol, int) or not 0 <= vol <= 127):
        errors.append("volume della patch non valido")
    cp["volume"] = vol if isinstance(vol, int) else None
    slots = p.get("slots")
    if not isinstance(slots, list) or not 1 <= len(slots) <= MAX_SLOTS:
        errors.append("la patch deve avere da 1 a 10 effetti")
        slots = []
    cs = []
    for s in slots:
        ok = isinstance(s, dict) and isinstance(s.get("effectId"), int) and 0 <= s["effectId"] < 2**32 \
            and isinstance(s.get("on"), bool) and isinstance(s.get("params"), list) and len(s["params"]) <= MAX_PARAMS \
            and all(isinstance(v, int) and 0 <= v < 65536 for v in s["params"])
        if not ok:
            errors.append("un effetto della patch non è valido")
            break
        cs.append({"effectId": s["effectId"], "on": s["on"], "params": s["params"]})
    cp["slots"] = cs
    clean["patch"] = cp
    if clean["name"] != cp["name"]:
        clean["name"] = cp["name"]
    return errors, clean


def patch_id(clean):
    core = json.dumps({"model": clean["model"], "slots": clean["patch"]["slots"], "sysex": clean["patch"].get("sysex")}, sort_keys=True)
    return hashlib.sha1(core.encode()).hexdigest()[:10]


def extract(body):
    """Il JSON della patch dal testo della segnalazione (blocco ```json), oppure dal file .json allegato."""
    body = body or ""
    m = re.search(r"```json\s*\n(.*?)\n```", body, re.S)
    raw = m.group(1).strip() if m else ""
    if raw.startswith("{"):
        try:
            return json.loads(raw)
        except json.JSONDecodeError as e:
            raise ValueError(f"il testo della patch non è JSON valido ({e.msg})")
    a = ATTACH_RE.search(body)
    if a:
        with urllib.request.urlopen(a.group(0), timeout=20) as r:
            data = r.read(MAX_FILE + 1)
        if len(data) > MAX_FILE:
            raise ValueError("file allegato troppo grande")
        return json.loads(data.decode("utf-8"))
    s, e = body.find("{"), body.rfind("}")
    if 0 <= s < e:
        return json.loads(body[s:e + 1])
    raise ValueError("non trovo la patch: usa «Condividi nella libreria…» in PatchPilot, oppure trascina qui il file .json")


def existing_ids():
    out = {}
    for d, _, files in os.walk(PATCH_DIR):
        for f in files:
            if f.endswith(".json"):
                m = re.search(r"-([0-9a-f]{10})\.json$", f)
                if m:
                    out[m.group(1)] = os.path.relpath(os.path.join(d, f), LIB)
    return out


def rebuild_index():
    items = []
    for d, _, files in os.walk(PATCH_DIR):
        for f in sorted(files):
            if not f.endswith(".json"):
                continue
            path = os.path.join(d, f)
            with open(path, encoding="utf-8") as fh:
                o = json.load(fh)
            errs, c = check(o)
            if errs:
                print(f"::warning::{path}: {'; '.join(errs)}")
                continue
            p = c["patch"]
            items.append({
                "id": patch_id(c), "file": os.path.relpath(path, LIB).replace(os.sep, "/"),
                "model": c["model"], "name": c["name"], "author": c["author"], "song": c["song"], "artist": c["artist"],
                "genre": c["genre"], "notes": c["notes"], "date": c["date"], "issue": o.get("issue"),
                "volume": p.get("volume"),
                "effects": [{"id": "%08X" % s["effectId"], "on": s["on"]} for s in p["slots"]],
            })
    items.sort(key=lambda x: (x.get("date") or ""), reverse=True)
    with open(INDEX, "w", encoding="utf-8") as fh:
        json.dump({"format": "patchpilot-libreria-elenco", "version": 1, "count": len(items), "patches": items}, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    return items


def gh(method, url, data=None):
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print(f"(senza GITHUB_TOKEN) {method} {url} {data}")
        return None
    req = urllib.request.Request("https://api.github.com" + url, method=method,
                                 data=None if data is None else json.dumps(data).encode(),
                                 headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
                                          "Content-Type": "application/json", "X-GitHub-Api-Version": "2022-11-28"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read()


def comment(repo, n, msg):
    gh("POST", f"/repos/{repo}/issues/{n}/comments", {"body": msg})


def labels(repo, n, add=(), remove=()):
    if add:
        gh("POST", f"/repos/{repo}/issues/{n}/labels", {"labels": list(add)})
    for l in remove:
        try:
            gh("DELETE", f"/repos/{repo}/issues/{n}/labels/{l}")
        except Exception:
            pass


def from_issue():
    with open(os.environ["GITHUB_EVENT_PATH"], encoding="utf-8") as fh:
        ev = json.load(fh)
    issue = ev["issue"]
    return os.environ["GITHUB_REPOSITORY"], issue["number"], issue.get("body") or ""


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "elenco":
        print(f"{len(rebuild_index())} patch nell'elenco")
        return
    if cmd == "prova":
        with open(sys.argv[2], encoding="utf-8") as fh:
            errs, c = check(json.load(fh))
        print("OK " + patch_id(c) if not errs else "ERRORI: " + "; ".join(errs))
        sys.exit(1 if errs else 0)
    repo, n, body = from_issue()
    try:
        errs, c = check(extract(body))
    except Exception as e:  # noqa: BLE001 — qualsiasi problema del testo diventa un messaggio per chi l'ha mandata
        errs, c = [str(e)], None
    dup = existing_ids().get(patch_id(c)) if c and not errs else None
    if cmd == "controlla":
        if errs:
            comment(repo, n, "❌ **La patch non va ancora bene · The patch is not valid yet**\n\n- " + "\n- ".join(errs) +
                    "\n\nCorreggi il testo qui sopra (modifica la segnalazione) e il controllo ripartirà da solo. · Edit the issue and the check runs again.")
            labels(repo, n, add=["da-correggere"], remove=["da-controllare"])
        elif dup:
            comment(repo, n, f"ℹ️ Questa patch è già nella libreria · Already in the library: `{dup}`")
            labels(repo, n, add=["doppione"], remove=["da-controllare"])
        else:
            song = f" · {c['song']}" if c["song"] else ""
            comment(repo, n, f"✅ **Patch valida · Valid patch**: {c['model']} · **{c['name']}**{song} · {len(c['patch']['slots'])} effetti · di {c['author']}\n\n"
                            "Grazie! Appena approvata comparirà nella libreria. · Thanks! It will appear in the library once approved.")
            labels(repo, n, add=["libreria", "da-controllare"], remove=["da-correggere"])
        return
    if cmd == "aggiungi":
        if errs:
            comment(repo, n, "❌ Non aggiunta: " + "; ".join(errs))
            sys.exit(1)
        if dup:
            comment(repo, n, f"ℹ️ Già nella libreria: `{dup}`")
            return
        pid = patch_id(c)
        c["issue"] = n
        folder = os.path.join(PATCH_DIR, slug(c["model"]))
        os.makedirs(folder, exist_ok=True)
        name = "-".join(slug(x) for x in [c["song"], c["name"]] if x) + f"-{pid}.json"
        with open(os.path.join(folder, name), "w", encoding="utf-8") as fh:
            json.dump(c, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
        rebuild_index()
        comment(repo, n, f"🎉 **Nella libreria · In the library!** {SITE}#{pid}\n\nGrazie per averla condivisa · Thanks for sharing.")
        labels(repo, n, remove=["da-controllare"])
        gh("PATCH", f"/repos/{repo}/issues/{n}", {"state": "closed", "state_reason": "completed"})
        return
    print(__doc__)
    sys.exit(2)


if __name__ == "__main__":
    main()
