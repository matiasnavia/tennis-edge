# Tennis Edge – Progress

Legend: ✅ done · 🔄 in progress · ⬜ not started

## Milestone 0 – Project setup
- ✅ Python 3.12 and Git installed
- ✅ Project folder structure created
- ✅ Colab notebook preserved in `notebooks/00_colab_win_rates.ipynb`
- ✅ Virtual environment (`.venv`) with pandas
- ✅ Git repository and first commit
- ✅ Private GitHub repository and first push (github.com/matiasnavia/tennis-edge)

## Milestone 1 – Data loading and validation
- ⬜ Move the data loading into reusable code in `src/` (download once, cache in `data/raw/`)
- ✅ Refactor `calculate_win_rate` to take the data as an argument (exercise in `notebooks/01_win_rate_function.ipynb`)
- ⬜ Validate the 2024 dataset: duplicates, dates, walkovers/retirements, missing values
- ⬜ Confirm the dataset licence
- ⬜ Extend to several seasons (needed for chronological validation)

## Milestone 2 – First predictive baseline
- ⬜ Simple baselines (higher-ranked player wins; ranking-based probability)
- ⬜ Elo rating model, updated strictly in chronological order (no leakage)
- ⬜ Evaluation: log loss, Brier score, calibration plot

## Later milestones (not designed in detail yet)
- ⬜ Surface-adjusted Elo and logistic regression
- ⬜ Bayesian model with posterior uncertainty
- ⬜ Historical odds dataset and market comparison
- ⬜ Decision engine with a defensible NO TRADE rule
- ⬜ Out-of-sample backtest and research report

## Findings so far
Descriptive only, from the 2024 dataset (not yet validated):
- Carlos Alcaraz: 54 wins, 13 losses (80.6%); on clay 17–4 (81.0%).
- Alcaraz on clay before 2024-07-01: 12–3 (80.0%). The extra 5–1 is the Paris Olympics.
- These are win rates, **not** match-win probabilities against a specific opponent.
- Data caveat: `tourney_date` is the tournament **start** date, not the match date. All
  matches of a tournament share it, so date filters must account for this to avoid leakage.
