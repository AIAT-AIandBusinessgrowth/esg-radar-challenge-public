# AI Developer Challenge: „ESG-Radar"

Version 1.0 · 2026-06 · Kontakt: AI:AT Hiring Team

Schön, dass du dabei bist. Das hier ist kein Trick-Test. Es ist ein kleines, echtes Stück von dem, was wir im Venture Studio und n8n CoE täglich tun: mit KI schnell etwas Lauffähiges bauen, das Mehrwert schafft.

Es gibt keine Musterlösung, die du treffen musst. Wir schauen, wie du ein unscharf spezifiziertes Problem zerlegst, Entscheidungen triffst und KI sinnvoll einsetzt.

## Die Mission

Mit der **CSRD** (Corporate Sustainability Reporting Directive) müssen zehntausende EU-Unternehmen ihre Nachhaltigkeit nach ESRS-Standard offenlegen, und scheitern oft schon an der ersten Frage: *Wo stehen wir eigentlich gegenüber unserem Sektor?* Bau einen „ESG-Radar": eine kleine Pipeline, die Nachhaltigkeits-Offenlegungen einliest, die KPIs gegen Sektor-Benchmarks vergleicht, Lücken und Risiken scort und einen kurzen Readiness-Report mit priorisierten Maßnahmen ausgibt.

Wir liefern dir ein Seed-Dataset mit Beispiel-Unternehmen (`disclosures.json` / `disclosures.csv`), Sektor-Benchmarks (`benchmarks.json`) und ein paar Einzel-Profile. Kein Domänenwissen nötig: alle Felder sind dokumentiert ([`../data/README.md`](../data/README.md)), und alles, was du brauchst, steckt im Dataset.

> 📂 **Im Repo:** [`../data/`](../data/) mit `disclosures.json`, `disclosures.csv`, `benchmarks.json` und Beispiel-Profilen (Feld-Doku: [`../data/README.md`](../data/README.md)). Seed-Dataset, synthetisch / vereinfacht, Stand 2026-06, keine offizielle AI:AT-Position.

### Teil A: Bau den PoC
- **Input:** eine oder mehrere Disclosures (ein Unternehmen je Datensatz: Branche, Sektor, GHG-Emissionen Scope 1/2/3, Energie und Erneuerbar-Anteil, Frauenquote Führung, Mitarbeitendenzahl, Unfallrate) plus die passenden Sektor-Benchmarks.
- **Output:** ein begründeter Readiness-Report je Unternehmen: ein Score (Skala ist deine Entscheidung, begründe sie kurz), je KPI ein „über/unter Benchmark, weil…" und 2–3 priorisierte Maßnahmen für die größten Lücken.
- **Form:** ein lauffähiges Git-Repo mit echtem Python-Code und ein README, das uns das Ding in unter 5 min zum Laufen bringt.

> **Die interessante Design-Entscheidung:** Die KPIs sind nicht direkt vergleichbar. Emissionen kommen als absolute Tonnen (`ghg_scope1_t_co2e` usw.), der Benchmark steht aber als Intensität pro Mitarbeitende (`benchmark_ghg_intensitaet_t_co2e_pro_ma`). Wie du normalisierst, mit welchen KPIs du startest, wie du fehlende Werte behandelst (z. B. `ghg_scope3 = null`, unbekannter Sektor) und wie du die KPIs zu einem Score gewichtest: genau da sehen wir dein Urteil. Wir achten auf die Begründung, nicht auf eine vorgegebene Formel.

> Ein echter LLM-Call (z. B. für die Maßnahmen-Texte) ist erlaubt, aber nicht Pflicht. Ein deterministisch oder templatebasiert erzeugter Report ist völlig okay, und ohne API-Key, falls du keinen hast. Stack: Python ≥ 3.11 (Libraries frei).

### Teil B: Code-Review (~15 min)
Wir geben dir ein kurzes, KI-generiertes Python-Snippet ([`code-review/snippet.py`](./code-review/snippet.py)). Tipp: vergleiche, was der Doc-Kommentar *verspricht*, mit dem, was der Code *tut*, und achte auf die Einheiten. Es gibt einen zentralen funktionalen Bug. Finde *den*, fixe ihn und begründe in 3–5 Sätzen, warum es einer ist. Sag uns auch, was dir sonst auffällt (fehlende Edge-Cases, fragwürdige Annahmen, Validierung); diese weiterführende Kritik zählt für uns genauso wie der Fix selbst. Wir wollen sehen, ob du KI-Output beurteilen kannst, nicht nur erzeugen.

> Das Snippet liegt als Datei unter [`code-review/snippet.py`](./code-review/snippet.py) und ist unten in **Anhang A** abgedruckt.

## Spielregeln

- **Aufwand: ~4–6 fokussierte Stunden.** Du hast eine Woche; die ist für *Flexibilität*, nicht zum Durchgrinden. Bitte nicht überinvestieren: wir bewerten Denken und Urteil, nicht Politur. *(Die 4–6 h schließen Walkthrough und Decision-Log ein. Loom: 1 Take, 3–5 min; Decision-Log: 5–10 Zeilen Stichworte.)*
- **Nutze jede KI, jede Library, google frei.** Wird erwartet, nicht nur erlaubt. Cursor, Claude, Copilot, Coding-Agents: leg los.
- **Der Kern (A + B) ist die Latte.** Dazu gehören auch ein paar sinnvolle Tests (kein Coverage-Theater; zählen mit 10 %). Echte Stretch-Goals (UI, Confidence-Scores, echte PDF-Extraktion, mehr Sektoren, Deployment, ein größeres Eval-Set) sind zum Glänzen und komplett optional.

> **Wichtig:** Ein rauer Kern mit klarem Denken schlägt eine polierte, aber oberflächliche Umsetzung. Wir meinen das ernst, bitte nicht überinvestieren. Mehr Stunden bedeuten bei uns nicht mehr Punkte; wir bewerten das Kern-Ergebnis, nicht den Zeitaufwand.

AI Factory Austria steht für Chancengleichheit. Brauchst du Unterstützung oder Anpassungen im Prozess, sag uns Bescheid, wir helfen. Ob Uni, Bootcamp oder self-taught: es zählt, wie du denkst und mit KI arbeitest.

## Was du abgibst

1. **Repo-Link** (GitHub/GitLab) mit Code + README.
2. **Code-Review-Antwort** (Teil B): als Datei im Repo oder kurzes Doc.
3. **Walkthrough (1 Take, 3–5 min, max. 5):** ein Loom/Screen-Recording. Zeig dein Ergebnis und erklär, *wie* du gebaut hast, vor allem die KI-Schritte. *(Kein Video möglich oder gewünscht? Ein knappes schriftliches Walkthrough-Skript zählt als gleichwertig, sag einfach Bescheid.)*
4. **Kurzes Decision-Log + Schlüssel-Prompts:** 5–10 Zeilen Entscheidungen/Trade-offs plus die KI-Prompts, die den Unterschied gemacht haben. Zeig uns, *wie du mit KI zusammenarbeitest*; das ist genau die Fähigkeit, für die wir die Rolle besetzen.
5. **Selbst-Report:** wie viele Stunden hast du investiert? (Ehrlich, kein Maluspunkt.)

## So bewerten wir (transparent)

| Dimension | Gewicht |
|---|---|
| Funktionalität (läuft es, erfüllt es den Kern) | 20% |
| Decomposition & Urteil (Ambiguität sinnvoll gelöst, gute Trade-offs) | 20% |
| AI-Collaboration / Prozess (wie du KI gehebelt & geprüft hast) | 20% |
| Code-Qualität & Taste (lesbar, wartbar, KI-„Slop" erkannt) | 15% |
| Kommunikation / Doku (README, Decision-Log, Walkthrough) | 15% |
| Tests (sinnvolle Tests, kein Coverage-Theater) | 10% |

> Teil B (Code-Review) fließt nicht in die obige Gewichtung ein. Es ist ein separates Signal mit besonders hohem Informationsgehalt über dein Urteil zu KI-Code und kann bei knappen Entscheidungen den Ausschlag geben.

## Abgabe & Zeitplan

- **Deadline:** Die Begleit-E-Mail nennt das verbindliche Abgabedatum (Richtwert: 7 Kalendertage ab Erhalt).
- **Abgabe:** per E-Mail an aiandbusinessgrowth@ai-at.eu.
- **Rückmeldung:** Wir melden uns innerhalb von ~10 Werktagen, mit einem Termin für den Live-Teil oder einer kurzen Rückmeldung.

> Die konkreten Daten (Abgabedatum, ggf. Upload-Link) findest du in der Begleit-E-Mail zu diesem Brief.

## Danach

Kurzer **Live-Walkthrough (30–45 min)**: du zeigst dein Ergebnis, wir setzen *live eine neue Anforderung* drauf und schauen, wie du deinen eigenen Code erweiterst. Die neue Anforderung ist bewusst klein; es geht darum, wie du laut denkst, nicht um ein perfektes Ergebnis in 10 Minuten. Deine gewohnten KI-Tools darfst du dabei nutzen, genau wie beim Bauen. Danach zeigen wir dir unsere eigene Lösung und reden ehrlich darüber. Jede Person bekommt Feedback, egal wie es ausgeht.

> **Fair und transparent.** Diese Challenge ist unbezahlt; dafür zeigen wir dir nach dem Debrief unsere eigene Lösung mit echten Entscheidungen, Prompts und Trade-offs. Das ist unser „Learn"-Versprechen in Aktion. Und: strukturiertes, ehrliches Feedback für jede Person, egal wie der Prozess ausgeht. Kein Ghosting, nie.

## Datenschutz

> **Datenschutz.** Deine Unterlagen (Repo-Link, Loom-Link, Dokumente, Prompts) nutzen wir ausschließlich für die Besetzungsentscheidung, geben sie nicht an unbeteiligte Dritte weiter und löschen sie spätestens **sechs Monate** nach Abschluss des Auswahlverfahrens (oder früher auf deinen Wunsch), gemäß DSGVO. Rechtsgrundlage ist die Anbahnung eines möglichen Arbeitsverhältnisses (Art. 6 DSGVO); du kannst jederzeit Auskunft oder Löschung verlangen. Was du erstellst, bleibt deins: wir verwenden es nur zur Bewertung, nie produktiv. Dein Repo kannst du auch privat halten und uns Zugriff geben; deinen Walkthrough sehen nur wir intern. Von dir gewählte Hosting-Dienste (z. B. GitHub, Loom) unterliegen deren eigenen Datenschutzbestimmungen. Fragen: aiandbusinessgrowth@ai-at.eu.

## Anhang A: Code-Snippet (Teil B)

Das ist das Snippet für Teil B: finde den Bug, fixe ihn, kritisiere kurz. Es liegt auch als Datei im Repo: [`code-review/snippet.py`](./code-review/snippet.py).

```python
"""
benchmark_score: berechnet je Unternehmen einen Benchmark-Score (0–100).

Für jeden KPI wird geprüft, ob das Unternehmen besser oder schlechter
als der Sektor-Durchschnitt abschneidet. Jeder bestandene KPI zählt
als ein Punkt. Score = Punkte / Anzahl KPIs × 100.
"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Disclosure:
    firma: str
    ghg_scope1_t_co2e: float
    ghg_scope2_t_co2e: float
    energie_gesamt_mwh: float
    anteil_erneuerbar_prozent: float
    frauenquote_fuehrung_prozent: float
    mitarbeiterzahl: int


@dataclass
class Benchmark:
    sektor: str
    benchmark_ghg_intensitaet_t_co2e_pro_ma: float
    benchmark_anteil_erneuerbar_prozent: float
    benchmark_frauenquote_fuehrung_prozent: float


def benchmark_score(disclosure: Disclosure, benchmark: Benchmark) -> float:
    """Gibt einen Score von 0 bis 100 zurück."""
    punkte = 0
    total = 3

    # KPI 1: GHG-Emissionen (Scope 1+2), niedriger ist besser
    ghg_absolut = disclosure.ghg_scope1_t_co2e + disclosure.ghg_scope2_t_co2e
    if ghg_absolut < benchmark.benchmark_ghg_intensitaet_t_co2e_pro_ma:
        punkte += 1

    # KPI 2: Anteil erneuerbarer Energie, höher ist besser
    if disclosure.anteil_erneuerbar_prozent > benchmark.benchmark_anteil_erneuerbar_prozent:
        punkte += 1

    # KPI 3: Frauenquote Führung, höher ist besser
    if disclosure.frauenquote_fuehrung_prozent > benchmark.benchmark_frauenquote_fuehrung_prozent:
        punkte += 1

    return (punkte / total) * 100


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    unternehmen = [
        Disclosure("AlpineLogistik GmbH", 4200, 810, 18500, 12, 18, 340),
        Disclosure("GreenBuild AG",       1850, 430,  7400, 54, 29, 210),
        Disclosure("UrbanTech GmbH",        45, 180,   820, 91, 33,  62),
    ]

    benchmark = Benchmark(
        sektor="Mischsektor",
        benchmark_ghg_intensitaet_t_co2e_pro_ma=14.0,
        benchmark_anteil_erneuerbar_prozent=35,
        benchmark_frauenquote_fuehrung_prozent=28,
    )

    for u in unternehmen:
        score = benchmark_score(u, benchmark)
        print(f"{u.firma}: Benchmark-Score = {score:.0f}/100")
```
