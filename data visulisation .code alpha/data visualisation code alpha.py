import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\work\python programs\ipl_player_performance_2015_2025.csv")
print(df)

# 1. Top Run Scorers
top_runs = df.groupby("Player")["Runs"].sum().nlargest(10)
top_runs.plot(kind="barh", color="skyblue", title="Top 10 Run Scorers")
plt.xlabel("Runs")
plt.tight_layout()
plt.show()

# 2. Top Wicket Takers
top_wickets = df.groupby("Player")["Wickets"].sum().nlargest(10)
top_wickets.plot(kind="barh", color="salmon", title="Top 10 Wicket Takers")
plt.xlabel("Wickets")
plt.tight_layout()
plt.show()

# 3. Strike Rate Analysis (Scatter Plot by Team)
plt.figure(figsize=(10,6))
filtered_df = df[df["Balls_Faced"] > 20]
sns.stripplot(data=filtered_df, x="Team", y="Strike_Rate", jitter=True, alpha=0.7)
plt.title("Strike Rate of Players by Team (Scatter)")
plt.xlabel("Team")
plt.ylabel("Strike Rate")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Player Performance by Season (Top 3 Players)
season_data = df.groupby(["Year", "Player"])["Runs"].sum().reset_index()
top_players = season_data.groupby("Player")["Runs"].sum().nlargest(3).index
for player in top_players:
    player_data = season_data[season_data["Player"] == player]
    plt.plot(player_data["Year"], player_data["Runs"], marker="o", label=player)
plt.title("Top 3 Players' Runs Over Seasons")
plt.xlabel("Year")
plt.ylabel("Runs")
plt.legend()
plt.tight_layout()
plt.show()

# 5. Most Sixes and Fours (Stacked Bar)
df["Total_Boundaries"] = df["Fours"] + df["Sixes"]
top_boundaries = df.groupby("Player")[["Fours", "Sixes"]].sum().nlargest(10, "Fours")
top_boundaries.plot(kind="bar", stacked=True, figsize=(10,6), title="Top 10 Boundary Hitters")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# 6. Player Role Distribution (Pie Chart)
batsmen = len(df[df["Runs"] >= 400])
bowlers = len(df[df["Wickets"] >= 15])
allrounders = len(df[(df["Runs"] >= 200) & (df["Wickets"] >= 8)])
plt.pie([batsmen, bowlers, allrounders], labels=["Batsmen", "Bowlers", "All-Rounders"],
        autopct="%1.1f%%", colors=["lightgreen", "lightcoral", "lightskyblue"])
plt.title("Player Role Distribution")
plt.tight_layout()
plt.show()
