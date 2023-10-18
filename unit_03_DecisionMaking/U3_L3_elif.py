# Oct 18, 2023
#ogracias


# imports



# functions


if __name__ == '__main__':
    print('\n\n********** sequential if **********')
    print('------ If statements -----')
    '''
    pH level        Category
    0 - 4            Strong acid
    5 - 6            weak acid
    7                Neutral
    8 - 9            Weak base
    10 - 14          Strong base
    '''
    
    pH = float(input('Enter the pH level: '))
    if pH < 7:
        print('\nIt is acidic!')
        print('You should be careful with that!!')
    if pH > 7:
        print('\nIt is basic!')
    if pH == 7:
        print('\nIt is neutral!')
    
    
    print('\n\n********** grades **********')
    grade = float(input('Enter your percent grade: '))
    if grade > 90:
        print('You have an A')
    if grade > 80:
        print('You have a B')
    if grade > 70:
        print('You have a C')
    if grade > 60:
        print('You have a D')
    else:
        print('Sorry, you failed.')
    

    
    print('\n\n********** grades elif **********')
    grade = float(input('Enter your percent grade: '))
    if grade > 90:
        print('You have an A')
    elif grade > 80:
        print('You have a B')
    elif grade > 70:
        print('You have a C')
    elif grade > 60:
        print('You have a D')
    else:
        print('Sorry, you failed.')
    
    
    
    
    print('\n\n********** Nested if statement **********')
    value = float(input('Enter the pH level: '))
    if value > 0:
        if value < 7.0:
            print('It is acidic')
        elif value > 7.0 and value <= 14:
            print('It is basic')
        elif value == 7:
            print('It is neutral.')
    elif value > -10:
        print('You input a negative pH value, but > -10')
    else:
        print('Less than -10')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
