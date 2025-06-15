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

signs = [rock, paper, scissors]
user_choice = int(input("What do you choose? "
                    "Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choice = random.randint(0, 2)

if user_choice in range(0,3):
    print(signs[user_choice])
    print("Computer chose:")
    print(signs[computer_choice])
    if user_choice == computer_choice:
        print("It's a draw!")
    elif computer_choice == 2 and user_choice == 0:
        print("You won!")
    elif computer_choice == 0 and user_choice == 2:
        print("Computer won!")
    elif user_choice > computer_choice:
        print("You won!")
    else:
        print("Computer won!")
else:
    print("You typed an invalid number, you lose!")