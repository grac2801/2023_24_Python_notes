# Oct 13, 2023
# Creator: ogracias


# imports




# functions





if __name__ == '__main__':
    print('\n\n********** simple if **********')
    language = input('What is your favorite programming language? ')
    if(language == 'Python'):
        print('I knew Python was your favorite.')
    print('Done')
    
    
    print('\n\n********** equality operators **********')
    notes = '''
    == equal to
    <= less than or equal to
    >= greater than or equal to
    !== not equal to
    '''
    print(notes)
    
    print('\n\n********** student exercise **********')
    #===========================================================================
    # prompt user to enter an integer
    # if integer is > 100, output so
    #===========================================================================
    number = int(input('Enter an integer: '))
    if number >= 100:
        print('Integer > 100')