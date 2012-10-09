# IPython log file

import numpy as np
from numpy import linalg
get_ipython().magic(u'cd ~/Economics/Econometrics/Homework/HW4')
get_ipython().magic(u'pwd ')
get_ipython().magic(u'logstart')
B1 = np.array([[2, -2, 2, 1], [-1, 3, 0, 3], [0, 0, 4, -2], [0, 0, 2, 01]])
B2 = np.array([[1, 0, -2], [0, 0, 0], [-2, 0, 4]])
B1_eig = linalg.eig(B1)
B2_eig = linalg.eig(B2)
B1 = np.array([[2, -2, 2, 1], 
              [-1, 3, 0, 3], 
              [0, 0, 4, -2], 
              [0, 0, 2, -1]])
B2 = np.array([[1, 0, -2],
              [0, 0, 0],
               [-2, 0, 4]])
B1_eig = linalg.eig(B1)
B2_eig = linalg.eig(B2)
B1_eig[0]
B1_eig
from __future__ import division
B2_eig
X = np.array([[-1, 3, -1], [-3, 5, -1], [-3, 3, 1]])
X
P = np.array([[1, 1, -1], [1, 1, 0], [1, 0, 3]])
P
A.dot(P)
X.dot(P_
X.dot(P)
X.dot(P)
linalg.inv(P).dot(X).dot(P)
linalg.eig(X)
linalg.eigh(X)
get_ipython().magic(u'pinfo linalg.eigh')
get_ipython().magic(u'pinfo linalg.eig')
X
P
linalg.eig(X)
A = np.array([[1, 2, 0], [0, 3, 0], [2, -4, 2]])
A
linalg.eig(A)
P = linalg.eig(A)[1]
P
linalg.inv(P).dot(A).dot(P)
B
A2
B1
B1_eig
.2582 * 2
.2582 * 3
P = B1_eig[1]
P
linalg.inv(P).dot(B1).dot(P)
linalg.inv(P).dot(B1).dot(P)
linalg.inv(P).dot(B1).dot(P).floor()
linalg.inv(P).dot(B1).dot(P)
linalg.inv(P)
print linalg.inv(P)
P
P2 = np.array([[-2, 1, 3, -3], [1, -1, 1, -2], [0, 0, 2, .5], [0, 0, 1, 1]])
P2
linalg.inv(P2).dot(B1).dot(P2)
linalg.inv(P2)
_.dot(B2).dot(P2)
_
linalg.inv(P2).dot(B2).dot(P2)
B2
linalg.inv(P2).dot(B1).dot(P2)
linalg.inv(P2)
_.dot(B1).dot(P2)
_.dot(B1).dot(P2)
linalg.inv(P2).dot(B1).dot(P2) == 0
B2_eig
A2
B
A
B1
B2
B2_eig
B2_eig[1]
B2_eig[1].dot(B2)
B2_eig[1].T.dot(B2).dotB2_eig[1]
B2_eig[1].T.dot(B2).dot(B2_eig[1])
A
A = A = np.array([
             [2, 4, 3]
             [4, 8, 6]
             [3, 6, 5]])
A = np.array([
             [2, 4, 3]
             [4, 8, 6]
             [3, 6, 5]])
get_ipython().magic(u'paste')
A = np.array([
             [2, 4, 3]
             [4, 8, 6]
             [3, 6, 5]])

A = np.array([
             [2, 4, 3],
             [4, 8, 6],
             [3, 6, 5]])
A
linalg.eig(A)
A
