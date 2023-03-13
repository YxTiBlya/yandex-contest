N, M = map(int, input().split())
dp = [[100000] + [0] + [100000]*(M-1)]

for i in range(1, N+1):
    row = [100000] + list(map(int, input().split()))

    for j in range(1, len(row)):
        row[j] += min(dp[i-1][j], row[j-1])
        
    dp.append(row)

print(dp[-1][-1])