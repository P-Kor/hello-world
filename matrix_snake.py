# Snake
# Fill the matrix with numbers by the spiral pattern

import itertools

inp = itertools.count(1)
n, m = map(int, (input().split()))

def move(pos, run):
    match directions[run]:
        case 'right':
            return (pos[0], pos[1] + 1)
        case 'left':
            return (pos[0], pos[1] - 1)
        case 'down':
            return (pos[0] + 1, pos[1])
        case 'up':
            return (pos[0] - 1, pos[1])

def in_range(pos):
    return 0 <= pos[0] < n and 0 <= pos[1] < m

def get_elem(pos):
    return lst[pos[0]][pos[1]]

def set_elem(pos, x):
    lst[pos[0]][pos[1]] = x
    return 1

lst = [[0]*m for _ in range(n)]
directions = ['right', 'down', 'left', 'up']
run = 0
pos = (0, 0)

while True:
    set_elem(pos, next(inp))
    turns_count = 0
    while True:
        next_pos = move(pos, run)
        if in_range(next_pos) and get_elem(next_pos) == 0:
            pos = next_pos
            break
        run = (run + 1) % 4
        turns_count += 1
        if turns_count == 3:
            break
    if turns_count == 3:
        break

for row in lst:
    print(*map(lambda m: str(m).ljust(3), row), sep='')
