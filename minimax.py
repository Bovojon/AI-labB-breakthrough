import random
from board import Board
from node import Node

def evasive(state, own_piece):
    count = 0
    for row in state:
        for square in row:
            if square.sign == own_piece:
                count += 1
    utility = count + random.random()
    return utility

def conqueror(state, opp_piece):
    count = 0
    for row in state:
        for square in row:
            if square.sign == opp_piece:
                count += 1
    utility = (0 - count) + random.random()
    return utility

def minimax(state, player, max_depth, heuristic):
    utility = heuristic(state, player)
    return action

def minimax(state):
    pass

def min_play(state):
    pass

def max_play(state):
    pass

if __name__ == '__main__':
    board = Board(8,8,2)
    state = board.intial_state(8,8,2)

    u = evasive(state, 'X')
    print(u)
