from urllib2 import urlopen
import datetime
import time
import re
import liveStatsSupportFunctions
import oldStatsReader
import trainer
import neural_network
import getTodaysGames
import os.path

'''

def getTspFromStats(stats):
    score = int(stats[0])
    fieldGoals = int(stats[3])
    freeThrows = int(stats[9])

    return float(score/(2*(fieldGoals+ (.44 * freeThrows))))

      

# THIS METHOD DOES THE WRITING TO FILE.  EVENTUALLY, THIS METHOD WILL BE REPLACED BY 
# THE NEURAL NETWORK CALCULATIONS...
def printStatsToFile(teamFileName, stats):
    year =  datetime.datetime.now().year
    month = datetime.datetime.now().month
    day =   datetime.datetime.now().day
    
    if not os.path.isfile('gameData/' +teamFileName + '/'+str(month) + '-' + str(day) + '-' + str(year)+'.csv'):
        teamFile = open('gameData/' +teamFileName + '/'+str(month) + '-' + str(day) + '-' + str(year)+'.csv', 'w+')
        teamFile.close()
    teamFile = open('gameData/' +teamFileName + '/'+str(month) + '-' + str(day) + '-' + str(year)+'.csv', 'a')
    for index in stats:
        teamFile.write(str(index)+', ')
    
    teamFile.write(str(getTspFromStats(stats)) + ', ')
    teamFile.write(str(0) + ',                     ')

    teamFile.write('\n')

# THIS METHOD TAKES THE HTML FROM ESPN.COM/NBA/SCOREBOARD/GAME_NUMBER AND RETURNS AN ARRAY WITH THE TOTAL STATS FOR BOTH
# TEAMS.

def removeStrongTags(statsLine):
    for i in range(0, len(statsLine)):
        statsLine[i] = statsLine[i].replace("<strong>", "")
        statsLine[i] = statsLine[i].replace("</strong>", "")
    return statsLine

def readLiveStats(game):
    
    finalHomeTeamStatsLine = []
    finalAwayTeamStatsLine = []
    homeStatsLine = []
    awayStatsLine = []
    
    # Scores
    finalHomeTeamStatsLine.append(game.homeTeamScore)
    finalHomeTeamStatsLine.append(game.awayTeamScore)
    finalAwayTeamStatsLine.append(game.awayTeamScore)
    finalAwayTeamStatsLine.append(game.homeTeamScore)
    
    html = urlopen("http://espn.go.com/nba/boxscore?gameId=" + game.gameId).read()
    rawGameData = re.findall("TOTALS[\s\S]+?Fast break points", html)
    
    for i in range(0, len(rawGameData)):
        
        statsLine = []
        rawStatsLine = re.findall("<strong>.+?</strong>", rawGameData[i])
        rawStatsLine = removeStrongTags(rawStatsLine)
            

        #rawStatsPercentages = re.findall("<strong>\d+.\d%</strong>", rawGameData[i])
        #rawStatsPercentages = removeStrongTags(rawStatsPercentages)

        # Field Goals
        statsLine.append(rawStatsLine[0].split("-")[0])
        statsLine.append(rawStatsLine[0].split("-")[1])
        if int(rawStatsLine[0].split("-")[1]) != 0:    
            statsLine.append(str(float(rawStatsLine[0].split("-")[0])/float(rawStatsLine[0].split("-")[1])))
        else:
            statsLine.append(".000")

        # 3-Pointers
        statsLine.append(rawStatsLine[1].split("-")[0])
        statsLine.append(rawStatsLine[1].split("-")[1])
        if int(rawStatsLine[1].split("-")[1]) != 0:    
            statsLine.append(str(float(rawStatsLine[1].split("-")[0])/float(rawStatsLine[1].split("-")[1])))
        else:
            statsLine.append(".000")

        # Free Throws
        statsLine.append(rawStatsLine[2].split("-")[0])
        statsLine.append(rawStatsLine[2].split("-")[1])
        if int(rawStatsLine[2].split("-")[1]) != 0:    
            statsLine.append(str(float(rawStatsLine[2].split("-")[0])/float(rawStatsLine[2].split("-")[1])))
        else:
            statsLine.append(".000")

        # Rebounds
        statsLine.append(rawStatsLine[3])
        statsLine.append(rawStatsLine[4])
        statsLine.append(rawStatsLine[5])

        # Assists
        statsLine.append(rawStatsLine[6])

        # Steals
        statsLine.append(rawStatsLine[7])        

        # Blocks
        statsLine.append(rawStatsLine[8])
   
        # Turnovers
        statsLine.append(rawStatsLine[9])

        if i == 0:
            awayStatsLine = statsLine
        if i == 1:
            homeStatsLine = statsLine


    for i in range(0, len(homeStatsLine)):
        finalHomeTeamStatsLine.append(homeStatsLine[i])
        finalAwayTeamStatsLine.append(awayStatsLine[i])
    
    for i in range(0, len(awayStatsLine)):
        finalHomeTeamStatsLine.append(awayStatsLine[i])
        finalAwayTeamStatsLine.append(homeStatsLine[i])



    printStatsToFile(game.homeTeam, finalHomeTeamStatsLine)
    printStatsToFile(game.awayTeam, finalAwayTeamStatsLine)


'''
'''
 ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ 
||B |||E |||G |||I |||N |||       |||S |||C |||R |||I |||P |||T ||
||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|   
'''
'''
print 'ARE YOU READY TO RUMBLE?'
# WAIT FOR THE (ALMOST) RIGHT TIME TO START THE LOOP.
# SHOULD CUT DOWN ON PROCESSOR WORKLOAD
theTime = datetime.datetime.now()
while theTime.hour < 15:
    print 'sleeping for an hour'
    time.sleep(3600)
    theTime = datetime.datetime.now()
'''



# THIS METHOD DOES ALL OF THE HEAVY LIFING.  IT RUNS INDEFENITELY.
# AT 01:01, IT READS THE OLD STATS AT PRINTS THEM TO A FILE (WILL BE DEPRICATED UPON COMPLETION OF NEURAL 
# NETWORK).
while(True):
    theTime = datetime.datetime.now()
    if theTime.hour == 1 and theTime.minute < 2:
        oldStatsReader.readOldStats()
    
    todaysGames = getTodaysGames.getTodaysGames()

    # READ THE DATA WHILE THERE IS STILL A GAME THAT ISN'T FINISHED
    for game in todaysGames:
        if game.gameInProgress != "STATUS_FINAL" and game.gameInProgress != "STATUS_SCHEDULED":
            readLiveStats(game)
    time.sleep(60)

raw_input('finished running.')








