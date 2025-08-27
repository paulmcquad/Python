courses = {
    '880254': { "name":"RS: Data Processing", "ects":3, 
        "students":{'u123456':8, 'u383213':7.5, 'u234178':6} }, 
    '822177': { "name":"Understanding Intelligence", "ects":6,
        "students":{'u123456':5, 'u223416':7, 'u234178':9} }, 
    '822164': { "name":"Computer Games", "ects":6,
        "students":{'u383213':6, 'u234178':4} } }

for c in courses:
    print( "{}: {} ({})".format( c, courses[c]["name"], 
        courses[c]["ects"] ) )
    for s in courses[c]["students"]:
        print( "{}: {}".format( s, courses[c]["students"][s] ) )
    print()