import itertools

inp = itertools.cycle('.*')
n, m = map(int, (input().split()))

lst = [[next(inp) for _ in range(m)] for i in range(n) if i == 0 or (m & 1) or next(inp)]

for row in lst:
    print(*row)
