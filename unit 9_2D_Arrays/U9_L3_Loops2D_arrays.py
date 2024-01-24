# Jan 22, 2024
# Author: ogracias


# imports





# functions




if __name__ == '__main__':
    print('\n\n********** 1.Single arrays **********')
    grades = [85, 82, 73, 91]
    for g in grades:
        print(g)
        
    print('\n\n********** 2.double array **********')
    grades = [
                [9, 8, 7, 8],
                [8, 7 ,7, 6],
                [9, 10, 8, 9]
             ]
    #print my array
    for row in grades:
        for col in row:
            print(col)
            
    #print in a matrix form, 4 spaces in width
    print('\n\n')
    for row in grades:
        for col in row:
            print(f'{col:<4}', end= "")
        print()    
    
    print('\n\n********** 3.counter variables **********')
    #This does not change the original values
    #count all A's
    grades = [[9, 8 , 7, 8], [8, 7, 7, 6], [9, 10, 8, 9]]
    counter = 0
    for row in grades:
        for col in row:
            if col >= 9:
                counter += 1
    print('The whole class got', counter, "A's")
    
    
    print('\n\n********** 4.change values in a matrix **********')
    grades = [[9, 8, 7, 8], [8, 7, 7, 6, 9, 6], [9, 10, 8, 9]]
    for row in range(len(grades)):
        for col in range(len(grades[row])):
            print(row, col, end='\t')
        print()
    
    print('\n\n********** 5.Change values in list by 1 **********')
    #Changes values
    for row in range(len(grades)):
        for col in range(len(grades[row])):
            grades[row][col] += 1
            
    #prints values   
    for r in grades:
        for c in r:
            print(f'{c:<4}', end ='')
        print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
