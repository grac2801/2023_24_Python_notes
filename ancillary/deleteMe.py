'''
Created on Jan 12, 2024

@author: ogracias
'''
a = 'A'

print(ord(a))

print(chr(65))

letters = ['a', 'b', 'c', 'd']
numbers = list()
for letter in letters:
    numbers.append(ord(letter))
print(numbers)