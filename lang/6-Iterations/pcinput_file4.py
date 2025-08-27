from pcinput import getInteger
from sys import exit

while True:
    x = getInteger( "Enter number 1: " )
    if x == 0:
        break
    y = getInteger( "Enter number 2: " )
    if y == 0:
        break
    if (x < 0 or x > 1000) or (y < 0 or y > 1000):
        print( "The numbers should be between 0 and 1000" )
        continue
    if x%y == 0 or y%x == 0:
        print( "Error: the numbers cannot be dividers" )
        exit()
    print( "Multiplication of", x, "and", y, "gives", x * y )

print( "Goodbye!" )