# Nov 3, 2023
# Author: ogracias


# imports
import time




# functions




if __name__ == '__main__':
    print('\n\n********** 1- rocket taking off **********')
    countdown = 3
    while(countdown > 0):
        print(countdown)
        time.sleep(1)
        countdown -= 1
        if(countdown == 0):
            print('Take off!!!')
            break
    print('Good luck explorers')
    
    
    
    print('\n\n********** 2- continue **********')
    startFloor = 8
    while(startFloor < 16):
        if(startFloor == 13):
            startFloor += 1
            continue
        print(f'Current floor: {startFloor}. Going to next')
        startFloor += 1
        time.sleep(2)
    else:
        print('you have reached the top of the building')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    











