class Dog:
    def __init__(self):
        self.temperament = "loyal"

    def bark(self):
        print("Woof, woof!")


class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.is_a_good_boy = True

    def bark(self):
        super().bark()
        print("Greetings, good sir. How do you do?")

sparky = Labrador()
sparky.bark()