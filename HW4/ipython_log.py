# IPython log file

get_ipython().magic(u'cd ~/Economics/Econometrics/Homework/HW4')
get_ipython().magic(u'logstart')
import scipy as sp
import numpy as sp
from scipy import linalg
A1 =np.array([[4, 2],[2, 1]])
linalg.eig(A1)
np.linalg.eig(A1)
np.linalg.eig(A1) == linalg.eig(A1)
np.linalg.eig(A1).any(linalg.eig(A1))
np.linalg.eig(A1).any() == (linalg.eig(A1).any()
_
np.linalg.eig(A1).any() == linalg.eig(A1).any()
np.linalg.eig(A1).any() == linalg.eig(A1)
A2 = np.array([[4, -1, 1],[-1, 4, -1],[1, -1, 4]])
linalg.det(A2)
linalg.eig(A2)
np.linalg.eig(A2)
B1 = np.array([[2, -2, 2, 1], 
               [-1, 3, 0, 3], 
               [0, 0, 4, -2], 
               [0, 0, 2, -1]])
B2 = np.array([[1, 0, -2],
               [0, 0, 0],
               [-2, 0, 4]])
B1_eig = linalg.eig(B1)
B2_eig = linalg.eig(B2)
B1_eig
B2_eig
A1 =np.array([[4, 2],[2, 1]])
linalg.eig(A1)
A2
linalg.eig(A2)
x = linalg.eig(A2)[1]
x
x[:, 2]
x = x[:, 2]
s
x
x / x[0]
A2.dot(x)
A2.dot(x)/x[0]
l1 = linalg.eig(A1_
)
l1 = linalg.eig(A1)
l2 = linalg.eig(A2)
l1
l1[1]
l1[1][:, 0].dot(l1[1][:,1]
)
l2[1][:, 0].dot(l2[1][:,1]
)
np.linalg.matrix_rank(A2)
np.linalg.matrix_rank(A1)
sp.linalg.det(A1)
sp.linalg.det(A2)
l2
np.trace(A1)
np.trace(A@)
np.trace(A2)
sp.linalg.eig(A1.dot(A1))
A1.dot(A1)
A2.dot(A2)
sp.linalg.eig(_)
sp.linalg.inv(A1)
sp.linalg.inv(A2)
sp.linalg.eig(_)
exit()
