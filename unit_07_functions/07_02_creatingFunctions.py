# Oct 30, 2023
# Author: ogracias


# imports
import random




# functions
def flipCoin():
    outcome = random.randint(0, 1)
    if outcome == 1:
        print('Heads')
    else:
        print('Tails')

def python():
    times = int(input('How many times do you wish to print the statement?'))
    for a in range(times):
        print('I \u2661 Python')

if __name__ == '__main__':
    print('This will print an imaginary coin')
    for i in range(5):
        flipCoin()
        
    print('\n\n********** Student activity **********')
    '''
    Create a function which will print: I love Python, using the
    unicode heart character. Ask the user how many times they
    wish to print the statement. Unicode value 2665 or 2661
    '''
    python()
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        