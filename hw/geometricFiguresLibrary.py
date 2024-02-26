# Nov 13, 2023
# Author: 1553159


#imports
import math as m




#functions
#=========================================================================================
# Area of a geometric shape
#========================================================================================= 
def areaTriangle(b, h):
    b = int(input('Enter the base of the triangle: '))
    h = int(input('Enter the height of the triangle: '))
    area = (b * h) / 2
    print('The area of the triangle is: ', area)
  
def areaRectangle(l, w):
    l = int(input('Enter the length of the rectangle: '))
    w = int(input('Enter the width of the rectangle: '))
    area = l * w
    print(f'The area of the triangle is: {area}')

def areaParallelogram(b, h):
    b = int(input('Enter the base of the Parallelogram: '))
    h = int(input('Enter the height of the parallelogram'))
    area = b * h
    print(f'The area of the parallelogram is: {area}')
    
def areaTrapezoid(bone, btwo, h):
    bone = int(input('Enter the base of the trapezoid: '))
    btwo = int(input('Enter the top base of the trapezoid'))
    h = int(input('Enter the height of the trapezoid: '))
    area = ((bone + btwo)/ 2) * h
    print(f'The area of the trapezoid is: {area}')

def areaCircle(r):
    r = int(input('Enter the radius of the circle: '))
    area = m.pi * r**2
    print(f'The area of the circle is about: {area}')

#=========================================================================================
# Perimeter of a geometric shape
#========================================================================================= 

def periParallelogram(b, h):
    b = int(input('Enter the base of the parallelogram: '))
    h = int(input('Enter the height of the parallelogram: '))
    perimeter = 2 * (b + h)
    print(f'The perimeter of the parallelogram is: {perimeter}')
    
def periTriangle(a, b, c):
    a = int(input('Enter side a of the triangle: '))
    b = int(input('Enter side b of the triangle: '))
    c = int(input('Enter side c of the triangle: '))
    perimeter = a + b + c
    print(f'The perimeter of the triangle is: {perimeter}')
    
def periRectangle(l, w):
    l = int(input('Enter the length of the rectangle: '))
    w = int(input('Enter the width of the rectangle:'))
    perimeter = 2 * (l + w)
    print(f'The perimeter of the rectangle is: {perimeter}')
    
def periSquare(a): 
    a = int(input('Enter the side of the square: '))
    perimeter = 4 * a
    print(f'The perimeter of the square is: {perimeter}')
    
def periTrapezoid(a, b, c, d):
    a = int(input('Enter side a of the trapezoid: '))
    b = int(input('Enter side b of the trapezoid: '))
    c = int(input('Enter side c of the trapezoid: '))
    d = int(input('Enter side d of the trapezoid: '))
    perimeter = a + b + c + d
    print(f'The perimeter of the trapezoid is: {perimeter}')

def periKite(a, b):
    a = int(input('Enter the side a of the kite: '))
    b = int(input('Enter the side b of the kite: '))
    perimeter = (2 * a) + (2 * b)
    print(f'The perimeter of the kite is: {perimeter}')
    
def periRhombus(a):
    a = int(input('Enter the side of the rhombus'))
    perimeter = 4 * a
    print(f'The perimeter of the rhombus is: {perimeter}')

def periHexagon(a):
    a = int(input('Enter the side of the Hexagon: '))
    perimeter = 6 * a
    print(f'The perimeter of a hexagon is: {perimeter}')


if __name__== '__main__': 
    print("\n\n********** Geometric Figures **********")
    periParallelogram(0, 0)
    