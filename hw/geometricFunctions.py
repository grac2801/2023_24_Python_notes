# Nov 13, 2023
# Author: 1553159


#imports
import geometricFiguresLibrary as lib



#functions




if __name__== '__main__': 
    print("\n\n********** Sovlving geometric functions **********")
   

    function = 0
    while function != 'stop':
        print('\nHere is a list of functions used to solve the area or perimeter of the shape, use [stop] to stop the loop')
        print('\n1. area of a triangle')
        print('2. area of a rectangle')
        print('3. area of a parallelogram')
        print('4. area of a trapezoid')
        print('5. area of a circle')
        print('6. perimeter of a parallelogram')
        print('7. perimeter of a triangle')
        print('8. perimeter of a rectangle')
        print('9. perimeter of a square')
        print('10. perimeter of a trapezoid')
        print('11. perimeter of a kite')
        print('12. perimeter of a rhombus')
        print('13. perimeter of a hexagon\n')
        function = input('\nWhich function number would you like to use?: ')
        if function == '1':
            lib.areaTriangle(0, 0)
        elif function == '2':
            lib.areaRectangle(0, 0)
        elif function == '3':
            lib.areaParallelogram(0, 0)
        elif function == '4':
            lib.areaTrapezoid(0, 0, 0)
        elif function == '5':
            lib.areaCircle(0)
        elif function == '6':
            lib.periParallelogram(0, 0)
        elif function == '7':
            lib.periTriangle(0, 0, 0)
        elif function == '8':
            lib.periRectangle(0, 0)
        elif function == '9':
            lib.periSquare(0)
        elif function == '10':
            lib.periTrapezoid(0, 0, 0, 0)
        elif function == '11':
            lib.periKite(0, 0)
        elif function == '12':
            lib.periRhombus(0)
        elif function == '13':
            lib.periHexagon(0)
        elif function == 'stop':
            break
        else:
            print('\nInvalid input try again.')