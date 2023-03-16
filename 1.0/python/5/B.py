n, k = map(int, input().split())
cars = list(map(int, input().split()))
prefix = [0 for _ in range(n+1)]

for i in range(1, len(cars)+1):
    prefix[i] = cars[i-1] + prefix[i-1]

left, right = 0, 1
ans = 0
while left < right and right < n+1:
    if prefix[right] - prefix[left] == k:
        ans += 1
        left, right = left+1, right+1
    elif prefix[right] - prefix[left] < k:
        right += 1
    elif prefix[right] - prefix[left] > k:
        left += 1

    if right - left == 0:
        right += 1

print(ans)
