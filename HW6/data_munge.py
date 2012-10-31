# data_munge.py
from __future__ import division

import numpy as np
import pandas as pd


df = pd.read_csv('greenDataFormat.csv', index_col=0, parse_dates=True)
df.columns = ['gas', 'popn', 'gas_p', 'income', 'new_car_p',
            'used_car_p', 'ppt', 'pd', 'pn', 'ps']
df = df[['gas', 'popn', 'gas_p', 'income', 'new_car_p',
            'used_car_p']]
df = df[['gas', 'popn', 'gas_p', 'income', 'new_car_p', 'used_car_p']]

endog = pd.DataFrame(np.log(df.gas), columns=['log_gas_pp'])
exog = pd.DataFrame(np.ones(len(df)))
exog.index = df.index
exog['log_income_pp'] = np.log(df.income)
exog['log_gas_p'] = np.log(df.gas_p)
exog['log_new_car_p'] = np.log(df.new_car_p)
exog['log_used_car_p'] = np.log(df.used_car_p)
exog = exog.rename(columns={0: 'constant'})
df = pd.merge(endog, exog, on=None, how='outer', left_index=True,
    right_index=True)
df.to_csv('CleanGreenData.csv')
