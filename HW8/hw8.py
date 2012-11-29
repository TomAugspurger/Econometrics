import pandas as pd
import statsmodels.api as sm

df = pd.read_csv('clean.csv')

# a.) ln(wage) on educ, exper, expersq, black, south, smsa, reg661 through reg668 and smsa66.
endog_a = df['lwage']
exog_a = df[['educ', 'exper', 'expersq', 'black', 'south', 'reg661', 'reg662',
    'reg663', 'reg664', 'reg665', 'reg666', 'reg667', 'reg668', 'smsa66']]

endog_a.head()
exog_a.head()

