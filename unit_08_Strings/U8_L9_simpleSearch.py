# Jan 22, 2024
# Author: ogracias


# imports





# functions
def search(animals, value):
    indexFound = -1
    for i in range(len(animals)):
        if(animals[i] == value):
            indexFound = i
            return indexFound
    return indexFound

def searchNums(nums, value):
    index = -1
    for i in range(len(nums)):
        if(nums[i] == value):
            index = i
            return 'Number found at index:', index
    return 'number not found.'

if __name__ == '__main__':
    words = ['cat', 'dog', 'mouse', 'lizard', 'bird']
    animal = input('What animal are you looking for? ')
    index = search(words, animal)
    print('The value appears at index position:', index, 
          '[index -1 means not found!]')
    
    print('/n/n')
    integers = [5, 7, 23, 43, 56, 76]
    val = int(input('What number are you looking for? '))
    print(searchNums(integers, val))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
