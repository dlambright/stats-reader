import re
from urllib2 import urlopen
from recyclerViewGame import RecyclerViewGame
import json
import os
import time
import datetime

year =  datetime.datetime.now().year
month = datetime.datetime.now().month
day =   datetime.datetime.now().day


scoreboardUrl = "http://espn.go.com/nba/scoreboard/_/date/" + str(year) + str(month) + str(day)

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




def getTodaysGamesBoxScoreIds():
    idArray = []
    html = urlopen(scoreboardUrl, "r+").read()  #<html><p>Para 1<p>Para 2<blockquote>Quote 1<blockquote>Quote 2"

    wholeScript = re.findall("<script>window.espn.scoreboardData.+</script>", html)
    # get the game IDs
    idStringArray = re.findall("/nba/boxscore\?gameId=[0-9]+", wholeScript[0])
    for item in idStringArray:
        temp = re.search("[0-9]+", item)
        idArray.append("http://espn.go.com/nba/boxscore?gameId=" + temp.group(0))
    
    for item in idArray:
        print item

    return idArray




def getTodaysGamesConversationIds():
    idArray = []
    html = urlopen(scoreboardUrl, "r+").read()  #<html><p>Para 1<p>Para 2<blockquote>Quote 1<blockquote>Quote 2"

    wholeScript = re.findall("<script>window.espn.scoreboardData.+</script>", html)
    # get the game IDs
    idStringArray = re.findall("/nba/conversation\?gameId=[0-9]+", wholeScript[0])
    for item in idStringArray:
        temp = re.search("[0-9]+", item)
        idArray.append("http://espn.go.com/nba/conversation?gameId=" + temp.group(0))
    for item in idArray:
        print item
    return idArray

def getTodaysGames():
    
    todaysGamesArray = []

    html = urlopen(scoreboardUrl, "r+").read()
    todaysGamesRaw = re.findall("{\"uid\":.+?[0-9]{9}~c.+?Z\"}", html)

    for rawGame in todaysGamesRaw:
        #Get the team names.  Home team shows up first
        teamArray = re.findall("shortDisplayName\":\"[A-Za-z0-9 ]+", rawGame)
        homeTeam = teamArray[0].replace("shortDisplayName\":\"", "") 
        awayTeam = teamArray[1].replace("shortDisplayName\":\"", "") 
        
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
        time = timeRaw[0].replace("displayClock\":\"", "")
        time = time + " " + period + "Q"

        #print "Home : " + homeTeam + " " + homeTeamScore
        #print "Away : " + awayTeam + " " + awayTeamScore       
        #print "ID   : " + gameId
        #print "Time : " + time
        
        todaysGamesArray.append(RecyclerViewGame(homeTeam, awayTeam, homeTeamScore, awayTeamScore, gameId, time))
    

    os.remove("gameData/todaysGames.txt")
    fileOut = open("gameData/todaysGames.txt", "w+")

    outString = json.dumps(todaysGamesArray, default= RecyclerViewGame.to_Json)

    fileOut.write(outString)
    fileOut.close()

    #1:00 notes:  use the list of games in this array in the liveStatsReader.  not sure how yet...

    return todaysGamesArray









    '''
    idArray = []
    scoreArray = []
    nameArray = []
    gameArray = []
    html = urlopen(scoreboardUrl, "r+").read()
    #print str(day)    

    # pick up the script that generates the data
    wholeScript = re.findall("<script>window.espn.scoreboardData.+</script>", html)

    # get the game IDs
    idStringArray = re.findall("/nba/conversation\?gameId=[0-9]+", wholeScript[0])
    for item in idStringArray:
        temp = re.search("[0-9]+", item)
        idArray.append(temp.group(0))

    #print "scores"
    scoreStringArray = re.findall("\"score\":\"[0-9]+", wholeScript[0])
    for item in scoreStringArray:
        temp =  re.search("[0-9]+", item)
        scoreArray.append(temp.group(0))

    #print "names"
    nameStringArray = re.findall("\"shortDisplayName\":\"[0-9A-Za-z ]+\",", wholeScript[0])
    for item in nameStringArray:
        temp = re.search(":\"[0-9A-Za-z ]+", item)
        #print temp.group(0)
        newTemp = re.sub(":\"","", temp.group(0))
        if newTemp in nameConversionDictionary:
            actualName = nameConversionDictionary[newTemp]
        else:
            actualName = "FOREIGN TEAM"
        #print actualName
        nameArray.append(actualName)
    #print len(idArray)
    
    #for item in nameArray:
    #    print item
    for index in range(len(idArray)):
        #print index
        if nameArray[index*2] != "FOREIGN TEAM" and nameArray[(index*2)+1] != "FOREIGN TEAM":
            #def __init__(self, homeTeamString, awayTeamString, newHomeTeamScore, newAwayTeamScore, newGameID):
            newGame = (RecyclerViewGame(nameArray[index*2], nameArray[(index*2)+1], scoreArray[index*2], scoreArray[(index*2)+1], idArray[index]))
            gameArray.append(newGame)
        #print newGame.homeTeam

    #for game in gameArray:
        #print game.homeTeam
 
    gameDict = {"games" : gameArray}

    os.remove("gameData/todaysGames.txt")
    fileOut = open("gameData/todaysGames.txt", "w+")

    outString = json.dumps(gameArray, default= RecyclerViewGame.to_Json)

    fileOut.write(outString)
    fileOut.close()

    '''



















if __name__ == "__main__":
    #while(True):
    getTodaysGames()
    #getTodaysGamesBoxScoreIds()  
    #getTodaysGamesConversationIds() 
#    time.sleep(60)






