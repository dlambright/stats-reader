from urllib2 import urlopen
import datetime
import time
import re
import liveStatsSupportFunctions
import oldStatsReader
import trainer
import neural_network
import getTodaysGames



def getTspFromStats(stats):
    score = stats[0]
    print "score: " + str(score)
    fieldGoals = stats[4]
    print "field goals: " + str(fieldGoals)
    freeThrows = stats[10]
    print "free throws: " + str(freeThrows)

    return 10






def getNamesFromHTML(htmlString):
    toReturn = []
    titleString = re.search("<title>.+</title>", htmlString)
    titleLine = titleString.group(0)
    
    homeTeamString = re.search(">[A-Za-z0-9 ]+ vs.", titleLine)
    homeTeamString = homeTeamString.group(0)[:3][1:]
    if "Blazers" in homeTeamString:
        homeTeamString = homeTeamString.replace("B", "b")
    homeTeamString = homeTeamString.replace(" ", "")
    
    awayTeamString = re.search("vs.[A-Za-z0-9 ]+-", titleLine)
    awayTeamString = awayTeamString.group(0)[:2][3:]
    if "Blazers" in awayTeamString:
        awayTeamString = awayTeamString.replace("B", "b")
    awayTeamString = awayTeamsString.replace(" ", "")
    
    toReturn.append(homeTeamString)
    toReturn.append(awayTeamString)

    return toReturn

    '''
    for line in htmlString:
        if 'title>' in line:
            toReturn = []
            arrayForFirstName = line.split(' vs. ')
            firstTeamTemp =  arrayForFirstName[0]
            #print firstTeamTemp
            firstTeamSpace = firstTeamTemp[8 : len(firstTeamTemp)]
            firstTeam = firstTeamSpace.replace(' ', '')
            #print firstTeam
            toReturn.append(firstTeam)
            
            #print "second"
            stringForSecondTeam = arrayForFirstName[1]
            secondTeamTemp = stringForSecondTeam.split(' -')
            secondTeamSpace = secondTeamTemp[0]
            secondTeam = secondTeamSpace.replace(' ', '')
            #print secondTeam
            toReturn.append(secondTeam)
            
            return toReturn
    '''
       
# GET THE LIVE DATA FROM THE TABLE
def pruneFromTags(line):
    toReturn = []
    for x in range(0, len(line)-5):
        offset = 1
        readInValues = []
        while line[x] == '>' and line[x+offset] != '<' and len(toReturn) < 18 and line[x+offset] != '&' and x+offset < len(line):
            readInValues.append(line[x+offset])
            offset += 1
        if '-' in readInValues:
            stringValue = ''.join(readInValues)
            splitValues = stringValue.split('-')
            toReturn.append(int(splitValues[0]))
            toReturn.append(int(splitValues[1]))
            if int(splitValues[1]) == 0:
                toReturn.append(0)
            else:
                toReturn.append(float(float(splitValues[0])/float(splitValues[1])))
            
        elif len(readInValues) > 0:
            toReturn.append(int(''.join(readInValues)))
  
    return toReturn

# THIS METHOD PUTS THE SCORES AT THE BEGINNING FOR BOTH TEAMS, IN THE CORRECT ORDER
def addScoresToCorrectPlaces(stats):
    score1 = [stats[0][17]]
    del stats[0][-1]
    statsLine1 = stats[0]
    
    score2 = [stats[1][17]]
    del stats[1][-1]
    statsLine2 = stats[1]
    finalStatsLine1 = score1 + score2 + statsLine1 + statsLine2
    finalStatsLine2 = score2 + score1 + statsLine2 + statsLine1
    stats[0] = finalStatsLine1
    stats[1] = finalStatsLine2
    
    return stats

# THIS METHOD DOES THE WRITING TO FILE.  EVENTUALLY, THIS METHOD WILL BE REPLACED BY 
# THE NEURAL NETWORK CALCULATIONS...
def printStatsToFile(teamFileName, stats):
    year =  datetime.datetime.now().year
    month = datetime.datetime.now().month
    day =   datetime.datetime.now().day
    
    teamFile = open('gameData/' +teamFileName + '/'+str(month) + '-' + str(day) + '-' + str(year)+'.csv', 'a')
    for index in stats:
        teamFile.write(str(index)+', ')
    
    teamFile.write(str(0) + ', ')
    teamFile.write(str(0) + ', ')

    teamFile.write('\n')

# THIS METHOD TAKES THE HTML FROM ESPN.COM/NBA/SCOREBOARD/GAME_NUMBER AND RETURNS AN ARRAY WITH THE TOTAL STATS FOR BOTH
# TEAMS.
def readLiveStats(html):
    html = html.splitlines()
    rightSpot = False
    stats = []
    for line in html:
        if rightSpot is True and '/tr' in line:
            stats.append(pruneFromTags(line))     
            rightSpot = False 
        if 'TOTALS' in line:
            rightSpot = True
    teams = getNamesFromHTML(html)
    print "Dusty"
    stats = addScoresToCorrectPlaces(stats)
    #stats = predict.predictWinProbability(stats)
    
    printStatsToFile(teams[0], stats[0])
    printStatsToFile(teams[1], stats[1])
    print teams[0] + ' ' + str(stats[0][0]) + ' - ' + teams[1] + ' ' +str(stats[1][0]) + '     ' +liveStatsSupportFunctions.getTimeRemaining(html)
    #print 'win prob: ' + teams[0] + ' ' + str(stats[0][36])# + ' ' + teams[1] + ' ' + str(stats[1][36] + '\n\n')





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
    
    scoreboardHTML = urlopen('http://scores.espn.go.com/nba/scoreboard').read()
    splitScoreboardHTML = scoreboardHTML.split('\n')

    todaysGames = getTodaysGames.getTodaysGamesBoxScoreIds() #liveStatsSupportFunctions.getGamesInProgress(splitScoreboardHTML)
    conversationGames = getTodaysGames.getTodaysGamesConversationIds() #liveStatsSupportFunctions.getGamesToBePlayed(splitScoreboardHTML)
    print str(len(todaysGames) + len(conversationGames)) + ' games to play today'


# READ THE DATA WHILE THERE IS STILL A GAME THAT ISN'T FINISHED
    badReads = 0
#while len(previewGames) > 0 or len(todaysGames) > 0: 


    for url in todaysGames:
        
        try:        
            html = urlopen(url).read()
            if 'TOTALS' in html:
                readLiveStats(html)
        except:
            badReads += 1
            print 'Unable to find ' + url
            
    try:
        #scoreboardHTML = urlopen('http://scores.espn.go.com/nba/scoreboard').read()
        #splitScoreboardHTML = scoreboardHTML.split('\n')
        
        todaysGames = getTodaysGames.getTodaysGamesBoxScoreIds() #liveStatsSupportFunctions.getGamesInProgress(splitScoreboardHTML)
        conversationGames = getTodaysGames.getTodaysGamesConversationIds() #liveStatsSupportFunctions.getGamesToBePlayed(splitScoreboardHTML)
        #todaysGames = liveStatsSupportFunctions.getGamesInProgress(splitScoreboardHTML)
        #conversationGames = liveStatsSupportFunctions.getGamesToBePlayed(splitScoreboardHTML)
    except:
        print 'unable to access scoreboard home'
            
            

    print str(datetime.datetime.now()) + '--------' + str(badReads) + ' bad reads.'
    time.sleep(60)




raw_input('finished running. ' + str(badReads) + ' bad reads.')








