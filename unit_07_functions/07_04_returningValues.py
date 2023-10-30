# Oct 30, 2023
# Author: ogracias


# imports
import random




# functions
def lower_method(str1):
    str1 = str1.lower()
    return str1
    
def random_card():
    card_total = 0
    num = random.randrange(1, 12)
    card_total += 1
    suites = ['hearts', 'spades', 'diamonds', 'clubs']
    suit = random.choice(suites)
    if num == 1:
        num = 'Ace'
    return str(num) + ' of ' + suit


if __name__ == '__main__':
    print('\n\n********** 1.lowercasing **********')
    word = 'UPPER'
    print(lower_method(word))
    
    
    print('\n\n********** 2.random card in a suit **********')
    numOfCards = int(input('How many cards do you need? '))
    for i in range(numOfCards):
        print(random_card())
    
    
    
    
    
    
    
    
    
    
    
