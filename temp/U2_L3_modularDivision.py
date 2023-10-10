# Oct 10, 2023
# Creator: ogracias


# imports




# functions





if __name__ == '__main__':
    print('\n\n********** modulus **********')
    print(10 % 3)
    print(23 % 7)
    print(4 % 6)
    
    # See video
    '''
    Conversion: time, length
    gameplay
    checking divisibility
    odd even
    '''
    
    for rounds in range(1, 100):
        turn = rounds % 4
        print("Round: ", rounds, 'Player:', turn)
        
        
    length = int(input('How many minutes long is the movie? '))
    hours = int(length / 60)
    minutes = int(length % 60)
    print('The movie is', hours, 'hours, and', minutes, 'minutes long.')
    
    #===========================================================================
    # What are the results?
    # 4 % 3
    # 16 % 4
    # 28 % 5
    # 7 % 0
    #===========================================================================
    