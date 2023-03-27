nums = []
n, k = map(int, input().split())

for _ in range(n):
    nums.append(int(input()))

l, r = 0, sum(nums)
while l < r:
    m = (l + r + 1) // 2

    ans = 0
    for num in nums:
        ans += num//m

    if ans >= k:
        l = m
    else:
        r = m - 1

print(l)