from __future__ import division

import numpy as np
import pandas as pd


df = pd.read_csv('/Users/tom/Dropbox/Economics/Econometrics/Icon Files/content/enforced2/1771216-ECON_06E221_SEC001_20123/Homework Data/FLP.txt', sep=' *')
endog = df['LFP']
exog = df[['WA', 'FAMINC', 'WE', 'KL6', 'K618']]
exog = exog.rename(columns={
                             'WA': 'age',
                             'FAMINC': 'income',
                             'WE': 'education',
                             'KL6': 'kids1',
                             'K618': 'kids2',
                             })
exog['kids'] = exog.kids1 + exog.kids2
exog['cons'] = np.ones(len(exog))
exog['age_sq'] = exog['age'] ** 2
exog = exog.reindex(columns=[['cons', 'age', 'age_sq',
                            'income', 'education', 'kids']])
exog.join(endog).to_csv('clean_LFP.csv')
