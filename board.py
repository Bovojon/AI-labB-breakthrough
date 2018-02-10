from square import Square

class Board:
    def __init__(self, rows, cols, rows_pieces):
        self.rows = rows
        self.cols = cols
        self.rows_pieces = rows_pieces
        self.rows_list = []

    def intial_state(self, rows, col, rows_pieces):
        for i in range(1, self.rows+1):
            row_of_squares = []
            for j in range(1, self.cols+1):

                # First [self.rows_pieces] rows
                if i < self.rows_pieces+1:
                    s1 = Square(i, j, 'X')
                    row_of_squares.append(s1)

                # Last [self.rows_pieces] rows
                elif i > self.rows - self.rows_pieces:
                    s2 = Square(i, j, 'O')
                    row_of_squares.append(s2)

                # Middle rows
                else:
                    s3 = Square(i, j, '.')
                    row_of_squares.append(s3)

            # We add current row to list of rows
            self.rows_list.append(row_of_squares)

        return self.rows_list

    def display_state(self):
        numbering = ""
        for i in range(1, self.cols+1):
            numbering+=str(i)
        print("  "+numbering)
        i = 1
        for row in self.rows_list:
            row_string = ''
            row_string += str(i)
            row_string += " "
            for square in row:
                row_string += square.sign
            row_string_right = ' '
            row_string += " "+str(i)
            i += 1
            print(row_string)
        print("  "+numbering)


if __name__ == '__main__':

    board = Board(8,8,2)
    state = board.intial_state(8,8,2)
    # for list_of_squares in state:
    #     for square in list_of_squares:
    #         print(square.sign)
    board.display_state()
