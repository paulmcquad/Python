fruit = "orange"
print( fruit[1] )
print( fruit[2] )
print( fruit[3] )
print( fruit[-2] )
print( fruit[-6] )
print( fruit[0] )
print( fruit[-3] )

from math import sqrt
fruit = "orange"
x = 3
print( fruit[3-2] )
print( fruit[int( sqrt( 4 ) )] )
print( fruit [2**2] )
print( fruit[int( (x-len( fruit ))/3 )] )
print( fruit[-len( fruit )])
print( fruit[-x] )

fruit = "orange"
print( fruit[:] )
print( fruit[0:] )
print( fruit[:6] )
print( fruit [:100] )
print( fruit[:len( fruit )] )
print( fruit[1:-1] )
print( fruit[2], fruit [1:6] )
