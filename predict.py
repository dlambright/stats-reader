import numpy as np
#import LogReg

'''
actualData = [[0 for x in range(21)] for x in range(82)]

with open('sanitizedData.csv', 'r') as dataFile:
    dataFile.readline()
    rowCount = 0    
    for line in dataFile:
        columnCount = 0
        if line.find('</span>') == 1:
            print 'found span'
            line = line.replace('</span>', '')
        tempArray = list(line)
        if 'W' in line:
            tempArray[0] = '1'
        else:
            tempArray[0] = '0'
        line = "".join(tempArray)
           
        temp = line.split(',')
        for data in temp:
            if data != ' ' and columnCount < 21:
                actualData[rowCount][columnCount] = float(data)
                columnCount += 1
        rowCount += 1
 
dataMatrix = np.matrix(actualData[0])  
for x in range(1,82):
    temp = np.matrix(actualData[x])
    dataMatrix = np.concatenate((dataMatrix, temp), axis =0)

print dataMatrix   
                
                
#print actualData
#dataMatrix = dataMatrix.reshape(21,82)

dataFile.closed
'''

def predictWinProbability(stats):
    #placeholder code.  Replace when the algo is finished.
    
    statsLine0 = stats[0]
    statsLine1 = stats[1]

    score0 = [stats[0][0]]
    score1 = [stats[1][0]]
    scoreSum = score0[0] + score1[0]
    
    
    statsLine0.append(float(score0[0])/float(scoreSum))
    statsLine1.append(float(score1[0])/float(scoreSum))
    
     
    stats = [statsLine0] + [statsLine1]
    
    
    return stats       

def readInYValues(teamName):
    valuesArray = [] 
    readFile = open('previousData/' + teamName+ '.csv', 'r').read()
    readFile = readFile.split('\n')
    
    for line in readFile:        
        if 'W' in line:
            valuesArray.append(1)
        elif 'L' in line:
            valuesArray.append(0)
        else:
            print 'ERROR.  COULD NOT DETERMINE WIN OR LOSS.  LOOK AT LINE 51 IN PREDICT.PY'
            
    yMatrix = np.empty(len(readFile)-1, dtype = int)
    for x in range(0, len(valuesArray)):
        yMatrix[x] = valuesArray[x]
    print valuesArray
    print yMatrix.shape
    
   # return yMatrix
def readInXValues(teamName):

    readFile = open('previousData/' + teamName + '.csv', 'r').read()
    readFile = readFile.split('\n') 
    bigArray = []
    
    for line in readFile:
        
        tempLineArray = []        
        line = line.split(',')
        del line[0] # take the w/l out
        for x in range(0,len(line)-1):
            tempLineArray.append(float(line[x]))
        
        if len(tempLineArray) > 0:
            bigArray.append(tempLineArray)
                   
   # print bigArray[0][1]
                   
    rows = len(readFile) - 1
    columns = len(bigArray[0])             
    toReturn = np.empty([rows, columns], dtype = float)
    
    for j in range(0, rows):
        for y in range(0, columns):
            toReturn[j][y] = bigArray[j][y]
            
    print toReturn.shape
    #return toReturn
    

    
    
#readInYValues('ATL')
readInXValues('ATL')
