# Optional Arguments

#Q1
def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)

bar(1, 2)

#Q2
def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)

bar(toast='nah', spam=4, eggs=2)

#Q3 - Tuple
def q_test(*args):
    print(args)

q_test(1, 2, 3, 5)

#Q4
def q_test(*args):
    print(args)

q_test(1, 2, 3, 5)

#Q5
def all_aboard(a, *args, **kw):
    print(a, args, kw)

all_aboard(4, 7, 3, 0, x=10, y=64)