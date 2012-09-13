## Filename npkde.py
## Based heavily on John Stachurski's work: http://johnstachurski.net/lectures/srs.html
import numpy as np

def g(x):
    return (1.0 / np.sqrt(2 * np.pi)) * np.exp(- 0.5 * x**2)
        
class NPKDE:
    
    def __init__(self, X = None, h = None, K = g):
        """
        Nonparametric kernel density estimator.
        
        Parameters:
            * X is a NumPy array holding the observations
            * h is a scaler
            * K is a vectorized callable that represents a density
        """
        self.X, self.h, self.K = X, h, K
        if self.h == None:
            # If bandwidth is not defined, default to Silverman's rule of thumb
            self.h = 1.06 * np.std(X) * len(X)**(-1.0 / 5)
            
    def __call__(self, x):
        return (1.0 / self.h) * np.mean(self.K((x - self.X) / self.h))