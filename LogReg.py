import numpy as np
from scipy.special import expit


def sigmoid(matrix):
    matrix = expit(matrix)
    return matrix
    
def getYInverse(y):
    for x in range(0, y.shape[0]):
        if y[x] == 1:
            y[x] = 0
        else:
            y[x] = 1
    return y
    
    
def getCostFunctionGradient(theta, X, y):
    #theta = [37, 1]
    #X     = [135, 37]
    #y     = [135, 1]

    #print 'theta ' + str(theta.shape)
    #print 'X     ' + str(X.shape)
    #print 'y     ' + str(y.shape)
      
    m = y.shape[0]
    #print m
    
    h = sigmoid(X * theta)    
    #print 'h     ' + str(h.shape)
    
    
    grad = (X.transpose()* (h-y)) / m 
    #print 'grad  ' + str(grad.shape)
    #print grad    
    return grad

def getCostFunctionJ(theta, X, y):
    print 'nuffin'



def costFunctionReg(theta, X, y, lambdaa):
#    J = 0;
#    grad = zeros(size(theta));
# 
#    h = sigmoid(X * theta);#

#    J = (-1/m) * ((y.transpose() * log(h)) + (!y.transpose() * log(1-h))) + ((lambdaa/(2*m)) * sum(theta([2:rows(theta)]).^2)); 

#    theta(1) = 0;
 #   grad = (1/m * (X'*(h-y))) + ((lambda/m) * theta);  %theta([2:rows(theta)]));
    return .5