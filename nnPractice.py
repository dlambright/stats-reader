import numpy as np
import neural_network as nn
import trainer as tr
import oldStatsReader
	


NN = nn.neuralNetwork()
T = tr.trainer(NN)

X = np.array(([3.0,5.0],[5.0,1.0],[10.0,2.0]), dtype = float)
y = np.array(([75.0],[82.0], [93.0]), dtype = float)


X, y = oldStatsReader.readOldStats()
print X.shape
print y.shape
print NN.W1.shape
print NN.W2.shape

X = X/np.amax(X, axis=0)
#y = y/100

NN.forward(X)
print 'first forward done. \n'
print '\n'
T.train(X,y)


#sampleDataRead = np.array([33, 21, 12, 21, 0.571428571429, 4, 8, 0.5, 5, 5, 1.0, 1, 12, 13, 9, 5, 5, 6, 6, 7, 24, 0.291666666667, 3, 8, 0.375, 4, 8, 0.5, 6, 6, 12, 6, 3, 0, 6, 3])

gameProgressionArray = np.empty([36])
openFile = open('gameData/AtlantaHawks/2-20-2015.csv').read()
fileData = openFile.split('\n')
for line in fileData:
    temp = np.fromstring(line, dtype=float, count = 36, sep=',')
    gameProgressionArray = np.vstack((gameProgressionArray, temp))
gameProgressionArray = gameProgressionArray[1:] 
print gameProgressionArray.shape
print gameProgressionArray[0]


result = NN.forward(gameProgressionArray)
print result
print 'sum: ' + str (sum(result))
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
