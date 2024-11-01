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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors: \n "))
user_image = ([rock, paper, scissors])
print(f"Your choice:{user_image[user_choice]}")

computer_choice = random.randint(0,2)
computer = [rock, paper, scissors]
print(f"Computer choice: {computer[computer_choice]}")


if user_choice == computer_choice:
    print("It's a tie.")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print ("You win!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("You lose!")


