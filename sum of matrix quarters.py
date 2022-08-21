# sum of matrix quarters.py

# 1 4 3 4 7
# 5 6 7 8 4
# 3 8 5 6 1
# 1 2 9 4 8
# 5 6 1 5 8
# Top quarter: 18
# Right quarter: 19
# Bottom quarter: 21
# Left quarter: 17
labels = 'Top quarter\nRight quarter\nBottom quarter\nLeft quarter'


n = 5
s = '1 4 3 4 7\n5 6 7 8 4\n3 8 5 6 1\n1 2 9 4 8\n5 6 1 5 8'
inp = iter(s.split('\n'))

# n = int(input())
# def m_input():
#     while True:
#         yield input()
# inp = m_input()

lst = [list(map(int, next(inp).split())) for _ in range(n)]

res = [0] * 4
for i, row in enumerate(lst):
    print(*row)
    for j, m in enumerate(row):
        t = (j > i and j < n - i - 1, j > i and j > n - i -1, j < i and j > n - i -1, j < i and j < n - i -1)
        match t:
            case (True, False, False, False):
                res[0] += m
            case (False, True, False, False):
                res[1] += m
            case (False, False, True, False):
                res[2] += m
            case (False, False, False, True):
                res[3] += m

for v, label in zip(res, labels.split('\n')):
    print(f'{label}: {v}')
