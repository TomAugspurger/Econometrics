import statsmodels.api as sm
import scipy as sp
import scipy.stats as ss
import pandas as pd
import csv
import numpy as np

"""
cd ~/Economics/Econometrics/Homework/HW3
"""

line = []
with open('line.csv', 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
        line.append(row)
        
line.pop(0)
line = pd.DataFrame(line)
line.columns = ['y1', 'y2']
line = sm.add_constant(line, prepend = True)
results = sm.GLM(line['y1'], exog = line[['const', 'y2']])
# http://statsmodels.sourceforge.net/stable/dev/generated/statsmodels.base.model.GenericLikelihoodModel.html
# http://statsmodels.sourceforge.net/stable/dev/generated/statsmodels.base.model.LikelihoodModel.fit.html

grid = np.linsapce(0.5, 1.5, num = 1000)

# logLike = lambda x: - x * sum(line[0])

###
# In R now

mydata = read.csv('/Users/tom/Desktop/line.csv')
mydata[c('y1', 'y2')]
