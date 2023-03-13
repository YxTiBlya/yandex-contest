n = int(input())
g = list(map(int, input().split()))

g.sort()

dp = [0] * (n + 1)
dp[2] = g[1] - g[0]

if n > 2:
    dp[3] = g[2] - g[0]
    for i in range(4, n + 1):
        dp[i] = min(dp[i - 1], dp[i - 2]) + g[i - 1] - g[i - 2]
print(dp[n])