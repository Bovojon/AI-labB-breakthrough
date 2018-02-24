import random
WHITE = 0
BLACK = 1

def smarterEvasive(state, side):
    assert(side in {WHITE, BLACK})
    if side == WHITE and len(state.m_whites)>0:
        sum_of_distance = 0
        for node in state.m_whites:
            sum_of_distance += state.m_height - 1 - node[1]
        average_distance = sum_of_distance / len(state.m_whites)
        return average_distance + len(state.m_whites) + random.random()
    elif side == BLACK and len(state.m_blacks)>0:
        sum_of_distance = 0
        for node in state.m_blacks:
            sum_of_distance += state.m_height - 1 - node[1]
        average_distance = sum_of_distance / len(state.m_blacks)
        return average_distance + len(state.m_blacks) + random.random()
