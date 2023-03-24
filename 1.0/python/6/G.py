n = int(input())
m = int(input())
t = int(input())

l, r = 0, min(n, m)
while l < r:
    width = (l + r + 1) // 2

    res = (width * m * 2) + (width * (n - width*2) * 2)
    if 0 < res <= t and width <= n//2 and width <= m//2:
        l = width
    else:
        r = width - 1

print(l)