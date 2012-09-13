""""
Alternative Method of filling
"""

from __future__ import division
import numpy as np
import scipy as sp
import statsmodels as sm
from statsmodels import iolib
from statsmodels import regression
import matplotlib as mpl
import pylab as py
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Clean the Data

data = sm.iolib.foreign.genfromdta('/Users/tom/Dropbox/Economics/Econometrics/Icon Files/content/enforced2/1771216-ECON_06E221_SEC001_20123/Homework Data/cps92_08.dta')

numberRows = len(data)
numberColumns = len(data[0])

AHE = np.transpose(np.zeros(numberRows)) # Average Hourly Earnings
age = np.transpose(np.zeros(numberRows))

A = pd.DataFrame(data)
AHE = np.array(A['ahe'])
age = np.array(A['age'])

age = sm.regression.linear_model.add_constant(age)

print(datetime.now()-startTime)

# Regression and Calculations
model = sm.regression.linear_model.OLS(AHE, age)
results = model.fit()
averageEarnings = results.predict(np.mean(age))
averageEarnings = averageEarnings[1]
x = results.conf_int()
low = x[0, 0]
high = x[0, 1]

# Answering Questions

# 5.1
print results.summary()
print 'Reject the null at 1% significance'

# 5.2
print 'The confidence 95%% confidence interval is (%f , %f).' % (low, high)

#5.3
print 'The average-aged worker makes %f.' % averageEarnings
#5.4
print 'Age does not represent a large fraction of the variance. The R-squared is %f.' % results.rsquared

# Plot Results
# py.plot(np.transpose(age[:, 0]), results.fittedvalues, 'r--.')
# py.scatter(np.transpose(age[:, 0]), AHE)
# py.show()

print(datetime.now()-startTime)