import json
class RecyclerViewGame:
    def __init__(self, homeTeamString, awayTeamString, newHomeTeamScore, newAwayTeamScore, newGameID):
        self.homeTeam = homeTeamString
        self.awayTeam = awayTeamString
        self.homeTeamScore = newHomeTeamScore
        self.awayTeamScore = newAwayTeamScore
        self.time = "12:00 Q1"
        self.gameId = newGameID

    def serialize(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)




