from board import Board
from square import Square

def end_game(state):
    last_row = len(state)

    # If there is an X in the last row
    for square in state[last_row-1]:
        if square.sign == 'X':
            print("End game 1")

    # If there is an 0 in the first row
    for square in state[0]:
        if square.sign == 'O':
            print("End game 2")

    # If either player has lost all their pieces
    x = o = False
    for some_list in state:
        for square in some_list:
            if square.sign == 'X':
                x = True
            if square.sign == 'O':
                o = True
    if (not x) or (not o):
        print("End game")
    else:
        print("Working game")


if __name__ == '__main__':
    b = Board(8,8,2)
    state = b.intial_state(8,8,2)
    end_game(state)
