n, k = map(int, input().split())
checkers = sorted(list(map(int, input().split())))
dt = {}

for now in checkers:
    if now not in dt:
        dt[now] = 0
    dt[now] += 1
uniqnums = list(dt.keys())

right = 0
ans = 0
dup = 0
for left in range(len(uniqnums)):
    while right < len(uniqnums) and uniqnums[left] * k >= uniqnums[right]:
        if dt[uniqnums[right]] >= 2:
            dup += 1
        right += 1

    rngln = right - left
    if dt[uniqnums[left]] >= 2:
        ans += (rngln - 1) * 3
    if dt[uniqnums[left]] >= 3:
        ans += 1

    ans += (rngln - 1) * (rngln - 2) * 3
    if dt[uniqnums[left]] >= 2:
        dup -= 1
    ans += dup * 3

print(ans)