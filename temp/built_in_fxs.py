# imports
# import math
import math as m


# functions

if __name__ == '__main__':
    number = float(input('What number do you want the square root of? '))
    x = m.sqrt(number)
    print(f'The square root of', number, 'is', x)
    
    
    gcd_item = m.gcd(12, 96, 24, 48)
    print('The gcd is: \u2192', gcd_item)