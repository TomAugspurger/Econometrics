from __future__ import division
import numpy as np
from numpy import random
from uniformRV import uniformRV
import statsmodels.api as sm
from HW2CoeffEst import coeffEst
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pylab as py
from datetime import datetime
import npkde

'''
cd ~/Economics/Econometrics/Homework/HW2
Project is structured as
    uniformRV to generate the random vector x
    statsmodels for the regression
    collect the results here, by calling coeffEst from HW2CoeffEst.py
    Plotting/analysis from this script
'''
startTime = datetime.now()

low, high, n = (0, 10, 100)
x = uniformRV(low, high, n)
x = sm.tools.tools.add_constant(x, prepend = True)

# b is an odd matrix. b[0] is (1000, 5) The order is b0, b1, variance for b0, variance for b1, cov(b0, b1).  b[1] is the list of 1000 sample means for the y. b[2] is the 1000 MSE's, one for each iteration.

# I should build the distribution of y into a parameter of coeffEst.  Currently is Normal with mean conditional mean 10 - x, and (homoskedastic) variance 25.
regressionResults = coeffEst(x, n, 1000)
ybar = regressionResults[1]
# mseModel = regressionResults[2] # I don't think we want these.  We want the MSE of the residuals.
mseResiduals = regressionResults[3]
beta0 = regressionResults[0][:, 0]
beta1 = regressionResults[0][:, 1]
varBeta0 = regressionResults[0][:, 2]
varBeta1 = regressionResults[0][:, 3]
covBeta = regressionResults[0][:, 4]

# Output
print 'The mean of x is %f' % np.mean(x[:, 1])
print 'The sample mean of the means of each y vector is %f' % np.mean(ybar)
print 'The sample mean of the intercept is %f' % np.mean(beta0)
print 'The sample mean of the slope is %f' % np.mean(beta1)
print 'The sample mean for the mean square errors of the residuals is %f' % np.mean(mseResiduals)


f, axarr = plt.subplots(1, 2)
n1, bins1, patches1 = axarr[0].hist(beta0, 100, normed = 1)
n2, bins2, patches1 = axarr[1].hist(beta1, 100, normed = 1, facecolor = 'green')

bincenters1 = 0.5 * (bins1[1:] + bins1[:-1])
bincenters2 = 0.5 * (bins2[1:] + bins2[:-1])

# Overlaying the population distribution of coefficients for beta0 & beta1.  Based on S&W p 133
# H = np.empty(100)

y1 = mlab.normpdf(bincenters1, 10, .9) # need to calculate actual mean, std
y2 = mlab.normpdf(bincenters2, -1, np.sqrt((1/n) * (np.var(x[:, 1] - 5)*25) / (np.var(x[:, 1])**2)))

l1 = axarr[0].plot(bincenters1, y1, 'r--', linewidth = 2)
l2 = axarr[1].plot(bincenters2, y2, 'r--', linewidth = 2)

axarr[0].set_xlabel('Beta 0')
axarr[1].set_xlabel('Beta 1')
axarr[0].set_ylabel('')
py.suptitle('Normed Histograms for Coefficient Distribution')
print(datetime.now()-startTime)

plt.show()

# Alt Plotting Code
# fig = plt.figure()
# ax = fig.add_subplot(111)
# n, bins, patches = ax.hist(beta0, 50)
# bincenters = 0.5 * (bins[1:] + bins[:-1]) # Centers the bins

# Trying to overlay a normal pdf. Not working correctly.
# z = mlab.normpdf(beta0, 10, 5)
# l = ax1.plot(beta0  , 10, 'r--', linewidth = 1)

