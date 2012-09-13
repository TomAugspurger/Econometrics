from __future__ import division
import numpy as np
from numpy import random
from /Users/tom/Dropbox/Economics/Econometrics/Homework/uniformRV import uniformRV
import statsmodels.api as sm

# Problem 1
low, high, n = (0, 10, 100)
x = uniformRV(low, high, n)

# Problem 2 (note numpy.random.normal() takes std dev, NOT variance)
y = np.empty(n, dtype = float)
y = np.random.normal(10 - x - (25/x), 5)
x = sm.tools.tools.add_constant(x, prepend = True)

model = sm.OLS(y, x)
results = model.fit()
print results.summary()