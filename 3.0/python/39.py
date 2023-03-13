N = int(input())

blocks = []
field = [[[-1 for _ in range(N)] for _ in range(N)] for _ in range(N)]
dm = [-1, 1]
x = y = z = 0

for k in range(N):
    input()

    tmp = []
    for i in range(N):
        layer = input()
        tmp.append(layer)

        for j in range(len(layer)):
            if layer[j] == "S":
                x, y, z = j, i, k

    blocks.append(tmp)

field[z][y][x] = 0
res = {0: [[z, y, x]]}
ans = 0
for i in range(1, N**3):
    res[i] = []
    for coords in res[i-1]:
        for delta in range(2):
            z = coords[0]
            y = coords[1]
            x = coords[2]

            if 0 <= z + dm[delta] < N and blocks[z + dm[delta]][y][x] == ".":
                if field[z + dm[delta]][y][x] == -1:
                    field[z + dm[delta]][y][x] = i
                    res[i].append([z + dm[delta], y, x])
                    if z + dm[delta] == 0 and ans == 0:
                        ans = i
                        break
            if 0 <= y + dm[delta] < N and blocks[z][y + dm[delta]][x] == ".":
                if field[z][y + dm[delta]][x] == -1:
                    field[z][y + dm[delta]][x] = i
                    res[i].append([z, y + dm[delta], x])
            if 0 <= x + dm[delta] < N and blocks[z][y][x + dm[delta]] == ".":
                if field[z][y][x + dm[delta]] == -1:
                    field[z][y][x + dm[delta]] = i
                    res[i].append([z, y, x + dm[delta]])

    if len(res[i]) == 0:
        break
print(ans)