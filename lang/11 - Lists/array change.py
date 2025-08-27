def changelist( x ):
    if len( x ) > 0:
        x[0] = "CHANGE!"

fruitlist = ["apple", "banana", "cherry", "durian"]
changelist( fruitlist )
print( fruitlist )