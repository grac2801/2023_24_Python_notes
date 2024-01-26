# Jan 12, 2024
# Author: ogracias


# imports





# functions
def switch(position1, position2, rainbow2):
    temp = rainbow2[position1 - 1]
    rainbow2[position1 - 1] = rainbow2[position2 -1]
    rainbow2[position2 - 1] = temp
    


if __name__ == '__main__':
    rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    print(rainbow)
    choice1 = int(input('Select first element you want to switch: (1 - 7)'))
    choice2 = int(input('Select second element you want to switch: (1 - 7)'))
    switch(choice1, choice2, rainbow)
    print(rainbow)
    
    
    
    
    
