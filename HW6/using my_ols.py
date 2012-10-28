# using my_ols
from __future__ import division

import my_ols
import pandas as pd
import numpy as np

# Read in
df = pd.read_csv('greenDataFormat.csv', index_col=0, parse_dates=True)
df.columns = ['gas', 'popn', 'gas_p', 'income', 'new_car_p',
            'used_car_p', 'ppt', 'pd', 'pn', 'ps']
df = df[['gas', 'popn', 'gas_p', 'income', 'new_car_p',
            'used_car_p']]
df = df[['gas', 'popn', 'gas_p', 'income', 'new_car_p', 'used_car_p']]
endog = np.log(df.gas / df.popn)
exog = pd.DataFrame(np.log(df.income / df.popn))
exog.columns = ['log_income_pp']
exog['log_gas_p'] = np.log(df.gas_p)
exog['log_new_car_p'] = np.log(df.new_car_p)
exog['log_used_car_p'] = np.log(df.used_car_p)

model = my_ols.my_ols(endog, exog, Y_varname='log_gas_pp', X_varnames=[
    'log_income_pp', 'log_gas_p', 'log_new_car_p', 'log_used_car_p'])
print model.b
print model.t
print model.p_value

print model.R2
