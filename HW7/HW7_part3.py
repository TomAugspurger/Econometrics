from __future__ import division

import pandas as pd
import statsmodels.api as sm
from quantile_regression import quantilereg

growth = pd.DataFrame(sm.iolib.foreign.genfromdta(
    '/Users/tom/Dropbox/Economics/Econometrics/Homework/HW3/Growth.dta'))

growth_no_malta = growth[:64]

# Model 1: growth on trade_share, years_school
endog = growth['growth']
exog = ['tradeshare', 'yearsschool']
model = sm.OLS(endog, sm.add_constant(growth[exog], prepend=True))
results = model.fit()

model_no_malta = sm.OLS(endog[:64], sm.add_constant(growth_no_malta[exog][:64],
    prepend=True))
results_no_malta = model_no_malta.fit()

qr_results = quantilereg(endog, growth[exog], .5)
qr_results_no_malta = quantilereg(endog[:64], growth_no_malta[exog], .5)

for i, v in enumerate(results.params):
    print 100 * (results.params[i] - results_no_malta.params[i]) / results.params[i]

for i, v in enumerate(qr_results):
    print 100 * (qr_results[i] - qr_results_no_malta[i]) / qr_results_no_malta[i]
