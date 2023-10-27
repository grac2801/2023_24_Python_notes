# Oct 23, 2023
# ogracias


# imports
import random


# functions


if __name__ == '__main__':
    print('\n\n********** While loop **********')
    num = 0 # declare and start value
    while num < 5: # iterate
        print('Hello')
        num += 1 # move forward
    print('Done')
    
    
    
    print('\n\n********** loop with a sentinel to stop **********')
    num = int(input('Enter a number, -1 to stop: '))
    while(num != -1):
        print('You entered:', num)
        num = int(input('Enter a number, -1 to stop: '))
    print('You entered -1. I stopped')
        
    
    
    print('\n\nTOPIC: --->', '  loops and strings')
    name = input('Enter a name: ')
    while name != 'Ada':
        print('Hmm... ' + name + ' is an interesting name.')
        name = input('Enter a name: ')
    print('Cool - That is my name too!')  
    
    print('\n\n********** randomizer **********')
    counter = 0
    
    while(counter < 10):
        number = random.randint(11, 20)
        print('number:', number)
        counter += 1
    
    
    
    
    
    