import sys
import scipy as sp
import scipy.stats as ss
import scipy.optimize as sciOpt


def myMLEEstimate(myFunc, par, data):
    def lnL_av(x, par):
        N = len(x)
        lnL = 0
        for i in range(N):
            lnL += sp.log(myFunc(par, x[i]))
        return lnL/N
        
        objFunc = lambda s: -lnL_av(data, s)
        par_mle = sciOpt.fmin(objFunc, par, disp=0)
        return par_mle
