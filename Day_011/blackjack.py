import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        print("Draw 🙃")
    elif c_score == 0:
        print("You lost, opponent has Blackjack 😱")
    elif u_score == 0:
        print("Win with a Blackjack 😎")
    elif u_score > 21:
        print("You went over. You lose 😭")
    elif c_score > 21:
        print("Opponent went over limit. You win 😁")
    elif u_score > c_score:
        print("You win 😁")
    else:
        print("You lose 😤")

def blackjack():
    print(logo)

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False
    user_score = 0
    computer_score = 0

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards are: {user_cards}, current score is: {user_score}.")
        print(f"Computer's first card is: {computer_cards[0]}.")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if draw_card == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17 and not (user_score == 0 or user_score > 21):
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    compare(user_score, computer_score)

while input("Do you want to play BlackJack? Type 'y' or 'n': ").lower() == 'y':
    blackjack()