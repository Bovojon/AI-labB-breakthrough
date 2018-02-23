from state import State
from state import WHITE, BLACK
from strategies.evasive import evasive


def main():
    state = State(8, 8, 2)
    playing = WHITE
    state.displayState()
    print()
    while not state.won():
        state = state.transition(playing, 3, evasive)
        if playing == WHITE:
            playing = BLACK
        else:
            playing = WHITE
    state.displayState()


if __name__ == "__main__":
    main()
