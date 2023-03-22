n, a, b, w, h = map(int, input().split())

l, r = 0, min(w, h)
while l < r:
    d = (l + r + 1) // 2
    x = max((w // (a + 2 * d)) * (h // (b + 2 * d)), (h // (a + 2 * d)) * (w // (b + 2 * d)))
    if x >= n:
        l = d
    else:
        r = d - 1

print(l)
