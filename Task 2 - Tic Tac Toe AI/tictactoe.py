import math

# create empty board
board = [' ' for i in range(9)]

# function to print board
def print_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

# function to check winner
def winner(player):
    if board[0] == board[1] == board[2] == player:
        return True
    if board[3] == board[4] == board[5] == player:
        return True
    if board[6] == board[7] == board[8] == player:
        return True
    if board[0] == board[3] == board[6] == player:
        return True
    if board[1] == board[4] == board[7] == player:
        return True
    if board[2] == board[5] == board[8] == player:
        return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# check draw
def draw():
    if ' ' not in board:
        return True
    return False

# minimax function (basic version)
def minimax(is_ai):
    if winner('O'):
        return 1
    if winner('X'):
        return -1
    if draw():
        return 0

    if is_ai:
        best = -100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                if score > best:
                    best = score
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                if score < best:
                    best = score
        return best

# function for AI move
def ai_turn():
    best_score = -100
    move = 0

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i

    board[move] = 'O'

# main program
print("TIC TAC TOE GAME")
print("You are X")
print("Computer is O")
print("Enter position from 1 to 9")

while True:
    print_board()

    user = int(input("Enter your move: ")) - 1

    if user < 0 or user > 8:
        print("Wrong input")
        continue

    if board[user] != ' ':
        print("Place already filled")
        continue

    board[user] = 'X'

    if winner('X'):
        print_board()
        print("You Win")
        break

    if draw():
        print_board()
        print("Game Draw")
        break

    ai_turn()

    if winner('O'):
        print_board()
        print("Computer Wins")
        break
