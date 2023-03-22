n, k = map(int, input().split())
s = input()

dt = dict.fromkeys(s, 0)
left, right, ansl, ansr = 0, 0, 0, 0
while right < n:
    if dt[s[right]] < k:
        if right - left > ansr - ansl:
            ansl, ansr = left, right
        dt[s[right]] += 1
        right += 1
    else:
        left = right - k + 1
        dt = dict.fromkeys(dt, 0)

print(ansr - ansl + 1, ansl + 1)