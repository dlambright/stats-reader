import numpy as np
import neural_network as nn
import trainer as tr
import oldStatsReader
import pylab as plt


jVals = [.00001, .0001, .001, .01, .1]
for j in range(0,4): #.000001, .00001, .0001, .001, .01, .1):
    for i in range(1, 45):#1,45):
        print 'i: ' + str(i)
        print 'j: ' + str(j)
        NN = nn.neuralNetwork(i, jVals[j])
        T = tr.trainer(NN)

        #X = np.array(([3.0,5.0],[5.0,1.0],[10.0,2.0]), dtype = float)
        #y = np.array(([75.0],[82.0], [93.0]), dtype = float)


        X, y = oldStatsReader.readOldStats()
        '''
        print X.shape
        print y.shape
        print NN.W1.shape
        print NN.W2.shape
        '''
        X = X/np.amax(X, axis=0) #<---- Check this value out....
        #y = y/100

        NN.forward(X)
        #print 'first forward done. \n'
        #print '\n'
        T.train(X,y)
        gameProgressionArray = np.empty([19])
        openFile = open('gameData/AtlantaHawks/2-25-2015.csv').read()
        fileData = openFile.split('\n')
        for line in fileData:
            temp = np.fromstring(line, dtype=float, count = 19, sep=',')
            gameProgressionArray = np.vstack((gameProgressionArray, temp))
        gameProgressionArray = gameProgressionArray[1:] 
        #print gameProgressionArray.shape
        #print gameProgressionArray[0]


        result = NN.forward(gameProgressionArray)
        '''
        for item in result:
            print '%.10f' %item

        #print 'sum: ' + str (sum(result))
        '''
        plt.plot(result)
        plt.xlim(0.,150)
        plt.ylim(0.,1.0)
        plt.xlabel('iteration')
        plt.ylabel('Win Probability')
        plt.title('Atlanta Hawks 2-25-2015')
        plt.grid(True)
        plt.savefig("result" + str(j)+ "index" +str(i)+"node.png")
        plt.clf()
        #show()


'''
END TEST BLOCK
'''


#NN = nn.neuralNetwork()
#T = tr.trainer(NN)

#X, y = oldStatsReader.readOldStats()


#X = np.array(([3,5],[5,1],[10,2]), dtype = float)
#y = np.array(([75],[82], [93]), dtype = float)
'''
print 'X:  ' + str(X.shape)
print 'y:  ' + str(y.shape)
print 'W1: ' + str(NN.W1.shape)#NN.W1)
print 'W2: ' + str(NN.W2.shape)#W2) 
'''
#T.train(X, y)
'''
print 'W1: ' + str(NN.W1.shape)
print 'W2: ' + str(NN.W2.shape) 
'''
#print NN.forward(T.X)
#y = np.array(([75],[82], [93]), dtype = float)
#print NN.forward(X)
