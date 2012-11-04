# using my_ols
from __future__ import division

import my_ols
import pandas as pd
import numpy as np

# Read in
df = pd.read_csv('/Users/tom/Dropbox/Economics/Econometrics/Homework/HW6/CleanGreenData.csv', index_col=0, parse_dates=True)
endog = df['log_gas_pp']
exog = df[['constant', 'log_income_pp', 'log_gas_p', 'log_new_car_p',
       'log_used_car_p']]

# Estimation
model = my_ols.my_ols(endog, exog, Y_varname='log_gas_pp', X_varnames=[
    'log_income_pp', 'log_gas_p', 'log_new_car_p',
    'log_used_car_p'], add_constant=False)

# Analysis
np.set_printoptions(precision=4, edgeitems=6, linewidth=100)

print '''
Ex-ante it's hard to say wheter the slope for new cars should be
positive or negative since we have these competing effects.  I would guess
that the price elasticity with respect to new cars would be negative due
to the increased age of the car fleet, and from that the decreased
average efficiency.
'''

for i, name in enumerate(model.X.columns):
    print 'The estimated coefficient for %s is: %r' % (name, model.b[i])

print '#' * 80
print '\n'

print 'The homoskedastic only variance esitmates are \n %r:' % model.cov_params.view()

print '#' * 80
print '\n'

print 'The heteroskedastic variance matrix is \n %r:' % model.white_cov

print '#' * 80
print '\n'

for i, name in enumerate(model.X.columns):
    print 'The robust t-statistics for %s is: %r' % (name, model.t_r[i])

print '#' * 80
print '\n'

for i, name in enumerate(model.X.columns):
    print 'The p-value for %s is: %r' % (name, model.p_value_r[i])
print '#' * 80
print '\n'

print 'The R**2 is %f' % model.R2

print '#' * 80
print '\n'

R = np.array([[0, 0, 0, 1, 0], [0, 0, 0, 0, 1]])
(f, p_value) = model.f_test(R)

print '#' * 80
print '\n'

print """
With an F-statistic of %f and a p-value of %f we can conclude that,
at the 10%% significance level, the new and used car price variables
are not stastically significant as a group.
""" % (f, p_value)
