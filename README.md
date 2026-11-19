<div align="center">

<img src="immagini/icona.png" width="120" alt="PatchPilot">

# 🎛️ PatchPilot

### Your multi-effects pedal, on your Android phone — and on Windows & Linux
**MS-50G+ · MS-60B+ · MS-70CDR+ · MS-80IR+ · MS-200D+ · G2 FOUR · B2 FOUR · G6 · G11 · B6** — over a **USB cable**

[![Windows](https://img.shields.io/badge/⬇_Download-Windows-0078d4?style=for-the-badge&logo=windows&logoColor=white)](../../releases/latest)
[![Linux](https://img.shields.io/badge/⬇_Download-Linux-333333?style=for-the-badge&logo=linux&logoColor=white)](../../releases/latest)
[![Google Play](https://img.shields.io/badge/Google_Play-coming_soon-45b86e?style=for-the-badge&logo=googleplay&logoColor=white)](#-on-google-play)
[![Testers](https://img.shields.io/badge/🙋_Testers-wanted-0e4a57?style=for-the-badge)](TEST.md#english)
[![Full version](https://img.shields.io/badge/🔑_Full_version-€4.99-003087?style=for-the-badge&logo=paypal&logoColor=white)](#full-version)

🌐 **Website:** https://francescorizzo-cyber.github.io/patchpilot/ · *[Italiano più sotto](#italiano)*

![PatchPilot](immagini/00_copertina.png)

</div>

PatchPilot connects your **Zoom-compatible multi-effects pedal** to your **Android phone or tablet** with a USB cable
and shows what is inside: **patches, effects, parameters and the tuner**. Zoom has a separate editor app for each pedal, almost all of them for iPhone only:
PatchPilot is made for players who use Android — and it also runs on **Windows and Linux** computers.

> 🧪 **This is a beta.** It has been built carefully but **not yet tested on every pedal**.
> 🙋 **Got one of these pedals?** Try it and send us the log from the app: [5-minute test guide](TEST.md#english) ·
> write to **[autofonic.mixer@gmail.com](mailto:autofonic.mixer@gmail.com)** · or **[open an issue](https://github.com/francescorizzo-cyber/patchpilot/issues/new/choose)**.

## 🎚️ Supported pedals

| Pedal | Model detection | Read patches & patch list | Tuner | Status |
|---|---|---|---|---|
| **MS-50G+** | ✅ | ✅ | ✅ | 🧪 waiting for testers |
| **MS-60B+ · MS-70CDR+ · MS-80IR+ · MS-200D+** | ✅ | ✅ | ✅ | 🧪 waiting for testers |
| **G2 FOUR / G2X FOUR · B2 FOUR** | ✅ | ✅ | ✅ | 🧪 waiting for testers |
| **G6 · G11 · B6** | ✅ | ⏳ later | ⏳ later | 🧪 limited support in the beta |

### 🙋 Your pedal is not in the list? Become a tester

Want PatchPilot to support your pedal, even from another brand? Help us learn how it talks.
The next version of the Windows/Linux program has a **Tester** page: a guided recording that only **listens**.
It sends your pedal nothing but the standard MIDI identity request, then records what the pedal sends while you
change patch, turn a knob, switch an effect on and off. You save one text file and email it to us.

It is not in the current download yet. In the meantime write to **[autofonic.mixer@gmail.com](mailto:autofonic.mixer@gmail.com)** with brand and model: we will tell you as soon as it is ready.

## 📱 What it does

**One app for 10 pedals**, on Android, Windows and Linux — instead of a separate app for each pedal.

**Look inside your pedal**
- **Connects over USB** and **recognises your pedal** automatically.
- **Patches**: loads the **full list with names** and reads the current patch.
- **Editor view**: each effect slot (on/off) with its parameters; import your **.ZD2** effect files to see effect and parameter names.
- **Tuner**: note and cents on the screen.

**Keep your sounds safe and organised** *(new in 0.8)*
- **Backup**: save all the patches of your pedal to a file, and load them back into the app whenever you want.
- **Sound sheets**: a readable card for every patch (effects, on/off, parameters) to print, save or share.
- **Search**: "where did I use that delay?" — find the patches that use an effect.
- **Compare**: two patches side by side, showing only what is different.

**On stage** *(new in 0.8)*
- **Setlist**: put your songs in order and choose the patch for each one — **one patch per pedal** if you use more than one pedal.
- **Stage mode**: a dark full-screen view with big text: the song, the patch to select on each pedal, and what comes next.

**And also**
- **Log + Share**: every MIDI message explained, sent to us with one tap when something does not work.
- **Demo mode and sample data**: try everything without a pedal.

*Coming after the tests on real pedals: changing patch from the app (also on several pedals at once) and editing parameters.*

## 🛡️ Your pedal is safe

The beta **only reads**. It **never writes, saves or deletes** anything in your pedal's memory: those commands are blocked in the code.
Backups, sound sheets and the setlist are files on your phone or computer: nothing is written to the pedal.
Read requests are sent only after you switch on **reading from the pedal** (Connect screen).

## ⬇️ Install

### 📱 Android: coming soon on Google Play

The Android app will be installed **only from Google Play**. It is not available yet: the link will appear here.
It will need **Android 8.0 or later** with **USB host (OTG)** and a **USB-C / OTG cable** for the pedal.

### 💻 Windows and Linux

- **Windows 10/11**: `PatchPilot-x.y.z-windows-x64-setup.exe` (installer) or `…-portatile.zip` (portable, no install). If SmartScreen warns you, click **More info → Run anyway**.
- **Linux**: `PatchPilot-x.y.z-linux-x64.deb` (Ubuntu/Debian: `sudo apt install ./PatchPilot-….deb`) or `…-linux-x64.tar.gz` (unpack and run `PatchPilot/bin/PatchPilot`).
- Java is included. Connect the pedal with its USB cable, then **Collega → Cerca dispositivi → Collega e identifica**. Close Guitar Lab first: the pedal's MIDI port works with one program at a time.

> ℹ️ If you installed an earlier APK from this page: when PatchPilot arrives on **Google Play**, uninstall it first. The two versions are signed differently.

<a id="full-version"></a>

## 🔑 Full version: €4.99, one time only

**Today every feature is free**, because PatchPilot is in beta. Later, exporting backups to a file, sound sheets, search, compare,
the setlist beyond 3 songs and stage mode will be part of the **full version: €4.99, paid once**, valid forever on that phone or computer.
Model detection, patch list, editor view, tuner and a 3-song setlist stay free.
If you buy now you support the project and you already have your code when the full version is switched on.

1. Open PatchPilot on your computer and go to the *Sostieni ♥* page. Your device code looks like `PP-ABCD-EFGH`.
2. Pay **€4.99**, either way:
   - **[💳 Card, Google Pay or Apple Pay (Stripe)](https://buy.stripe.com/00w6oG96j0DqcBG5DX63K01)**: type your device code when asked and the **unlock code appears right after the payment**.
   - **[🅿️ PayPal](https://paypal.me/AutoFonicMixer/4.99EUR)**: then send the email to **[autofonic.mixer@gmail.com](mailto:autofonic.mixer@gmail.com)** and you receive your **unlock code** by email, usually within a day.

One code per computer (Windows and Linux). On Android (coming soon on Google Play) the full version will be bought inside the app, with Google Play.
Just want to say thanks? Any amount is welcome: **[paypal.me/AutoFonicMixer](https://paypal.me/AutoFonicMixer)**.

## 🛒 On Google Play

Coming soon. The Android app will be available only from Google Play; the link will appear here.

## 📄 Privacy & license

No account, no ads, no data collected, no internet access: [privacy policy](PRIVACY.md). Free to use: [license](LICENSE).

PatchPilot is an independent project, **not affiliated with, endorsed or sponsored by Zoom Corporation**.
Zoom, MultiStomp and Handy Guitar Lab are trademarks of their respective owners, mentioned only to describe compatibility.

---

<a id="italiano"></a>

# 🇮🇹 Italiano

<div align="center">

![PatchPilot](immagini/00_copertina_it.png)

</div>

PatchPilot collega il tuo **multieffetto a pedale compatibile Zoom** al **telefono o tablet Android** con un cavo USB
e ti mostra cosa contiene: **patch, effetti, parametri e accordatore**. Zoom ha un'app diversa per ogni pedale, quasi tutte solo per iPhone:
PatchPilot nasce per chi usa Android, e funziona anche sui computer **Windows e Linux**.

🌐 **Sito:** https://francescorizzo-cyber.github.io/patchpilot/it/ · 🔑 **[Versione completa: 4,99 €](#versione-completa)**

> 🧪 **È una beta.** È stata costruita con cura ma **non è ancora stata provata su tutti i pedali**.
> 🙋 **Hai uno di questi pedali?** Provala e mandaci il registro dall'app: [guida di prova in 5 minuti](TEST.md#italiano) ·
> scrivi a **[autofonic.mixer@gmail.com](mailto:autofonic.mixer@gmail.com)** · oppure **[apri una segnalazione](https://github.com/francescorizzo-cyber/patchpilot/issues/new/choose)**.

## 🎚️ Pedali supportati

| Pedale | Riconoscimento | Lettura patch ed elenco | Accordatore | Stato |
|---|---|---|---|---|
| **MS-50G+** | ✅ | ✅ | ✅ | 🧪 aspetta i tester |
| **MS-60B+ · MS-70CDR+ · MS-80IR+ · MS-200D+** | ✅ | ✅ | ✅ | 🧪 aspetta i tester |
| **G2 FOUR / G2X FOUR · B2 FOUR** | ✅ | ✅ | ✅ | 🧪 aspetta i tester |
| **G6 · G11 · B6** | ✅ | ⏳ più avanti | ⏳ più avanti | 🧪 supporto limitato nella beta |

### 🙋 Il tuo pedale non è in elenco? Diventa tester

Vuoi che PatchPilot supporti il tuo pedale, anche di un'altra marca? Aiutaci a capire come parla.
La prossima versione del programma per Windows e Linux ha la pagina **Tester**: una registrazione guidata che **ascolta soltanto**.
Al pedale manda solo la richiesta di identità MIDI standard, poi registra quello che il pedale invia mentre
cambi patch, giri una manopola, spegni e riaccendi un effetto. Alla fine salvi un file di testo e ce lo mandi per email.

Non è ancora nel download attuale. Intanto scrivi a **[autofonic.mixer@gmail.com](mailto:autofonic.mixer@gmail.com)** con marca e modello: ti avvisiamo appena è pronta.

## 📱 Cosa fa

**Una sola app per 10 pedali**, su Android, Windows e Linux, al posto di un'app diversa per ogni pedale.

**Guarda dentro il pedale**
- **Si collega via USB** e **riconosce il pedale** da solo.
- **Patch**: carica **l'elenco completo con i nomi** e legge la patch corrente.
- **Editor**: ogni slot (acceso/spento) con i suoi parametri; importa i tuoi file **.ZD2** per vedere i nomi di effetti e parametri.
- **Accordatore**: nota e cents sullo schermo.

**Tieni i tuoi suoni al sicuro e in ordine** *(novità 0.8)*
- **Backup**: salva su file tutte le patch del pedale e ricaricale nell'app quando vuoi.
- **Schede suono**: una scheda leggibile per ogni patch (effetti, acceso/spento, parametri) da stampare, salvare o condividere.
- **Cerca**: "dove ho usato quel delay?" — trova le patch che usano un effetto.
- **Confronta**: due patch a confronto, mostrando solo le differenze.

**Sul palco** *(novità 0.8)*
- **Scaletta**: metti in ordine i brani e scegli la patch per ognuno — **una patch per pedale** se ne usi più di uno.
- **Modalità palco**: schermo scuro a caratteri grandi con il brano, la patch da selezionare su ogni pedale e il brano successivo.

**E inoltre**
- **Registro + Condividi**: ogni messaggio MIDI spiegato, e con un tocco ce lo mandi se qualcosa non va.
- **Modalità demo e dati di esempio**: per provare tutto senza pedale.

*In arrivo dopo le prove sui pedali reali: cambio patch dall'app (anche su più pedali insieme) e modifica dei parametri.*

## 🛡️ Il tuo pedale è al sicuro

La beta **legge soltanto**. **Non scrive, non salva e non cancella** nulla nella memoria del pedale: quei comandi sono bloccati nel codice.
Backup, schede suono e scaletta sono file sul tuo telefono o computer: sul pedale non viene scritto niente.
Le richieste di lettura partono solo dopo aver attivato la **lettura dal pedale** (schermata Collega).

## ⬇️ Installazione

### 📱 Android: in arrivo su Google Play

L'app Android si installerà **solo da Google Play**. Non è ancora disponibile: il link comparirà qui.
Servirà **Android 8.0 o successivo** con **USB host (OTG)** e un cavo **USB-C / OTG** per il pedale.

### 💻 Windows e Linux

- **Windows 10/11**: `PatchPilot-x.y.z-windows-x64-setup.exe` (installatore) oppure `…-portatile.zip` (senza installazione). Se SmartScreen avvisa, clicca **Ulteriori informazioni → Esegui comunque**.
- **Linux**: `PatchPilot-x.y.z-linux-x64.deb` (Ubuntu/Debian: `sudo apt install ./PatchPilot-….deb`) oppure `…-linux-x64.tar.gz` (scompatta e avvia `PatchPilot/bin/PatchPilot`).
- Java è incluso. Collega il pedale con il suo cavo USB, poi **Collega → Cerca dispositivi → Collega e identifica**. Chiudi prima Guitar Lab: la porta MIDI del pedale funziona con un programma alla volta.

> ℹ️ Se avevi installato un APK scaricato da questa pagina: quando PatchPilot arriverà su **Google Play**, disinstallalo prima. Le due versioni sono firmate in modo diverso.

<a id="versione-completa"></a>

## 🔑 Versione completa: 4,99 €, una volta sola

**Oggi tutte le funzioni sono gratuite**, perché PatchPilot è in beta. Più avanti l'esportazione dei backup su file, le schede suono,
la ricerca, il confronto, la scaletta oltre i 3 brani e la modalità palco faranno parte della **versione completa: 4,99 €, una volta sola**,
valida per sempre su quel telefono o computer. Riconoscimento del pedale, elenco patch, editor, accordatore e scaletta di 3 brani restano gratuiti.
Se la compri adesso sostieni il progetto e hai già il tuo codice quando la versione completa verrà attivata.

1. Apri PatchPilot sul computer e vai alla pagina *Sostieni ♥*. Il codice dispositivo ha la forma `PP-ABCD-EFGH`.
2. Paga **4,99 €**, come preferisci:
   - **[💳 Carta, Google Pay o Apple Pay (Stripe)](https://buy.stripe.com/00w6oG96j0DqcBG5DX63K01)**: scrivi il codice dispositivo quando viene chiesto e il **codice di sblocco appare subito dopo il pagamento**.
   - **[🅿️ PayPal](https://paypal.me/AutoFonicMixer/4.99EUR)**: poi invia l'email ad **[autofonic.mixer@gmail.com](mailto:autofonic.mixer@gmail.com)** e ricevi il **codice di sblocco** per email, di solito entro un giorno.

Un codice per ogni computer (Windows e Linux). Su Android (in arrivo su Google Play) la versione completa si comprerà dentro l'app, con Google Play.
Vuoi solo dire grazie? Qualsiasi offerta è benvenuta: **[paypal.me/AutoFonicMixer](https://paypal.me/AutoFonicMixer)**.

## 📄 Privacy e licenza

Nessun account, nessuna pubblicità, nessun dato raccolto, nessun accesso a Internet: [informativa privacy](PRIVACY.md). Uso gratuito: [licenza](LICENSE).

PatchPilot è un progetto indipendente, **non affiliato, approvato o sponsorizzato da Zoom Corporation**.
Zoom, MultiStomp e Handy Guitar Lab sono marchi dei rispettivi proprietari, citati solo per indicare la compatibilità.

Contatti: **[autofonic.mixer@gmail.com](mailto:autofonic.mixer@gmail.com)**
