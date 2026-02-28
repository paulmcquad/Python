# **kwargs: Many Keyword Arguments

def calculate(n, **kwargs):
    #print(kwargs)
    #print(kwargs["add"])

    for key, value in kwargs.items():
        print(f'{key} = {value}')

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(f'{n}')


calculate(2, add=3, multiply=5)

# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)