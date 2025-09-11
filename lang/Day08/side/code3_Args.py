# Functions that allows for inputs
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
# greet_with_name("Paul")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# Positional Arguments
greet_with("Jack Bauer", "Nowhere")
# Keyword Arguments
greet_with(name="Jack Bauer",location="Nowhere")