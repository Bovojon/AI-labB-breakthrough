from state import State
from state import WHITE, BLACK
from strategies.evasive import evasive


def main():
    state = State(5, 5, 1)
    playing = WHITE
    turn = 0
    state.displayState()

    while not state.won():
        turn += 1
        state = state.transition(playing, 3, evasive)
        if playing == WHITE:
            playing = BLACK
        else:
            playing = WHITE
        #state.displayState()


if __name__ == "__main__":
    main()
