apple = "apple"
banana = "banana"
cherry = "cherry"
durian = "durian"

def printfruits_1():
    print( apple, banana )

def printfruits_2( apple ):
    banana = cherry
    print( apple, banana )

def printfruits_3( apple, banana ):
    cherry = "mango"
    banana = cherry
    print( apple, banana )

printfruits_1()
printfruits_2( cherry )
printfruits_3( cherry, durian )

print( "apple =", apple )
print( "banana =", banana )
print( "cherry =", cherry )
print( "durian =", durian )