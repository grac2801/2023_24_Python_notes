# Jan 19, 2024
# Author: ogracias


# imports





# functions




if __name__ == '__main__':
    print('\n\n********** Starting with nested loops **********')
    for x in range(1, 11):# rows
        print(x, end = ': ')
        for y in range(1, 6): # columns
            print(y, end = ' ')
        print()
    
    print('\n\n********** better formatting for nested loops **********')
    for x in range(1, 11):
        print(f'{x:>2}', end =': ')
        for y in range(1, 6):
            print(f'{y:<2}', end='')
        print()
    
    print('\n\n********** user input for rows and columns **********')
    # rows = int(input('How many rows do you need? '))
    # cols = int(input('How many columns do you need? '))
    # symbol = input('What symbol do you wish to print? ')
    # print()
    #
    #
    # for a in range(rows):
    #     for b in range(cols):
    #         print(f'{symbol:<5}', end='')
    #     print()
    #

    
    print('\n\n********** Elements from the periodic table **********')
    outer = ['li', 'Na', 'K']
    inner = ['F', 'Cl', 'Br']
    
    for metal in outer:
        for non_metal in inner:
            print(metal + non_metal)
    
    #Alternative way to print by grouping
    for metal in outer:
        for non_metal in inner:
            print(f'{metal + non_metal:<6}', end = '')
        print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
