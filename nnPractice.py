import numpy as np
import neural_network as nn
import trainer as tr
import oldStatsReader
import pylab as plt
import os


'''
IF THIS FALLS TO SHIT, MAYBE TAKE THE PERCENTAGES OUT.  THEY MIGHT BE CAUSING SOMETHING FISHY IN THE CALCULATION.
'''
#teams = ['ATL', 'DAL']
#teamFullNames = ["AtlantaHawks", "DallasMavericks"]

teams = ['ATL','BOS','BRK','CHA','CHI','CLE','DAL','DEN','DET','GSW','HOU','IND','LAC','LAL','MEM','MIA','MIL','MIN','NOP','NYK','OKC','ORL','PHI','PHO','POR','SAC','SAS','TOR','UTA','WAS']

teamFullNames = ["AtlantaHawks", "BostonCeltics", "BrooklynNets", "CharlotteHornets", "ChicagoBulls", "ClevelandCavaliers", "DallasMavericks", "DenverNuggets", "DetroitPistons", "GoldenStateWarriors", "HoustonRockets", "IndianaPacers", "LosAngelesClippers", "LosAngelesLakers", "MemphisGrizzlies", "MiamiHeat", "MilwaukeeBucks", "NewOrleansPelicans", "NewYorkKnicks", "OklahomaCityThunder", "OrlandoMagic", "Philadelphia76ers", "PhoenixSuns", "PortlandTrailblazers", "SacramentoKings", "SanAntonioSpurs", "TorontoRaptors", "UtahJazz", "WashingtoWizards"]

# Input Layer size, Hidden Layer size, lambda size

for index in range(0,len(teams)):
    
        
    NN = nn.neuralNetwork(36, 24, .005)
    T = tr.trainer(NN)
    #X = np.array(([3.0,5.0],[5.0,1.0],[10.0,2.0]), dtype = float)
    #y = np.array(([75.0],[82.0], [93.0]), dtype = float)


    X, y = oldStatsReader.readOldStats(teams[index])
    size = X.shape[0]
    X = X/np.amax(X, axis=0) #<---- Check this value out....
    #y = y/100
    trainSize = int(.7 * size)
    testSize = int(.3 * size)

    # training matrices
    trainX = X[np.arange(testSize, size),:]
    trainY = y[np.arange(testSize, size),:]
    trainX = trainX/np.amax(trainX, axis=0)
    print trainX.shape

    # testing matrices
    testX = X[np.arange(0, testSize),:]
    testY = y[np.arange(0, testSize),:]
    testX = testX/np.amax(testX, axis=0)
    print testX.shape

    print 'training...'
    T.train(trainX, trainY, testX, testY)
    '''
    #plot the test vs train 
    plt.plot(T.J)
    plt.plot(T.testJ)
    plt.grid(1)
    plt.xlabel('Iterations')
    plt.ylabel('Cost')
    plt.show()
    '''
    '''
    print X.shape
    print y.shape
    print NN.W1.shape
    print NN.W2.shape
    '''
    NN.forward(X)
    #print 'first forward done. \n'
    #print '\n'
    #T.train(trainX, trainY, testX, testY)


    print teamFullNames[index] 
    if os.path.exists('gameData/'+teamFullNames[index]+'/2-25-2015.csv'):
        print 'in loop'
        gameProgressionArray = np.empty([36])
        openFile = open('gameData/' + teamFullNames[index] + '/2-25-2015.csv').read()
        fileData = openFile.split('\n')
        for line in fileData:
            temp = np.fromstring(line, dtype=float, count = 36, sep=',')
            gameProgressionArray = np.vstack((gameProgressionArray, temp))
        gameProgressionArray = gameProgressionArray[1:] 

    #gameProgressionArray = gameProgressionArray[:, [0,2,3,5,6,8,9,11,12,13,14,15,16,17,18]]
        #print gameProgressionArray.shape
        #print gameProgressionArray[3]



        result = NN.forward(gameProgressionArray)
        print 'gameData/' + teamFullNames[index] + '/NN_Result.csv'    
        fileOut = open('gameData/' + teamFullNames[index] + '/NN_Result.csv', 'w')
        for item in result:
            fileOut.write(str(item[0]) + ", ")
            #print item
        fileOut.close()


        #for item in result:
        #    print '%.10f' %item

        #print 'sum: ' + str (sum(result))

    '''
    plt.plot(result)
    plt.xlim(0.,150)
    plt.ylim(0.,1.0)
    plt.xlabel('iteration')
    plt.ylabel('Win Probability')
    plt.title('Dallas mavericks 2-25-2015')
    plt.grid(True)
    #plt.savefig("result" + str(j)+ "index" +str(i)+"node.png")
    plt.show()
    '''


    #END TEST BLOCK
'''


#NN = nn.neuralNetwork()
#T = tr.trainer(NN)

#X, y = oldStatsReader.readOldStats()


#X = np.array(([3,5],[5,1],[10,2]), dtype = float)
#y = np.array(([75],[82], [93]), dtype = float)
'''
#print 'X:  ' + str(X.shape)
#print 'y:  ' + str(y.shape)
#print 'W1: ' + str(NN.W1.shape)#NN.W1)
#print 'W2: ' + str(NN.W2.shape)#W2) 
'''
#T.train(X, y)
'''
#print 'W1: ' + str(NN.W1.shape)
#print 'W2: ' + str(NN.W2.shape) 
'''
#print NN.forward(T.X)
#y = np.array(([75],[82], [93]), dtype = float)
#print NN.forward(X)
'''
