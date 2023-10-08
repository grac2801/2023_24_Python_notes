'''
Created on Oct 7, 2023

@author: mrgracias
'''
name = "Mr. Gracias"
print("Hello " + name) #concatenation
print("Hello" + " " + name)
print("Hello", name)
print("Hello " + "name") #concatenation

print('\n\n')
print("Hello \nWorld")

print("\"Everybody should learn how to program a computer,\nbecause it teaches you how to think.\" \n-Steve Jobs")

print('\n\n-----Important escape keys-----')
print("Escape keys \u2192 \\n, \\, \\t, \\\', \\\\")
print('A\tB\tC\nD\tE\tF')

print('\n\n-----Parameters for print command-----')
print('Hello', end='\n')
print('World')

result = 5 * 4 + 8
print('(' + str(result) + ')')
print(5 * 4 + 8)
print('5 * 4 + 8')

# Single comment

myComment = '''
This is my comment
    I want to make an indent
'''

print(myComment)

value = 5
print(6 * value)

print('\n\nSeparator')
print('Today', 'is', 'Monday')
print('Today', 'is', 'Monday', sep='$')



