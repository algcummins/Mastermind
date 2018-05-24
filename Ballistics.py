# -*- coding: utf-8 -*-
"""
Created on Sun May 20 23:56:13 2018

@author: Anthony -
"""
from numpy import array
from math import pi, sin, cos, atan2
from mathtools import rad, deg, norm 

def catapult(R, phi, phistop, L0, Ke, m, S):
    
    ct = {'g': 9.80665, 'rho_air': 1.225, 'rho_stone': 1600, 'cd': 0.7}
    
    beta = rad((90-phi)/2)
    phidotdot = 0.
    phidot = 0.
    V = R*phidot
    
    t = 0.0
    dt = 0.0001  
    
    ttab = [t]
    Vtab = [V]

    Le = 2*R*sin(beta)
    Fe = Ke*(Le - L0)

    while phi < phistop and t < 100:
        t = t + dt
        
        beta = (pi/2 - phi)/2
        
        Le = 2*R*sin(beta)
        Fe = Ke*(Le - L0)
        
        phidotdot = Fe/(R*m)*cos(beta) - ct['g']*cos(phi)/R 
        phidot = phidot + phidotdot*dt 
        phi = phi + phidot*dt
        
        V = R*phidot
       
        ttab.append(t)
        Vtab.append(V)
    
#==============================================================================
#     print("\nSimulation Part 1 Complete: \n") 
#     print("Launch speed =", round(V,1), "m/s")
#==============================================================================
    
    Vx = V*cos(2*beta)
    Vy = V*sin(2*beta)
    V =  norm(Vx,Vy)
    D = ct['cd']*0.5*ct['rho_air']*V**2*S
    angle = atan2(-Vy, -Vx)
    Dx = D*cos(angle)
    Dy = D*sin(angle)
    
    y = R*sin(phi)
    ytab = [y]
    x = 0
    xtab = [x]
    Vtab = [V]
    Vxtab = [Vx]
    Vytab = [Vy]
    Vtab  = [V]

    while y > 0 and t < 100:
        t = t + dt 
        
        Fy = -m*ct['g'] + Dy
        Fx = Dx
        
        ay = Fy/m
        ax = Fx/m
        
        Vy = Vy + ay*dt
        Vx = Vx + ax*dt
        V = norm(Vx, Vy)
        
        y = y + Vy*dt
        x = x + Vx*dt
        
        ttab.append(t)
        ytab.append(y)
        xtab.append(x)
        Vtab.append(V)
        Vxtab.append(Vx)
        Vytab.append(Vy)
        Vtab.append(V)
        
    tarray = array(ttab)
    yarray = array(ytab)
    xarray = array(xtab)
    Vxarray = array(Vxtab)
    Vyarray = array(Vytab)
    Varray = array(Vtab)
#==============================================================================
#     print("\nSimulation Part 2 Complete: \n" )
#     print("Distance achieved =", round(x,1), "m\n")
#==============================================================================
    
    return(yarray, xarray, tarray, Vxarray, Vyarray, Varray)







    

    

    
    
