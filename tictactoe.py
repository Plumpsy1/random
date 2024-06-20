def print_board(saved):

    print("   1    2    3 ")
    print("a  " + saved[0] + " || " + saved[1] + " || " + saved[2] + " ")
    print("  -------------")
    print("b  " + saved[3] + " || " + saved[4] + " || " + saved[5] + " ")
    print("  -------------")
    print("c  " + saved[6] + " || " + saved[7] + " || " + saved[8] + " ")


def receive(person):
    coordinates = input("Use coordinates to input answer player " + person + " (number first)")
    if coordinates == "1a":
        return 0
    if coordinates == "2a":
        return 1
    if coordinates == "3a":
        return 2
    if coordinates == "1b":
        return 3
    if coordinates == "2b":
        return 4
    if coordinates == "3b":
        return 5
    if coordinates == "1c":
        return 6
    if coordinates == "2c":
        return 7
    if coordinates == "3c":
        return 8


def win_check(board):

    if board[0] == board[1] == board[2] and board[0] != " ":
        return "Win"

    if board[3] == board[4] == board[5] and board[3] != " ":
        return "Win"

    if board[6] == board[7] == board[8] and board[6] != " ":
        return "Win"

    if board[0] == board[3] == board[6] and board[0] != " ":
        return "Win"

    if board[1] == board[4] == board[7] and board[1] != " ":
        return "Win"

    if board[2] == board[5] == board[8] and board[2] != " " :
        return "Win"

    if board[0] == board[4] == board[8] and board[0] != " " :
        return "Win"

    if board[2] == board[4] == board[6] and board[2] != " " :
        return "Win"


while True:
    player = "X"
    print("   1    2    3 ")
    print("a    ||   ||   ")
    print("  -------------")
    print("b    ||   ||   ")
    print("  -------------")
    print("c    ||   ||   ")

    locations_used = []*9
    len_locations_used = len(locations_used)
    values_of_board = [
                             " ",
                             " ",
                             " ",
                             " ",
                             " ",
                             " ",
                             " ",
                             " ",
                             " ",
                             " "
    ]

    i = 0

    while win_check(values_of_board) != "Win" and i < 9:

        location = receive(player)

        while check_ans(locations_used, location) == 1:
            print("Already occupied")
            location = receive(player)

        values_of_board[location] = player
        print_board(values_of_board)
        locations_used.append(location)

        if player == "X":
            player = "O"

        else:
            player = "X"

        i = i+1

    if player == "X":
        player = "O"

    else:
        player = "X"

    if win_check(values_of_board) == "Win":
        print("PLayer " + player + " won")

    else:
        print("Draw")

    if input("Do you want to play again if so say Y") != "Y":
        break
