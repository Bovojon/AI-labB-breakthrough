from state import State
from state import WHITE, BLACK


def main():
    state = State(8, 8, 2)
    playing = WHITE
    state.displayState()
    while not state.won():
        state = state.transition(playing, 0)
        if playing == WHITE:
            playing = BLACK
        else:
            playing = WHITE

    print()
    state.displayState()


if __name__ == "__main__":
    main()
