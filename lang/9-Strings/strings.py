s1 = "apple"
s2 = ' banana '
print( s1 )
print( s2 )
print( s1 + s2 )
print( 3 * s1 )
print( s2 * 3 )
print( 2 * s1 + 2 * s2 )


s1 = "orange"
s2 = "banana"
for letter in s1:
    if letter in s2:
        print( s1, "and", s2, "share the letter", letter )
