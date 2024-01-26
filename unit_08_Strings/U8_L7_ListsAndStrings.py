# Jan 12, 2024
# Author: ogracias


# imports





# functions




if __name__ == '__main__':
    month = "October"
    for i in range(len(month)):
        print(month[i], end='  ')
    
    print()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for i in range(len(weekdays)):
        print(weekdays[i])
        
    #remove the ending 'day' for every string in weekdays
    for i in range(len(weekdays)):
        print(weekdays[i].replace('day', ''))
    print('\n\n')
    
    
    #print the first letter for every day of the week
    for i in range(len(weekdays)):
        print(weekdays[i][0])
    
    #parallel processing
    name = ['Alice', 'Bob', 'Carl']
    color = ['blue', 'orange', 'red']
    age = [16, 15, 17]
    for i in range(len(name)):
        print(name[i] + ' is ' + str(age[i]) + " years old.")
        print('His/Her favorite color is: ' + color[i])
        print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
