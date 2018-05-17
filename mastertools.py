# -*- coding: utf-8 -*-
"""
Created on Wed May 16 22:56:40 2018

@author: Anthony
"""

import random 


def gencode():
    codeint = random.sample(range(1,6),4) #selects 4 different numbers
    codestr = [str(i) for i in codeint]
    global code 
    code = ''.join(codestr)
 #   print(code)
    return code


def goodplace(code, guess):
    global placetotal
    placetotal = 0
    for i in range(4):
        if guess[i] == code[i]:
            placetotal += 1
    return placetotal

    
def goodcolor(code, guess):
    temptotal = 0 
    for color in guess:
            if color in code:
                temptotal += 1
    colortotal = temptotal - placetotal
    return colortotal 





