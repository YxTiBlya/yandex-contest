N = int(input())

if N == 0:
    print(0)
    print(0, 0)
elif N == 1:
    a = int(input())
    print(a)
    if a > 100:
        print(1, 0)
    else:
        print(0, 0)
else:
    a = [0 for _ in range(N)]
    for i in range(N):
        a[i] = int(input())
    dp = [[float('inf') for _ in range(N + 1)] for _ in range(N)]

    if a[0] > 100:
        dp[0][1] = a[0]
    else:
        dp[0][0] = a[0]

    for i in range(1, N):
        for j in range(N):
            if a[i] > 100:
                dp[i][j] = min(dp[i-1][j-1] + a[i], dp[i-1][j+1])
            else:
                dp[i][j] = min(dp[i-1][j] + a[i], dp[i-1][j+1])

    ans = float('inf')
    k1 = k2 = 0
    for j in range(N):
        if dp[N-1][j] <= ans:
            ans = dp[N-1][j]
            k1 = j
    days = []
    tmp = k1
    for i in range(N - 1, 0, -1):
        if dp[i][tmp] == dp[i - 1][tmp + 1]:
            k2 += 1
            days.append(i + 1)
            tmp += 1
        elif dp[i][tmp] == dp[i - 1][tmp] + a[i]:
            pass
        elif dp[i][tmp] == dp[i-1][tmp-1] + a[i]:
            tmp -= 1

    print(ans)
    print(k1, k2)
    print(*reversed(days))