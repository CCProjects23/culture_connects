# Culture Connects Network
## Onion-Service – Konzept und technische Einordnung

**Stand:** September 2026  
**Dokumenttyp:** Architektur- und Strategie-Notiz

---

# 1. Grundidee

Culture Connects soll langfristig eine Plattform für echte menschliche Begegnungen, strukturierte Debatten und gegenseitiges Verständnis werden.

Ein zusätzlicher Zugang über das Tor-Netzwerk kann zu dieser Zielsetzung passen, weil Privatsphäre und pseudonyme Nutzung bereits Bestandteil des Gesamtkonzepts sind.

Der Onion-Service sollte dabei nicht als eigenes Produkt verstanden werden.

> **Er ist eine zusätzliche, privacy-orientierte Zugangsebene zur bestehenden Culture-Connects-Plattform.**

---

# 2. Warum ein Onion-Service interessant sein kann

Culture Connects soll ausdrücklich pseudonyme Nutzung ermöglichen und Privatsphäre als wichtigen Bestandteil der Plattform behandeln.

Ein Onion-Service könnte diese Philosophie technisch ergänzen.

Mögliche Vorteile:

- zusätzlicher Schutz der Netzwerkidentität
- Zugang ohne klassischen Clearnet-Zugriff
- zusätzliche Option für privacy-orientierte Nutzer
- glaubwürdige Ergänzung einer Privacy-by-Design-Strategie
- möglicher Zugang für Nutzer, die ihre reguläre Netzwerkidentität nicht mit der Plattform verbinden möchten

Der Onion-Service sollte dabei nicht als Marketing-Gimmick verstanden werden.

Der technische Ansatz sollte tatsächlich mit der übrigen Datenschutzarchitektur übereinstimmen.

---

# 3. Wichtig: Tor bedeutet nicht automatisch vollständige Anonymität

Ein Onion-Service allein macht eine Anwendung nicht automatisch anonym.

Wenn die Anwendung beispielsweise unnötig speichert:

- IP-Adressen
- Tracking-Daten
- identifizierende Browserinformationen
- unnötige Verbindungsdaten
- andere personenbezogene Metadaten

kann die Gesamtarchitektur weiterhin Rückschlüsse auf Nutzer ermöglichen.

Deshalb muss ein Onion-Service Bestandteil eines umfassenderen Privacy-by-Design-Konzepts sein.

Grundprinzip:

> **Nicht nur den Transportweg schützen, sondern die gesamte Datenverarbeitung datensparsam gestalten.**

---

# 4. Mögliche Architektur

Der Onion-Zugang sollte auf dieselbe Anwendung wie der normale Zugang führen.

Vereinfacht:

```text
                  Culture Connects
                         │
              ┌──────────┴──────────┐
              │                     │
           Clearnet                 Tor
              │                     │
       HTTPS / normale          Onion Service
          Verbindung                │
              │                     │
              └──────────┬──────────┘
                         ↓
                  Application Layer
                         ↓
               Culture Connects Core
```

Dadurch müssen nicht zwei vollständig getrennte Plattformen betrieben werden.

Der Onion-Service ist lediglich ein zusätzlicher Zugang zum bestehenden System.

---

# 5. Abgrenzung zum MVP

Der Onion-Service ist **nicht MVP-kritisch**.

Der erste MVP sollte zunächst den zentralen Produkt-Loop beweisen:

```text
User
 ↓
Profil
 ↓
Matching
 ↓
Textdebatte
 ↓
KI-Analyse
 ↓
Reflexion
 ↓
erneute Begegnung
```

Der Tor-Zugang kann danach ergänzt werden.

Alternativ kann er technisch relativ früh bereitgestellt werden, wenn der zusätzliche Infrastrukturaufwand gering bleibt.

Entscheidend ist:

> **Der MVP darf nicht von der Fertigstellung des Onion-Services abhängig werden.**

---

# 6. Warum ein früher technischer Aufbau trotzdem sinnvoll sein kann

Im Gegensatz zu komplexen späteren Features benötigt ein Onion-Service keine eigene Produktlogik.

Wenn die bestehende Webanwendung sauber aufgebaut ist, kann der zusätzliche Zugang prinzipiell vor der eigentlichen Anwendungsschicht liegen.

Beispielsweise:

```text
Clearnet
   ↓
HTTPS
   ↓
Application

Tor
   ↓
Onion Service
   ↓
Application
```

Damit kann die Funktionalität der Plattform unabhängig vom Zugang weiterentwickelt werden.

---

# 7. Privacy-by-Design

Für Culture Connects sollte bereits früh festgelegt werden, welche Daten überhaupt benötigt werden.

Besondere Aufmerksamkeit verdienen:

- öffentliche Profildaten
- private Profildaten
- interne KI-Profile
- Debatteninhalte
- KI-Analysen
- Nutzerbewertungen
- Moderationsdaten
- technische Logs
- Veröffentlichungszustimmungen

Die Tatsache, dass ein Nutzer über Tor zugreift, sollte nicht dazu führen, dass intern plötzlich unnötige zusätzliche Daten gespeichert werden.

---

# 8. Pseudonymität und Identität

Das Culture-Connects-Konzept sieht pseudonyme Nutzung vor.

Ein Onion-Service passt dazu.

Gleichzeitig kann es später Funktionen geben, bei denen eine stärkere Identitätsprüfung sinnvoll oder notwendig sein könnte.

Beispielsweise:

- bestimmte Video-Funktionen
- besondere Community-Funktionen
- bestimmte Organisationsfunktionen

Deshalb sollte die Identitätsarchitektur zwischen:

```text
Pseudonyme Nutzung
        ↓
optionale zusätzliche Verifikation
```

unterscheiden können.

Eine solche Verifikation darf nicht automatisch zur Voraussetzung für die gesamte Plattform werden.

---

# 9. Textkommunikation

Für den MVP ist Textkommunikation die einfachste Form der Debatte.

Ein Onion-Service kann dabei relativ sauber als zusätzlicher Zugang eingesetzt werden.

Das ergibt zunächst:

```text
Tor Browser
    ↓
Culture Connects Onion Service
    ↓
Web Application
    ↓
Debate Engine
```

Die eigentliche Debattenlogik bleibt unverändert.

---

# 10. Voice und Video

Mit späteren Kommunikationsformen wird die Architektur anspruchsvoller.

Geplante Erweiterungen:

- Voice
- Speech-to-Text
- Video

Insbesondere Echtzeitkommunikation kann zusätzliche Netzwerkkomponenten erfordern.

Deshalb sollte Voice/Video nicht einfach als direkte Erweiterung der Textarchitektur betrachtet werden.

Für spätere Phasen müssen insbesondere untersucht werden:

- Medienrouting
- WebRTC
- STUN/TURN
- Medienserver
- Metadaten
- mögliche Netzwerk-Leaks
- Datenschutz der Teilnehmer

Der Onion-Service sollte deshalb für Text nicht unnötig von der späteren Videoarchitektur abhängig gemacht werden.

---

# 11. Onion-Service und Vertrauen

Ein offizieller Onion-Service kann bei Culture Connects mehr sein als technische Infrastruktur.

Er kann zeigen, dass Aussagen wie:

> „Privatsphäre ist uns wichtig.“

auch technisch umgesetzt werden.

Das ist besonders relevant, weil Culture Connects Gespräche zu potenziell sensiblen Themen ermöglichen soll.

Mögliche Themenbereiche sind unter anderem:

- Politik
- Religion
- Gesellschaft
- persönliche Fragen
- Philosophie
- internationale Themen

Je persönlicher oder kontroverser eine Diskussion wird, desto relevanter kann ein privacy-orientierter Zugang für bestimmte Nutzer sein.

---

# 12. Technische Leitlinie

Der Onion-Service sollte möglichst wenig zusätzliche Komplexität in den Anwendungskern bringen.

Ziel:

```text
                     ┌── Clearnet
                     │
Application Core ────┤
                     │
                     └── Tor Onion
```

Nicht:

```text
Clearnet Application
        +
separate Tor Application
        +
separate database
        +
separate business logic
```

Sofern Sicherheits- oder Betriebsanforderungen nichts anderes notwendig machen, sollte der Anwendungskern gemeinsam genutzt werden.

---

# 13. Verhältnis zu Blockchain

Tor und Blockchain erfüllen im Projekt völlig unterschiedliche Rollen.

### Tor

Privacy-orientierter Zugang und Schutz der Netzwerkidentität.

### Blockchain

Mögliche spätere Infrastruktur für:

- Reputation
- Rewards
- Attestierungen
- Community-Leistungen

Daher sollten beide Themen architektonisch getrennt behandelt werden.

---

# 14. Roadmap-Einordnung

Empfohlene Einordnung:

### Phase MVP

- Clearnet-Zugang
- Privacy-Grundlagen
- Pseudonymität
- saubere Datenarchitektur

### Frühe Erweiterung

- Onion-Service
- Privacy-Audit
- technische Überprüfung der Metadaten
- Dokumentation der Datenschutzarchitektur

### Später

- Voice über privacy-orientierte Architektur
- Video
- weitergehende Identitätsmodelle
- internationale Infrastruktur

---

# 15. Technische Prüfungen vor produktivem Einsatz

Vor einer öffentlichen Bereitstellung sollten mindestens folgende Punkte geprüft werden:

- Welche Netzwerkdaten werden gespeichert?
- Welche Logs entstehen?
- Welche Logs sind wirklich notwendig?
- Gibt es externe Dienste, die Nutzerinformationen erhalten?
- Werden Drittanbieter-Skripte verwendet?
- Werden Analyse-/Tracking-Systeme eingesetzt?
- Welche Browserdaten werden verarbeitet?
- Welche Daten werden an KI-Anbieter übertragen?
- Wie lange werden Debatten gespeichert?
- Wie lange werden KI-Analysen gespeichert?
- Wie funktioniert Löschung?
- Welche Daten sind öffentlich?
- Welche Daten bleiben intern?

Ein Onion-Service sollte erst dann als echte Privacy-Funktion betrachtet werden, wenn diese Fragen zur Gesamtarchitektur beantwortet sind.

---

# 16. Produktphilosophie

Der Onion-Service passt besonders gut zu Culture Connects, wenn folgende Prinzipien erhalten bleiben:

> **Pseudonymität statt unnötiger Identifizierung.**

> **Privatsphäre statt unnötiger Datensammlung.**

> **Begegnung statt Überwachung.**

> **KI als Werkzeug statt KI als Richter.**

---

# 17. Fazit

Ein Onion-Service ist für Culture Connects grundsätzlich sinnvoll.

Er sollte jedoch:

- kein eigenes Produkt sein
- kein MVP-Blocker sein
- keine künstliche technische Komplexität erzeugen
- nicht mit vollständiger Anonymität gleichgesetzt werden

Stattdessen sollte er als **zusätzlicher privacy-orientierter Zugang** zur bestehenden Plattform betrachtet werden.

Die sinnvollste technische Strategie lautet:

> **Ein gemeinsamer Application Core – mehrere Zugangsebenen.**

Damit kann Culture Connects zunächst schnell als normales Webprodukt entwickelt werden und später einen offiziellen Onion-Zugang anbieten, ohne die gesamte Anwendung neu entwickeln zu müssen.

---

# 18. Leitgedanke

> **Privacy by Design beginnt nicht beim Onion-Service.**
>
> **Der Onion-Service ist ein Baustein einer insgesamt datensparsamen Architektur.**

Und für Culture Connects:

> **Menschen sollen selbst entscheiden können, wie viel sie von sich preisgeben, während die Plattform ihnen trotzdem echte Begegnungen ermöglicht.**
