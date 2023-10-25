# October 25
# Class activity on loops

# imports
import random



# functions


if __name__ == '__main__':
    print('\n\n********** Case 1 **********')
    '''
    #1 which type of loop?
    Print python 10 times. One with a count variable
    or user input
    '''
    for i in range(1,11):
        print(i, ": Python")
    
    
    
    print('\n\n********** Case 2 **********')
    '''
    #2 prompt the user for 5 numbers, state when the number
    is divisible by 3. Show the total sum of these numbers at the end.
    '''
    sum = 0
    count = 0
    ans = 0
    while count < 5:
        count += 1
        ans = int(input("Enter a number: "))
        if (ans % 3) == 0:
            print('This number is divisible by 3.')
            sum += ans
    print('The sum of all numbers divisible by 3 is:', sum)
    
    print('\n\n********** Case 3 **********')
    '''
    #3 Have the user input a number > 100, and
    repeat until they do
    '''
    
    num = int(input('Enter a number < 100: '))
    while num < 100:
        num = int(input('Enter a number < 100: '))
    
    
    print('\n\n********** Case 4 **********')
    '''
    #4 user to enter in numbers and then average
    #them
    '''
    num = 0
    counter = 0
    sum = 0
    while(num != -1):
        num = int(input('Please enter an integer (-1 to end): '))
        if num != -1:
            counter += 1
            sum += num
    total = sum / counter
    print('Your average is:', total)
    
    
    
    print('\n\n********** Case 5 **********')
    '''
    Randomize 3 unicode symbols, 5 times. Show the name of the symbol
    ''' 
    c = 0
    
    thickArrow = '\u27A5'
    triangular_arrow = '\u27A4'
    anchor = '\u2693'
    while(c < 5):
        value = random.randint(0, 2)
        
        if(value == 0):
            print('arrow:', thickArrow)
            c += 1
        elif(value == 1):
            print('triangular arrow:', triangular_arrow)
            c += 1
        elif(value == 2):
            print('anchor:', anchor)
            c += 1
        

