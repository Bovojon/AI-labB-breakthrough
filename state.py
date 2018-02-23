import random
import copy

WHITE = 0
BLACK = 1


class State:
    def __init__(self, width, height, rowNum):
        self.m_width = width
        self.m_height = height
        self.m_blacks = []
        self.m_whites = []

        for x in range(self.m_width):
            for y in range(rowNum):
                self.m_whites.append((x, y))
                self.m_blacks.append((x, self.m_height - y - 1))

    def heuristicValue(self, utilityFunction, side):
        return utilityFunction(side, self)

    def moveNode(self, fromPos, toPos, side):
        if side == WHITE:
            self.m_whites.remove(fromPos)
            self.m_whites.append(toPos)
            if toPos in self.m_blacks:
                self.m_blacks.remove(toPos)
        else:
            self.m_blacks.remove(fromPos)
            self.m_blacks.append(toPos)
            if toPos in self.m_whites:
                self.m_whites.remove(toPos)

    def possibleMoves(self, side):
        possibleStates = []
        if side == WHITE:
            for node in self.m_whites:
                # Check straight
                if (node[0], node[1] + 1) not in (self.m_whites + self.m_blacks):
                    newState = copy.deepcopy(self)
                    newState.moveNode(node, (node[0], node[1] + 1), WHITE)
                    possibleStates.append(newState)
                #Check diagonal
                if (node[0] - 1, node[1] + 1) not in self.m_whites:
                    if node[0] - 1 >= 0:
                        newState = copy.deepcopy(self)
                        newState.moveNode(node, (node[0] - 1, node[1] + 1), WHITE)
                        possibleStates.append(newState)
                if (node[0] + 1, node[1] + 1) not in self.m_whites:
                    if node[0] + 1 < self.m_width:
                        newState = copy.deepcopy(self)
                        newState.moveNode(node, (node[0] - 1, node[1] + 1), WHITE)
                        possibleStates.append(newState)
        else:
            for node in self.m_blacks:
                # Check straight
                if (node[0], node[1] - 1) not in (self.m_whites + self.m_blacks):
                    newState = copy.deepcopy(self)
                    newState.moveNode(node, (node[0], node[1] + 1), BLACK)
                    possibleStates.append(newState)
                #Check diagonal
                if (node[0] - 1, node[1] - 1) not in self.m_blacks:
                    if node[0] - 1 >= 0:
                        newState = copy.deepcopy(self)
                        newState.moveNode(node, (node[0] - 1, node[1] - 1), BLACK)
                        possibleStates.append(newState)
                if (node[0] + 1, node[1] - 1) not in self.m_blacks:
                    if node[0] + 1 < self.m_width:
                        newState = copy.deepcopy(self)
                        newState.moveNode(node, (node[0] - 1, node[1] - 1), BLACK)
                        possibleStates.append(newState)
        return possibleStates

    def transition(self, side, utilityFunction):
        return random.choice(self.possibleMoves(side))

    def won(self):
        for node in self.m_blacks:
            if node[1] == 0:
                return True

        for node in self.m_whites:
            if node[1] == self.m_height - 1:
                return True

        return False

    def displayState(self):
        for y in range(self.m_height):
            for x in range(self.m_width):
                if (x, y) in self.m_whites:
                    print("O", end="")
                elif (x, y) in self.m_blacks:
                    print("X", end="")
                else:
                    print(".", end="")
            print()

