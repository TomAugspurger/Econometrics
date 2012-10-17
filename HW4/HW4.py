""""
Python file for ECM Homework 4
Tom Augspurger
"""
from __future__ import division

import numpy as np
import scipy as sp
from scipy import linalg


cd ~/Economics/Econometrics/Homework/HW4

# Number 2/3

A1 =np.array([[4, 2],[2, 1]])
linalg.eig(A1)

linalg.eig(A1)[1]
linalg.eig(A1)[1][:,1]
linalg.eig(A1)[1][:,0]
v1 = linalg.eig(A1)[1][:,0]
v1 * A1
A1.dot(v1)
v1.dot(A1)
A2 = np.array([[4, -1, 1],[-1, 4, -1],[1, -1, 4]])
linalg.det(A2)
linalg.eig(A2)
eig = linalg.eig(A2)
eig[1][0].dot(eig[1][1])
eig[1][0].dot(eig[1][2])
eig[1][:,0].dot(eig[1][:,1])
eig[1][:,0].dot(eig[1][:,2])
eig[1][:,1].dot(eig[1][:,2])



# Number 4

B1 = np.array([[2, -2, 2, 1], 
               [-1, 3, 0, 3], 
               [0, 0, 4, -2], 
               [0, 0, 2, -1]])
B2 = np.array([[1, 0, -2],
               [0, 0, 0],
               [-2, 0, 4]])


B1_eig = linalg.eig(B1)
B2_eig = linalg.eig(B2)

# Part b
P1 = B1_eig[1]
linalg.inv(P1)
P1 = np.array([[-2, 1, 3, -3], [1, -1, 1, -2], [0, 0, 2, .5], [0, 0, 1, 1]])
linalg.inv(P1)

B2_eig[1].T.dot(B2).dot(B2_eig[1]) #Symmetric B2 so this forumula gives the diagonalized A2.


# Number 5
A = np.array([[2, 4, 3],
              [4, 8, 6],
              [3, 6, 4]])


# part b

             
