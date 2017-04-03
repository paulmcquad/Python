fruitlist = ["apple", "Strawberry", "banana", "raspberry", 
    "CHERRY", "banana", "durian", "blueberry"]
fruitlist.sort() 
print( fruitlist )
fruitlist.sort( key=str.lower ) # case-insensitive sort
print( fruitlist )