from board import Board
from square import Square

class Action:
    def __init__(self, square):
        self.square = square

    def transition(self, player, dest):
        self.square = '.'
        dest = player       # Where player is either 'X' or 'O'

    def move_generator(self, state):
        possible_moves = []
        # Get the next corresponding row
        if self.square.sign == 'X':
            next_row = self.square.row + 1
        elif self.square.sign == 'O':
            next_row = self.square.row - 1
        else:
            next_row = -1

        if next_row != -1:
            # Get left
            if (self.square.col - 1) > 0:
                left_square = state[next_row-1][self.square.col-2]
                if left_square.sign == '.':
                    possible_moves.append(left_square)
            # Get the middle
            middle_square = state[next_row-1][self.square.col-1]
            if middle_square.sign == '.':
                possible_moves.append(middle_square)
            # Get the right
            if (self.square.col + 1) < len(state[0])+1:
                right_square = state[next_row-1][self.square.col]
                if right_square.sign == '.':
                    possible_moves.append(right_square)

            print("Square "+str(self.square.row)+" "+str(self.square.col)+" can move to following coordinates: ")
            if len(possible_moves) > 0:
                for square in possible_moves:
                    print(square.row, square.col)
            else:
                print("No where")
            print("\n")

if __name__ == '__main__':
    board = Board(8,8,2)
    state = board.intial_state(8,8,2)
    for list_of_squares in state:
        for square in list_of_squares:
            action = Action(square)
            action.move_generator(state)
