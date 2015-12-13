import json
class StatsLine: 
    def __init__(self, s, fg, fga, fgp, thp, thpa, thpp, ft, fta, ftp, orb, drb, trb, ast, stl, blk, tsp, wp, time):
        self.score = s
        self.fieldGoals = fg
        self.fieldGoalsAttempted = fga
        self.fieldGoalPercentage = fgp
        self.threePointers = thp
        self.threePointersAttempted = thpa
        self.threePointerPercentage = thpp
        self.freeThrows = ft
        self.freeThrowsAttempted = fta
        self.freeThrowPercentage = thp
        self.offensiveRebounds = orb
        self.defensiveRebounds = drb
        self.totalRebounds = trb
        self.assists = ast
        self.steals = stl
        self.blocks = blk
        self.trueShootingPercentage = tsp
        self.winProbability = wp
        self.gameTime = time

    def serialize(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

    def to_Json(self):
        return dict(
            score = self.score,
            fieldGoals = self.fieldGoals,
            fieldGoalsAttempted = self.fieldGoalsAttempted,
            fieldGoalPercentage = self.fieldGoalPercentage,
            threePointers = self.threePointers,
            threePointersAttempted = self.threePointersAttempted,
            threePointerPercentage = self.threePointerPercentage,
            freeThrows = self.freeThrows,
            freeThrowsAttempted = self.freeThrowsAttempted,
            freeThrowPercentage = self.freeThrowPercentage,
            offensiveRebounds = self.offensiveRebounds,
            defensiveRebounds = self.defensiveRebounds,
            totalRebounds = self.totalRebounds,
            assists = self.assists,
            steals = self.steals,
            blocks = self.blocks,
            trueShootingPercentage = self.trueShootingPercentage,
            winProbability = self.winProbability,
            gameTime = self.gameTime
            )

