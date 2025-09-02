import random
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(random.choice(friends))

# 2nd Option
random_index = random.randint(0, 4)
print(friends[random_index])