# Oct 23, 2023
# ogracias


# imports
import random


# functions


if __name__ == '__main__':
    print(range(5))
    print(range(5, 10)) # Last value not inclusive
    print(range(0, 10, 2)) # Last value is a step
    
    print('\n\n********** Review and comparison while and for loops **********')
    # while
    count = 0
    while(count < 5):
        print('Hello')
        count += 1
    print('\n\n') 
    
      
    # for loop
    for i in range(5):
        print('Hello')


    print('\n\n********** print the i values **********')
    for i in range(5):
        print(i)
        
    print('\n\n')
    for i in range(1, 11):
        print(i)
        
    print('\n\n')
    for i in range(1, 4):
        print('Day', i, ':', 'Great day')
        
        
    print('\n\n********** student activity **********')
    print("Simulate the toss of 2 coins three times,\n" + \
      'and state how many times the sides were \n' + \
      'the same. Use both loops.')
    counter = 0
    n = int(input('How many coin tosses do you want? '))
    for i in range(1, n + 1):
        print('Toss #', i)
        coin_1 = random.randint(0, 1)
        print('coin_1:', coin_1)
        
        print('Toss #', i)
        coin_2 = random.randint(0, 1)
        print('coin_2:', coin_2)
        print()
        
        if(coin_1 == coin_2):
            counter += 1
    
        print('Coins were the same', counter, 'times')
    
    
    
    
    
    
    
    
    
    
    
    
    