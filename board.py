from square import Square

class Board:
    def __init__(self, rows, cols, rows_pieces):
        self.rows = rows
        self.cols = cols
        self.rows_pieces = rows_pieces
        self.squares_list = []

        for i in range(1, self.rows+1):
            row_of_squares = []
            for j in range(1, self.cols+1):

                # First [self.rows_pieces] rows
                if i < self.rows_pieces+1:
                    s1 = Square(i, j, 'X')
                    row_of_squares.append(s1)

                # Last [self.rows_pieces] rows
                elif i > self.rows - self.rows_pieces:
                    s2 = Square(i, j, '0')
                    row_of_squares.append(s2)

                # Middle rows
                else:
                    s3 = Square(i, j, '.')
                    row_of_squares.append(s3)

            # We add current row to list of rows
            self.squares_list.append(row_of_squares)


if __name__ == '__main__':

    board = Board(8,8,2)
    for i in board.squares_list:
        for j in i:
            print(j.piece)
