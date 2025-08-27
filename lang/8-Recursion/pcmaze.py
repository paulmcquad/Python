def connected( x, y ):
    if x > y:
        return connected( y, x )
    if (x,y) in ((1,5),(2,3),(3,7),(4,8),(5,6),(5,9),(6,7),(8,12),
        (9,10),(9,13),(10,11),(10,14),(11,12),(11,15),(15,16)):
        return True
    return False
    
def entrance():
    return 1
    
def exit():
    return 16