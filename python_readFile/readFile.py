# Feb 12, 2024
# Author: ogracias


# imports





# functions




if __name__ == '__main__':
    print('\n\n********** 1.Not preferred way **********')
    file = open('text_files//planets.txt', 'r')
    contents = file.read()
    file.close()
    print(contents)
    
    print('\n\n********** 1a. out of directory **********')
    file = open('..//planets2.txt', 'r')
    contents = file.read()
    file.close()
    print('planets2:', contents)


    print('\n\n********** 2.Using context editor **********')
    with open('text_files//planets.txt', 'r') as file:
        contents = file.read()
    print('#2:', contents)


    print('\n\n********** 3.partial read **********')
    with open('text_files//planets.txt', 'r') as file:
        partial = file.read(30)
        print(partial)


    print('\n\n********** 4. read only one line **********')
    with open('text_files//planets.txt', 'r') as file:
        print('Read only one line:', file.readline())
        
    print('\n\n********** 5.Using for loop **********')
    with open('text_files//planets.txt', 'r') as file:
        for line in file:
            line = line.strip()
            print(line)

    print('\n\n********** 6.read and place into list **********')
    with open('text_files//planets.txt', 'r') as file:
        my_list = file.readlines()
        for line in range(len(my_list)):
            my_list[line] = my_list[line].strip()
    print(my_list)
        
        
        
        
    