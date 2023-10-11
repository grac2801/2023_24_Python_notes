# imports
# import math
import math as m
import random as rand
import secrets as sec
# functions

if __name__ == '__main__':
    # number = float(input('What number do you want the square root of? '))
    # x = m.sqrt(number)
    # print(f'The square root of', number, 'is', x)
    
    
    gcd_item = m.gcd(12, 96)
    print('The gcd is: \u2192', gcd_item)
    
    print('\n\n********** random **********')
    print('random =', rand.random())
    
    #===========================================================================
    # Random value between 35 and 45
    #===========================================================================
    print('\n\n********** Random value between 35 and 45 **********')
    print(int(rand.random() * 11 + 35))
    
    
    print('\n\n********** randint **********')
    selectedInteger = rand.randint(1, 12)
    print('The selected value is:', selectedInteger)
    
    print('\n\n********** randrange **********')
    steps = rand.randrange(5, 21, 5)
    print('The selected multiple of 5 (from 5 .. 20) is:', steps)
    
    print('\n\n********** secrets **********')
    print('A random value from 0 thru 30 \u2192', sec.randbelow(5))
    
   
    
    