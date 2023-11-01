# Nov 1, 2023
# Author: ogracias


# imports
import math




# functions
def main():
    a = int(input('Enter value for a: '))
    b = int(input('Enter value for b: '))
    c = int(input('Enter value for c: '))
    solution_1(a, b, c)
    solution_2(a, b, c)


def solution_1(a, b, c):
    total1 = part1(b)
    total2 = part2(a, b, c)
    total3 = part3(a)
    sol1 = (total1 + total2)/ total3
    print('The first solution (+) is', sol1)
    
    
def solution_2(a, b, c):
    total1 = part1(b)
    total2 = part2(a, b, c)
    total3 = part3(a)
    sol2 = (total1 - total2)/ total3
    print('The second solution (-) is', sol2)

def part1(b):
    return -(b)

def part2(a, b, c):
    b_squared = math.pow(b, 2)
    four_ac = 4 * a * c
    total = math.sqrt(b_squared - four_ac)
    return total

def part3(a):
    return 2 * a



if __name__ == '__main__':
    main() #3, 7, 2
