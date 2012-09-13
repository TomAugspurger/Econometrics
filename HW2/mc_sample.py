from __future__ import division
import numpy as np
from numpy import random

def uniformRV(low, high, n):
    """
    A function that generates an array with simulated data from a uniform distribution over (low, high) of size n.
    
    Parameters:
    -low: the lower support of the uniform distribution
    -high: the upper support of the uniform distribution
    -n: the sample size
    
    Returns: A flat np array containing the sample data.
    """
    
    x = np.empty(n, dtype = float)
    for t in range(n):
        x[t] = np.random.uniform(low, high)
        
    return x