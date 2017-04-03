from datetime import datetime

numlist = []
for i in range( 10000 ):
    numlist.append( i )

start = datetime.now()
count = 0
for i in range( 10000, 20000 ):
    if i in numlist:
        count += 1
end = datetime.now()

print( "{}.{} seconds needed to find {} numbers".format( 
    (end - start).seconds, (end - start).microseconds,count ) )