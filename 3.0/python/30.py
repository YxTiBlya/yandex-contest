N = int(input())
np = [0] + list(map(int, input().split()))
M = int(input())
mp = [0] + list(map(int, input().split()))

dp = [[0 for j in range(M+1)] for i in range(N+1)]
cert = []
for i in range(1, N+1):
    for j in range(1, M+1):
        if np[i] == mp[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

i, j = N, M
while dp[i][j] != 0:
    if dp[i][j-1] == dp[i][j]:
        j -= 1
    elif dp[i-1][j] == dp[i][j]:
        i -= 1
    else:
        cert.append(np[i])
        i, j = i-1, j-1
    
print(*reversed(cert))