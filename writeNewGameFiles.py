import thread
import time
import os

timeToWait = 1
#Define a function for the thread
def print_game(fileName, delay, predictions):
    count = 0
    try:
        os.remove(fileName + "-today.csv")
    except:
        print "no file " + fileName + "-today.csv"
    
    with open(fileName+".csv") as f:
        print "reading " + fileName        
        for line in f:
            line.replace(" ", "")
            separatedLine = line.split(",")

            score = float(separatedLine[0])
            fieldGoalsAttempted = float(separatedLine[3])
            foulShotsAttempted = float(separatedLine[9])

            denominator = (2*(fieldGoalsAttempted + (.44*foulShotsAttempted)))
            
            TSP = 0
            if denominator != 0: 
                TSP = score / (2*(fieldGoalsAttempted + (.44*foulShotsAttempted))) 
            separatedLine.pop()
            separatedLine.append(str(TSP))
            separatedLine.append(predictions[count])
            fileOut = open(fileName + "-today.csv", 'a')
            
            

            for item in separatedLine:
                fileOut.write(item + ", ")
            fileOut.write('\n')
            fileOut.close()
            time.sleep(delay)
            count += 1


def run():
    # MinnesotaTimberwolves, WashingtonWizards
    todaysGames = ["AtlantaHawks", "DallasMavericks", "BostonCeltics",  "NewYorkKnicks", "ChicagoBulls", "CharlotteHornets", "DenverNuggets", "PhoenixSuns", "HoustonRockets", "LosAngelesClippers", "MilwaukeeBucks", "Philadelphia76ers", "MinnesotaTimberwolves", "WashingtonWizards", "NewOrleansPelicans", "BrooklynNets", "OrlandoMagic", "MiamiHeat", "PortlandTrailBlazers", "SanAntonioSpurs", "SacramentoKings", "MemphisGrizzlies", "UtahJazz", "LosAngelesLakers"]
    # Create two threads as follows
    try:
        for team in todaysGames:
            print team
            fileIn = open("gameData/"+team+"/NN_Result.csv", 'r+').read()
            predictions = fileIn.split(",")
            
            thread.start_new_thread(print_game, ("gameData/" + team + "/2-25-2015", timeToWait, predictions ))
            time.sleep(1)
    except:
        print "Error: unable to start thread"
    index = 0
    while index < 200:
        index += 1
        #print "+++ iteration +++ " + str(index)
        time.sleep(timeToWait)

    print 'Finished Emulating'

if __name__ == "__main__":
    run()
