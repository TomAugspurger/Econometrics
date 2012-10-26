from __future__ import division

import pandas as pd
import numpy as np
import statsmodels.api as sm

df = pd.read_csv('greenDataFormat.csv', index_col=0, parse_dates=True)
df.columns = ['gas', 'pop', 'gas_p', 'income', 'new_car_p',
            'used_car_p', 'ppt', 'pd', 'pn', 'ps']
df['ones'] = np.ones(len(df))
