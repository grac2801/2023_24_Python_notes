# Oct 23, 2023
# ogracias


# imports
import math as m


# functions


if __name__ == '__main__':
    my_pi = m.pi
    print('\n\n********** older way **********')
    print("My value for pi is {}, Today is {}".format(my_pi, "Monday"))
    print("My value for pi is {0}, Today is {1}".format(my_pi, "Monday"))
    # Let's reverse the indices
    print("My value for pi is {1}, Today is {0}".format(my_pi, "Monday"))
    # f strings come to replace
    print(f"My value for pi is {my_pi}, Today is {'Monday'}")
    
    
    print('\n\n********** printing numbers **********')
    print(f'Using Numeric {my_pi}')
    print(f"|{my_pi:25}|")
    print(f"|{my_pi:<25}|")
    print(f"|{my_pi:>25}|")
    print(f"|{my_pi:^25}|")
    
    
    print('\n\n********** printing fillers **********')
    print(f"Using numeric {my_pi}")
    print(f"|{my_pi:*<25}|")
    print(f"|{my_pi:*>25}|")
    print(f"|{my_pi:*^25}|")
    
    print('\n\n********** data types **********')
    dataTypes = '''
    s\t\tString
    d\t\tinteger
    n\t\tNumber, same as d except it uses current locale 
    e\t\tExponent location
    f\t\tFixed point notation
    %\t\tPercentage. Multiplies by 100, displays f format
    '''
    print(dataTypes)
    
    print('\n\n********** f-string variables in use **********')
    my_pi = 1000
    print(f"Using numeric {my_pi}")
    print(f'This prints without formatting {my_pi}')
    print(f'This prints with formatting {my_pi:d}')
    print(f'This prints with formatting {my_pi:n}')
    print(f'This prints with formatting {my_pi:10d}')
    my_pi = m.pi
    print(f'This prints without formatting {my_pi}')
    print(f'This prints without formatting {my_pi:f}')
    print(f'This prints without formatting {my_pi:20f}')
    print(f'This prints without formatting {my_pi:e}')
    
    
    
    print('\n\n********** formatting for decimal numbers **********')
    print(f'This prints with 2 decimal places formatting {my_pi:.2f}')
    print(f'This prints with 2 decimal places formatting {my_pi:.3f}')
    
    

