import random

word_list = ["aardvark","baboon","camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"

print(placeholder)

guess = input("Guess a letter: ").lower()

display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)
