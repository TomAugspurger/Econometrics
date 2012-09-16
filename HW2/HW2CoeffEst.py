from __future__ import division
import numpy as np
from numpy import random
from uniformRV import uniformRV
import statsmodels.api as sm

# To do: Calculate yHat (in or out of for loop?) and find s^2, the variance of predictions.
def coeffEst(x, N):
    """
    Estimates the coefficients from a simple regression between two vectors.
    
    Parameters
    -x is the independent variable. e.g. a sample drawn from a uniform distribution
    -N is the length of the resulting output vector. The number of iterations.  1000 in the HW.
    
    -n is taken from the uniformRV variable, the length of our independent random vector.
    Returns: 
        A flat np array containing each estimate of the intercept and slope 
        on x from the (y, x) regression; the variance of b0 and b1 and the cov(b0, b1)
        y is the mean of the n (= 100 in the Homework) predictions.
    
    Need to build in handling for if x has a constant column or not.
    Need to check on if s^2 = mse_model or something else.
    """
    y = np.empty(len(x), dtype = float)
    b = np.empty(5 * N, dtype = float)
    b = b.reshape(N, 5)
    yHat = np.empty(N, dtype = float) #Not using yet
    ybar = np.empty(N, dtype = float)
    mseModel = np.empty(N, dtype = float)
    mseResiduals = np.empty(N)
    
    for j in range(0, N):
        y[:] = np.random.normal(10 - x[:, 1], 5)
        model = sm.OLS(y, x)
        results = model.fit()
        b[j, 0] = results.params[0]
        b[j, 1] = results.params[1]
        b[j, 2] = results.cov_params()[0, 0] # For beta 0 Non-robust.  Use results.HC0_se or 1, 2, 3.
        b[j, 3] = results.cov_params()[1, 1] # For beta 1. Take sqrt of the std error.
        b[j, 4] = results.cov_params()[0, 1] # For the cov(beta 0, beta 1)
        ybar[j] = np.mean(y)
        mseModel[j] = results.mse_model
        mseResiduals[j] = results.mse_resid
    return (b, ybar, mseModel, mseResiduals)
