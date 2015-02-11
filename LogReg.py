
import numpy
from scipy.special import expit


def sigmoid(matrix):
    matrix = expit(matrix)
    return matrix
    
    
#testMatrix = numpy.matrix([-2,-1,0,1,2])
#print sigmoid(testMatrix)


def costFunctionReg(theta, X, y, lambdaa):
#    J = 0;
#    grad = zeros(size(theta));
# 
#    h = sigmoid(X * theta);#

#    J = (-1/m) * ((y.transpose() * log(h)) + (!y.transpose() * log(1-h))) + ((lambdaa/(2*m)) * sum(theta([2:rows(theta)]).^2)); 

#    theta(1) = 0;
 #   grad = (1/m * (X'*(h-y))) + ((lambda/m) * theta);  %theta([2:rows(theta)]));
    return .5