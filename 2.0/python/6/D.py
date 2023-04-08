a, k, b, m, x = map(int, input().split())
l, r = 0, x*2 // a+1
while l < r:
    d = (l + r) // 2
    if (d - d//k) * a + (d - d//m) * b < x:
        l = d + 1
    else:
        r = d

print(l)