N, M = map(int, input().split())
dp = [[0] * (M+1)]
prev = [["0"] * (M+1) for i in range(N+1)]
cert = []

for i in range(1, N+1):
    row = [0] + list(map(int, input().split()))

    for j in range(1, len(row)):
        if dp[i-1][j] >= row[j-1]:
            row[j] += dp[i-1][j]
            prev[i][j] = "D"
        else:
            row[j] += row[j-1]
            prev[i][j] = "R"
    
    dp.append(row)


i, j = N, M
while prev[i][j] != "0":
    cert.append(prev[i][j])

    if prev[i][j] == "D":
        i -= 1
    elif prev[i][j] == "R":
        j -= 1
        
print(dp[-1][-1])
for i in range(len(cert)-2, -1, -1):
    print(cert[i], end=" ")