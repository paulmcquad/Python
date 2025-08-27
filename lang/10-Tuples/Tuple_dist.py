from math import sqrt

# Returns the distance between two points in 2-dimensional space.
# The points are the parameters of the function; each point is a 
# tuple of two numeric values.
def distance( p1, p2 ):
    return sqrt( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 )

point1 = (1,2)
point2 = (5,5)
print( "Distance between", point1, "and", point2, "is", 
    distance( point1, point2 ) )