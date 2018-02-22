import random

WHITE = 0
BLACK = 1


class State:
    def __init__(self, width, height, rowNum):
        self.m_width = width
        self.m_height = height
        self.rowNum = rowNum
        self.blacks = []
        self.whites = []

    def heuristic(self, function, side):
        function(side, self)

    def possibleMoves(self, side):
        if side == WHITE:
            pass
        else:
            pass

    def transition(self, side):
        pass

    def won(self):
        return False
