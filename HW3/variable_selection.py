# Built in!

import pandas as pd
import statsmodels.api as sm
import numpy as np

## Filename: variable_selection
def variableSelection(dataFrame, exog):
    """
    Used to extract desired columns from a Pandas dataFrame.
    
    Parameters
    * dataFrame: pd.dataFrame containing the full set of data
    * exog: a list of the desired variables 
    
    
    Returns a pandas dataFrame with just the desired variables.
    """
    
    # Error check with exog in dataFrame.columns
    
    n = len(exog)
    out = np.empty(len(dataFrame))
    for i in range(n):
        out += dataFrame[exog[i]]
        
    out = pd.DataFrame(out)
