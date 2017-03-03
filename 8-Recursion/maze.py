from pcmaze import entrance, exit, connected

def leads_to_exit( comingfrom, cell ):
    if cell == exit():
        return True
    for i in range( entrance(), exit()+1 ):
        if i == comingfrom:
            continue
        if not connected( cell, i ):
            continue
        if leads_to_exit( cell, i ):
            print( cell, "->", i )
            return True
    return False

if leads_to_exit( 0, entrance() ):
    print( "Path found!" )
else:
    print( "Path not found" )