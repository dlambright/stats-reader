import os
base_dir = "/Users/charliebuckets/Desktop/projects/stats-reader/gameData"

def addTSP(dataMatrix):
    dataMatrix = dataMatrix.split("\n")
    for i in range(0,len(dataMatrix)):
        #print row
        rowArray = dataMatrix[i].split(",")
        if len(rowArray) > 1:
            print dataMatrix[i]
            print "\n"
            points = float(rowArray[0])
            FGA = int(rowArray[3])
            FTA = int(rowArray[9])
            
            if FGA == 0 and FTA == 0:
                result = 0
            else:
                result = points / (2*(FGA + (.44*FTA)))
            
            dataMatrix[i] = dataMatrix[i] + str(result)
    return dataMatrix            


atlData = open(base_dir+"/DallasMavericks/2-25-2015.csv").read()
data = addTSP(atlData)

testFile = open("wutWut.csv", 'a')
for line in data:
    testFile.write(line+"\n")
    print line




'''
for folder in os.listdir(base_dir):
    if folder != ".DS_Store":
        for item in os.listdir(base_dir+"/"+folder):
            gameData = open(base_dir+"/"+folder+"/"+item).read()
            newData = addTSP(gameData)
            fileOut = open(base_dir+"/gameDataII/"+folder+"/"+item, 'a')
            for line in newData:
                 fileOut.write(line+"\n")
'''









              
