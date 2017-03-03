from pcinput import getInteger

num = getInteger( "Enter a number: " )
total = 0
while num != 0:
    total += num
    num = getInteger( "Enter a number: " )
print( "Total is", total )
