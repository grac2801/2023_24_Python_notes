'''
Created on Oct 16, 2023

@author: ogracias
'''
# imports 


# functions



if __name__ == '__main__':
    print('\n\n********** simple ifs **********')
    value = int(input('Enter a number (integer): '))
    if value > 0:
        print('positive')
    print('Done')
    
    
    print('\n\n********** Another if example **********')
    sunny = False
    if sunny:
        print('I don\'t need an umbrella')
    if not sunny:
        print('I do need an umbrella')
        
        
    print('\n\n********** Odd or even **********')
    number = int(input('Enter a number (integer): '))
    # check if odd or even
    if number % 2 == 0:
        print(number, 'is even')
    if number % 2 == 1:
        print(number, 'is odd')
    if number % 2 == 0 or number % 3 == 0:
        print(number, 'is divisible by 2 or 3')
    if number % 2 == 0 and number % 3 == 0:
        print(number, 'is divisible by 2 and 3')
        
        
        
    print('\n\n********** syntax is grammar in coding **********')
    word = input('Enter the secret word: ')
    if word == 'python':
        print('correct')
        
    print('\n\n')
    print('==================================================')
    print('TOPIC: -->', 'relational operators' )
    print('==================================================')
    print('==', 'equal to')   
    print('!=', 'not equal to')   
    print('<', 'less than')   
    print('<=', 'less than or equal to')   
    print('>', 'greater than')   
    print('>=', 'greater than or equal to')  
    print('in', 'membership')    
        
    print('\n\n')
    print('==================================================')
    print('TOPIC: -->', 'student activity' )
    print('==================================================')
    print('write a program to input an int number and test whether')
    print('this number is even and if between 50 inclusive and 75 ')
    print('not inclusive')    
    value = int(input('Enter a number: '))
    if value % 2 == 0:
        print('Number is even')
    if value >= 50 and value < 75:
        print('Number is between 50 - 75 not inclusive')
    print('You entered', value)
        
        
        
        
        
        
        
        
        