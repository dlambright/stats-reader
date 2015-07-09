import thread
import time
import os

timeToWait = 10
#Define a function for the thread
def print_game(fileName, delay):
    print "emulating " +fileName
    count = 0
    try:
        os.remove(fileName + "yoloswag.csv")
    except:
        print "no file " + fileName + "-today.csv"
    
    with open(fileName+".csv") as f:
        for line in f:
            line.replace(" ", "")
            fileOut = open(fileName + "-today.csv", 'a')
            fileOut.write(line)
            fileOut.close()
            time.sleep(delay)
            #print "read line " + str(count)
            count += 1


todaysGames = ["AtlantaHawks", "DallasMavericks", "BostonCeltics",  "NewYorkKnicks", "ChicagoBulls", "CharlotteHornets", "DenverNuggets", "PhoenixSuns", "HoustonRockets", "LosAngelesClippers", "MilwaukeeBucks", "Philadelphia76ers", "MinnesotaTimberwolves", "WashingtonWizards", "NewOrleansPelicans", "BrooklynNets", "OrlandoMagic", "MiamiHeat", "PortlandTrailBlazers", "SanAntonioSpurs", "SacramentoKings", "MemphisGrizzlies", "UtahJazz", "LosAngelesLakers"]
# Create two threads as follows
try:
    for team in todaysGames:
        print team
        thread.start_new_thread(print_game, ("gameData/" + team + "/2-25-2015", timeToWait ))
        #thread.start_new_thread(print_game, ("gameData/DallasMavericks/2-25-2015", timeToWait))
except:
    print "Error: unable to start thread"
index = 0
while index < 200:
    index += 1
    #print "+++ iteration +++ " + str(index)
    time.sleep(timeToWait)


print 'send it'
