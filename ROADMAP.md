# 🗺️ Culture Connects – Roadmap

> **Große Vision behalten · kleinen Kern bauen · mit echten Menschen testen · aus Ergebnissen lernen.**

**Stand:** Oktober 2026 · **Dokumenttyp:** Produkt- & Technik-Roadmap (Checklist)

---

## 🧭 Leitprinzip

Die Vision bleibt groß. Die erste technische Version bleibt klein.

Das MVP beweist **eine einzige Hypothese**:

> ❓ *Können zwei Menschen mit unterschiedlichen Perspektiven durch eine strukturierte digitale Begegnung und anschließende KI-Reflexion zu besserem gegenseitigem Verständnis gelangen – und möchten sie danach **freiwillig erneut** teilnehmen?*

Die wichtigste frühe Kennzahl ist **nicht** die Nutzerzahl, sondern die **zweite freiwillige Begegnung**.

---

## 🔑 Legende

| Symbol | Bedeutung |
|:------:|-----------|
| ☐ | offen / geplant |
| ◔ | in Arbeit |
| ☑ | erledigt |
| 🎯 | MVP-kritisch |
| 🧩 | modular erweiterbar |
| 🔮 | Post-MVP / Vision |

**Status-Konvention:** Beim Abarbeiten `☐` → `◔` → `☑` setzen.

---

## 🧱 Architektur-Leitentscheidungen (für alle Phasen gültig)

Diese Entscheidungen reduzieren Aufwand und Risiko erheblich und gelten als verbindlicher Rahmen:

- [ ] **🎯 Asynchrone (rundenbasierte) Textdebatte zuerst**, nicht Live-Chat.
  *Grund: löst Cold-Start, Zeitzonen- und Verfügbarkeitsproblem bei < 100 Nutzern. Live/Real-time erst nach validiertem Kern.*
- [x] **🎯 Modularer Monolith** statt Microservices.
  *Klare Domänengrenzen (Users, Profiles, Topics, Matching, Debates, Reputation, Moderation, AI) in **einem** Deploy-Artefakt. — Umgesetzt: Django-Apps unter `backend/apps/`.*
- [x] **🎯 KI hinter einem Adapter** (`AIProvider`-Interface), Analyse **asynchron** über Job-Queue.
  *Adapter + `MockAIProvider` in `apps/ai/providers` umgesetzt; asynchrone Job-Queue folgt in M5.*
- [ ] **🧩 Service-Interfaces für spätere Austauschbarkeit** (`ReputationService`, `RewardService`) – DB-Implementierung heute, Blockchain-Adapter optional später.
- [ ] **🎯 Privacy-by-Design & Server-seitige Zustandsvalidierung** von Beginn an (siehe [README](./README.md)).

---

## 📊 Milestone-Übersicht

| # | Milestone | Fokus | Scope |
|:-:|-----------|-------|:-----:|
| M0 | 🏗️ Fundament ◔ | Repo, CI, Grundgerüst | 🎯 |
| M1 | 👤 Identität & Profile | Registrierung, Pseudonym, Profil | 🎯 |
| M2 | 🗂️ Themen | Topic-Engine | 🎯 |
| M3 | 🔗 Matching | deterministisches Matching | 🎯 |
| M4 | 💬 Debatten-Engine | async, strukturierter Ablauf | 🎯 |
| M5 | 🤖 KI-Reflexion | Analyse nach Abschluss | 🎯 |
| M6 | 🪞 Nutzer-Reflexion | subjektives Feedback | 🎯 |
| M7 | 🛡️ Reputation & Trust/Safety | Bewertung, Moderation, Meldung | 🎯 |
| M8 | 📊 Persönliche Statistik | minimaler Verlauf | 🎯 |
| M9 | 🔁 Wiederbegegnung | zweite Begegnung ermöglichen | 🎯 |
| M10 | 🧪 Pilot | Test mit 0–100 echten Menschen | 🎯 |
| V1+ | 🔮 Vision | Voice, i18n, Community, Blockchain … | 🔮 |

**MVP = M0 → M10.** Erst wenn M10 die Hypothese stützt, beginnt die Vision-Phase.

---

## 🏗️ M0 – Fundament

**Ziel:** Lauffähiges Grundsystem ohne unnötige Komplexität.

- [ ] **◔** Monorepo-Struktur (`backend/`, `frontend/`, `docs/`, `infra/`)
  *`backend/`, `frontend/`, `docs/` vorhanden; `infra/` noch offen – Docker Compose liegt im Root, CI unter `.github/`.*
- [x] Entwicklungsumgebung reproduzierbar (Docker Compose: App + DB + Queue)
  *`docker-compose.yml` (backend, frontend, PostgreSQL, Redis); Config validiert & Images gebaut.*
- [x] Backend-Grundgerüst + Health-Endpoint *(Django + DRF, `GET /api/health`)*
- [x] Datenbank + Migrationssystem *(Django-Migrationen; PostgreSQL via `DATABASE_URL`, SQLite-Fallback)*
- [x] Frontend-Grundgerüst *(React + TypeScript + Vite, Backend-Health-Statusanzeige)*
- [x] Konfiguration über Umgebungsvariablen (`.env.example`) *(`django-environ`, liest Repo-`.env`)*
- [ ] **◔** Strukturiertes Logging + zentrale Fehlerbehandlung
  *Logging nach stdout konfiguriert; zentrale Fehlerbehandlung noch DRF-Default.*
- [ ] Basis-Sicherheitskonzept (Auth-Strategie, Secret-Handling, Rate-Limit-Stelle)
  *Teilweise: Secret-Handling über Env, DRF-SessionAuth als Standard; Rate-Limit-Stelle noch offen.*
- [x] CI-Pipeline (Lint + Tests + Build) *(GitHub Actions: ruff · check · test | oxlint · build)*
- [x] `AIProvider`-Interface mit Mock-Implementierung *(`apps/ai/providers`, `MockAIProvider`, Factory)*

**✅ Definition of Done:** `docker compose up` startet App, DB & Queue; Health-Check grün; CI läuft.
*Status: Compose-Config validiert & Images gebaut (Container-Start in der Dev-Sandbox durch rlimit-Beschränkung blockiert); Health-Check lokal grün; CI-Workflow vorhanden, erster Lauf auf GitHub noch ausstehend.*

---

## 👤 M1 – Identität & Profile 🎯

**Ziel:** Nutzer registrieren sich und legen ein pseudonymes Profil an.

- [ ] Registrierung / Login / Logout
- [ ] Pseudonym (kein Klarname erforderlich)
- [ ] Trennung **öffentliches** vs. **privates** Profil
- [ ] Interessen & Themenkategorien
- [ ] Sprache, bevorzugte Debattendauer, Matching-Modus
- [ ] Datenschutz-Einstellungen (Sichtbarkeit, Veröffentlichungs-Einwilligung)
- [ ] Altersangabe + Minderjährigenschutz-Flag

**Matching-Modi:** ähnlich · ausgewogen · unterschiedlich · konträr · maximal konträr (mit Safety-Grenzen).

**✅ DoD:** Ein Nutzer kann ein Profil erstellen, auf dessen Basis ein Match erzeugt werden kann.

---

## 🗂️ M2 – Topic Engine 🎯 🧩

**Ziel:** Debattenthemen strukturiert verwalten.

- [ ] Themenkategorien (Politik, Gesellschaft, Philosophie, Wissenschaft, Technik, Kultur …)
- [ ] Vordefinierte Startthemen (kuratiertes Seed-Set)
- [ ] Nutzer können Themen vorschlagen (mit Status/Review)
- [ ] Themen-Metadaten + Debatten-Eignung + Filter
- [ ] 🔮 KI-Unterstützung: Formulierung, Kategorisierung, Vorschläge *(nur formale Kriterien, keine ideologische „Richtigkeit")*

**✅ DoD:** Ein kuratiertes Set debattierbarer Themen ist verfügbar und filterbar.

---

## 🔗 M3 – Matching Engine 🎯

**Ziel:** Zwei geeignete Gesprächspartner zusammenführen – **deterministisch**, nicht ML.

- [ ] Kandidaten-Pool nach Sprache, Thema, Dauer, Perspektivunterschied (+ optional Alter/Region)
- [ ] Zweistufig: **1. Pool bestimmen → 2. Begegnung auswählen** (Kontrolle + Überraschung)
- [ ] Eignungs-Filter (Minderjährigenschutz, Sperrlisten, Safety-Grenzen bei „maximal konträr")
- [ ] Async-tauglich: Match ohne gleichzeitige Anwesenheit beider Personen

**✅ DoD:** Für ein Nutzerpaar entsteht ein valider Match, der eine Debatte starten kann.

---

## 💬 M4 – Debatten-Engine 🎯

**Ziel:** Der eigentliche Kern – **asynchrone, strukturierte Textdebatte**.

- [ ] Debattenraum mit explizitem Zustandsmodell: `CREATED → MATCHED → WAITING → ACTIVE → REFLECTION → COMPLETED`
- [ ] Rollen/Positionen, definierter Ablauf (Einführung → Position A/B → Argumentation → Rückfragen → Abschluss)
- [ ] Rundenbasierte Beiträge mit Benachrichtigung bei Zug des Partners
- [ ] Server-seitige Validierung **jedes** Zustandsübergangs (Client nie vertrauen)
- [ ] Abbruch-/Timeout-Logik (inaktiver Partner)
- [ ] Persistente Debattenstruktur

**Bewusst noch nicht:** Live-Chat, Video, öffentliche Chats, Community-Feed.

**✅ DoD:** Zwei Menschen führen eine Debatte von Start bis Abschluss durch.

---

## 🤖 M5 – KI Debate Analysis 🎯 🧩

**Ziel:** Nach Abschluss eine strukturierte Reflexion erzeugen – **Werkzeug, nicht Richter**.

- [ ] Analyse läuft **asynchron** (Job-Queue), erst nach `COMPLETED`
- [ ] Dimensionen: Argumentationsqualität, Logik, Fairness, Zuhören, Verständnis, Sachlichkeit, Quellen, Gemeinsamkeiten/Unterschiede, Begriffsdefinitionen, Lernimpulse
- [ ] Ausgabe: *Gemeinsamkeiten · Unterschiede · Missverständnisse · neue Perspektiven · offene Fragen*
- [ ] **Keine** Sieger-/„wer hat recht"-Wertung
- [ ] Klare Kennzeichnung **Beobachtung** vs. **Interpretation/Hypothese**
- [ ] Kostenkontrolle: strukturierter, begrenzter Kontext statt ganzer Verlauf

**✅ DoD:** Nach jeder abgeschlossenen Debatte liegt eine hilfreiche, neutrale Reflexion vor.

---

## 🪞 M6 – Nutzer-Reflexion & Feedback 🎯

**Ziel:** KI-Analyse mit der subjektiven Wahrnehmung verbinden.

- [ ] Fragebogen: Fühlte ich mich verstanden? Verstehe ich die andere Person besser? Hat sich meine Sicht verändert? Erneut sprechen?
- [ ] Selbstmarkierung „**Das hat meine Sicht verändert**" (+ optionaler Grund: Fakt, Argument, Erfahrung, Werte, Freitext)
- [ ] Keine automatische KI-Behauptung einer Meinungsänderung

**✅ DoD:** Nutzer können nach der Debatte ihr Erleben erfassen; Signale sind auswertbar.

---

## 🛡️ M7 – Reputation & Trust/Safety 🎯

**Ziel:** Konstruktives Verhalten erfassen **und** Sicherheit gewährleisten. *(Trust & Safety ist MVP-kritisch, nicht später!)*

- [ ] Gegenseitige Bewertung: Respekt · Fairness · Zuhören · konstruktives Verhalten *(kein Sieger-System)*
- [ ] **Melde-Funktion** für Belästigung/Missbrauch
- [ ] **Blockieren** einer Person
- [ ] Moderations-Backend (Review-Queue, Sperren) – nutzt Admin-Oberfläche des Frameworks
- [ ] Verhaltensbasierte Regeln statt ideologischer Klassifikation
- [ ] Rate-Limiting & Spam-/Manipulationsschutz

**✅ DoD:** Nutzer können melden/blockieren; Meldungen sind moderierbar; Bewertungen fließen in Reputation.

---

## 📊 M8 – Persönliche Statistik 🎯

**Ziel:** Minimaler persönlicher Entwicklungsüberblick.

- [ ] Anzahl (abgeschlossener) Debatten, Themenbereiche, Wiederbegegnungen, eigene Reflexionsangaben
- [ ] 🔮 Später: Argumentationsmuster, Positionsentwicklung, Kommunikationsqualität *(mit Beobachtung/Interpretation-Trennung)*

**✅ DoD:** Nutzer sehen einen einfachen, ehrlichen Überblick ihrer Begegnungen.

---

## 🔁 M9 – Wiederholte Begegnungen 🎯

**Ziel:** Aus einzelnen Begegnungen Lernverläufe entstehen lassen – **der entscheidende Hypothesen-Test**.

- [ ] „Erneut mit dieser Person sprechen" / „keine erneute Begegnung" / „blockieren"
- [ ] Neue Debatte für dasselbe Paar
- [ ] 🔮 Später: kontrastierende Themen, gemeinsamer Entwicklungsverlauf (beidseitige Zustimmung)

**✅ DoD:** Eine zweite Begegnung ist technisch möglich und messbar.

---

## 🧪 M10 – MVP-Pilot 🎯

**Ziel:** Mit echten Menschen testen – Fokus auf **Lernen**, nicht Wachstum.

- [ ] Startgröße **0–100 Nutzer** (persönliche Kontakte, Hochschul-/Vereins-/Themen-Communities)
- [ ] Analytics für den Funnel (datensparsam!)
- [ ] Feedback-Kanal für Pilot-Teilnehmer
- [ ] Rechtliches Minimum: Datenschutzerklärung, AGB, Einwilligungen, Minderjährigenschutz

**Funnel-Messgrößen:**

```text
Match → Debatte gestartet
Debatte gestartet → beendet
beendet → KI-Analyse angesehen
beendet → Nutzer fühlt sich verstanden
1. Debatte → 2. Debatte          ⭐ wichtigste Kennzahl
1. Debatte → Weiterempfehlung
```

**✅ DoD:** Belastbare erste Daten zur zweiten freiwilligen Begegnung liegen vor.

---

# 🔮 Vision-Phasen (Post-MVP)

> Erst starten, wenn der MVP-Kern validiert ist. Jede Phase ist ein eigenständiges, modular ergänzbares Modul 🧩.

### 🎙️ V1 – Voice
- [ ] Voice-Debatte, Transkription, Sprechererkennung, KI-Analyse des Gesprächs

### 🌍 V2 – Mehrsprachigkeit
- [ ] Mehrsprachige UI, automatische Übersetzung von Textdebatten, später Voice-Übersetzung

### 🎲 V3 – Challenge Mode
- [ ] Konfigurierbare Gegensätzlichkeit (Thema, Region, Sprache, Schwierigkeit)
- [ ] Schutzmechanismen für Minderjährige & sensible Themen

### 🏛️ V4 – Community
- [ ] „Debate of the Week/Month", kuratierte Debatten, Themen-Abstimmungen
- [ ] *Entdecken statt Scrollen* – kein endloser Social Feed

### 📣 V5 – Organisches Empfehlungsmodell
- [ ] Einladung aus guter Erfahrung heraus – keine aggressiven Referral-Mechaniken

### ⭐ V6 – Creator & Multiplikatoren
- [ ] Einbindung von Personen aus Philosophie, Wissenschaft, Bildung, Technik …

### 🤝 V7 – Projekte & Kooperation
- [ ] Gemeinsame Projekte, Veranstaltungen, lokale Initiativen; Projekt-Matching

### 💼 V8 – Beruflicher Bereich *(bewusst nachrangig)*
- [ ] Freiwillige fachliche Sichtbarkeit; keine automatisierten Einstellungsentscheidungen

### ⛓️ V9 – Blockchain-Adapter *(optional)*
- [ ] Nur bei konkretem Mehrwert: Reputation, Rewards, Attestierungen via Adapter
- [ ] `ReputationService → DatabaseImpl` heute · `→ BlockchainImpl` später

### 🧅 V10 – Onion-Service *(Privacy-Zugang)*
- [ ] Zusätzlicher Tor-Zugang **zur bestehenden App** (keine zweite Plattform)
- [ ] Teil eines ganzheitlichen Privacy-by-Design, nicht als Gimmick
- [ ] Für Text früh möglich; nicht von Video-Architektur abhängig machen

---

## 🧷 Leitgedanke

> **Nicht Einigkeit um jeden Preis. Nicht Sieg um jeden Preis. Sondern Verständnis.**
>
> **Den Kern bauen · mit echten Menschen testen · lernen · dann erweitern.**

Der erste echte Meilenstein: *Zwei Fremde führen eine strukturierte Debatte, schließen sie ab, erhalten eine hilfreiche KI-Reflexion – und möchten freiwillig wieder teilnehmen.*
