import pandas as pd                         

url = "https://raw.githubusercontent.com/farhadGithub/tennis-atp-data/main/data/raw/atp_matches_2024.csv"


# Write your function here
def calculate_win_rate(data, player, surface):
    # Filter player wins and losses
    player_wins = data[data["winner_name"] == player]
    player_losses = data[data["loser_name"] == player]

    # Filter by surface
    surface_wins = player_wins[player_wins["surface"] == surface]
    surface_losses = player_losses[player_losses["surface"] == surface]

    # Count matches
    total_matches = len(surface_wins) + len(surface_losses)

    # Handle missing data
    if total_matches == 0:
        return None

    # Calculate win rate
    win_rate = (len(surface_wins) / total_matches) * 100
    return win_rate