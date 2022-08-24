axis_x = 'abcdefgh'
axis_y = '87654321'

def print_board(show_axis=False):
    if show_axis:
            print('  ', *axis_x)
    for i, row in enumerate(board):
        if not show_axis:
            print(*row)
        else:
            print(axis_y[i], end='  ')
            print(*row, end='  ')
            print(axis_y[i])
    if show_axis:
        print('  ', *axis_x)

def pos_on_board(pos, mark):
    board[pos[0]][pos[1]] = mark

def is_on_board(x, y):
    return 0 <= x < 8 and 0 <= y < 8

board = [['.']*8 for _ in range(8)]
pos = (lambda s: (axis_y.index(s[1]), axis_x.index(s[0])))(input().casefold())
pos_on_board(pos, 'N')

possible_moves = (lambda lst: lst + [t[::-1] for t in lst])([(i, j) for i in (-2, 2) for j in (-1, 1)])
possible_pos = (p for p in map(lambda t: (pos[0] + t[0], pos[1] + t[1]), possible_moves) if is_on_board(*p))

for p in possible_pos:
    pos_on_board(p, '*')

print_board(True)
