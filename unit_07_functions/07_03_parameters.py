# Oct 30, 2023
# Author: ogracias


# imports





# functions
#n is a parameter and a copy of the value passed
def name0(n):
    print('Nice to meet you', n)

def name1(fn, ln, age):
    print('Nice to meet you', fn)
    print(ln, 'is a nice last name!')
    if(age >= 21):
        print('You are old enough to vote.')
    else:
        print('You are not old enough to vote.')

def calculate(x, y):
    operation = input('What operation do you want? ')
    if operation == '+':
        print('x + y:', x + y)
    elif operation == '-':
        print('x - y:', x - y)
    elif operation == '*':
        print('x * y:', x * y)
    elif operation == '/':
        print('x / y:', (float)(x / y))
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    # name0('Mr. G')
    #
    # name1('Oscar','Gracias', 52)
    #
    # firstName = input('Enter your first name: ')
    # lastName = input('Enter your last name: ')
    # yourAge = int(input('Enter your age: '))
    #
    # name1(firstName, lastName, yourAge)
    calculate(2, 5)
    
    
    #===========================================================================
    # create a calculator function which solves for +, -, *, /
    #===========================================================================








