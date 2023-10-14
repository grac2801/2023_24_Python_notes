# Oct 10, 2023
# Author: mrgracias
from random import randint
from random import random as rand
from random import choice
import random




#imports



#functions



if __name__ == '__main__':
    
    print('\n\n********** Random() **********')
    # a number > 0 but < 1
    print('random:', rand())
    
    print('\n\n********** ranges **********')
    # A number between 10 and 25
    myNumber = int(rand() * 16) + 10
    print(myNumber)
    
    
    print('\n\n********** only evens between 1 and 100 **********')
    even = int((rand() * 50)  + 1 ) * 2
    print('even', even)
    
    print('\n\n********** randint() **********')
    print(randint(1, 5))
    
    print('\n\n********** randomize 1-10 (5 chances) **********')
    print(randint(1, 10))
    print(randint(1, 10))
    print(randint(1, 10))
    print(randint(1, 10))
    print(randint(1, 10))
    
    print('\n\n********** random() **********')
    print(rand())
    print(rand())
    print(rand())
    print(rand())
    print(rand())
    
    print('\n\n********** random.choice() **********')
    selection = choice(['Monday', 'Tuesday', 'Wednesday'])
    print(selection)
    
    
    print('\n\n********** Generate a unique password **********')
    '''
    A number from 1 - 100
    an animal
    another number from 1 - 10
    output = [randomValues]
    '''
    first = randint(1, 100)
    animal = choice(['lion', 'fish', 'zebra', 'octopus'])
    second = int(random.random() * 10 + 1)
    print('output = ' + str(first) + animal + str(second))
    
    
    
    