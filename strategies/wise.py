import random
WHITE = 0
BLACK = 1


def wise(state, side):
    if side == WHITE:
        return len(state.m_whites) - len(state.m_blacks) + random.random()
    elif side == BLACK:
        return len(state.m_blacks) - len(state.m_whites) + random.random()
    else:
        print("Error")
