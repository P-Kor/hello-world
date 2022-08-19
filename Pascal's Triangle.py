# Pascal's Triangle

def pascal(n):
    if n < 0:
        return []

    for i in range(n + 1):
        if i < 2:
            row = [1] + [1] * i
        else:
            row_previous = row
            row = [1] + [row_previous[j - 1] + row_previous[j] for j in range(1, len(row_previous))] + [1]
    return row

for i in range(15):
    print(pascal(i))