# Jan 31, 2024
# Author: ogracias


# imports





# functions




if __name__ == '__main__':
    grid = []
    
    rows = int(input('How many rows for your grid? '))
    for r in range(rows):
        grid.append([])
    
    # print(grid)
    
    cols = int(input('How many columns for your grid? '))
    for r in range(len(grid)):
        for c in range(cols):
            value = int(input('What value to add at position ' + str(r) + ', ' + str(c) + '? '))
            grid[r].append(value)
    print()
    print(grid) #prints like a 2D list with brackets
    
    # print without brackets
    for row in grid:
        for col in row:
            print(f'{col:<3}', end='')
        print()
    
    
    
    
    
    
    
    
    
    
