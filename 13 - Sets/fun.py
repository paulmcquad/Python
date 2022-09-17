def union(A, B):
    _union = A.union(B)
    print(sorted(_union))

union({1, 2, 3, 4, 5, 6}, {4, 5, 6, 7, 8, 9, 0})

def difference(A, B):
    _difference = A.symmetric_difference(B)
    print(sorted(_difference))
 
difference({1,2,3,4,5}, {4,5,6,7,8})