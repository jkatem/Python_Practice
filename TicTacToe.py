# tic tac toe is an array inside an array

# handle user input, something between 1 and 9
    # if enter something else, tell them to go again

# check if input is a duplicate
    # if not, add it to the board

# check if user won

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def print_board(board):
    # iterate
    for row in board:
        for slot in row:
            print(slot, end="")

print_board(board)