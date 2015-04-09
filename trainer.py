from scipy import optimize


class trainer(object):
    def __init__(self, N):
        self.N = N
    
    def costFunctionWrapper(self, params, X, y):
        self.N.setParams(params)
        cost = self.N.costFunction(X, y)
        grad = self.N.computeGradients(X, y)
        return cost, grad

    def callbackF(self, params):
        self.N.setParams(params)
        self.J.append(self.N.costFunction(self.X, self.y))
        self.testJ.append(self.N.costFunction(self.testX, self.testY))

    def train(self, trainX, trainY, testX, testY):
        self.X = trainX
        self.y = trainY

        self.testX = testX
        self.testY = testY
        
        self.J = []
        self.testJ = []
        params0 = self.N.getParams()
        
        

        options = {'maxiter': 200, 'disp' : True} 
        _res = optimize.minimize(self.costFunctionWrapper, 
                                    params0, 
                                    jac = True, 
                                    method='BFGS', 
                                    args = (trainX,trainY), 
                                    options=options, 
                                    callback=self.callbackF)
        #print _res
        self.N.setParams(_res.x)
        self.optimizationResults = _res
