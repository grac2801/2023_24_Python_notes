'''
Jan 29, 2024
ogracias
'''
#imports



#functions




if __name__ == '__main__':
    grid = []
    
    rows = int(input('How many rows for your grid? '))
    for r in range(rows):
        grid.append([])
    
    cols = int(input('How many columns for your grid? '))
    for r in range(len(grid)):
        for c in range(cols):
            value = input("What value to add at position " + str(r) + ', ' + str(c) + '? ')
            grid[r].append(value)
            
    print()
    for row in grid:
        for col in row:
            print(f'{col:<5}', end='')
        print()
