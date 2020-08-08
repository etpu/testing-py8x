coords = []
coord_x = []
coord_y = []
f = [[] for _ in range(8)]

for i in range(8):
    x, y = [int(z) for z in input().split()]
    cord = x, y
    coord_x.append(x)
    coord_y.append(y)
    coords.append(cord)

coord_x = set(coord_x)
coord_y = set(coord_y)

if len(coord_x) < 8 or len(coord_y) < 8:
    print("YES")
else:
    for i in range(8):
        x, y = coords[i][0], coords[i][1]
        if x >= y:
            z = x - y
            for j in range(1, 9 - z):
                f[i].append((j + z, j))
        if x < y:
            z = y - x
            for j in range(1, 9 - z):
                f[i].append((j, j + z))
        if x + y >= 10:
            z = 16 - (x + y + 1)
            for j in range(z):
                f[i].append((8 - j, (8 + j) - (z + 1)))
        if x + y < 10:
            z = x + y - 1
            for j in range(z):
                f[i].append((j + 1, z - j))
        f[i] = list(set(f[i]))
        if len(set(f[i] + coords)) - len(f[i]) != 7:
            print("YES")
            break
        else:
            if i == 7:
                print("NO")

#coords = [(1, 7), (2, 7), (3, 2), (4, 8), (5, 6), (6, 1), (7, 3), (8, 5)]