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
        turn = round % 4
        print("Round: ", rounds, 'Player:', turn)
    