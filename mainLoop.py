from state import State
from state import WHITE, BLACK
from strategies.evasive import evasive
from strategies.conqueror import conqueror
from strategies.meanHeuristic import meanHeuristic


def switchSide(side):
    if side == WHITE:
        return BLACK
    else:
        return WHITE

def main():
    state = State(5, 5, 1)
    playing = WHITE
    turn = 0
    #state.displayState()

    while not state.won():
        turn += 1
        if playing == WHITE:
            state = state.transition(playing, 3, evasive)
            playing = BLACK
        else:
            state = state.transition(playing, 3, conqueror)
            playing = WHITE
        #state.displayState()
    whiteCaptured = state.m_totalPiece - len(state.m_whites)
    blackCaptured = state.m_totalPiece - len(state.m_blacks)

    print(whiteCaptured)
    print(blackCaptured)
    return switchSide(playing)


if __name__ == "__main__":
    whiteWins = 0
    blackWins = 0
    for i in range(10):
        if main() == WHITE:
            whiteWins += 1
        else:
            blackWins += 1
    print("White win percentage: ", whiteWins/(whiteWins+ blackWins) * 100)
    print("Black win percentage: ", blackWins/(whiteWins+ blackWins) * 100)

