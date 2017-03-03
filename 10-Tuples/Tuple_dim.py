from math import sqrt

# Distance between two points in N-dimensional space.
# The points should have the same dimension, i.e., they are tuples 
# of numeric values, and they should have the same length.
def distance( p1, p2 ):
    total = 0
    for i in range( len( p1 ) ):
        total += (p1[i] - p2[i])**2
    return sqrt( total )

# 1-dimensional space
point1 = (1,)
point2 = (5,)
print( "1D: Distance between", point1, "and", point2, "is", 
    distance( point1, point2 ) )

# 2-dimensional space
point1 = (1,2)
point2 = (5,5)
print( "2D: Distance between", point1, "and", point2, "is", 
    distance( point1, point2 ) )

# 3-dimensional space
point1 = (1,2,4)
point2 = (5,5,8)
print( "3D: Distance between", point1, "and", point2, "is", 
    distance( point1, point2 ) )