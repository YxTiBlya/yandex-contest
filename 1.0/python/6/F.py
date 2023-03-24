n, x, y = map(int, input().split())

l, r = 0, max(x, y) * (n-1)
while l < r:
    m = (l + r) // 2
    if m // x + m // y >= n-1:
        r = m 
    else:
        l = m + 1

print(min(x, y) + l)
