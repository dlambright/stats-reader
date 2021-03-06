from urllib2 import urlopen
import numpy as np

print "Reading training data....."

teams = ['ATL','BOS','BRK','CHA','CHI','CLE','DAL','DEN','DET','GSW','HOU','IND','LAC','LAL','MEM','MIA','MIL','MIN','NOP','NYK','OKC','ORL','PHI','PHO','POR','SAC','SAS','TOR','UTA','WAS']
#teams = ['ATL']
years = ['2012', '2013', '2014', '2015', '2016']
gameLog = 'gamelog/'
BASE_URL = "http://www.basketball-reference.com/teams"

nameConversionDictionary = {"AtlantaHawks":"ATL", 
    "BostonCeltics":"BOS",
    "BrooklynNets":"BRK",
    "CharlotteHornets":"CHA",
    "ChicagoBulls":"CHI",
    "ClevelandCavaliers":"CLE",
    "DallasMavericks":"DAL",
    "DenverNuggets":"DEN",
    "DetroitPistons":"DET",
    "GoldenStateWarriors":"GSW",
    "HoustonRockets":"HOU",
    "IndianaPacers":"IND",
    "LosAngelesClippers":"LAC",
    "LosAngelesLakers":"LAL",
    "MemphisGrizzlies":"MEM",
    "MiamiHeat":"MIA",
    "MilwaukeeBucks":"MIL",
    "MinnesotaTimberwolves":"MIN",
    "NewOrleansPelicans":"NOP",
    "NewYorkKnicks":"NYK",
    "OklahomaCityThunder":"OKC",
    "OrlandoMagic":"ORL",
    "Philadelphia76ers":"PHI",
    "PhoenixSuns":"PHO",
    "PortlandTrailblazers":"POR",
    "SacramentoKings":"SAC",
    "SanAntonioSpurs":"SAS",
    "TorontoRaptors":"TOR",
    "UtahJazz":"UTA",
    "WashingtonWizards":"WAS"}






# DEFENSIVE REBOUDS NOT INCLUDED IN HTML.  DO THE MATH AND ADD THEM MANUALLY.
def addDefensiveRebounds(text):
    x = 0
    #:W
    while x < (len(text)):
        orb1 = int(text[12+x])
        trb1 = int(text[13+x])
        orb2 = int(text[28+x])
        trb2 = int(text[29+x])
        defReb1 = trb1 - orb1
        defReb2 = trb2 - orb2

        text.insert(13 + x, str(defReb1))
        text.insert(30 + x, str(defReb2))
        x += 37

    return text 

#
def sanitizeArray(array):
    
    toReturn = []
    
    for dataCell in array:
        afterFirstTag = False
        beforeSecondTag = False
        sanitizedValue = ''
        for x in range(0, len(dataCell)): 
            
            if dataCell[x] == '<':
                beforeSecondTag = not beforeSecondTag
            if afterFirstTag == True and beforeSecondTag == True:
                sanitizedValue += dataCell[x]
            if dataCell[x] == '>':
                afterFirstTag = True
        if sanitizedValue != '':
            toReturn.append(sanitizedValue)
    
    toReturn = addDefensiveRebounds(toReturn)
    return toReturn        

           
# THIS METHOD DOES ALL OF THE HEAVY LIFTING.  IT READS THE OLD STATS, ONE ROW AT A TIME,
# AND APPENDS THEM TO A MASTER LIST.
def readOldStats(teamName):
    print teamName
    teamName = nameConversionDictionary[teamName]
    print teamName
    X = np.empty([38])
    teamNumber = -1
    #for team in teams:
    teamNumber = teamNumber + 1
    readInData = []
    dataFile = open('previousData/'+ teamName + '.csv', 'w+')
    for year in years:
        rightSpot = False
        #print BASE_URL + '/' + team + '/' + year + '/' + gameLog
        pageHTML = urlopen(BASE_URL + '/' + teamName + '/' + year + '/' + gameLog).read()
        currentLines = pageHTML.split('\n')        
        
        for x in range(0, len(currentLines)):
            if 'tgl_basic.'in currentLines[x]:
                rightSpot = True
            if rightSpot == True:
                #readInData.append(currentLines[x+3])   
                rightSpot = False
                if "2015-02-25" in currentLines[x+3]:
                    continue
                for y in range(6,42):
                    readInData.append(currentLines[x+y])
                x += 42
        
        
        readInData = sanitizeArray(readInData)
        
        #create training data
        for x in range(0, len(readInData)/37):
            tempArray = readInData[slice(x*37, (x+1) *37)]
            tempArray.insert(0, teamNumber)
            if 'W' in tempArray[1]:
                tempArray[1] = 1
            elif 'L' in tempArray[1]:
                tempArray[1] = 0
                
            tempNPArray = np.asarray(tempArray, dtype = float )
            X = np.vstack((X, tempNPArray))

        # write out data to file (probably delete down the road)
        #for x in range(0, len(readInData)):
        #    if x % 37 == 0 and x != 0:
        #        dataFile.write('\n')
        #    dataFile.write(readInData[x] + ',')

        #dataFile.write('\n')    
        #dataFile.closed
        
    print str(teamName) + ' done.'
    
    X = X[1:]
    
    #print "scan complete"
    y = X[:,1]
    #print y
    y = np.array([X[:,1]])
    y = y.T
    #print y
    X = X[:,2:]
    #X = X[:, [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]]
    #print "length of X: " + str(len(X))
    #print "length of Y: " + str(len(y)) 
    return X, y

#sampleDataRead = np.array([93, 91, 34, 79, 0.430379746835, 10, 25, 0.4, 15, 20, 0.75, 8, 29, 37, 23, 12, 5, 18, 19, 32, 81, 0.395061728395, 7, 26, 0.269230769231, 20, 21, 0.952380952381, 14, 33, 47, 17, 12, 3, 23, 16])

        
        

#X, y = readOldStats()
#print y
#print X[0]
#print sampleDataRead.shape

#if __name__ == "__main__":
#      readOldStats("UtahJazz") 


















