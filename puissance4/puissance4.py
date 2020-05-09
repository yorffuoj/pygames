import numpy as np

EMPTY = 0
YELLOW = 1
RED = 2


def initialize_grid():
    return np.zeros(dtype=np.int8, shape=(6, 7))


def set_color(color, column, grille):
    for row in grille:
        if row[column] == EMPTY:
            row[column] = color
            return True, grille
    return False, grille


def gagnant(grille):
    from enum import Enum
    class Verify(Enum):
        COLUMN = (1, 0)
        ROW = (0, 1)
        UPPER_DIAG = (1, 1)
        LOWER_DIAG = (-1, 1)

        def win(i, j, verif):
            ref = grille[i][j]
            for n in range(1, 4):
                if grille[i + n * verif.value[0]][j + n * verif.value[1]] != ref:
                    return False
            return True

    row_max = len(grille)
    col_max = len(grille[0])

    for row in range(row_max):
        for col in range(col_max):
            value = grille[row][col]
            if value == YELLOW or value == RED:
                if col <= col_max - 4:
                    if win(row, col, Verify.ROW):
                        return value
                if row <= row_max - 4 and col <= col_max - 4:
                    if win(row, col, Verify.UPPER_DIAG):
                        return value
                if row <= row_max - 4:
                    if win(row, col, Verify.COLUMN):
                        return value
                if col <= col_max - 4 and row >= row_max - 4:
                    if win(row, col, Verify.LOWER_DIAG):
                        return value
    return
