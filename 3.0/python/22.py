N, k = map(int, input().split())
dp = [-1] * N
dp[0] = 1

for i in range(1, N):
    c = 0

    if i >= k:
        for j in range(i-k, i):
            c += dp[j]
    else:
        for j in range(i):
            c += dp[j]

    dp[i] = c

print(dp[-1])