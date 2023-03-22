w, h, n = map(int, input().split())

l = max(w, h)
r = l * n
while l < r:
    m = (l + r) // 2
    if (m // w) * (m // h) >= n:
        r = m
    else:
        l = m + 1

print(l)