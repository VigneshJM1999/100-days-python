import random
from art import logo

def check_winner(board, symbol):
    win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combo in win_conditions:
        if all(board[i] == symbol for i in combo):
            return True
    return False

def draw_board(board):
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i + 1]} | {board[i + 2]}")
        if i < 6:
            print("___________")

def tic_tac_toe():

    print(logo)
    board = [' '] * 9
    draw_board(board)

    is_game_over = False
    positions = [i for i in range(0,9)]
    while not is_game_over:
        player_symbol = input("Please select which symbol you want? 'X' or 'O' ")
        computer_symbol = "O" if player_symbol == "X" else "X"
        current_player = "player" if player_symbol == "X" else "computer"

        while len(positions) > 0:

            if current_player == "player":

                position = int(input("Enter the position where you want to draw first (1 - 9): ")) - 1
                if position in range(0, 9):
                    if position in positions:
                        board[position] = player_symbol
                        positions.remove(position)
                        draw_board(board)

                    else:
                        print("The spot is already taken!")
                        position = int(input("Enter the position where you want to draw first (1 - 9): ")) - 1
                        board[position] = player_symbol
                        positions.remove(position)
                        draw_board(board)

                if check_winner(board, player_symbol):
                    print("🎉 You have won!")
                    return
                current_player = "computer"

            else:
                position = random.choice(positions)
                print(f"\nOpponent has chose position: {position + 1}\n")
                board[position] = computer_symbol
                positions.remove(position)
                draw_board(board)

                if check_winner(board, computer_symbol):
                    print("💻 Opponent has won!")
                    return
                current_player = "player"

        print("It's a draw!")

tic_tac_toe()