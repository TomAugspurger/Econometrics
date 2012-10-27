from __future__ import division

import pandas as pd
import numpy as np
import scipy as sp
import statsmodels.api as sm

# Read in
df = pd.read_csv('greenDataFormat.csv', index_col=0, parse_dates=True)
df.columns = ['gas', 'popn', 'gas_p', 'income', 'new_car_p',
            'used_car_p', 'ppt', 'pd', 'pn', 'ps']
df = df[['gas', 'popn', 'gas_p', 'income', 'new_car_p',
            'used_car_p']]
df = df[['gas', 'popn', 'gas_p', 'income', 'new_car_p', 'used_car_p']]
endog = np.log(df.gas / df.popn)
exog = pd.DataFrame(np.ones(len(df)))
exog.index = df.index
exog['log_income_pp'] = np.log(df.income / df.popn)
exog['log_gas_p'] = np.log(df.gas_p)
exog['log_new_car_p'] = np.log(df.new_car_p)
exog['log_used_car_p'] = np.log(df.used_car_p)

# With Statsmodels
model = sm.OLS(endog, exog)
results = model.fit()
results.HC0_se  # Need to call to get the matrix
results.cov_HC0  # Robust Standard Error Matrix
se = results.cov_params()  # Non-robust

results.rsquared

# Now by hand


def coeff_est(endog, exog):
    """
    Estimate the coefficients of the regression equation, b,
    using b = (X'X)^-1 * X'
    """
    Q = exog.T.dot(exog)
    A = sp.linalg.inv(Q).dot(exog.T)
    b = A.dot(endog)
    return b


def std_errors(endog, exog):
    """
    Non robust standard errors. V(b) = sigma^2 Q^-1, assuming
    homoskedasticity. ASG p. 167
    """
    n = len(endog)
    k = len(exog.columns)
    Q = exog.T.dot(exog)
    A = sp.linalg.inv(Q).dot(exog.T)
    N = exog.values.dot(A)
    M = np.eye(n) - N
    e = M.dot(endog)
    sigma_sq = e.T.dot(e) * (1 / (n - k))
    return (sigma_sq, sigma_sq * sp.linalg.inv(Q))

def r_squared(endog, exog):
    """
    """
    n = len(endog)
    Q = exog.T.dot(exog)
    A = sp.linalg.inv(Q).dot(exog.T)
    N = exog.values.dot(A)
    M = np.eye(n) - N
    e = M.dot(endog)

    num = e.T.dot(e)
    M0 = np.eye(n) - (1 / n) * np.ones([n, n])
    denom = endog.T.dot(M0).dot(endog)
    r_sqr = 1 - num / denom
    return r_sqr
