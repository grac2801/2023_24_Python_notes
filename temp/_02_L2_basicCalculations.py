'''
Created on Oct 10, 2023

@author: ogracias
'''
x = 37
y = 14;

# incorrect
# print('The answer is ' + x + y)

# correct
print('The answer is ' + str(x + y))


y = int(input('Enter an integer: '))
print('The answer is ' + str(x + y))

# = is not equality, but assignment
 
isItTrue = y == 88
print('Is it true or false? ', isItTrue)


print('\n\n********** Fahrenheit degrees **********')
# Convert 100 C to F.
c = float(input('Enter the Celsius degrees: '))
f = c * (9 / 5) + 32
print(c, 'degrees Celsius is =', f, 'degrees F')


#===============================================================================
# Have students convert from Fahrenheit to Celsius
#===============================================================================

'''
PEMDAS applies:
power, exponents, multiplication, division, addition, substraction from left to right.
'''


print('\n\n********** exponents **********')
num = int(input('Enter an integer value: '))
print('The square of num is ' + str(num * num))
print('The square of num is ' + str(num ** 2))
print('16 raised to the 0.5 power = ' + str(16 ** 0.5))
