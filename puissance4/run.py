from puissance4.color import Color
from puissance4.grid import Grid


def htmlize(array):
    s = []
    for row in reversed(array):
        s.append('|')
        for cell in row:
            s.append('▓▓' if cell == 1 else '░░' if cell == 2 else '  ')
            s.append('|')
        s.append('\n')
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
won = g.won()
players = [first, second]
i = 0
while not won:
    column = -1
    while not g.column_exists(column) or g.is_column_full(column):
        column = input(f"{players[i].name}'s turn. Pick a number:\n")
    g.add_piece(players[i], column)
    print(htmlize(g.grid))
    i += 1
    i = i % 2
    won = g.won()
