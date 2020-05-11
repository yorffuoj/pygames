import numpy as np

from puissance4.color import Color


class Grid:
    """
        Create a grid and defines all operations available on this grid
    """

    def __init__(self, nb_row=6, nb_col=7, align=4):
        """
            Initialize an empty grid of 6 rows and 7 columns
            :param nb_row: the number of rows in the grid
            :param nb_col: the number of columns in the grid
            :param align: the number of pieces to align in order to win
        """
        assert nb_row > 0, "There should be at least one row"
        assert nb_col > 0, "There should be at least one column"
        assert align > 1, "There should be at least 2 pieces to align"
        assert align <= nb_row, "The number of pieces to align has to be lower or equals to the row number"
        assert align <= nb_col, "The number of pieces to align has to be lower or equals to the column number"

        self.align = align
        self.grid = np.zeros(dtype=np.int8, shape=(nb_row, nb_col))
        self.winner = False

    def column_exists(self, col_index):
        """
            Determine if the specified column index exists
            :param col_index: the column index
            :return: True if the column exists, False otherwise
        """
        col_max = np.shape(self.grid)[1]
        return 0 <= col_index <= col_max - 1

    def is_column_full(self, col_index):
        """
            determine if the specified column can receive a piece
            :param col_index: the column index
            :return: True if the column can receive a piece, False otherwise
        """
        assert self.column_exists(col_index), "This column does not exist"
        column = self.grid[:, col_index]
        return Color.WHITE.value not in column

    def add_piece(self, color, col_index):
        """
            Add a piece in a specific column of the grid.
            The piece is et in the first empty cell in the grid is set to the specified color.
            :param color: the piece color
            :param col_index: the column index
            :return: False if no empty cell was found in the column, otherwise the coordinates of the filled cell
        """
        assert color == Color.YELLOW or color == Color.RED, "Acceptable colors are yellow and red"
        assert self.column_exists(col_index), "The column does not exist"

        if self.is_column_full(col_index):
            return False

        col_max = np.shape(self.grid)[1]
        for i in range(col_max):
            if self.grid[i][col_index] == Color.WHITE.value:
                self.grid[i][col_index] = color.value
                self.winner_present()
                return i, col_index

    def winner_present(self):
        """
            Determines if there is a winner for the grid
            :return: The winners name if there is any, False otherwise
        """

        def row_win(row, col):
            portion = self.grid[row, col:col + self.align]
            return len(set(portion)) == 1

        def col_win(row, col):
            portion = self.grid[row:row + self.align, col]
            return len(set(portion)) == 1

        def upper_diag_win(row, col):
            portion = [self.grid[row + i][col + i] for i in range(self.align)]
            return len(set(portion)) == 1

        def lower_diag_win(row, col):
            portion = [self.grid[row - i][col + i] for i in range(self.align)]
            return len(set(portion)) == 1

        def set_winner(cell):
            self.winner = Color(cell)

        row_max, col_max = np.shape(self.grid)

        for row in range(row_max):
            for col in range(col_max):
                cell = self.grid[row][col]
                # if the cell is empty, there is no chance another cell is not empty in the column
                if Color(cell) == Color.WHITE:
                    continue
                # check it's a win in the row
                if col <= col_max - self.align and row_win(row, col):
                    set_winner(cell)
                    return True
                # check if it's a win in the upper diagonal
                if row <= row_max - self.align \
                        and col <= col_max - self.align \
                        and upper_diag_win(row, col):
                    set_winner(cell)
                    return True
                # check if it's a win in the column
                if row <= row_max - self.align and col_win(row, col):
                    set_winner(cell)
                    return True
                # check if it's a win the lower diagonal
                if col <= col_max - self.align \
                        and row >= row_max - self.align \
                        and lower_diag_win(row, col):
                    set_winner(cell)
                    return True
        # in case there is no enough pieces in ar row, return False
        return False
