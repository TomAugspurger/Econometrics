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

logLike = lambda x: - x * sum(line[0])
