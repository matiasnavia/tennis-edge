# Tennis Edge

An independent quantitative research project using professional tennis data to study
probabilistic prediction, market efficiency, uncertainty and decision-making.

**Research question:** Can a probabilistic model identify situations where tennis betting
market probabilities are mispriced, while learning when *not* to trade because its own
predictions are too uncertain?

This is an educational research project. No real-money betting is involved.

## Planned components

1. **Prediction engine** – estimates the probability that player A beats player B.
2. **Uncertainty engine** – quantifies how uncertain that probability is.
3. **Decision engine** – compares model probabilities with market prices and returns
   `POSITIVE EDGE`, `NEGATIVE EDGE` or `NO TRADE`.

None of these are built yet. See [PROGRESS.md](PROGRESS.md) for the current status.

## Project layout

```
Tennis Edge/
├── data/
│   ├── raw/          # downloaded source data, never edited by hand (not committed)
│   └── processed/    # cleaned data produced by our code (not committed)
├── notebooks/        # exploratory analysis
├── src/              # reusable Python code
├── tests/            # automated checks for the code in src/
├── reports/          # write-ups and figures
├── requirements.txt  # Python packages the project needs
├── PROGRESS.md       # what is done and what comes next
└── README.md
```

## Setup

From the project folder, in PowerShell:

```powershell
py -3.12 -m venv .venv                 # create the virtual environment (once)
.venv\Scripts\Activate.ps1             # activate it (every new terminal)
pip install -r requirements.txt        # install packages
```

## Data and licences

| Dataset | Source | Licence | Status |
|---|---|---|---|
| ATP matches 2024 | [farhadGithub/tennis-atp-data](https://github.com/farhadGithub/tennis-atp-data), apparently derived from Jeff Sackmann's [tennis_atp](https://github.com/JeffSackmann/tennis_atp) | Sackmann's data is CC BY-NC-SA 4.0 (non-commercial, attribution, share-alike) — **to verify for this mirror** | In use, not yet validated |

Raw data files are kept out of Git and downloaded by code, so the repository does not
redistribute anyone else's data.
