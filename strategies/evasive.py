import random
WHITE = 0
BLACK = 1


def evasive(state, side):
    if side == WHITE:
        return len(state.m_whites) + random.random()
    elif side == BLACK:
        return len(state.m_blacks) + random.random()
    else:
        print("Error")
