# Tic-Tac-Toe game in Python

# initialize the board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# function to display the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# function to check if the game is over
def check_game_over():
    # check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != "-":
            return True
    # check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != "-":
            return True
    # check diagonals
    if board[0] == board[4] == board[8] and board[0] != "-":
        return True
    if board[2] == board[4] == board[6] and board[2] != "-":
        return True
    # check for tie
    if "-" not in board:
        return True
    return False

# function to handle player turn
def handle_turn(player):
    valid = False
    while not valid:
        position = input(f"{player}, choose a position (1-9): ")
        try:
            position = int(position) - 1
            if position >= 0 and position <= 8 and board[position] == "-":
                valid = True
                board[position] = player
            else:
                print("Invalid position. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1-9.")

# main game loop
player = "X"
game_over = False
while not game_over:
    display_board()
    handle_turn(player)
    game_over = check_game_over()
    if player == "X":
        player = "O"
    else:
        player = "X"

# game over message
if "-" not in board:
    print("It's a tie!")
else:
    print(f"{player} wins!")
