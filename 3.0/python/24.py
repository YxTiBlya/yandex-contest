N = int(input())
dp = [0] * (N + 3)
nums = [[0,0,0]] * (N+3)

for i in range(3, N + 3):
    a, b, c = map(int, input().split())

    mn = dp[i-1] + a
    if dp[i-2] + nums[i-1][1] != 0 and dp[i-2] + nums[i-1][1] < mn:
        mn = dp[i-2] + nums[i-1][1]
    if dp[i-3] + nums[i-2][2] != 0 and dp[i-3] + nums[i-2][2] < mn:
        mn = dp[i-3] + nums[i-2][2]

    dp[i] = mn
    nums[i] = [a, b, c]

print(dp[-1])