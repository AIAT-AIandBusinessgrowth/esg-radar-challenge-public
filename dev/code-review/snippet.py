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

    # KPI 1: GHG-Emissionen (Scope 1+2) — niedriger ist besser
    ghg_absolut = disclosure.ghg_scope1_t_co2e + disclosure.ghg_scope2_t_co2e
    if ghg_absolut < benchmark.benchmark_ghg_intensitaet_t_co2e_pro_ma:
        punkte += 1

    # KPI 2: Anteil erneuerbarer Energie — höher ist besser
    if disclosure.anteil_erneuerbar_prozent > benchmark.benchmark_anteil_erneuerbar_prozent:
        punkte += 1

    # KPI 3: Frauenquote Führung — höher ist besser
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
