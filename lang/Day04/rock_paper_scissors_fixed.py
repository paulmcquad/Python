import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n")

computer_choice = random.randint(0, 2)
#print(f"Computer chose {computer_choice}")

user_choice = int(user_choice)
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose.")

game_images = [rock, paper, scissors]
if 0 <= user_choice <= 2:
    print("User chose:")
    print(game_images[user_choice])
    print("Computer chose:")
    print(game_images[computer_choice])

if user_choice == computer_choice:
    print("It's a draw.")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose.")
elif user_choice > computer_choice:
    print("You win!")
else:
    print("You lose.")
