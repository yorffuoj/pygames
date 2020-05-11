from puissance4.color import Color
from puissance4.grid import Grid
import time


def htmlize(array):
    s = []
    for row in reversed(array):
        s.append('|')
        for cell in row:
            s.append('▓▓' if cell == 1 else '░░' if cell == 2 else '  ')
            s.append('|')
        s.append('\n')
    s.extend(["  0  1  2  3  4  5  6 \n"])
    return ''.join(s)


first = ''
while first != 'Y' and first != 'R':
    print(first != 'Y' or first != 'R')
    first = input("Which player want to start ([Y] or [R]?\n")
    print(f"after: {first}")
if first == 'Y':
    first = Color.YELLOW
    second = Color.RED
else:
    first = Color.RED
    second = Color.YELLOW

g = Grid()
won = g.winner_present()
players = [first, second]
i = 0
while not g.winner:
    column = -1
    while not g.column_exists(column) or g.is_column_full(column):
        column = int(input(f"{players[i].name}'s turn. Pick a column number:\n"))
    g.add_piece(players[i], column)
    print(htmlize(g.grid))
    i += 1
    i = i % 2
print(f"And the winneeeeeeeeeeeeeer is {g.winner.name}")
