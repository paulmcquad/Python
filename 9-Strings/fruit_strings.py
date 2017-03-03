fruit = 'apple'

for i in range( 0, len( fruit ) ):
    print( fruit[i], "- ", end="" )
print()

i = 0
while i < len( fruit ):
    print( fruit[i], "- ", end="" )
    i += 1

fruit = "banana"
print( fruit [::2] )
print( fruit [1::2] )
print( fruit[::-1] )
print( fruit[::-2] )

fruit = "banana"
print( fruit[::-1] )
for i in range( 5, -1, -1 ):
    print( fruit[i] )

fruit = "oringe"
fruit = fruit[:2] + "a" + fruit[3:]
print( fruit )
