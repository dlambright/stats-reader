import numpy as np
import neural_network as nn
import trainer as tr
#import oldStatsReader



NN = nn.neuralNetwork()
T = tr.trainer(NN)

X = np.array(([3.0,5.0],[5.0,1.0],[10.0,2.0]), dtype = float)
y = np.array(([75.0],[82.0], [93.0]), dtype = float)

X = X/np.amax(X, axis=0)
y = y/100

print NN.forward(X)
print '\n'
T.train(X,y)
print NN.forward(X)

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
