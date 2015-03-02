import numpy as np
import trainer as tr

class neuralNetwork(object):
    def __init__(self):
        self.inputLayerSize = 2
        self.outputLayerSize = 1
        self.hiddenLayerSize = 3
        self.W1 = np.random.randn(self.inputLayerSize, self.hiddenLayerSize)
        self.W2 = np.random.randn(self.hiddenLayerSize, self.outputLayerSize)
        self.Lambda = .0001
    def sigmoid(self, z):
        toReturn = 1/(1+np.exp(-z))
        return toReturn
    
    def sigmoidPrime(self, z):
        return np.exp((-z)/((1+np.exp(-z))**2))

    def costFunction(self, X, y):
        self.yHat = self.forward(X)
        J = .5 * sum((y-self.yHat)**2)/X.shape[0] + (self.lambda/2) * sum(self.W1**2) + sum(self.W2**2)
        return J
         
    def forward(self, X):
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.sigmoid(self.z3)
        return yHat
    
    def costFunctionPrime(self, X, y):
        self.yHat = self.forward(X)
        
        delta3 = np.multiply(-(y-self.yHat), self.sigmoidPrime(self.z3))
        dJdW2 = np.dot(self.a2.T, delta3) + self.Lambda * self.W2

        delta2 = np.dot(delta3, self.W2.T)* self.sigmoidPrime(self.z2)
        dJdW1 = np.dot(X.T, delta2) + self.Lambda * self.W1

        return dJdW1, dJdW2
    
    def getParams(self):
        params = np.concatenate((self.W1.ravel(), self.W2.ravel()))
        return params

    def setParams(self, params):
        W1_start = 0
        W1_end = self.hiddenLayerSize*self.inputLayerSize
        self.W1 = np.reshape(params[W1_start:W1_end], (self.inputLayerSize, self.hiddenLayerSize))
        W2_end = W1_end + self.hiddenLayerSize * self.outputLayerSize
        self.W2 = np.reshape(params[W1_end:W2_end], (self.hiddenLayerSize, self.outputLayerSize))

    def computeGradients(self, X, y):
        dJdW1, dJdW2 = self.costFunctionPrime(X,y)
        return np.concatenate((dJdW1.ravel(), dJdW2.ravel()))


    def computeNumericalGradients(self, X, y):
        paramsInitial = self.getParams()
        numGrad = np.zeros(paramsInitial.shape)
        perturb = np.zeros(paramsInitial.shape)
        e = 1e-4

        for p in range(len(paramsInitial)):
            perturb[p] = e
            self.setParams(paramsInitial + perturb)
            loss2 = self.costFunction(X,y)
        
            self.setParams(paramsInitial - perturb)
            loss1 = self.costFunction(X,y)

            numGrad[p] = (loss2-loss1) / (2*e)

            perturb[p] = 0

        self.setParams(paramsInitial)

        return numGrad


def computeNumericalGradient(N, X, y):
    paramsInitial = N.getParams()
    numGrad = np.zeros(paramsInitial.shape)
    perturb = np.zeros(paramsInitial.shape)
    e = 1e-4

    for p in range(len(paramsInitial)):
        perturb[p] = e
        N.setParams(paramsInitial + perturb)
        loss2 = N.costFunction(X,y)
        
        N.setParams(paramsInitial - perturb)
        loss1 = N.costFunction(X,y)

        numGrad[p] = (loss2-loss1) / (2*e)

        perturb[p] = 0

    N.setParams(paramsInitial)

    return numGrad



NN = neuralNetwork()
T = tr.trainer(NN)

X = np.array(([3,5],[5,1],[10,2]), dtype = float)
y = np.array(([75],[82], [93]), dtype = float)

print NN.forward(X)




#T.train(X, y)

#numGrad = computeNumericalGradient(NN, X, y)
#grad = NN.computeNumericalGradients(X, y)

#print numGrad 
#print grad

#check the difference.  should be < 10*e-7 or so
#print np.linalg.norm(grad-numGrad)/np.linalg.norm(grad+numGrad)










#yHat = NN.forward(X)
#print yHat
