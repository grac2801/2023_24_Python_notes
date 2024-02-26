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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    