# Feb 12, 2024
# Author: ogracias


# imports





# functions




if __name__ == '__main__':
    print('\n\n********** 1.Empty tuple **********')
    empty_tuple = ()
    print(empty_tuple)
    
    print('\n\n********** 2.Make a tuple **********')
    friends = ('Rob', 'Mary', "Esther")
    print('friends:', friends)
    
    animals = 'dogs', 'lions', 'cats'
    print(animals)
    print(type(animals))
    
    myTuple = 5,
    print(myTuple)
    
    print('\n\n********** 3. Assign multiple values **********')
    trees = ('cedar', 'oak', 'lemon')
    #unpacking a tuple
    a, b, c = trees
    print(a)
    print(b)
    print(c)
    
    
    print('\n\n********** 4.swapping values **********')
    password = 'swordfish'
    ice_cream = 'chocolate'
    print('pw:', password, ',', 'ice_cream:', ice_cream)
    password, ice_cream = 'chocolate', 'swordfish'
    print('pw:', password, ',', 'ice_cream:', ice_cream)
    
    print('\n\n********** 5.Tuple function **********')
    my_list = ['one', 'two', 'three']
    my_tuple = tuple(my_list)
    print(my_tuple)
    
    
    #===========================================================================
    # Advantages
    # 1.Tuples use less space
    # 2.Can not be changed by error
    # 3.you can use tuples and dictionary keys
    # 4.can be passed as parameters in functions
    #===========================================================================
    print(my_tuple.index('two'))
    
    
    print('\n\n********** 6.For loop **********')
    my_tuple = ('Ram', 23, 10, 'Stephanie', 17, 'Alexa')
    myElement = 23
    for t in my_tuple:
        if t == myElement:
            print('Index found:', my_tuple.index(t))
            
            
            
    # print('\n\n********** 7. They can vary in size **********')
    # student_list = []
    # numStudents = int(input('How many students? '))
    # for i in range(numStudents):
    #     fn = input('First name: ')
    #     ln = input('Last name: ')
    #     idNum = int(input('Id number: '))
    #     student_tuple = (fn, ln, idNum)
    #     student_list.append(student_tuple)
    #     print('\n\n')
    # print(student_list)    
        

    print('\n\n********** 8.tuples to dictionary **********')
    tuple_fn = ('John', 'Mary', 'Francis')
    tuple_ln = 'Cooper', 'Armstrong', 'Peters'
    tuple_to_dictionary = dict(zip(tuple_fn, tuple_ln))
    print(tuple_to_dictionary)
    
    
    
    
    print('\n\n********** 9.tuples and indices **********')
    tuple_cities = 'San Jose', 'San Diego', 'San Francisco'
    print('The second city is:', tuple_cities[1])