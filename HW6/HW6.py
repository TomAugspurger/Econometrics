from __future__ import division

import pandas as pd
import numpy as np
import statsmodels.api as sm

df = pd.read_csv('greenDataFormat.csv', index_col=0, parse_dates=True)
df.columns = ['gas', 'popn', 'gas_p', 'income', 'new_car_p',
            'used_car_p', 'ppt', 'pd', 'pn', 'ps']

df = df[['gas', 'popn', 'gas_p', 'income', 'new_car_p', 'used_car_p']]

endog = np.log(df.gas / df.popn)
exog = pd.DataFrame(np.ones(len(df)))
exog.index = df.index
exog['log_income_pp'] = np.log(df.income / df.popn)
exog['log_gas_p'] = np.log(df.gas_p)
exog['log_new_car_p'] = np.log(df.new_car_p)
exog['log_used_car_p'] = np.log(df.used_car_p)

model = sm.OLS(endog, exog)
results = model.fit()

robust_se = results.cov_HC0

print "The robust standard errors are\n"
print robust_se

#Non robust
se = results.cov_params()

