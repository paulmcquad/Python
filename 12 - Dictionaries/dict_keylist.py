fruitbasket = { "apple":3, "banana":5, "cherry":50, "durian":0, "mango":2 }
keylist = list( fruitbasket.keys() )
keylist.sort()
for key in keylist:
    print( "{}:{}".format( key, fruitbasket[key] ) )