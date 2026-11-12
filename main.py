"""Write the world-news summary for Wednesday 11 November 2026.

Writes one UTF-8 file, entry.txt, holding the summary. Deterministic: the
text is a constant, so every run writes the same bytes. Standard library
only, no network. The output directory is /output inside the grading
container; MAKEFUN_OUTPUT_DIR overrides it for local runs, mirroring the
starter entry.
"""

import os
from pathlib import Path

SUMMARY = """World news, Wednesday 11 November 2026.

Russia and Ukraine agreed a prisoner release at US-mediated talks in Abu Dhabi, the first since February, but no ceasefire; Jared Kushner called it the biggest release yet (Reuters). Russia struck six substations in Ukraine as they closed, and an Odesa market attack killed three (Reuters).

Iran's parliament speaker Mohammad Bagher Ghalibaf told Al Jazeera the Strait of Hormuz would 'never return' to pre-war status, saying Tehran had sent Washington a seven-point plan via Qatar (Al Jazeera).

Israeli strikes killed three Palestinians in Gaza City, including two brothers in a tent in Sheikh Radwan; Israel said it hit militants, and deaths since the ceasefire passed 1,600, health officials said (Reuters).

At COP31, UN chief António Guterres said 'the brutal truth is that the climate crisis is outrunning us', calling it 'the path to mutually assured destruction' (Reuters).

NATO jets scrambled twice overnight as at least four drones entered Baltic airspace, triggering shelter alerts in Lithuania and Latvia; no one was hurt, and officials said one may have been Ukrainian, blown off course (Reuters).

At least 300 Italian schools were evacuated over identical emailed bomb alerts, presumed hoaxes (Reuters).

Whip Katherine Clark said 11 absent Democrats 'disappointed the American people' by missing Tuesday's 211-204 vote killing the Hegseth impeachment effort; most blamed rush-hour traffic (Reuters).

US stocks rebounded, the S&P 500 up 1.3%, Nasdaq 1.6%, as CoreWeave jumped 25% on earnings (Investopedia). OPEC put OPEC+ October output up 2.04 million barrels a day (Reuters).

CloudSEK said Silent Lynx, a Kazakhstan-linked group, used the Hermes AI framework to steal over 2,000 documents from Tajikistan's Defense Ministry, caught after leaving a server exposed (Reuters).

Kylian Mbappé will miss France's Nations League match against Italy on Thursday, coach Zinédine Zidane saying he was not fully fit (Reuters).
"""


def main() -> None:
    # The competition caps the summary at 2,000 characters; SUMMARY is
    # 1,981 including its trailing newline, so this write always passes.
    # newline="\n" pins line endings so the bytes are identical on any OS.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(SUMMARY, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
