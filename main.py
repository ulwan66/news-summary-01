"""Write one summary of the world's news of 11 November 2026.

The summary is held as a constant and written to entry.txt in the
output directory: /output in the grading container, or the directory
named by MAKEFUN_OUTPUT_DIR on local runs. Standard library only,
no network, and every run writes the same bytes.
"""

import os
from pathlib import Path

SUMMARY = """World news, Wednesday 11 November 2026.

Russia and Ukraine agreed a major prisoner exchange at US-mediated talks in Abu Dhabi, the first in nine months, but no ceasefire. Russian strikes hit six substations in Ukraine; a market strike in Chornomorsk killed three (Reuters).

Iran's speaker Mohammad Bagher Ghalibaf told Al Jazeera the Strait of Hormuz would 'never return' to pre-war status, saying Tehran sent Washington a seven-point plan via Qatar.

Israeli strikes killed three Palestinians in Gaza City, including brothers Mahmoud and Jamil Al-Absi in a Sheikh Radwan tent; Israel said it hit militants, and deaths since the ceasefire passed 1,600, health officials said (Reuters).

At COP31, UN chief António Guterres said 'the brutal truth is that the climate crisis is outrunning us', calling it 'the path to mutually assured destruction' (Reuters).

NATO jets scrambled twice overnight as four drones were detected near Baltic airspace, triggering shelter alerts in Lithuania and Latvia, closing Vilnius and Kaunas airports; no one was hurt (Reuters).

At least 300 Italian schools were evacuated over emailed bomb alerts, presumed hoaxes; the same message reached about 6,300 schools, and similar emails in Britain and Ireland were dismissed (Reuters).

Whip Katherine Clark said 11 absent Democrats 'disappointed the American people' by missing Tuesday's 211-204 vote killing the Hegseth impeachment bid; most blamed rush-hour traffic (Reuters).

US stocks rebounded, the S&P 500 up 1.3%, Nasdaq 1.6%, as CoreWeave jumped 25% on earnings (Investopedia). OPEC put OPEC+ October output up 2.04 million barrels a day, led by Riyadh (Reuters).

CloudSEK said the Kazakhstan-linked Silent Lynx used the Hermes AI framework to steal over 2,000 national-security documents from Tajikistan, caught after leaving a server exposed (Reuters).

Kylian Mbappé will miss France's Nations League match with Italy on Thursday, coach Zinédine Zidane saying he was not fully fit (Reuters).
"""


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(SUMMARY, encoding="utf-8")


if __name__ == "__main__":
    main()
