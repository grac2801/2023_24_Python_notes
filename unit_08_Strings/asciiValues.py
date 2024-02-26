# Jan 17, 2024
# Author: ogracias


# imports





# functions




if __name__ == '__main__':
    x_int = 65
    x_str = 'C'
    print(x_str)
    print('C ascii value:', ord(x_str))
    
    print(chr(x_int))
    
    name = 'Oscar'
    for letter in range(len(name)):
        print(ord(name[letter]), end = ' ')
    
    
    print()
    
    numbers = [67, 87, 70, 100, 111]
    print('[', end ='')
    for number in range(len(numbers)):
        print(chr(numbers[number]), end = ' ')
    print(']')
    
    
    
    
    
