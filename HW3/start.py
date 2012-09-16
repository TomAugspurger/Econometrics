from __future__ import division
import numpy as np
import scipy as sp
import scipy.stats as ss
import statsmodels as sm
from uniformRV import uniformRV

N = 1000
x = np.zeros(N)
for t in range(len(x)):
    x[t] = np.random.uniform(0, 1)

print x

muFit, sigmaFit = ss.norm.fit(x)
print muFit, sigmaFit