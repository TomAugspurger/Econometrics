from __future__ import division

from scipy import linalg, c_, diagonal, dot
from scipy import stats
import numpy as np


class my_ols:
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

        self.Q = dot(self.X.T, self.X)
        self.Q_inv = linalg.inv(self.X.T.dot(self.X))
        self.A = linalg.inv(self.Q).dot(self.X.T)

        try:
            self.N = self.X.values.dot(self.A)
        except:
            self.N = self.X.dot(self.A)

        self.M = np.eye(self.nobs) - self.N
        XY = dot(self.X.T, self.Y)
        self.b = dot(self.Q_inv, XY)

        self.df_e = self.nobs - self.ncoef
        self.df_r = self.ncoef - 1

        self.e = self.Y - dot(self.X, self.b)
        self.sse = dot(self.e, self.e) / self.df_e  # SSE
        self.se = np.sqrt(diagonal(self.sse * self.Q_inv))  # Non robust SE
        self.t = self.b / self.se

        # TODO: make this take optional arg for one-sided vs. default of 2
        self.p_value = (1 - stats.t.cdf(abs(self.t), self.df_e)) * 2
        self.R2 = 1 - self.e.var() / self.Y.var()
        self.R2adj = 1 - (1 - self.R2) * ((self.nobs - 1) / (self.nobs - self.ncoef))
        self.F = (self.R2 / self.df_r) / ((1 - self.R2) / self.df_e)
        self.F_p_value = 1 - stats.f.cdf(self.F, self.df_r, self.df_e)
        self.s_sq = self.e.T.dot(self.e) / (self.nobs - self.ncoef)  # Greene p161

    def f_test(self, R, q=None):
        if q == None:
            j = np.shape(R)[0]
            q = np.zeros(j)  # Careful w/ dim here.
            l = R.dot(self.b.T) - q
            m = linalg.inv(R.dot(self.s_sq * self.Q_inv).dot(R.T))
            r = (R.dot(self.b) - q).T
            F = (l.dot(m).dot(r) / j)
        else:
            j = np.shape(R)[0]
            l = R.dot(self.b.T) - q
            m = linalg.inv(R.dot(self.s_sq * self.Q_inv).dot(R.T))
            r = (R.dot(self.b) - q).T
            F = (l.dot(m).dot(r) / j)
        return F


if __name__ == '__main__':
    print 'hi'
