from pcinput import getInteger
total = 0
count = 0
while count < 5:
    total += getInteger( "Please give a number: " )
    count += 1
print( "Total is", total )
