'''
Created on Feb 23, 2024

@author: ogracias
'''
if __name__ == '__main__':
    #1-create a set
    empty_set = set()
    print('Empty set:', empty_set)
    even_numbers = {2, 4, 6, 8, 10}
    print(even_numbers)
    #sets are like dictionaries with no values
    
    #2- convert other data into sets
    letters = set('letters')
    print('letters:', letters)
    print('the length of letters:', len(letters))
    
    
    #3- make a set from a list
    reindeer_list = ['Dasher', 'Dancer', 'Prancer', 'Dancer']
    reindeer_set = set(reindeer_list)
    print('reindeer set', reindeer_set)
    
    
    #4- make a set from a tuple
    sea_animals = 'dolphin', 'tuna', 'whale', 'tuna'
    sea_animals_set = set(sea_animals)
    print(sea_animals_set)
    
    
    #5-Dictionary into set
    fruit_list = {'apples': 'red',
                  'orange': "orange",
                  'pear': 'green'
                  }
    fruits_set = set(fruit_list)
    print(fruits_set)
    
    #6. test for a value in a set
    animals = {'bipedal': {'humans', 'kangaroo'},
               'carnivore' : {'lion', 'pig'},
               'omnivore': {'humans', 'pig', 'chimpanzee'},
               'herbivore': {'pig', 'cow', 'deer', 'humans'},
               'quadripedal': {'dog', 'lion'},
               'smart': {'humans', 'whales', 'chimpanzee'}
               }
    print(animals)
    
    #which types have humans in them?
    counter = 0
    for types, creatures in animals.items():
        if 'humans' in creatures:
            counter += 1
            print(counter, ' - ', types)
    
    # which types have humans and either chimpanzees or kangaroos?
    for types, creatures in animals.items():
        if 'humans' in creatures and ('kangaroo' in creatures or 'chimpanzee' in creatures):
            print(types)
    
    
    # finds humans but not kangaroos?
    for types, creatures in animals.items():
        if 'humans' in creatures and ('kangaroo' not in creatures):
            print(types)
    
    
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '8. set operators')
    print('TOPIC: --->', '8a.intersection() or &')
    print('===============================================')
    set_a = {1, 2}
    set_b = {2, 3}
    print(set_a & set_b)  # only items in common
    print(set_a.intersection(set_b))
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '8b.union or |')
    print('===============================================')
    print(set_a.union(set_b))
    print(set_a | set_b)  # list all items in both
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '8c.difference or -')
    print('===============================================')
    print(set_a - set_b)  # member of first set but not second
    print(set_a.difference(set_b))
    print(set_b.difference(set_a))
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '8c.symmetric_difference or ^')
    print('Items in one set or the other, but not both')
    print('===============================================')
    print(set_a ^ set_b)
    print(set_a.symmetric_difference(set_b))
        
    print(animals['bipedal'].symmetric_difference(animals['omnivore']))

    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '8d.issubset() or <=')
    print('===============================================')
    set_a = {1, 2}
    set_b = {1, 2, 3}
    print('a subset of b?', set_a.issubset(set_b))
    
    # any set is a subset of itself
    print('set_a subset of itself?', set_a <= set_a)

    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '8e.issuperset() or >==')
    print('===============================================')
    set_a = {1, 2}
    set_b = {1, 2, 3}
    print('set_b >= set_a?', set_b >= set_a)
    
    print('\n\n')
    print('===============================================')
    print('TOPIC: --->', '9.Make bigger data structures')
    print('===============================================')
    marxes = ['Groucho', 'Chico', 'Harpo']
    pythons = ['Chapman', 'Cleese', 'Gillian', 'Jones', 'Palin']
    stooges = ['Moe', 'Curly', 'Larry']
    
    # Make a tuple that contains each list as an element
    tuple_of_lists = (marxes, pythons, stooges)
    print(tuple_of_lists)
    
    # Make a list that contains each list as an element
    list_of_lists = [marxes, pythons, stooges]
    print(list_of_lists)
    
    # Make a dictionary that contains each list as an element
    dict_of_lists = {'marxes': marxes, 'pythons': pythons, 'stooges':stooges}
    print(dict_of_lists)
    
    # only limitation: data types
    # dict key needs to be immutable --> so list, dict or set can't be
    # keys for dictionaries, but a tuple can be
    houses = {(44.79, -93, 285): 'My house',
           (34.56, 32.98, 87): 'Aunt\'s house'
        }
    print(houses)
    

    # You get add to a set
    numSet = {-5, 1, 2, 3, 4, 5}
    print(numSet)
    numSet.add(7)
    print(numSet)
    numSet.remove(3)
    print(numSet)
    removedItem = numSet.pop()
    print(removedItem)
    print(numSet)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    