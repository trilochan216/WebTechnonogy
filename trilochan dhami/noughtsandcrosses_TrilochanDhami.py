# trilochan dhami 
#233294  

import random
import os.path
import json
random.seed()


def draw_board(board):
    # develop code to draw the board
    print('\n' + '-' * 13)
    for i in range(3):
        print('|', board[i][0], '|', board[i][1], '|', board[i][2], '|')
        print('-' * 13)

def welcome(board):
    # prints the welcome message
    print('\nWelcome to the Noughts and Crosses Game!\n')
    print('The board layout is shown below:\n')
    # display the board by calling draw_board(board)
    draw_board(board)

def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board

def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    while True:
        move = input('Enter your move (1-9): ')
        if move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('Invalid input. Please try again.')
            continue
        else:
            move = int(move)
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] != ' ':
                print('Cell already occupied. Please try again.')
                continue
            else:
                return row, col

def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col
    while True:
        move = random.randint(1, 9)
        row = (move - 1) // 3
        col = (move - 1) % 3
        if board[row][col] == ' ':
            return row, col

def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    # checking the rows
    for i in range(3):
        if board[i][0] == mark and board[i][1] == mark and board[i][2] == mark:
            return True
    # checking the columns
    for i in range(3):
        if board[0][i] == mark and board[1][i] == mark and board[2][i] == mark:
            return True
    # checking the diagonals
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True
    return False

def check_for_draw(board):
    # develop code to check if all cells are occupied
    # return True if it is, False otherwise
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True


def play_game(board):
    initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)
        if check_for_win(board, 'X'):
            return 1
        if check_for_draw(board):
            return 0
        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        draw_board(board)
        if check_for_win(board, 'O'):
            return -1
        if check_for_draw(board):
            return 0


def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    choice = input("Enter 1 to play the game,\n"
                   "2 to save the score in 'leaderboard.txt',\n"
                   "3 to load and display the scores,\n"
                   "or 'q' to quit: ")
    return choice


def load_scores():
     # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    leaders = {}
    try:
        with open('leaderboard.txt', 'r') as file:
            for line in file:
                name, score = line.strip().split(',')
                leaders[name] = int(score)
        return leaders
    except FileNotFoundError:
        print("File not found")
        return {}


def save_score(score):
    #Saving the current score to the leaderboard file.
    name = input("Enter your name: ")
    try:
        with open('leaderboard.txt', 'a', encoding='utf-8') as file:
            file.write(f"{name},{score}\n")
        print(f"Score saved successfully for {name}")
    except Exception as err:
        print(f"Error saving score: {err}")



def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    if not leaders:
        print("No scores found.")
        return

    print("LEADERBOARD:")
    for i, (name, score) in enumerate(sorted(leaders.items(), key=lambda x: x[1], reverse=True)):
        print(f"{i + 1}. {name}: {score}")
