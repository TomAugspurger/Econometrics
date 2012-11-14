from __future__ import division

from math import ceil
import pandas as pd
import statsmodels.api as sm

df = pd.read_csv('/Users/tom/Dropbox/Economics/Econometrics/Homework/HW7/clean_LFP.csv')
endog = df['LFP']
exog = df[['cons', 'age', 'age_sq', 'income', 'education', 'kids']]

linear_model = sm.OLS(endog, exog)
probit_model = sm.Probit(endog, exog)
logit_model = sm.Logit(endog, exog)

linear_results = linear_model.fit()
probit_results = probit_model.fit()
logit_results = logit_model.fit()

# Part a
linear_results.params

probit_marg_eff = probit_results.get_margeff()
probit_marg_eff.margeff  # +.summary()

logit_marg_eff = logit_results.get_margeff()
logit_marg_eff.margeff  # +.summary()

# Part b
my_means = exog.mean()
my_means['age'] = ceil(my_means['age'])
my_means['age_sq'] = my_means['age'] ** 2

linear_results.predict(my_means)
logit_results.predict(my_means)

# Part c

