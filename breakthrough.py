from board import Board
from square import Square

def end_game(state):
    last_row = len(state)

    # If there is an X in the last row
    for square in state[last_row-1]:
        if square.piece == 'X':
            print("End game")

    # If there is an 0 in the first row
    for square in state[0]:
        if square.piece == '0':
            print("End game")

    # If either player has lost all their pieces
    x = o = []
    for some_list in state:
        for square in some_list:
            if square.piece == 'X':
                x.append(square.piece)
            elif square.piece == '0':
                o.append(square.piece)
    if len(x) == 0 or len(o) == 0:
        print("End game")


if __name__ == '__main__':
    b = Board(8,8,2)
    state = b.intial_state(8,8,2)
    end_game(state)
