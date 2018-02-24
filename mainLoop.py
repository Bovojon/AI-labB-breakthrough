from state import State
from state import WHITE, BLACK
from strategies.evasive import evasive
from strategies.conqueror import conqueror
from strategies.meanHeauristic import meanHeauristic
from strategies.wise import wise

def switchSide(side):
    if side == WHITE:
        return BLACK
    else:
        return WHITE

def play_game(white_heuristic, black_heuristic, state):
    playing = WHITE
    turn = 0
    while not state.end_game():
        turn += 1
        print(playing)
        if playing == WHITE:
            state = state.transition(playing, 4, white_heuristic)
            playing = BLACK
        else:
            state = state.transition(playing, 4, black_heuristic)
            playing = WHITE
        state.displayState()

    whiteCaptured = state.m_totalPiece - len(state.m_whites)
    blackCaptured = state.m_totalPiece - len(state.m_blacks)
    print(whiteCaptured)
    print(blackCaptured)
    return switchSide(playing), whiteCaptured, blackCaptured


if __name__ == "__main__":
    fileToWrite = open('report.txt', 'w')
    row = 5
    col = 5
    pieces = 2
    state = State(row, col, pieces)
    whiteWins = 0
    blackWins = 0
    games_to_play = 10
    for i in range(games_to_play):
        if play_game(evasive, conqueror, state)[0] == WHITE:
            whiteWins += 1
        else:
            blackWins += 1
    fileToWrite.write("Played {} games.\n".format(games_to_play))
    fileToWrite.write("Board state: ({}, {}, {})\n".format(row, col, pieces))
    fileToWrite.write("White wins: "+str(whiteWins/(whiteWins + blackWins) * 100)+"%\n")
    fileToWrite.write("Black wins: "+str(blackWins/(whiteWins + blackWins) * 100)+"%\n")
    fileToWrite.write("------------------------------------------------------------")
    fileToWrite.close()
