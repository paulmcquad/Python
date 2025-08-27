from pcmaze import entrance, exit, connected

def leads_to_exit( comingfrom, cell ):
    if cell == exit():
        return "{}".format( exit() )
    for i in range( entrance(), exit()+1 ):
        if i == comingfrom:
            continue
        if not connected( cell, i ):
            continue
        check = leads_to_exit( cell, i )
        if check != "":
            return "{} -> {}".format( cell, check )
    return ""

check = leads_to_exit( 0, entrance() )
if check != "":
    print( "Path found!", check )
else:
    print( "Path not found" )