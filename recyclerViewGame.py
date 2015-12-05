import json
class RecyclerViewGame:
    def __init__(self, homeTeamString, awayTeamString, newHomeTeamScore, newAwayTeamScore, newGameID, newTime):
        self.homeTeam = homeTeamString
        self.awayTeam = awayTeamString
        self.homeTeamScore = newHomeTeamScore
        self.awayTeamScore = newAwayTeamScore
        self.time = newTime
        self.gameId = newGameID

    def serialize(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True) 

    def to_Json(self):
        return dict(
            homeTeam = self.homeTeam,
            awayTeam = self.awayTeam,
            homeTeamScore = self.homeTeamScore,
            awayTeamScore = self.awayTeamScore,
            time = self.time,
            gameId = self.gameId,
            )
    

