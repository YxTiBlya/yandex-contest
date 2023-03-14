N, M, K = map(int, input().split())
field = [[0 for _ in range(M)] for _ in range(N)]

dy = [-1, -1, -1, 0, 1, 1,  1,  0]
dx = [-1,  0,  1, 1, 1, 0, -1, -1]

for _ in range(K):
    y, x = map(int, input().split())
    field[y-1][x-1] = "*"

for y in range(N):
    for x in range(M):
        for delta in range(8):
            ny = y + dy[delta]
            nx = x + dx[delta]

            if 0 <= ny < N and 0 <= nx < M:
                if field[ny][nx] == "*" and field[y][x] != "*":
                    field[y][x] += 1

for line in field:
    print(*line)
