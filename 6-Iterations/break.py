i = 1
while i <= 1000000:
    num1 = int( "1" + str( i ) )
    num2 = int( str( i ) + "1" )
    if num2 == 3 * num1:
        break
    i += 1
print( num2 , "is three times", num1 )

for grade in ( 8, 7.5, 9, 6, 6, 6, 5.5, 7, 5, 8, 7, 7.5 ):
    if grade < 5.5:
        print( "The student fails!" )
        break
else:
    print( "The student passes!" )
