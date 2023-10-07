'''
Created on Sep 22, 2023

@author: ogracias
'''
# print('++++++++++ introduction to input ++++++++++')
# name = input('What is your name? ')
# print('Good morning. ' + name + " Nice to meet you.")


print('\n\n++++++++++ name and adjective ++++++++++')
name = input('What is your name? ')
adjective = input('Enter your adjective: ')
print('Hello ' + name +', Let\'s go to the zoo. The Panda bears' +
     ' are ' + adjective + ' today.')


print('\n\n++++++++++ name and adjective [Alternative]++++++++++')
print('Hello', name, ', Let\'s go to the zoo. The Panda bears',
     'are', adjective,'today.', sep=' ')


print('\n\n++++++++++ variable names ++++++++++')
print('''
1-They can use letters and numbers
2-They must start with a letter preferably lowercase
3-They can not start with a number
4-Use descriptive names
5-Use camel case (daysOfTheWeek) or snake method 
(days_of_the_week)
''')