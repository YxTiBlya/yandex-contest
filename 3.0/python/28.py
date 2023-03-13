N, M = map(int, input().split())
dp = [[0 for j in range(M)] for i in range(N)]
dp[0][0] = 1

for i in range(N-1):
    for j in range(M-1):
        if i == 0 and j == 0 or dp[i][j] != 0:
            if i + 2 < N and j + 1 < M:
                dp[i+2][j+1] += dp[i][j]
            if i + 1 < N and j + 2 < M:
                dp[i+1][j+2] += dp[i][j]

print(dp[-1][-1])