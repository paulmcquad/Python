from datetime import datetime

numdict = {}
for i in range( 10000 ):
    numdict[i] = 1

start = datetime.now()
count = 0
for i in range( 10000, 20000 ):
    if i in numdict:
        count += 1
end = datetime.now()

print( "{}.{} seconds needed to find {} numbers".format( 
    (end - start).seconds, (end - start).microseconds,count ) )