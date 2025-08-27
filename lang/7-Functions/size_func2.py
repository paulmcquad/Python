num11, num12, num13 = 436, 178, 992
num21, num22, num23 = 880, 543, 101

def smallest_of_two( n1, n2 ):
    if n1 < n2:
        return n1
    return n2

def largest_of_two( n1, n2 ):
    if n1 > n2:
        return n1
    return n2

def smallest( n1, n2, n3 ):
    return smallest_of_two( smallest_of_two( n1, n2 ), n3 )

def middle( n1, n2, n3 ):
    return n1 # just return something for now

def largest( n1, n2, n3 ):
    return largest_of_two( largest_of_two( n1, n2 ), n3 )

print( "sum of smallest =", smallest( num11, num12, num13 ) + 
    smallest( num21, num22, num23 ) )
print( "sum of middle =", middle( num11, num12, num13 ) + 
    middle( num21, num22, num23 ) )
print( "sum of largest =", largest( num11, num12, num13 ) + 
    largest( num21, num22, num23 ) )