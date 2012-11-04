from __future__ import division

from scipy import linalg, c_, diagonal, dot
from scipy import stats
import numpy as np


class my_ols:
    """
    Class used for eistimating OLS.

    Parameters
    * Y: column vector containing the n observations of the dependent variable.
    * X: the n x k matrix containing observed values for independent variables.
    * Y_varname: For ease. A string.
    * X_varnames: likewise. A string.
    * add_constant: Bool, default True.  If false adds a col vector of 1's.

    Attributes
    nobs: number of observations
    ncoef: number of coefficients (includes the constant)
    Q_inv: (X'X)^-1
    A: Q_inv * X'
    N: XA
    M: I - N; Residual maker
    b: Q^(-1)XY; Estimate of coefficients.
    df_e: Degrees of freedom for the regression. n - # coeffs.
    df_r: # coeffs - 1
    e: residuals. y - y-hat
    sse: sum of square errors.
    se: standard error of regrssion (estimate)
    t: b / se
    p_value: using student's t. Two sided
    cov_params: Homoskedastic only cov matrix. sse * Q^(-1)
    white_cov: White covariance matrix.  Use X'e*eX as an estimate
        for sigma, the true covarance.
        (X'X)^(-1)X'e**2X(X'X)^(-1).  e**2 is an (n x n) matrix with
        nonzeros e**2 on the main diagonal, zero off-diagonal.
    

    """

    def __init__(self, Y, X, Y_varname='Y', X_varnames='', add_constant=True):
        self.Y = Y
        if add_constant == True:
            self.X = c_[np.ones(X.shape[0]), X]
        else:
            self.X = X
        self.Y_varname = Y_varname
        if not isinstance(X_varnames, list):
            self.X_varnames = ['const'] + list(X_varnames)
        else:
            self.X_varnames = ['const'] + X_varnames

        self.estimate()

    def estimate(self):
        self.nobs = self.Y.shape[0]
        self.ncoef = self.X.shape[1]

        self.Q_inv = linalg.inv(self.X.T.dot(self.X))
        self.A = dot(self.Q_inv, self.X.T)

        try:
            self.N = dot(self.X, self.A)
        except:
            self.N = dot(self.X.values, self.A)

        self.M = np.eye(self.nobs) - self.N
        XY = dot(self.X.T, self.Y)
        self.b = dot(self.Q_inv, XY)

        self.df_e = self.nobs - self.ncoef
        self.df_r = self.ncoef - 1

        self.e = self.Y - dot(self.X, self.b)
        self.sse = dot(self.e, self.e) / self.df_e  # SSE
        self.se = np.sqrt(diagonal(self.sse * self.Q_inv))  # Non robust SE

        self.t = self.b / self.se
        self.p_value = (1 - stats.t.cdf(abs(self.t),   self.df_e)) * 2

        self.cov_params = self.sse * self.Q_inv
        self.white_cov = dot(dot(dot(dot(self.Q_inv,
            self.X.T),
            self.e.values ** 2 * np.eye(self.nobs)),
            self.X),
            self.Q_inv)

        self.t_r = self.b / self.white_cov.diagonal()
        self.p_value_r = (1 - stats.t.cdf(abs(self.t_r), self.df_e)) * 2

        # TODO: make this take optional arg for one-sided vs. default of 2
        self.R2 = 1 - self.e.var() / self.Y.var()
        self.R2adj = 1 - (1 - self.R2) * ((self.nobs - 1) / (self.nobs - self.ncoef))
        self.F = (self.R2 / self.df_r) / ((1 - self.R2) / self.df_e)
        self.F_p_value = 1 - stats.f.cdf(self.F, self.df_r, self.df_e)
        self.s_sq = self.e.T.dot(self.e) / (self.nobs - self.ncoef)  # Greene p161

    def f_test(self, R, q=None):
        """
        Pass the model (self), a restriction matrix, and the hypothesized value.  The if/else
        is for testing more general restrictions then just e.g. b1 = b2 = 0self.
        """

        if q == None:
            j = np.shape(R)[0]
            q = np.zeros(j)  # Careful w/ dim here.
            self.l = R.dot(self.b.T) - q
            self.m = linalg.inv(R.dot(self.s_sq * self.Q_inv).dot(R.T))
            self.r = (R.dot(self.b) - q).T
            self.F = (self.l.dot(self.m).dot(self.r) / j)
            self.F_p_value = 1 - stats.f.cdf(self.F, j, self.nobs - self.ncoef)
        else:
            j = np.shape(R)[0]
            self.l = R.dot(self.b.T) - q
            self.m = linalg.inv(R.dot(self.s_sq * self.Q_inv).dot(R.T))
            self.r = (R.dot(self.b) - q).T
            self.F = (self.l.dot(self.m).dot(self.r) / j)
            self.F_p_value = 1 - stats.f.cdf(self.F, j, self.nobs - self.ncoef)
        return (self.F, self.F_p_value)


if __name__ == '__main__':
    print 'Phil rules.'
