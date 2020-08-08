x, y = [], []
coords = [(1, 7), (2, 7), (3, 2), (4, 8), (5, 6), (6, 1), (7, 3), (8, 5)]

for i in range(8):
    new_x, new_y = coords[i]
    x.append(new_x)
    y.append(new_y)

correct = True
for i in range(8):
    for j in range(i + 1, 8):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False

if correct:
    print('NO')
else:
    print('YES')
