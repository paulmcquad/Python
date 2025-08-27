s = " And now for something completely different \n "
print( "["+s+"]" )
s = s.strip()
print( "["+s+"]" )

s = "The Meaning of Life"
print( s )
print( s.upper() )
print( s.lower() )

s = "Humpty Dumpty sat on the wall"
print( s.find( "sat" ) )
print( s.find( "t" ) )
print( s.find( "t", 12 ) )
print( s.find( "q" ) )

s = ' Humpty Dumpty sat on the wall '
print( s.replace( ' sat on ' , ' fell off ' ) )

s = ' Humpty Dumpty sat on the wall '
wordlist = s.split()
for word in wordlist:
    print( word )

csv = "2016,September ,28,Data Processing ,Tilburg University"
values = csv.split( ' , ' )
for value in values:
    print( value )

s = "Humpty;Dumpty;sat;on;the;wall"
wordlist = s.split( ' ; ' )
s = " ".join( wordlist )
print( s )
