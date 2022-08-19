# Pascal's Triangle

def pascal(n):
    if n < 0:
        return []

    row = [1]
    if n > 0:
        for _ in range(n):
            row = [sum(pair) for pair in zip([0] + row, row +[0])]
    return row

for i in range(5):
    print(pascal(i))