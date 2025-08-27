from pcmaze import entrance, exit, connected

def leads_to_exit( comingfrom, cell, depth ):
    indent = depth * 4 * " "
    if cell == exit():
        return True
    for i in range( entrance(), exit()+1 ):
        if i == comingfrom:
            continue
        if not connected( cell, i ):
            continue
        print( indent + "Check connection", cell, "->", i )
        if leads_to_exit( cell, i, depth + 1 ):
            print( indent + "Path found:", cell, "->", i )
            return True
    return False

if leads_to_exit( 0, entrance(), 0 ):
    print( "Path found!" )
else:
    print( "Path not found" )