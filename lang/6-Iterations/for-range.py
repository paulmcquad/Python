for x in range( 10 ):
    print( x )

for x in range( 1, 11, 2 ):
    print( x )

for x in ( 10, 100, 1000, 10000 ):
    print( x )

for x in ("apple", "pear", "orange", "banana", "mango", "cherry"):
    print( x )

for i in range( 3 ):
    print( "Entering the outer loop for i =", i )
    for j in range( 3 ):
        print( " Entering the inner loop for j =", j )
        print( " (i,j) = ({},{})".format( i, j ) )
        print( " Leaving the inner loop for j =", j )
    print( "Leaving the outer loop for i =", i )
