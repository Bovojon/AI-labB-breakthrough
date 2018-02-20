from board import Board
from square import Square

class Action:
    def transition(self, board_state, starting_square, transition_square):
        board_state[transition_square.row][transition_square.col].sign = starting_square.sign
        board_state[starting_square.row][starting_square.col].sign = '.'
        return board_state

    # TODO: NEED TO IMPLEMENT CAPTURING PIECES
    def move_generator(self, state, square):
        possible_moves = []
        # Get the next corresponding row
        if square.sign == 'X':
            next_row = square.row + 1
        elif square.sign == 'O':
            next_row = square.row - 1
        else:
            next_row = -1                   # For empty squares
        # Get the left, middle and right columns in the next row
        if next_row != -1:
            # Get left
            if (square.col - 1) > 0:
                left_square = state[next_row-1][square.col-2]
                if left_square.sign == '.':
                    possible_moves.append(left_square)
            # Get the middle
            middle_square = state[next_row-1][square.col-1]
            if middle_square.sign == '.':
                possible_moves.append(middle_square)
            # Get the right
            if (square.col + 1) < len(state[0])+1:
                right_square = state[next_row-1][square.col]
                if right_square.sign == '.':
                    possible_moves.append(right_square)
        return possible_moves
