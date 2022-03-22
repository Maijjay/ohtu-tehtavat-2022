from player import Player

class PlayerStats:

    def __init__(self, allPlayers):
        self.allPlayers = allPlayers
    
    def score(self, player):
        return player.score
    
    def top_scorers_by_nationality(self, country):
        players = []
        for player_dict in self.allPlayers:
            if player_dict['nationality'] == country:
                player = Player(
                    player_dict['name'], player_dict['team'], player_dict['goals'], player_dict['assists']
                )
                players.append(player)
               
        players.sort(key=self.score, reverse=True)
        return players

    