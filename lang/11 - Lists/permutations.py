triplelist = [ (x,y,z) for x in range( 1, 5 ) 
    for y in range( 1, 5 ) for z in range( 1, 5 ) 
    if x != y if x != z if y != z]
print( triplelist )