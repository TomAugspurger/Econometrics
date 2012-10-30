from __future__ import division

import pandas as pd
import numpy as np
import statsmodels.api as sm

# Read in
df = pd.read_csv('CleanGreenData.csv', index_col=0, parse_dates=True)
endog = df['log_gas_pp']
exog = df[['constant', 'log_income_pp', 'log_gas_p', 'log_new_car_p',
       'log_used_car_p']]

# With Statsmodels
model = sm.OLS(endog, exog)
results = model.fit()
results.HC0_se  # Need to call to get the matrix
results.cov_HC0  # Robust Standard Error Matrix
se = results.cov_params()  # Non-robust

results.rsquared
R = np.array([[0, 0, 0, 1, 0], [0, 0, 0, 0, 1]])
results.f_test(R)
