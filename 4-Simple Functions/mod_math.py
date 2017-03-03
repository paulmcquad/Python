import math
print( math.sqrt( 4 ) )

from math import sqrt
print( sqrt( 4 ) )

from math import sqrt as squareroot
print( squareroot( 4 ) )

from math import exp , log
print( "The value of e is approximately", exp( 1 ) )
e_sqr = exp( 2 )
print( "e squared is", e_sqr )
print( "which means that log(", e_sqr , ") is", log( e_sqr ) )
