import re
from urllib2 import urlopen
from recyclerViewGame import RecyclerViewGame
from statsLine import StatsLine
import json
import os
import time
import datetime


year =  datetime.datetime.now().year
month = datetime.datetime.now().month
day =   datetime.datetime.now().day


scoreboardUrl = "http://espn.go.com/nba/scoreboard/_/date/" + str(year) + str(month) + str(day)
#scoreboardUrl = "http://espn.go.com/nba/scoreboard"

nameConversionDictionary = {"Hawks":"AtlantaHawks", 
    "Celtics":"BostonCeltics",
    "Nets":"BrooklynNets",
    "Hornets":"CharlotteHornets",
    "Bulls":"ChicagoBulls",
    "Cavaliers":"ClevelandCavaliers",
    "Mavericks":"DallasMavericks",
    "Nuggets":"DenverNuggets",
    "Pistons":"DetroitPistons",
    "Warriors":"GoldenStateWarriors",
    "Rockets":"HoustonRockets",
    "Pacers":"IndianaPacers",
    "Clippers":"LosAngelesClippers",
    "Lakers":"LosAngelesLakers",
    "Grizzlies":"MemphisGrizzlies",
    "Heat":"MiamiHeat",
    "Bucks":"MilwaukeeBucks",
    "Timberwolves":"MinnesotaTimberwolves",
    "Pelicans":"NewOrleansPelicans",
    "Knicks":"NewYorkKnicks",
    "Thunder":"OklahomaCityThunder",
    "Magic":"OrlandoMagic",
    "76ers":"Philadelphia76ers",
    "Suns":"PhoenixSuns",
    "Trail Blazers":"PortlandTrailblazers",
    "Kings":"SacramentoKings",
    "Spurs":"SanAntonioSpurs",
    "Raptors":"TorontoRaptors",
    "Jazz":"UtahJazz",
    "Wizards":"WashingtonWizards"}


def removeStrongTags(statsLine):
    for i in range(0, len(statsLine)):
        statsLine[i] = statsLine[i].replace("<strong>", "")
        statsLine[i] = statsLine[i].replace("</strong>", "")
    return statsLine

def createStatsLineFromString(string):

    newStatsLine = StatsLine(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:00 -1Q" )
    rawStatsLine = re.findall("<strong>.+?</strong>", string)
    rawStatsLine = removeStrongTags(rawStatsLine)

        
    # Field Goals
    newStatsLine.fieldGoals = int(rawStatsLine[0].split("-")[0])
    newStatsLine.fieldGoalsAttempted = int(rawStatsLine[0].split("-")[1])
    if newStatsLine.fieldGoalsAttempted != 0:    
        newStatsLine.fieldGoalPercentage = float(rawStatsLine[0].split("-")[0])/float(rawStatsLine[0].split("-")[1])
    else:
        newStatsLine.fieldGoaPercentage = .000

    # 3-Pointers 
    newStatsLine.threePointers = int(rawStatsLine[1].split("-")[0])
    newStatsLine.threePointersAttempted = int(rawStatsLine[1].split("-")[1])
    if newStatsLine.threePointersAttempted != 0:    
        newStatsLine.threePointerPercentage = float(rawStatsLine[1].split("-")[0])/float(rawStatsLine[1].split("-")[1])
    else:
        newStatsLine.threePointerPercentage = .000

    # Free Throws
    newStatsLine.freeThrows = int(rawStatsLine[2].split("-")[0])
    newStatsLine.freeThrowsAttempted = int(rawStatsLine[2].split("-")[1])
    if newStatsLine.freeThrowsAttempted != 0:    
        newStatsLine.freeThrowPercentage = float(rawStatsLine[2].split("-")[0])/float(rawStatsLine[2].split("-")[1])
    else:
        newStatsLine.freeThrowPercentage = .000

    # Rebounds
    newStatsLine.offensiveRebounds = int(rawStatsLine[3])
    newStatsLine.defensiveRebounds = int(rawStatsLine[4])
    newStatsLine.totalRebounds = int(rawStatsLine[5])

    # Assists
    newStatsLine.assists = int(rawStatsLine[6])

    # Steals
    newStatsLine.steals = int(rawStatsLine[7])        

    # Blocks
    newStatsLine.blocks = int(rawStatsLine[8])

    # Score
    newStatsLine.score = int(rawStatsLine[11])

    # True shooting percentage
    try:
        newStatsLine.trueShootingPercentage = float(newStatsLine.score)/(2 *float(newStatsLine.fieldGoalsAttempted + (.44 * float(newStatsLine.freeThrowsAttempted))))
    except ZeroDivisionError:
        newStatsLine.trueShootingPercentage = .000

    # Win probability
    newStatsLine.winProbability = .000

    return newStatsLine

def writeTeamStats(filePath, gameDataHtml, gameTime):
    totalAwayTeamStats = []
    if os.path.exists(filePath):        
        awayDataFile =  open(filePath)
        totalAwayTeamStats = json.load(awayDataFile)   
        awayDataFile.close() 
    awayStatsLine = createStatsLineFromString(gameDataHtml)
    awayStatsLine.gameTime = gameTime
    totalAwayTeamStats.append(awayStatsLine)
    outString = json.dumps(totalAwayTeamStats, default= StatsLine.to_Json)
    dataFile = open(filePath, 'w')
    dataFile.write(outString)
    

def readLiveStats(game):
    try:
        html = urlopen("http://espn.go.com/nba/boxscore?gameId=" + game.gameId).read()
    except Error as e:
        print e.reason
    rawGameData = re.findall("TOTALS[\s\S]+?Fast break points", html)

    if len(rawGameData) == 2: 
        writeTeamStats('gameData/' + game.awayTeam + '/' + str(month) + '-' + str(day) + '-' + str(year) + '.nnbadat', rawGameData[0], game.gameTime)
        writeTeamStats('gameData/' + game.homeTeam + '/' + str(month) + '-' + str(day) + '-' + str(year) + '.nnbadat', rawGameData[1], game.gameTime)
    else:
        print "Box Score not available for " + game.homeTeam + " vs " + game.AwayTeam    
        


def getTodaysGames():
    
    todaysGamesArray = []


    html = urlopen(scoreboardUrl, "r+").read()
    todaysGamesRaw = re.findall("{\"uid\":.+?[0-9]{9}~c.+?Z\"}", html)
 
    for rawGame in todaysGamesRaw:
        #Get the team names.  Home team shows up first
        teamArray = re.findall("shortDisplayName\":\"[A-Za-z0-9 ]+", rawGame)
        homeTeam = nameConversionDictionary[teamArray[0].replace("shortDisplayName\":\"", "")] 
        awayTeam = nameConversionDictionary[teamArray[1].replace("shortDisplayName\":\"", "")] 

        #Get the scores.  home team first
        scoreArray = re.findall("score\":\"[0-9]+", rawGame)
        homeTeamScore = scoreArray[0].replace("score\":\"", "")
        awayTeamScore = scoreArray[1].replace("score\":\"", "")

        #Det the game Id
        gameIdArray = re.findall("\"[0-9]{9}\"", rawGame)
        gameId = gameIdArray[0].replace("\"", "")    

        #Get the game period
        periodRaw = re.findall("period\":[0-9]", rawGame)
        period = periodRaw[0].replace("period\":", "")
        
        #Get the period clock
        timeRaw = re.findall("displayClock\":\"[0-9]+:[0-9]+", rawGame)
        gameTime = timeRaw[0].replace("displayClock\":\"", "")
        gameTime = gameTime + " " + period + "Q"

        #Get game in progress
        progressRaw = re.findall("STATUS_.+?\"", rawGame)
        progress = progressRaw[0].replace("\"", "")
        
        
        todaysGamesArray.append(RecyclerViewGame(homeTeam, awayTeam, homeTeamScore, awayTeamScore, gameId, gameTime, progress))
    
   

    os.remove("gameData/todaysGames.txt")
    
    fileOut = open("gameData/todaysGames.txt", "w+")

    outString = json.dumps(todaysGamesArray, default= RecyclerViewGame.to_Json)

    fileOut.write(outString)
    fileOut.close()


    return todaysGamesArray

if __name__ == "__main__":
    #while(True):
    getTodaysGames()
    #getTodaysGamesBoxScoreIds()  
    #getTodaysGamesConversationIds() 
    #time.sleep(60)
