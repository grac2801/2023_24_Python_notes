'''
Created on Oct 13, 2023

@author: ogracias
'''
# imports
import random


# functions


if __name__ == '__main__':
    print('\n\n********** random() **********')
    # a number >= 0 but < 1
    print('random() =', random.random())
    print('random() =', random.random())
    print('random() =', random.random())
    print('random() =', random.random())
    print('random() =', random.random())
    
    print('\n\n********** range **********')
    # number between 10 and 25 inclusive
    myNumber = int(random.random() * 16) + 10
    ''' 
    * value = range of possible values
    + value = starting point
    '''
    print('Random between 10 - 25:', myNumber)
    
    #===========================================================================
    # randomize an integer value between 1 and 100 that is always even
    #===========================================================================
    even = int((random.random() * 50) + 1) * 2;
    print('even:', even)
    
    print('\n\n********** randint() **********')
    print(random.randint(1, 5))
    
    print('\n\n********** randon.choice() **********')
    selection = random.choice(['Monday', 'Tuesday', 'Wednesday'])
    print('The selected day is:', selection)
    
    #===========================================================================
    # Randomize a password
    #===========================================================================
    '''
    a) A random number between 40 and 50 inclusive
    b) a random animal from a list of 5
    c) an even number between 10 and 20
    output as a password string.
    '''
    first = random.randint(40, 50)
    animal = random.choice(['lion', 'fish', 'zebra', 'octopus', 'cheetah'])
    second = int(random.random() * 5 + 5) * 2
    print('output = ' + str(first) + animal + str(second))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    