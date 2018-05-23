# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:04:52 2018

@author: Anthony
"""
from Ballistics import catapult
#from math import pi
from mathtools import rad 
import numpy as np
from math import pi
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

S = pi*0.2376**2
L0 = 0.5 
m = 90.
phi = 0
phistop = rad(60)
Ke = 5000
R = 3.

#==============================================================================
yarray, xarray, tarray, Vxarray, Vyarray, Varray = catapult(R, phi, phistop, L0, Ke, m, S)
# plt.scatter(xarray, yarray)
# plt.show()

X1tot = []
Y1tot = []
X2tot = []
Y2tot = []
X3tot = []
Y3tot = []


for c in range (4000, 44000, 4000):
    yarray, xarray, tarray, Vxarray, Vyarray, Varray = catapult(R, phi, phistop, L0, Ke, m, S)
    Ke = c
    X1tot.append(xarray)
    Y1tot.append(yarray)
    
plt.subplot(131)    
#plt.figure()
for c in range(0, 10):
    plt.plot(X1tot[c], Y1tot[c])

plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.show()

Ke = 5000
########################
for c in range (0, 11, 1):
    yarray, xarray, tarray, Vxarray, Vyarray, Varray = catapult(R, phi, phistop, L0, Ke, m, S)
    L0 = c/10
    X2tot.append(xarray)
    Y2tot.append(yarray)

plt.subplot(132)    
#plt.figure()
for c in range(0, 11):
    plt.plot(X2tot[c], Y2tot[c])

plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.show()

L0 = 0.5
########################
for c in range (45, 95, 5):
    yarray, xarray, tarray, Vxarray, Vyarray, Varray = catapult(R, phi, phistop, L0, Ke, m, S)
    phistop = rad(c)
    X3tot.append(xarray)
    Y3tot.append(yarray)

plt.subplot(133)    
#plt.figure()
for c in range(0, 10):
    plt.plot(X3tot[c], Y3tot[c])

plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.show()



#==============================================================================
#==============================================================================
# 
# def helper_k(k):
#     yarray, xarray, tarray, Vxarray, Vyarray = catapult(R, phi, phistop, L0, k, m, S)
#     return xarray[-1] - 300

# k_sol = fsolve(helper_k, 10000)
# print(k_sol)
#==============================================================================

#==============================================================================
# def helper_L(L0):
#     return catapult(3., 0., rad(60.), L0, 30000, 90., S)[1][-1] - 300
#==============================================================================

#==============================================================================
# L0_sol = fsolve(helper_L, 0.1)
# print(L0_sol)
# 
#==============================================================================

#==============================================================================
# def helper_p(phi):
#     plt.plot(xarray[-1],,"b")
#     return catapult(3., 0., phi, .5, 30000, 90., S)[1][-1] -300
# 
# phistop_sol = fsolve(helper_p, 0.977)
# print(phistop_sol)
# 
# 
#==============================================================================

#==============================================================================
# xopt = [xarray[-1]]
# for Ke in range(5000, 36000, 1000):
#     catapult(R, phi, phistop, L0, Ke, m, S)
#     xfinal = xarray[-1]
#     xopt.append(xfinal)
# 
#==============================================================================





#==============================================================================
# thetaarray = np.degrees((np.arctan2(Vyarray, Vxarray)))
# plt.subplot(121)
# plt.plot(thetaarray, tarray)
# plt.show()
# 
#==============================================================================

