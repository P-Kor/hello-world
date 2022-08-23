s = '1 9 4 2\n3 8 1 5\n6 7 4 6\n1 9 7 8'

lst = [row.split() for row in s.split('\n')]

for row in lst:
    print(*row)
print()

lst = [list(t)[::-1] for t in zip(*lst)]

for row in lst:
    print(*row)
