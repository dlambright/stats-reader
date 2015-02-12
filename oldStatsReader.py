from urllib2 import urlopen


print "Running Scraper..."

teams = ['ATL','BOS','BRK','CHA','CHI','CLE','DAL','DEN','DET','GSW','HOU','IND','LAC','LAL','MEM','MIA','MIL','MIN','NOP','NYK','OKC','ORL','PHI','PHO','POR','SAC','SAS','TOR','UTA','WAS']
years = ['2014', '2015']
gameLog = 'gamelog/'
BASE_URL = "http://www.basketball-reference.com/teams"

def addDefensiveRebounds(text):
    x = 0
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

def sanitizeArray(array):
    toReturn = []
    for row in array:    
        afterFirstTag = False
        beforeSecondTag = False
        sanitizedValue = ''
        for x in range(0, len(row)): 
            
            if row[x] == '<':
                beforeSecondTag = not beforeSecondTag
            if afterFirstTag == True and beforeSecondTag == True:
                sanitizedValue += row[x]
            if row[x] == '>':
                afterFirstTag = True
        if sanitizedValue != '':
            toReturn.append(sanitizedValue)
    
    toReturn = addDefensiveRebounds(toReturn)
    return toReturn        



def readOldStats():
    for team in teams:
        readInData = []
        dataFile = open('previousData/'+ team + '.csv', 'w+')
        for year in years:
            rightSpot = False
            print BASE_URL + '/' + team + '/' + year + '/' + gameLog
            pageHTML = urlopen(BASE_URL + '/' + team + '/' + year + '/' + gameLog).read()
            currentLines = pageHTML.split('\n')        
        
            for x in range(0, len(currentLines)):
                if 'tgl_basic.' in currentLines[x]:
                    rightSpot = True
                if rightSpot == True:   
                    for y in range(6,42):
                        readInData.append(currentLines[x+y])
                    x += 42
                    rightSpot = False
        
        
            readInData = sanitizeArray(readInData)
        
            for x in range(0, len(readInData)):
                if x % 37 == 0 and x != 0:
                    dataFile.write('\n')
                dataFile.write(readInData[x] + ',')
            dataFile.closed
        
        print str(team) + ' done.'    
    print "scan complete"




#readOldStats()






















