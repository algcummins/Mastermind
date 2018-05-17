# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:51:44 2018

@author: Anthony
"""

from mastertools import gencode, goodplace, goodcolor

print('\n *** Codebreaking Mastermind Game ***\n' )
print('I have a code of 4 colours, each different. Each color is represented by a number 1-6, as there are 6 possible colors.')

sw = 'Y'

while sw == 'Y' or sw == 'YES' or sw == '': 
    code = gencode()
    cont = 'y'
            
    tries = 1
    place = 0
    color = 0
    
    while place != 4 and tries != 11:
        
        correct = False
        while not correct: # ensures the correct number of digits is entered
            print('Try #', tries)
            tempguess = input(str('Guess a 4 digit # with all digits between 1 & 6: '))
            guess = tempguess.replace(" ", "")
            if len(guess) == 4:
                correct = True
            else: 
                correct = False
               
        place = goodplace(code, guess)
        color = goodcolor(code, guess)
        
        if place == 4:
            print('Yes, the code is', code)
            win = True
        else:
            print('There is/are', place, 'correct number(s) in the correct position, and', color, ' correct number(s) in the incorrect position.')
            win = False
        tries += 1
          
    if win:
        print('Congratulations!')
    
    else: 
        print('You have lost. The code is', code)
    
    swtemp = input(str('Press Y or Enter to play again. Press any other key to quit : '))
    sw = swtemp.upper()




    
