# Seed-Dataset: Felder & Hinweise

> ⚠️ **Das Dataset ist synthetisch und vereinfacht (Stand 2026-06) und keine offizielle AI:AT-Position.** Die Firmennamen sind frei erfunden; die KPI-Werte (Emissionen, Energieverbrauch, Quoten) sind gerundet und vereinfacht, angelehnt an EU-Branchendurchschnitte. Kein Domänenwissen nötig: die Felder unten verstehst du ohne Vorwissen.

## Inhalt

| Datei | Inhalt |
|---|---|
| `disclosures.json` | 5 Beispiel-Unternehmen mit ESG-KPIs (über 5 Sektoren) |
| `disclosures.csv` | Dieselben Daten als CSV, bequem in Excel/Sheets zu öffnen |
| `benchmarks.json` | Sektor-Durchschnitte (5 Sektoren, je 4 Benchmark-KPIs) |
| `examples/` | 3 zusätzliche Einzel-Profile (`company_1.json`–`company_3.json`) als Ausgangspunkt |

`disclosures.json` und `disclosures.csv` enthalten dieselben Daten. Die CSV öffnest du bequem in Excel/Sheets; die JSON ist praktisch zum Einlesen im Code. Jeder JSON-Eintrag trägt zusätzlich ein `_hinweis`-Feld mit dem Synthetik-Vermerk. *(Die `disclosures.csv` beginnt direkt mit der Header-Zeile; der Disclaimer steht hier im README, damit Excel/Sheets die CSV sauber einlesen.)*

> **Zwei Hinweise zum Dataset:**
> - **Sektor-Abdeckung ist nur illustrativ.** Nicht jedes Unternehmen hat alle Felder befüllt (z. B. `ghg_scope3_t_co2e = null`, wenn nicht erhoben; `csrd_pflichtig_ab = null`, wenn unbekannt). Das ist beabsichtigt und ein realistischer Praxisfall fürs Matching, keine Marktaussage.
> - **Du musst nicht jedes Feld nutzen.** Wähle, was für deine Pipeline bzw. Analyse sinnvoll ist (ob z. B. `unfaelle_pro_1000_ma` einfließt, entscheidest du und begründest es kurz).

## Schema-Tabelle (`disclosures.json` / `disclosures.csv`)

| Feld | Typ | Bedeutung |
|---|---|---|
| `_hinweis` | string | Synthetik-Disclaimer (nur JSON; Pflichtfeld) |
| `firma` | string | Unternehmensname (frei erfunden) |
| `branche` | string | Branche |
| `land` | string | ISO-Länderkürzel |
| `sektor_esrs` | string | ESRS-Primärstandard (z. B. E1/E2/S1/G1) |
| `berichtsjahr` | number | Berichtsjahr |
| `ghg_scope1_t_co2e` | number | Direkte Emissionen Scope 1 in t CO₂e |
| `ghg_scope2_t_co2e` | number | Emissionen aus Energieeinkauf Scope 2 in t CO₂e |
| `ghg_scope3_t_co2e` | number\|null | Vor-/nachgelagerte Emissionen Scope 3; `null` wenn nicht erhoben |
| `energie_gesamt_mwh` | number | Gesamtenergie in MWh |
| `anteil_erneuerbar_prozent` | number | Erneuerbar-Anteil 0–100 |
| `frauenquote_fuehrung_prozent` | number | Frauenanteil Führung 0–100 |
| `mitarbeiterzahl` | number | Mitarbeitende (VZÄ) |
| `unfaelle_pro_1000_ma` | number | Arbeitsunfälle je 1.000 MA |
| `csrd_pflichtig_ab` | number\|null | Pflichtjahr CSRD; `null` = unbekannt |
| `nachhaltigkeitsbericht_vorhanden` | boolean | Bericht vorhanden? |
| `kommentar` | string | Freitext-Kontext (nur JSON) |

## Schema-Tabelle (`benchmarks.json`)

| Feld | Typ | Bedeutung |
|---|---|---|
| `_hinweis` | string | Synthetik-Disclaimer |
| `sektor` | string | Sektor-Bezeichnung |
| `sektor_esrs` | string | ESRS-Standard |
| `benchmark_ghg_intensitaet_t_co2e_pro_ma` | number | GHG-Intensität (Scope 1+2 / MA): Sektor-Durchschnitt |
| `benchmark_anteil_erneuerbar_prozent` | number | Sektor-Durchschnitt Erneuerbar |
| `benchmark_frauenquote_fuehrung_prozent` | number | Sektor-Durchschnitt Frauenquote |
| `benchmark_unfaelle_pro_1000_ma` | number | Sektor-Durchschnitt Unfallrate |
| `quelle` | string | Datenhinweis |

## `examples/company_*.json` (zusätzliche Einzel-Profile)

Drei weitere Einzel-Unternehmen im selben Schema wie `disclosures.json`, ein guter Ausgangspunkt, um deine Pipeline an einem einzelnen Datensatz auszuprobieren.
