from playerReader import PlayerReader
from playerStats import PlayerStats

def main():

    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    allPlayers = reader.get_players()
    stats = PlayerStats(allPlayers)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)
        

if __name__ == "__main__":
    main()
