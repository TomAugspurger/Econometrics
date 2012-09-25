import statsmodels.api as sm
import scipy as sp
import scipy.stats as ss
import pandas as pd
import csv
import numpy as np

def str2float(list, out):
    for i in range(1, len(list)):
        for j in range(0, len(line[0])):
            out.append(float(line[i][j]))

def loglike4(x, theta):
    np.sum(np.log(theta * x[i] + 1) / (theta**3))

def loglike2(x, theta):
    np.log(theta * x + 1) / (theta **3)

def fun(x, theta):
    if x[0] > x[1]:
        return 0
    else:
        return np.exp(-theta * x[0])

def loglike3(x, theta):
    return - theta * np.sum(x)
    
def like(y1, y2, theta):
    if y1 < y2:
        return 0
    else:
        return np.exp(-theta * y1)
    


"""
cd ~/Economics/Econometrics/Homework/HW3
"""

line = []
with open('line.csv', 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
        line.append(row)

line.pop(0)
data = pd.DataFrame(line).astype('float')

# str2float(line, data)
# data = np.array(data)
# data = data.reshape([100, 2])



# # http://statsmodels.sourceforge.net/stable/dev/generated/statsmodels.base.model.GenericLikelihoodModel.html
# # http://statsmodels.sourceforge.net/stable/dev/generated/statsmodels.base.model.LikelihoodModel.fit.html
# 
# grid = np.linsapce(0.5, 1.5, num = 1000)
# 
# # logLike = lambda x: - x * sum(line[0])
# 
# ###
# # In R now
# 
# mydata = read.csv('/Users/tom/Desktop/line.csv')
# mydata[c('y1', 'y2')]
