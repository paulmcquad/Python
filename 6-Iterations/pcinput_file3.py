from pcinput import getInteger
x = 3
y = 7

while (x != 0) and (y != 0) and (x%y != 0) and (y%x != 0):
    x = getInteger( "Enter number 1: " )
    y = getInteger( "Enter number 2: " )
    if (x > 1000) or (y > 1000) or (x < 0) or (y < 0):
        print( "Numbers should both be between 0 and 1000" )
        continue
    print( "Multiplication of", x, "and", y, "gives", x * y )

if x == 0 or y == 0:
    print( "Goodbye!" )
else:
    print( "Error: the numbers cannot be dividers" )
