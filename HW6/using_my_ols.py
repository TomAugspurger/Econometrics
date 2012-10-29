# using my_ols
from __future__ import division

import my_ols
import pandas as pd

# Read in
df = pd.read_csv('CleanGreenData.csv', index_col=0, parse_dates=True)
endog = df['log_gas_pp']
exog = df[['constant', 'log_income_pp', 'log_gas_p', 'log_new_car_p',
       'log_used_car_p']]

# Estimation
model = my_ols.my_ols(endog, exog, Y_varname='log_gas_pp', X_varnames=[
    'log_income_pp', 'log_gas_p', 'log_new_car_p', 'log_used_car_p'], add_constant=False)
print model.b
print model.t
print model.p_value

print model.R2
