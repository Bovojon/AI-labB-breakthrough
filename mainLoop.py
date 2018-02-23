from state import State
from state import WHITE, BLACK
from strategies.evasive import evasive
from strategies.conqueror import conqueror
from strategies.meanHeuristic import meanHeauristic


def main():
    state = State(5, 5, 1)
    playing = WHITE
    turn = 0
    state.displayState()

    while not state.won():
        turn += 1
        if playing == WHITE:
            state = state.transition(playing, 3, evasive)
            playing = BLACK
        else:
            state = state.transition(playing, 3, meanHeauristic)
            playing = WHITE
        state.displayState()


if __name__ == "__main__":
    main()
