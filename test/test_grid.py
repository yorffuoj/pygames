from puissance4.grid import Grid
from puissance4.color import Color
import numpy as np
import pytest


def test_init_default():
    g = Grid()
    assert g.align == 4, "the number of pieces to align is not well set"
    assert g.row_max == 5, "the row max is not well set"
    assert g.col_max == 6, "the col max is not well set"
    expected_grid = [[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0], ]
    assert np.all(g.grid == expected_grid), "the grid is not well build"


def test_init_set_col():
    g = Grid(col_nb=9)
    assert g.align == 4, "the number of pieces to align is not well set"
    assert g.row_max == 5, "the row max is not well set"
    assert g.col_max == 8, "the col max is not well set"
    expected_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0], ]
    assert np.all(g.grid == expected_grid), "the grid is not well build"


def test_init_set_row():
    g = Grid(row_nb=9)
    assert g.align == 4, "the number of pieces to align is not well set"
    assert g.row_max == 8, "the row max is not well set"
    assert g.col_max == 6, "the col max is not well set"
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
    assert g.row_max == 5, "the row max is not well set"
    assert g.col_max == 6, "the col max is not well set"
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


def test_add_piece_yellow():
    g = Grid()
    g.add_piece(Color.YELLOW, 2), "it should be possible to add a piece in this column as it is not full"
    expected_grid = [[0, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0], ]
    assert np.all(g.grid == expected_grid), "a problem occurred while filling the grid"


def test_add_piece_red():
    g = Grid()
    assert g.add_piece(Color.RED, 4), "it should be possible to add a piece in this column as it is not full"
    expected_grid = [[0, 0, 0, 0, 2, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0], ]
    assert np.all(g.grid == expected_grid), "a problem occurred while filling the grid"


def test_add_piece_2_pieces_different_columns():
    g = Grid()
    assert g.add_piece(Color.RED, 4), "it should be possible to add a piece in this column as it is not full"
    assert g.add_piece(Color.YELLOW, 5), "it should be possible to add a piece in this column as it is not full"
    expected_grid = [[0, 0, 0, 0, 2, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0], ]
    assert np.all(g.grid == expected_grid), "a problem occurred while filling the grid"


def test_add_piece_2_pieces_same_column():
    g = Grid()
    assert g.add_piece(Color.RED, 4), "it should be possible to add a piece in this column as it is not full"
    assert g.add_piece(Color.YELLOW, 4), "it should be possible to add a piece in this column as it is not full"
    expected_grid = [[0, 0, 0, 0, 2, 0, 0],
                     [0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0], ]
    assert np.all(g.grid == expected_grid), "a problem occurred while filling the grid"


def test_add_piece_2_pieces_fill_column():
    g = Grid()
    assert g.add_piece(Color.RED, 4), "it should be possible to add a piece in this column as it is not full"
    assert g.add_piece(Color.YELLOW, 4), "it should be possible to add a piece in this column as it is not full"
    assert g.add_piece(Color.RED, 4), "it should be possible to add a piece in this column as it is not full"
    assert g.add_piece(Color.YELLOW, 4), "it should be possible to add a piece in this column as it is not full"
    assert g.add_piece(Color.RED, 4), "it should be possible to add a piece in this column as it is not full"
    assert g.add_piece(Color.YELLOW, 4), "it should be possible to add a piece in this column as it is not full"
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
    g = Grid(row_nb=3, align=2)  # create a f=grid with 3 rows only
    assert not g.is_column_full(3), "after grid creation the column should be empty"
    g.add_piece(Color.RED, 3)
    assert not g.is_column_full(3), "there is just one piece in the row, so there are 2 empty cells"
    g.add_piece(Color.RED, 3)
    assert not g.is_column_full(3), "there are 2 pieces in the row, so there is 1 empty cell"
    g.add_piece(Color.RED, 3)
    assert g.is_column_full(3), "there are 3 pieces in the row, so there shouldn't be any empty cell"


def test_column_has_free_space_out_of_bounds():
    g = Grid()
    with pytest.raises(AssertionError):
        g.is_column_full(7)
    with pytest.raises(AssertionError):
        g.is_column_full(-1)
