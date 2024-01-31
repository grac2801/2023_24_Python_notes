# Jan 31, 2024
# Author: ogracias


# imports





# functions
def addRows():
    rows = int(input('How many rows for your grid? '))
    for r in range(rows):
        grid.append([])

def addColumns():
    cols = int(input('How many columns for your grid? '))
    for r in range(len(grid)):
        for c in range(cols):
            value = int(input('What value to add at position ' + str(r) + ', ' + str(c) + '? '))
            grid[r].append(value)
    print()
    

def outputGrid():
    # print without brackets
    for row in grid:
        for col in row:
            print(f'{col:<3}', end='')
        print()
        
def swapCols():
    col1 = int(input('Which column do you want to swap? '))
    col2 = int(input('Which other column do you want to swap? '))
    for r in range(len(grid)):
        temp = grid[r][col1]
        grid[r][col1] = grid[r][col2]
        grid[r][col2] = temp
    print()
    for row in grid:
        for col in row:
            print(f'{col:<3}', end='')
        print()
    
if __name__ == '__main__':
    #abstraction
    grid = []
    addRows()
    addColumns()
    outputGrid()
    swapCols()
    
    
    
    
    
    
    
    
    
    
    
