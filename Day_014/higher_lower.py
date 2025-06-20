from art import logo, vs
from game_data import data
import random

def choose_data():
    return random.choice(data)

def check_followers(followers_1, followers_2):
    return 'a' if followers_1 > followers_2 else 'b'

def higher_lower():
    print(logo)
    score = 0
    f_compare = choose_data()
    n_compare = choose_data()

    while f_compare == n_compare:
        n_compare = choose_data()

    game_continue = True

    while game_continue:
        print(f"\nCompare A: {f_compare['name']}, {f_compare['description']}, from {f_compare['country']}.")
        print(vs)
        print(f"Compare B: {n_compare['name']}, {n_compare['description']}, from {n_compare['country']}.")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        correct_answer = check_followers(f_compare['follower_count'], n_compare['follower_count'])

        if user_choice == correct_answer:
            score += 1
            print(f"You've guessed right! Your current score is: {score}.")
            f_compare = n_compare
            n_compare = choose_data()

            while f_compare == n_compare:
                n_compare = choose_data()
        else:
            print(f"Sorry, that's wrong. Your final score is: {score}.")
            game_continue = False

higher_lower()
