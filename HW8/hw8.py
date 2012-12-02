import os

import pandas as pd
import statsmodels.api as sm


os.chdir('/Users/tom/Dropbox/Economics/Econometrics/Homework/HW8')
df = pd.read_csv('clean.csv')

# a.) ln(wage) on educ, exper, expersq, black, south, smsa, reg661 through reg668 and smsa66.
endog_a = df['lwage']
exog = ['educ', 'exper', 'expersq', 'black', 'south', 'reg661', 'reg662',
        'reg663', 'reg664', 'reg665', 'reg666', 'reg667', 'reg668', 'smsa66']

exog_a = df[exog]
exog_a = sm.add_constant(exog_a, prepend=True)

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

# Part c: IV lwage on explanatory w/ nearc4 as instr. for educ.
endog_x = df['educ']
exog_x = df[['const', 'nearc4', 'exper', 'expersq', 'black', 'south',
        'reg661', 'reg662', 'reg663', 'reg664', 'reg665',
        'reg666', 'reg667', 'reg668', 'smsa66']]


model_x = sm.OLS(endog_x, exog_x)
results_x = model_x.fit()
df['educ_hats'] = results_x.fittedvalues

endog_c = df['lwage']

# replace educ with IV.
exog_c = df[['const', 'educ_hats' 'exper', 'expersq', 'black', 'south',
        'reg661', 'reg662', 'reg663', 'reg664', 'reg665',
        'reg666', 'reg667', 'reg668', 'smsa66']]

model_c = sm.OLS(endog_c, exog_c)
results_c = model_c.fit()

# Need to compare the widths of the two intervals on Beta_educ.

##########################
#### PART D
##########################
# Reuse endog_x from c;
exog_x2 = df[['const', 'nearc2', 'nearc4']]
