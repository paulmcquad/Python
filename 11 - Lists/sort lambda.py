fruitlist = ["apple", "strawberry", "banana", "raspberry", 
    "cherry", "banana", "durian", "blueberry"]
fruitlist.sort( key=lambda x: (len(x),x) )
print( fruitlist )