# 🌐 Culture Connects

> **Eine Plattform für echte Begegnungen zwischen Menschen mit unterschiedlichen Perspektiven – strukturierte Debatten mit KI-gestützter Reflexion.**

Culture Connects will nicht Menschen überzeugen, ihre Meinung zu ändern. Das Ziel ist ein anderes:

> 💡 *„Ich verstehe jetzt besser, warum dieser Mensch so denkt – auch wenn ich weiterhin anderer Meinung bin."*

**Mensch → Mensch → Austausch → Verständnis → Reflexion → Lernen.** Die Technologie unterstützt diesen Prozess, sie ersetzt ihn nicht.

---

## 📑 Inhalt

- [✨ Was ist Culture Connects?](#-was-ist-culture-connects)
- [🔄 Der Produktkern](#-der-produktkern-mvp-loop)
- [🎯 MVP-Funktionsumfang](#-mvp-funktionsumfang)
- [🧱 Architektur](#-architektur)
- [🛠️ Tech-Stack](#️-tech-stack)
- [📁 Projektstruktur](#-projektstruktur)
- [🚀 Schnellstart](#-schnellstart)
- [🔐 Datenschutz & Sicherheit](#-datenschutz--sicherheit)
- [🤖 KI-Prinzipien](#-ki-prinzipien)
- [🧪 Tests](#-tests)
- [🗺️ Roadmap](#️-roadmap)
- [🤝 Mitwirken](#-mitwirken)
- [📄 Lizenz](#-lizenz)

---

## ✨ Was ist Culture Connects?

Culture Connects bringt zwei Menschen zusammen, die sich vorher nicht kannten, für eine **strukturierte, themenbezogene Textdebatte**. Nach dem Abschluss erstellt eine KI eine **neutrale Reflexion** – keine Bewertung, wer „gewonnen" hat, sondern: *Was ist in dieser Begegnung tatsächlich passiert?*

Die wichtigste Frage für den Erfolg ist nicht die Nutzerzahl, sondern:

> ❓ **Wollen Menschen nach einer ersten Begegnung freiwillig eine zweite führen?**

---

## 🔄 Der Produktkern (MVP-Loop)

```text
👤 Registrierung → 📝 Profil → 🗂️ Themen → 🔗 Matching
      → 💬 strukturierte Debatte → ✅ Abschluss
      → 🤖 KI-Analyse → 🪞 Reflexion → ⭐ Bewertung → 🔁 erneute Begegnung
```

Alles Weitere baut auf diesem funktionierenden Kern auf.

---

## 🎯 MVP-Funktionsumfang

| Bereich | Enthalten |
|---------|-----------|
| 👤 **Identität** | Registrierung, Login, Pseudonym (kein Klarname) |
| 📝 **Profil** | öffentlich/privat getrennt, Interessen, Sprache, Datenschutz-Einstellungen |
| 🗂️ **Themen** | kuratierte Kategorien + Nutzervorschläge |
| 🔗 **Matching** | deterministisch, Perspektivunterschied wählbar |
| 💬 **Debatte** | asynchron, rundenbasiert, strukturierter Ablauf |
| 🤖 **KI-Reflexion** | neutrale Analyse nach Abschluss |
| 🪞 **Feedback** | subjektives Nutzer-Erleben |
| 🛡️ **Trust & Safety** | Melden, Blockieren, Moderation |
| 📊 **Statistik** | minimaler persönlicher Verlauf |
| 🔁 **Wiederbegegnung** | zweite Begegnung ermöglichen |

**Bewusst (noch) nicht im MVP:** Video, Live-Chat, Blockchain/Token, Onion-Service, Social-Feed, berufliches Netzwerk. → siehe [ROADMAP.md](./ROADMAP.md).

---

## 🧱 Architektur

**Modularer Monolith** mit klaren Domänengrenzen – ein Deploy-Artefakt, saubere interne Module statt verfrühter Microservices.

```text
          🖥️  Frontend (SPA)
                 │  REST / JSON
                 ▼
     ┌───────────────────────────┐
     │   API / Application Layer  │
     ├───────────────────────────┤
     │  👤 Users     📝 Profiles  │
     │  🗂️ Topics    🔗 Matching  │
     │  💬 Debates   ⭐ Reputation │
     │  🛡️ Moderation             │
     │  🤖 AI ──► AIProvider-Adapter (austauschbar)
     └───────────┬───────────────┘
                 ▼
     🗄️ PostgreSQL     📨 Queue (async KI-Jobs)
```

**Verbindliche Leitentscheidungen:**

- ⚡ **Async-first:** rundenbasierte Debatten statt Live-Chat → löst Cold-Start & Verfügbarkeit bei < 100 Nutzern.
- 🔌 **KI hinter Adapter**, Analyse asynchron über Job-Queue.
- 🧩 **Service-Interfaces** (`ReputationService`, `RewardService`) ermöglichen späteren Blockchain-Adapter ohne Core-Umbau.
- 🔒 **Server-seitige Validierung** jedes Debatten-Zustandsübergangs – dem Client wird nie vertraut.

Debatten-Lebenszyklus (server-validiert):

```text
CREATED → MATCHED → WAITING → ACTIVE → REFLECTION → COMPLETED
```

---

## 🛠️ Tech-Stack

> Empfohlener, bewusst **pragmatischer** Stack für maximale MVP-Geschwindigkeit. Anpassbar – die Architektur ist stack-agnostisch.

| Schicht | Technologie | Warum |
|---------|-------------|-------|
| 🖥️ Frontend | **React + TypeScript + Vite** | schnelle DX, typsicher |
| 🔙 Backend | **Python + Django + Django REST Framework** | Auth, Migrationen & **Admin-Panel für Moderation** out-of-the-box |
| 🗄️ Datenbank | **PostgreSQL** | relationale Integrität |
| 📨 Async | **Celery + Redis** | KI-Analyse als Hintergrund-Job |
| 🤖 KI | **Provider-Adapter** (Mock → echter Anbieter) | austauschbar, testbar, kostenbewusst |
| 🐳 Dev/Deploy | **Docker Compose** | reproduzierbare Umgebung |
| ✅ CI | **GitHub Actions** | Lint + Test + Build |

💡 *Das Django-Admin-Panel deckt Moderation (M7) früh und günstig ab – ein konkreter Effizienzgewinn.*

---

## 📁 Projektstruktur

```text
culture_connects/
├── 📄 README.md
├── 🗺️ ROADMAP.md
├── 🤖 AGENT.md                # Anweisungen für KI-Entwicklungs-Agenten
├── 📚 docs/                   # Konzept & Strategie
│   ├── Culture_Connects_Gemeinsame_Erkenntnisse.md
│   └── Culture_Connects_Onion_Service.md
├── 🔙 backend/                # Django-Projekt (Domänen-Apps)
│   ├── users/  profiles/  topics/  matching/
│   ├── debates/  reputation/  moderation/
│   └── ai/                    # AIProvider-Adapter + Analyse-Tasks
├── 🖥️ frontend/               # React + TS + Vite
├── 🐳 infra/                  # docker-compose, CI, Deploy
├── ⚙️ .env.example
└── 🙈 .gitignore
```

> Backend-/Frontend-/Infra-Ordner werden in **M0** angelegt (siehe Roadmap). Dieses Repo enthält aktuell Konzept, Roadmap und Agenten-Instruktionen.

---

## 🚀 Schnellstart

> Die ausführbaren Teile entstehen in **Milestone M0**. Die folgenden Schritte sind die Zielvorgabe für das Setup.

### Voraussetzungen

- 🐳 Docker & Docker Compose
- 🐍 Python 3.12+ (für lokale Backend-Entwicklung)
- 📦 Node.js 20+ (für lokale Frontend-Entwicklung)

### 1. Repository klonen

```bash
git clone <repo-url> culture_connects
cd culture_connects
```

### 2. Umgebung konfigurieren

```bash
cp .env.example .env
# .env mit lokalen Werten füllen (DB, Secret, KI-Provider-Key …)
```

### 3. Mit Docker starten

```bash
docker compose up --build
```

Danach erreichbar:

- 🖥️ Frontend: `http://localhost:5173`
- 🔙 API: `http://localhost:8000/api`
- 🛡️ Moderation (Django-Admin): `http://localhost:8000/admin`

### 4. Health-Check

```bash
curl http://localhost:8000/api/health
```

---

## 🔐 Datenschutz & Sicherheit

Culture Connects verarbeitet potenziell sensible Gespräche – **Privacy-by-Design** ist Pflicht, kein späteres Feature.

- 🕵️ **Pseudonyme Nutzung**, kein Klarname erforderlich
- 📊 **Datensparsamkeit** – nur erfassen, was gebraucht wird
- 🔓 **Öffentlich/privat getrennt**, interne KI-Profile nie über öffentliche APIs
- ✅ **Einwilligung** vor jeder Veröffentlichung von Debatten
- 🛡️ Auth, Autorisierung, Input-Validierung, Rate-Limiting, sicheres Secret-Handling
- 🔒 **Keine Secrets** in Code, Config, Frontend-Bundles oder Doku → nur Umgebungsvariablen
- 🧅 Ein optionaler **Onion-Service** ist langfristig vorgesehen (siehe [docs/](./docs)), aber **nicht MVP-kritisch**.

---

## 🤖 KI-Prinzipien

> Die KI ist **Werkzeug, nicht Richter.**

- ❌ Keine Wertung „Person A hat recht" / „Person B hat gewonnen"
- ✅ Fragt: *Was ist in dieser Begegnung passiert?* (Gemeinsamkeiten, Unterschiede, Missverständnisse, Lernimpulse)
- 🏷️ Klare Trennung **Beobachtung** vs. **Interpretation/Hypothese**
- 🔌 Alle KI-Aufrufe hinter einem Adapter – Provider austauschbar, mit Mocks testbar
- 💰 Kostenbewusst: strukturierter, begrenzter Kontext statt ganzer Verläufe

---

## 🧪 Tests

| Ebene | Fokus |
|-------|-------|
| 🔬 Unit | Matching-Logik, Debatten-Zustandsübergänge, Berechtigungen, Reputation, Validierung |
| 🔗 Integration | Registrierung, Matching, Debatten-Lebenszyklus, KI-Service, DB |
| 🎭 E2E | Haupt-Journey: Register → Profil → Match → Debatte → Abschluss → KI-Analyse → Feedback → Wiederbegegnung |

Kein Streben nach 100 % Coverage, bevor der Kern-Workflow validiert ist.

---

## 🗺️ Roadmap

Vollständige, abhakbare Meilensteine in 👉 [**ROADMAP.md**](./ROADMAP.md).

**MVP = M0 → M10.** Vision-Phasen (Voice, Mehrsprachigkeit, Community, Challenge, Blockchain, Onion …) folgen erst nach validiertem Kern.

---

## 🤝 Mitwirken

Culture Connects wird von einem kleinen Team entwickelt. Bauphilosophie:

```text
bauen → testen → beobachten → lernen → verbessern → erneut testen
```

- 🎯 **MVP first:** Features gegen den Kern-Loop prüfen, sonst Erweiterungspunkt statt Vollimplementierung.
- 🧩 **Modular bleiben:** neue Funktionen erweitern den Kern, destabilisieren ihn nicht.
- 📏 **Einfachheit vor Cleverness**, klare Commits (`feat:`, `fix:`, `test:` …).
- 🤖 KI-Entwicklungs-Agenten folgen [AGENT.md](./AGENT.md).

---

## 📄 Lizenz

Noch festzulegen. Bis dahin: alle Rechte vorbehalten. *(Empfehlung vor Veröffentlichung klären – z. B. AGPL-3.0 für Privacy-orientierte Plattformen oder eine proprietäre Lizenz.)*

---

> **Culture Connects darf groß gedacht werden – aber es muss klein anfangen.**
> Ein klarer kleiner Anfang ist der beste Weg, die große Idee überhaupt zu beweisen.
