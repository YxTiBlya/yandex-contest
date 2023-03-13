N, M, S, T, Q = map(int, input().split())
S, T = S-1, T-1

field = [[-1]*M for _ in range(N)]
field[S][T] = 0
res = {0: [(T, S)]}

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

for i in range(1, N * M):
    res[i] = []
    for coords in res[i - 1]:
        for delta in range(8):
            x = coords[0] + dx[delta]
            y = coords[1] + dy[delta]
            if 0 <= x < M and 0 <= y < N:
                if field[y][x] == -1:
                    field[y][x] = i
                    new = (x, y)
                    res[i].append(new)

ans = 0
for _ in range(Q):
    y, x = map(int, input().split())
    x -= 1
    y -= 1
    if field[y][x] == -1:
        ans = -1
        break
    ans += field[y][x]
print(ans)