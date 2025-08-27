from pcinput import getInteger
from sys import exit

num = getInteger( "Please enter a positive integer: " )
if num < 0:
    print( "You should have entered a positive integer!" )
    exit()

print( "Now I am processing your integer", num )
print( "Lots and lots of processing" )
print( "Hundreds of lines of code here" )