import random
WHITE = 0
BLACK = 1


def conqueror(state, side):
    if side == WHITE:
        return 0 - len(state.m_blacks) + random.random()
    elif side == BLACK:
        return 0 - len(state.m_whites) + random.random()
    else:
        print("Error")
