# Rules of Breakthrough

* A piece may move one space straight or diagonally forward if the target square is empty.
* A piece may remove an opponent's piece if the opponent's piece is in a square that is one step diagonally forward.

### There are 3 ways to determine winning state:
* The first player to reach the opponent's home row is the winner.
* If all the pieces of a player are captured, that player loses.
* A draw is impossible.

### Representing moves - Use Action Object
* Which piece (x,y)
* Where is it moving to? (x,y)
* Check to see if spot is occupied

## Part 1

B) Representation Scheme: A board is represented as a list of lists of the Square Objects. Each Square Object represents a square on the board.

E) Transition function conditions:
1. Spot must be empty
2. Spot must exist - cannot transition outside of the board


## TODO
1) Check to make sure that number of rows of pieces not more than allowed.
2) Return state for transition function

## References
https://en.wikipedia.org/wiki/Breakthrough_(board_game)

https://www.codeproject.com/Articles/37024/Simple-AI-for-the-Game-of-Breakthrough

https://github.com/lcwadle/AI-Breakthrough

https://chessprogramming.wikispaces.com/Breakthrough+(Game)
