"""Loading match data."""

from pathlib import Path

import pandas as pd

DATA_URL = "https://raw.githubusercontent.com/farhadGithub/tennis-atp-data/main/data/raw/atp_matches_{year}.csv"
RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"


def load_matches(year):
    """Return the ATP matches for one season.

    The first time, the CSV is downloaded and saved in data/raw/.
    After that it is read from disk, so we always work with the same file.
    """
    path = RAW_DIR / f"atp_matches_{year}.csv"
    if not path.exists():
        matches = pd.read_csv(DATA_URL.format(year=year))
        matches.to_csv(path, index=False)
    return pd.read_csv(path)
