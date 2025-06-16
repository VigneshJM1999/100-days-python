import random
from art import logo

EASY_MODE = 10
HARD_MODE = 5

def guess_number(lives, number):
    while lives > 0:
        print(f"You have {lives} attempts to guess the number between 1 & 100.")
        user_guess = int(input("Type in your guess: "))
        if user_guess == number:
            print(f"You guessed it right! The number is {number}!")
            return
        else:
            if user_guess > number:
                print("The guess is too high!")
            else:
                print("The guess is too low!")
            lives -= 1

    print("You've run out of guesses. Restart the program to play again.")
    return

chosen_number = random.randint(1, 100)

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


if difficulty == 'easy':
    guess_number(EASY_MODE, chosen_number)
elif difficulty == 'hard':
    guess_number(HARD_MODE, chosen_number)
else:
    print("Entered incorrect value.")
