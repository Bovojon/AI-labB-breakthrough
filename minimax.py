import random
from board import Board
from node import Node
from action import Action

class Game(Action, Node):

    def evasive_heuristic(self, state, own_piece):
        count = 0
        for row in state:
            for square in row:
                if square.sign == own_piece:
                    count += 1
        utility = count + random.random()
        return utility

    def conqueror_heuristic(self, state, opp_piece):
        count = 0
        for row in state:
            for square in row:
                if square.sign == opp_piece:
                    count += 1
        utility = (0 - count) + random.random()
        return utility
#-----------------------------------------------------------------------------#
    # Need to change
    def minimax(self, state, player, depth, heuristic):
        all_moves = self.move_generator(state)
        best_move = all_moves[0]
        best_score = float('-inf')
        for move in all_moves:
            state_copy = state.transition(move)
            score = min_player(state_copy, depth)
            if score > best_score:
                best_move = move
                best_score = score
        return best_move

    def min_player(self, state, depth):
        all_moves = state.move_generator()
        best_score = float('inf')
        for move in all_moves:
            state_copy = state.transition()
            score = max_player(state_copy, depth)
            if score < best_score:
                best_move = move
                best_score = score
        return best_score

    def max_player(self, state, depth):
        all_moves = state.move_generator()
        best_score = float('inf')
        for move in all_moves:
            state_copy = state.transition()
            score = min_player(state_copy, depth)
            if score > best_score:
                best_move = move
                best_score = score
        return best_score
#-----------------------------------------------------------------------------#

    def minimax_wiki(node_state, depth, maximizingPlayer, player_sign):
        if depth = 0 or node_state.is_terminal():
            return self.evasive_heuristic(node_state, player_sign)
        if maximizingPlayer:
            best_value = float('-inf')
            for child in node_state.children:
                v = minimax_wiki(child, depth-1, FALSE)
                best_value = max(best_value, v)
            return best_value
        else:
            best_value = float('inf')
            for child in node_state.children:
                v = minimax_wiki(child, depth-1, TRUE)
                best_value = min(best_value, v)
            return best_value

"""
The basic idea is as follows:
(i) Lookahead 3 steps
(ii) Take the best move
(iii) Lookahead 3 steps
(iv) Take the best move
Repeat...

"""

    def build_tree(self, initial_board_state, depth):
        node_state = Node()
        node_state.state = initial_board_state
        for row in initial_board_state:
            for square in row:
                if square.sign == 'X' or square.sign == 'O'
                    possible_moves = self.move_generator(state, square)
                    # Make the transitions for those possible_moves
                    for transition_square in possible_moves:
                        new_state = self.transition(square, transition_square)
                        node_state.children.append(new_state)
                    # Get the state and pass it into Node



    def play_game(self, heuristic_X, heuristic_O, board_state, depth):
        pass




if __name__ == '__main__':
    depth = 3
    board = Board(8,8,2)
    state = board.intial_state(8,8,2)
    test_game = Game()

    # u = evasive(state, 'X')
    # print(u)
