from urllib2 import urlopen
import time

urlBeginning = 'http://scores.espn.go.com'
baseURL = 'http://scores.espn.go.com/nba/scoreboard'
previewURL = '/nba/preview?gameId='
boxScoreURL = '/nba/boxscore?gameId='
recapURL = '/nba/recap?gameId='




# GETS THE REMAINING GAME TIME
def getTimeRemaining(gameData):
     for line in gameData:
        if line.find('In Progress') != -1:
            splitUp = line.split(' - ')
            tempLine = splitUp[1]
            splitUp = tempLine.split('<')
            return splitUp[0]
     return 'End of game'


# PULLS THE ID FROM THE GAME URL
def getIdFromLine(line, subString):
    startIndex = line.index(subString)
    if previewURL in line:
        gameId = line[startIndex+20 : startIndex+29]
    elif boxScoreURL in line:
        gameId = line[startIndex+21 : startIndex+30] 
    elif recapURL in line:
        gameId = line[startIndex+18 : startIndex+27]
    return gameId 
             
# GET GAMES THAT ARE ALREADY OVER             
def getFinishedGames():  
    toReturn = []
    try:
        html = urlopen(baseURL).read()
    except:
        time.sleep(10)
        html = urlopen(baseURL).read()
    htmlSplit = html.split('\n')
    
    for line in htmlSplit:
        while line.find(recapURL) != -1:
            firstIndex = line.index(recapURL)
            temp = line[firstIndex : firstIndex+27]
            line = line[firstIndex+27 : len(line)]
            gameId = getIdFromLine(temp, recapURL)
            game = urlBeginning + boxScoreURL + gameId
            gameHTML = urlopen(game).read()
            game = gameHTML.split('\n')
            
            if recapURL+gameId in htmlSplit or getTimeRemaining(game) == 'End of game':
                readInLine = recapURL + gameId 
                toReturn.append(readInLine)  
    return toReturn
   
# GET GAMES THAT ARE BEING PLAYED   
def getGamesInProgress():
    toReturn = []
    try:    
        html = urlopen(baseURL).read()
    except:
        time.sleep(10)
        html = urlopen(baseURL).read()
    htmlSplit = html.split('\n')
    finishedGames = getFinishedGames()
    for line in htmlSplit:
        while line.find(boxScoreURL) != -1:
            firstIndex = line.index(boxScoreURL)
            temp = line[firstIndex : firstIndex+30]
            line = line[firstIndex+30 : len(line)]
            gameId = getIdFromLine(temp, boxScoreURL)
            readInLine = urlBeginning + boxScoreURL + gameId 
            if not recapURL+gameId in finishedGames and readInLine not in toReturn:
     
                toReturn.append(readInLine)  
    return toReturn
       
# GET GAMES THAT HAVEN'T STARTED YET
def getGamesToBePlayed():
    toReturn = []
    try:
        html = urlopen(baseURL).read()
    except:
        time.sleep(10)
        html = urlopen(baseURL).read()
    htmlSplit = html.split('\n')
    for line in htmlSplit:
        while line.find(previewURL) != -1:
            firstIndex = line.index(previewURL)
            temp = line[firstIndex : firstIndex+29]
            line = line[firstIndex+29 : len(line)]
            gameId = getIdFromLine(temp, previewURL)
            readInLine = urlBeginning + previewURL + gameId 
            if readInLine not in toReturn:
                toReturn.append(readInLine)  
    return toReturn
    


#getTimeRemaining(NEEDS A URL)
#getGamesInProgress()
#getGamesToBePlayed()       
