from math import sqrt

def euclideanDistance( x1, y1, x2, y2 ):

    def pythagoras_inside( a, b ):
        if a <= 0 or b <= 0:
            return -1
        return sqrt( a*a + b*b )

    return pythagoras_inside( abs( x1 - x2 ), abs( y1 - y2 ) )

print( euclideanDistance( 1, 1, 4, 5 ) )
# print( pythagoras_inside( 3, 4 ) )