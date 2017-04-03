courses = {
    '880254':['u123456', 'u383213', 'u234178'], 
    '822177':['u123456', 'u223416', 'u234178'], 
    '822164':['u123456', 'u223416', 'u383213', 'u234178']}

for c in courses:
    print( c )
    for s in courses[c]:
        print( s, end=" " )
    print()