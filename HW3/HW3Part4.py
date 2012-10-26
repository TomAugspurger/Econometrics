## Filename: HW3Part4
## Author: Tom Augspurger

#To Do: Automate Latex summary
from __future__ import division
import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

"""
cd /Users/tom/Dropbox/Economics/Econometrics/Homework/HW3
"""

growthData = sm.iolib.foreign.genfromdta('Growth.dta')
growthData = sm.add_constant(growthData, prepend=True)
growthData = pd.DataFrame(growthData)
growthData = growthData[:64]  # Removes Malta, the last item'

endog = growthData['growth']

# Regessions: growth on
# 1: tradeshare and yearsschool
exog1 = ['const', 'tradeshare', 'yearsschool']
model1 = sm.OLS(endog, growthData[exog1])
results1 = model1.fit()

# 2: tradeshare and log(yearsschool)
exog2 = growthData[['const', 'tradeshare']]
exog2['logSchool'] = np.log(growthData['yearsschool'])
model2 = sm.OLS(endog, exog2)
results2 = model2.fit()

# 3: tradeshare, rev_coups, assasinations, logSchool, logRgdp60
exog3 = growthData[['const', 'tradeshare', 'rev_coups', 'assasinations']]
exog3['logSchool'] = np.log(growthData['yearsschool'])
exog3['logRgdp60'] = np.log(growthData['rgdp60'])
model3 = sm.OLS(endog, exog3)
results3 = model3.fit()

# 4: tradeshare, rev_coups, assasinations, logSchool, logRgdp60, tradeLnSchool
exog4 = growthData[['const', 'tradeshare', 'rev_coups', 'assasinations']]
exog4['logSchool'] = np.log(growthData['yearsschool'])
exog4['logRgdp60'] = np.log(growthData['rgdp60'])
exog4['tradeLnSchool'] = growthData[
                        'tradeshare'] * np.log(growthData['tradeshare'])
model4 = sm.OLS(endog, exog4)
results4 = model4.fit()

'''
5: tradeshare, rev_coups, assasinations, tradeSquared, tradeCubed, logSchool, logRgdp60
'''

exog5 = growthData[['const', 'tradeshare', 'rev_coups', 'assasinations']]
exog5['tradeSquared'] = growthData['tradeshare'] ** 2
exog5['tradeCubed'] = growthData['tradeshare'] ** 3
exog5['logSchool'] = np.log(growthData['yearsschool'])
exog5['logRgdp60'] = np.log(growthData['rgdp60'])
model5 = sm.OLS(endog, exog5)
results5 = model5.fit()

# Part a
plt.figure(); scatter1 = pd.tools.plotting.scatter_plot(growthData, 'tradeshare', 'growth')
plt.savefig('/Users/tom/Economics/Econometrics/Homework/HW3/tradeGrowthScatter.png', dpi=300)

# Part b
results1.params['yearsschool'] * 2
results2.params['logSchool'] * np.log(2)

# Part c
A = [[0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0]]  # rev_coups and assasinations are 3rd and 4th
print results3.f_test(A)  # Non-robust
R = sm.stats.sandwich_covariance.cov_white_simple(results3)
print results3.f_test(A, cov_p=R)  # Robust

# Part d
print results4.HC0_se['tradeshare']

# Part e
print results5.HC0_se[['tradeSquared', 'tradeCubed']]
print "No, but this may not be the appropriate model."
print "Controlling for everything simultaneously may mask the result."

# Part f
results3.params['tradeshare'] * .5
results5.params['tradeshare'] * 0.5 + results5.params[
    'tradeSquared'] * (0.5 ** 2) + results5.params['tradeCubed'] * (0.5 ** 3)
