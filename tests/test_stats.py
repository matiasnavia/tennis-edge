import pandas as pd

from tennis_edge.stats import calculate_win_rate


def make_matches():
    # A tiny fake dataset where we know the answers by hand
    return pd.DataFrame({
        "winner_name": ["A", "A", "A", "B", "A"],
        "loser_name": ["B", "C", "D", "A", "B"],
        "surface": ["Clay", "Clay", "Clay", "Clay", "Hard"],
    })


def test_win_rate_on_clay():
    # On clay, A won 3 and lost 1, so 75%
    assert calculate_win_rate(make_matches(), "A", "Clay") == 75.0


def test_no_matches_returns_none():
    # A never played on grass
    assert calculate_win_rate(make_matches(), "A", "Grass") is None
