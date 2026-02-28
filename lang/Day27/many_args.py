# Many Arguments

def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(3, 5, 6))
print(add(2, 1, 4, 5, 5))
