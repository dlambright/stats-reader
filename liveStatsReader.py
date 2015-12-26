from urllib2 import urlopen
import datetime
import time
import re
import oldStatsReader
#import trainer
#import neural_network
import getTodaysGames
import os.path

nnParamsDictionary = {}

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
        nnParamsDictionary = {}
        print "early eh?"
    try:
        todaysGames = getTodaysGames.getTodaysGames()
        print "todaysGames Done"

        # READ THE DATA WHILE THERE IS STILL A GAME THAT ISN'T FINISHED
        for game in todaysGames:
            if game.homeTeam not in nnParamsDictionary:
                nnParamsDictionary.update({game.homeTeam : oldStatsReader.readOldStats(game.homeTeam)})

            if game.awayTeam not in nnParamsDictionary:
                nnParamsDictionary.update({game.awayTeam : oldStatsReader.readOldStats(game.awayTeam)})

            if game.gameInProgress != "STATUS_FINAL" and game.gameInProgress != "STATUS_SCHEDULED":
                print game.homeTeam
                game.homeTeamNnParams = nnParamsDictionary[game.homeTeam]
                game.awayTeamNnParams = nnParamsDictionary[game.awayTeam]
                getTodaysGames.readLiveStats(game)
    except:
        print 'yolo'
    print ""
    time.sleep(60)
    
raw_input('finished running.')








