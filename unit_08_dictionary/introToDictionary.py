# Feb 5, 2024
# Author: ogracias


# imports





# functions




if __name__ == '__main__':
    print('\n\n********** 1.Declare a dictionary / Remove last item **********')
    capitals = {"UK":"London", "France": "Paris", "Germany":"Berlin"}
    print(capitals)
    return_value = capitals.popitem()
    print(return_value)
    print(capitals)
    
    print('\n\n********** 2. Copy key into variable, and print **********')
    UK_capital = capitals['UK']
    print(UK_capital)
    print('The length of my city is', len(UK_capital))
    
    
    print('\n\n********** 3.Add items to a dictionary **********')
    print(capitals)
    capitals['USA'] = 'Washington DC'
    print(capitals)
    
    print('\n\n********** 4.print keys from a dictionary **********')
    returned_keys = capitals.keys()
    print(returned_keys)
    
    
    print('\n\n********** 5. Make a dictionary into a list **********')
    capitals = {"UK":"London", "France": "Paris", "Germany":"Berlin"}
    
    capitals_list = list(capitals.keys())
    print(capitals_list)
    
    print('\n\n********** 6. values for keys **********')
    returned_values = capitals.values()
    print(returned_values)
    
    print('Getting values using a loop')
    for i in capitals.values():
        print(i)
    
    print('\n\n********** 7. Make values into a list **********')
    print(capitals)
    print(list(capitals.values()))
    print(capitals)
    
    print('\n\n********** 8.popitem() raises keyerror if empty **********')
    capitals = {'Mexico': 'Mexico city'}
    print(capitals)
    # modified_capitals = capitals.popitem()
    # print(capitals)
    # returned_value = capitals.popitem()
    
    
    print('\n\n********** 9. Errors **********')
    capitals = {"UK":"London", "France": "Paris", "Germany":"Berlin"}
    try:
        print(capitals['UK'])
        print(capitals['Spain'])
    except KeyError:
        print('This country is not in your list')
    
    
    print('\n\n********** 10. Now use get() method instead **********')
    capitals = {"UK":"London", "France": "Paris", "Germany":"Berlin"}
    print(capitals.get("UK"))
    print(capitals.get("Spain", 'Not found in dictionary'))
    
    
    print('\n\n********** 11.items() **********')
    capitals = {"UK":"London", "France": "Paris", "Germany":"Berlin"}
    print(capitals.items())
    capitals_list = list(capitals.items())
    print(capitals_list)
    
    print('\n\n********** 12.update a dictionary **********')
    capitals = {"UK":"London", "France": "Paris", "Germany":"Berlin"}
    more_capitals = {'Spain': "Madrid", 'USA': 'Washington DC'}
    # Add more_capitals to capitals
    capitals.update(more_capitals)
    print(capitals)
    
    
    print('\n\n********** 13. Copying a dictionary **********')
    car = {
            'Make': 'Ford',
            'model': 'Mustang',
            'year': 1964
            }
    copied_car = car.copy()
    print('car:', car)
    print('copied_car:', copied_car)
    copied_car['Make'] = 'Toyota'
    print('car:', car)
    print('copied_car:', copied_car)
    
    
    print('\n\n********** 14.Populate a dictionary **********')
    good_students = {
                        'Jason': 100,
                        'Mary':98,
                        'Luisa': 100
                    }
    # students with a grade of 0
    students = ['John', 'Johnie', 'Juan']
    bad_grade = 0
    
    
    #create a dictionary
    bad_students = dict.fromkeys(students, bad_grade)
    print(bad_students)
    
    print('\n\n********** 15. pop() **********')
    car = {
        'Make': 'Ford',
        'model': 'Mustang',
        'year': 1964
        }
    print(car)
    car.pop('model')
    print(car)
    
    
    print('\n\n********** 16.setdefault() **********')
    car = {
        'Make': 'Ford',
        'model': 'Mustang',
        'year': 1964
        }
    print(car.setdefault('year'))
    print(car)
    
    car.setdefault('tire model', '4XTMZW')
    print('Added tire model', car)
    
    
    
    print('\n\n********** 17a. 1st way to make a list into a dictionary **********')
    fruits = ['Apples', 'Pears', 'Peaches', 'Bananas']
    fruit_dictionary = dict.fromkeys(fruits, 'in stock')
    print(fruit_dictionary)
    
    print('\n\n********** 17b. second way to make list from dictionary **********')
    fruit_dictionary = {}
    fruits = ['Apples', 'Pears', 'Peaches', 'Bananas']
    for i in range(len(fruits)):
        fruit_dictionary = dict.fromkeys(fruits, 5.00)
    print(fruit_dictionary)
    
    
    print('\n\n********** 18.zip() **********')
    pants = ['jeans', 'casual', 'dress']
    prices = [45.98, 63.50, 89.25]
    pants_dictionary = dict(zip(pants, prices))
    print(pants_dictionary)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    