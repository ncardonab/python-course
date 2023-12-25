options = [1, 2, 3, 4, 6, 7, 8, 9]

winner_patterns = []


def display_board(board):
    for row in board:
        first, second, third = row
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {first}   |   {second}   |   {third}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    pass


def make_move(board, turn):
    import random

    move = 0
    mark = ''
    if turn == "User":
        move = int(input("Enter your move: "))
        mark = 'X'
    elif turn == "CPU":
        move = random.choice(options)
        mark = 'O'

    if move in options:
        del options[options.index(move)]

        for row in board:
            if move in row:

                move_index = row.index(move)
                row[move_index] = mark
                break

    return board


if __name__ == "__main__":
    board = [[1, 2, 3],
             [4, 'O', 6],
             [7, 8, 9]]

    turn = "User"
    display_board(board)
    while options:
        board = make_move(board, turn)
        display_board(board)
        turn = "CPU" if turn == "User" else "User"
