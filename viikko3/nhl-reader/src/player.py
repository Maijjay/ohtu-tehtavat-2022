class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.score = goals + assists

    def __str__(self):
        return f"{self.name:20} team: {self.team} score: {self.goals} + {self.assists} = {self.score}"
