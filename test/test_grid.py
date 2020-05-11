from puissance4.grid import Grid
from puissance4.color import Color
import numpy as np
import pytest


def test_init_default():
    g = Grid()
    assert g.align == 4, "the number of pieces to align is not well set"
    expected_grid = [[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0], ]
    assert np.all(g.grid == expected_grid), "the grid is not well build"


def test_init_set_col():
    g = Grid(nb_col=9)
    assert g.align == 4, "the number of pieces to align is not well set"
    expected_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0], ]
    assert np.all(g.grid == expected_grid), "the grid is not well build"


def test_init_set_row():
    g = Grid(nb_row=9)
    assert g.align == 4, "the number of pieces to align is not well set"
    expected_grid = [[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0], ]
    assert np.all(g.grid == expected_grid), "the grid is not well build"


def test_init_set_align():
    g = Grid(align=5)
    assert g.align == 5, "the number of pieces to align is not well set"
    expected_grid = [[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0], ]
    assert np.all(g.grid == expected_grid), "the grid is not well build"


def test_init_set_align_higher():
    with pytest.raises(AssertionError):
        Grid(align=9)


def test_init_set_align_lower():
    with pytest.raises(AssertionError):
        Grid(align=1)


def test_column_exists():
    g = Grid()
    assert not g.column_exists(-1)
    assert g.column_exists(0)
    assert g.column_exists(1)
    assert g.column_exists(2)
    assert g.column_exists(3)
    assert g.column_exists(4)
    assert g.column_exists(5)
    assert g.column_exists(6)
    assert not g.column_exists(7)


def test_add_piece_yellow():
    g = Grid()
    assert g.add_piece(Color.YELLOW, 2) == (0, 2), "it should be possible to add a piece in this column as it is not " \
                                                   "full "
    expected_grid = [[0, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0], ]
    assert np.all(g.grid == expected_grid), "a problem occurred while filling the grid"


def test_add_piece_red():
    g = Grid()
    assert g.add_piece(Color.RED, 4) == (0, 4), "it should be possible to add a piece in this column as it is not full"
    expected_grid = [[0, 0, 0, 0, 2, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0], ]
    assert np.all(g.grid == expected_grid), "a problem occurred while filling the grid"


def test_add_piece_2_pieces_different_columns():
    g = Grid()
    assert g.add_piece(Color.RED, 4) == (0, 4), "it should be possible to add a piece in this column as it is not full"
    assert g.add_piece(Color.YELLOW, 5) == (0, 5), "it should be possible to add a piece in this column as it is not " \
                                                   "full "
    expected_grid = [[0, 0, 0, 0, 2, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0], ]
    assert np.all(g.grid == expected_grid), "a problem occurred while filling the grid"


def test_add_piece_2_pieces_same_column():
    g = Grid()
    assert g.add_piece(Color.RED, 4) == (0, 4), "it should be possible to add a piece in this column as it is not full"
    assert g.add_piece(Color.YELLOW, 4) == (1, 4), "it should be possible to add a piece in this column as it is not " \
                                                   "full "
    expected_grid = [[0, 0, 0, 0, 2, 0, 0],
                     [0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0], ]
    assert np.all(g.grid == expected_grid), "a problem occurred while filling the grid"


def test_add_piece_2_pieces_fill_column():
    g = Grid()
    assert g.add_piece(Color.RED, 4) == (0, 4), "it should be possible to add a piece in this column as it is not full"
    assert g.add_piece(Color.YELLOW, 4) == (1, 4), "it should be possible to add a piece in this column as it is not " \
                                                   "full "
    assert g.add_piece(Color.RED, 4) == (2, 4), "it should be possible to add a piece in this column as it is not full"
    assert g.add_piece(Color.YELLOW, 4) == (3, 4), "it should be possible to add a piece in this column as it is not " \
                                                   "full "
    assert g.add_piece(Color.RED, 4) == (4, 4), "it should be possible to add a piece in this column as it is not full"
    assert g.add_piece(Color.YELLOW, 4) == (5, 4), "it should be possible to add a piece in this column as it is not " \
                                                   "full "
    expected_grid = [[0, 0, 0, 0, 2, 0, 0],
                     [0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 2, 0, 0],
                     [0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 2, 0, 0],
                     [0, 0, 0, 0, 1, 0, 0], ]
    assert np.all(g.grid == expected_grid), "a problem occurred while filling the grid"


def test_add_piece_impossible_column_full():
    g = Grid()
    assert g.add_piece(Color.RED, 4), "it should be possible to add a piece in this column as it is not full"
    assert g.add_piece(Color.YELLOW, 4), "it should be possible to add a piece in this column as it is not full"
    assert g.add_piece(Color.RED, 4), "it should be possible to add a piece in this column as it is not full"
    assert g.add_piece(Color.YELLOW, 4), "it should be possible to add a piece in this column as it is not full"
    assert g.add_piece(Color.RED, 4), "it should be possible to add a piece in this column as it is not full"
    assert g.add_piece(Color.YELLOW, 4), "it should be possible to add a piece in this column as it is not full"
    assert not g.add_piece(Color.RED, 4), "it shouldn't be possible to add a piece in this column as it is full"


def test_column_is_full_empty_grid_false():
    g = Grid()
    assert not g.is_column_full(0), "after grid creation the column should be empty"
    assert not g.is_column_full(1), "after grid creation the column should be empty"
    assert not g.is_column_full(2), "after grid creation the column should be empty"
    assert not g.is_column_full(3), "after grid creation the column should be empty"
    assert not g.is_column_full(4), "after grid creation the column should be empty"
    assert not g.is_column_full(5), "after grid creation the column should be empty"
    assert not g.is_column_full(6), "after grid creation the column should be empty"


def test_column_is_full():
    g = Grid(nb_row=3, align=2)  # create a f=grid with 3 rows only
    assert not g.is_column_full(3), "after grid creation the column should be empty"
    g.add_piece(Color.RED, 3)
    assert not g.is_column_full(3), "there is just one piece in the row, so there are 2 empty cells"
    g.add_piece(Color.RED, 3)
    assert not g.is_column_full(3), "there are 2 pieces in the row, so there is 1 empty cell"
    g.add_piece(Color.RED, 3)
    assert g.is_column_full(3), "there are 3 pieces in the row, so there shouldn't be any empty cell"


def test_is_column_full_out_of_bounds():
    g = Grid()
    with pytest.raises(AssertionError):
        g.is_column_full(7)
    with pytest.raises(AssertionError):
        g.is_column_full(-1)


def create_grid(array):
    nb_row = len(array)
    nb_col = len(array[0])
    g = Grid(nb_row=nb_row, nb_col=nb_col)
    for i in range(nb_row):
        for j in range(nb_col):
            cell = array[i][j]
            if cell == 0:
                continue
            if cell == 1:
                g.add_piece(Color.YELLOW, j)
            else:
                g.add_piece(Color.RED, j)
    return g


def test_winner_empty_no_win():
    array = [[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0], ]
    g = create_grid(array)
    assert not g.winner_present()


def test_winner_not_enough_no_win():
    array = [[0, 0, 1, 1, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0], ]
    g = create_grid(array)
    assert np.all(array == g.grid)
    assert not g.winner_present()


def test_winner_row_left_win():
    array = [[1, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0], ]
    g = create_grid(array)
    assert g.winner_present()
    assert g.winner == Color.YELLOW


def test_winner_row_right_win():
    array = [[1, 1, 2, 1, 2, 2, 2],
             [0, 0, 0, 2, 2, 2, 2],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0], ]
    g = create_grid(array)
    assert g.winner_present()
    assert g.winner == Color.RED


def test_winner_col_upper_win():
    array = [[0, 1, 1, 2, 1, 1, 0],
             [0, 0, 0, 2, 0, 0, 0],
             [0, 0, 0, 2, 0, 0, 0],
             [0, 0, 0, 2, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0], ]
    g = create_grid(array)
    assert g.winner_present()
    assert g.winner == Color.RED


def test_winner_col_lower_win():
    array = [[0, 1, 1, 2, 1, 1, 2],
             [0, 0, 0, 2, 0, 0, 2],
             [0, 0, 0, 2, 0, 0, 1],
             [0, 0, 0, 1, 0, 0, 1],
             [0, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0, 1], ]
    g = create_grid(array)
    assert g.winner_present()
    assert g.winner == Color.YELLOW


def test_winner_upper_diag_win():
    array = [[0, 1, 1, 2, 1, 1, 2],
             [0, 0, 0, 2, 2, 1, 1],
             [0, 0, 0, 1, 0, 2, 1],
             [0, 0, 0, 2, 0, 0, 2],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0], ]
    g = create_grid(array)
    assert g.winner_present()
    assert g.winner == Color.RED


def test_winner_upper_diag_upper_right_win():
    array = [[0, 1, 1, 2, 1, 1, 2],
             [0, 0, 0, 2, 1, 2, 1],
             [0, 0, 0, 1, 2, 2, 1],
             [0, 0, 0, 2, 0, 0, 2],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0], ]
    g = create_grid(array)
    assert g.winner_present()
    assert g.winner == Color.RED


def test_won_lower_diag_upper_left_win():
    array = [[1, 1, 1, 2, 1, 1, 2],
             [0, 1, 2, 2, 1, 2, 1],
             [0, 0, 1, 1, 2, 2, 1],
             [0, 0, 0, 1, 0, 0, 2],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0], ]
    g = create_grid(array)
    assert g.winner_present()
    assert g.winner == Color.YELLOW


if __name__ == "__main__":
    test_is_column_full_out_of_bounds()
