import os

import pandas as pd
import statsmodels.api as sm


os.chdir('/Users/tom/Dropbox/Economics/Econometrics/Homework/HW8')
df = pd.read_csv('clean.csv')
df = sm.add_constant(df, prepend=True)
# a.) ln(wage) on educ, exper, expersq, black, south, smsa, reg661
#   through reg668 and smsa66.
endog_a = df['lwage']
exog = ['const', 'educ', 'exper', 'expersq', 'black', 'south',
        'smsa', 'reg661', 'reg662', 'reg663', 'reg664', 'reg665',
        'reg666', 'reg667', 'reg668', 'smsa66']

exog_a = df[exog]

endog_a.head()
exog_a.head()

model_a = sm.OLS(endog_a, exog_a)
results_a = model_a.fit()

print(results_a.summary())

#b: educ on exog_a - educ + nearc4
endog_b = df['educ']
exog_b = exog_a.drop('educ', axis=1).join(df['nearc4'])

model_b = sm.OLS(endog_b, exog_b)
results_b = model_b.fit()

print(results_b.summary())

# Part c: IV lwage on explanatory w/ nearc4 as instr. for educ.
endog_x = df['educ']
exog_x = df[['const', 'nearc4', 'exper', 'expersq', 'black', 'south',
        'smsa', 'reg661', 'reg662', 'reg663', 'reg664', 'reg665',
        'reg666', 'reg667', 'reg668', 'smsa66']]


model_x = sm.OLS(endog_x, exog_x)
results_x = model_x.fit()
df['educ_hats'] = results_x.fittedvalues

endog_c = df['lwage']

# replace educ with IV.
exog_c = df[['const', 'educ_hats', 'exper', 'expersq', 'black', 'south',
        'smsa', 'reg661', 'reg662', 'reg663', 'reg664', 'reg665',
        'reg666', 'reg667', 'reg668', 'smsa66']]

model_c = sm.OLS(endog_c, exog_c)
results_c = model_c.fit()

# Need to compare the widths of the two intervals on Beta_educ.

##########################
#### PART D
##########################
# Reuse endog_x from c;
exog_x2 = df[['const', 'nearc2', 'nearc4', 'exper', 'expersq', 'black',
        'south', 'smsa', 'reg661', 'reg662', 'reg663', 'reg664', 'reg665',
        'reg666', 'reg667', 'reg668', 'smsa66']]

model_x2 = sm.OLS(endog_x, exog_x2)
results_x2 = model_x2.fit()
df['educ_hats2'] = results_x2.fittedvalues

exog_d = df[['const', 'nearc2', 'nearc4', 'exper', 'expersq', 'black',
        'south', 'smsa', 'reg661', 'reg662', 'reg663', 'reg664', 'reg665',
        'reg666', 'reg667', 'reg668', 'smsa66'] + ['educ_hats2']]

model_d = sm.OLS(endog_c, exog_d)
results_d = model_d.fit()

print(results_d.summary())

# PART E
df[['iq', 'nearc4']].corr()

# PART F
endog_f = df['iq'].dropna()
idx = endog_f.index
exog_f = df[['const', 'nearc4', 'smsa66', 'reg661',
                                'reg662', 'reg669']].ix[idx]

model_f = sm.OLS(endog_f, exog_f)
results_f = model_f.fit()
print(results_f.summary())

