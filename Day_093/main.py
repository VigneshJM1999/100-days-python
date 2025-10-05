import requests
import csv

url = "https://api.steampowered.com/ISteamChartsService/GetMostPlayedGames/v1/"
response = requests.get(url)
data = response.json()

games = data["response"]["ranks"]

file_name = "steam_most_played.csv"
with open(file_name, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Rank", "App ID", "Last Week Rank", "Peak In-Game Players"])

    for game in games:
        writer.writerow([
            game["rank"],
            game["appid"],
            game["last_week_rank"],
            game["peak_in_game"]
        ])

print(f"Data saved to {file_name}")
