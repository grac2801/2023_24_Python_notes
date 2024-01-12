# Nov 29, 2023
# Author: ogracias


# imports





# functions
def _1_capitalize(fn, ln):
    '''
    capitalize both first and last names for the customer
    str, str --> str, str
    example: michAEl --> Michael
    '''
    capitalized_fn = fn.capitalize()
    capitalized_ln = ln.capitalize()
    return capitalized_fn + ' ' + capitalized_ln



if __name__ == '__main__':
    #===========================================================================
    # Ways to ensure changes in strings
    #===========================================================================
    country = 'argentina'
    print(f'The country is: {country.capitalize()}')
    country = country.capitalize() #keep change --> save in variable
    print('after the function call:', country )
    
    
    print('\n\n********** 2.count() **********')
    phrase = 'I like fruits, cakes, and everything that is sweet!'
    print('How many i\'s do I have in the phrase? ')
    numTotal_i = phrase.count('i')
    print('I see', numTotal_i, 'letter i\'s in my phrase.')
    
    
    print('\n\n********** make use of my function **********')
    fn = input('What is your first name? ')
    ln = input('What is your last name? ')
    properName = _1_capitalize(fn, ln)
    print(properName)
    
    
    