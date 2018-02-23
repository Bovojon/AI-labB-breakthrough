import random
WHITE = 0
BLACK = 1


def meanHeauristic(state, side):
    assert(side in {WHITE, BLACK})
    if side == WHITE:
        returnValue = 0
        for node in state.m_whites:
            returnValue += state.m_height - node[1] - 1
        returnValue /= len(state.m_whites) + random.random()
    elif side == BLACK:
        returnValue = 0
        for node in state.m_blacks:
            returnValue += node[1]
        returnValue /= len(state.m_blacks) + random.random()
    return returnValue

