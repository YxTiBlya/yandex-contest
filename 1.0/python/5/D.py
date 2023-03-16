n, r = map(int, input().split())
monuments = list(map(int, input().split()))

left, right = 0, 1
ans = 0
while left < len(monuments)-1 and right < len(monuments):
    if monuments[right] - monuments[left] > r:
        ans += n - right
        left += 1
    else:
        right += 1

print(ans)