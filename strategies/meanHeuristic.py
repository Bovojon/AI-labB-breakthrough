import random
WHITE = 0
BLACK = 1


def meanHeuristic(state, side):
    assert(side in {WHITE, BLACK})
    returnValue = 0
    if side == WHITE:
        for node in state.m_whites:
            for other in state.m_blacks:
                if (other[0] + 1, other[1] - 1) == node or (other[0] - 1, other[1] - 1):
                    returnValue -= 1
        returnValue += random.random()
    elif side == BLACK:
        returnValue = 0
        for node in state.m_blacks:
            returnValue += node[1]
        returnValue /= len(state.m_blacks) + random.random()
    return returnValue
