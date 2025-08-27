def len_alphabetical( element ):
    return len( element ), element 

fruitlist = ["apple", "strawberry", "banana", "raspberry", 
    "cherry", "banana", "durian", "blueberry"]
fruitlist.sort( key=len_alphabetical )
print( fruitlist )