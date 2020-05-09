import numpy as np

from puissance4.color import Color


class Grid:
    """
    Create a grid and defines all operations available on this grid
    """

    def __init__(self, row_nb=6, col_nb=7, align=4):
        """
        Initialize an empty grid of 6 rows and 7 columns
        :param row_nb: the number of rows in the grid
        :param col_nb: the number of columns in the grid
        :param align: the number of pieces to align in order to win
        """
        assert row_nb > 0, "There should be at least one row"
        assert col_nb > 0, "There should be at least one column"
        assert align > 1, "There should be at least 2 pieces to align"
        assert align <= row_nb, "The number of pieces to align has to be lower or equals to the row number"
        assert align <= col_nb, "The number of pieces to align has to be lower or equals to the column number"

        self.row_max = row_nb-1
        self.col_max = col_nb-1
        self.align = align
        self.grid = np.zeros(dtype=np.int8, shape=(row_nb, col_nb))

    def is_column_full(self, col_index):
        """
        determine if the specified column can receive a piece
        :param col_index: the column index
        :return: True if the column can receive a piece, False otherwise
        """
        assert 0 <= col_index <= self.col_max, "This column does not exist"
        column = self.grid[:, col_index]
        return Color.WHITE.value not in column

    def add_piece(self, color, col_index):
        """
        Add a piece in a specific column of the grid.
        The piece is et in the first empty cell in the grid is set to the specified color.
        :param color: the piece color
        :param col_index: the column index
        :return: True if an empty cell was found in the column, False otherwise
        """
        assert color == Color.YELLOW or color == Color.RED, "Acceptable colors are yellow and red"
        assert 0 <= col_index < self.col_max, "The column does not exist"

        if self.is_column_full(col_index):
            return False

        for i in range(self.col_max+1):
            if self.grid[i][col_index] == Color.WHITE.value:
                self.grid[i][col_index] = color.value
                return True

    def winner(self):
        """
        Determines if there is a winner for the grid
        :return: The winners name if there is any, False otherwise
        """

        def row_win(row, col):
            portion = self.grid[row][col:col+self.align]
            return len(set(portion)) == 1

        def col_win(row, col):
            portion = self.grid[row:row+self.align][col]
            return len(set(portion)) == 1

        def upper_diag_win(row, col):
            portion = [self.grid[row+i][col+i] for i in range(self.align)]
            return len(set(portion)) == 1

        def lower_diag_win(row, col):
            portion = [self.grid[row-i][col+i] for i in range(self.align)]
            return len(set(portion)) == 1

        for row in range(self.row_max):
            for col in range(self.col_max):
                cell = self.grid[row][col]
                # if the cell is empty, there is no chance another cell is not empty in the column
                if cell == Color.WHITE.value:
                    break
                # check it's a win in the column
                if col <= self.col_max - self.align and col_win(row, col):
                    return cell
                # check if it's a win in the upper diagonal
                if row <= self.row_max - self.align\
                        and col <= self.col_max - self.align\
                        and upper_diag_win(row, col):
                    return cell
                # check if it's a win in the row
                if row <= self.row_max - self.align and row_win(row, col):
                    return cell
                # check if it's a win the lower diagonal
                if col <= self.col_max - self.align\
                        and row >= self.row_max - self.align\
                        and lower_diag_win(row, col):
                    return cell
        # in case there is no enough pieces in ar row, return False
        return False
