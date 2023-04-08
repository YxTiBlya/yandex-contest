n, k = map(int, input().split())
points = sorted(list(map(int, input().split())))

l, r = 0, points[-1] - points[0]
while l < r:
    m = (l + r) // 2

    cnt = 0
    lr = points[0] - 1
    for point in points:
        if point > lr:
            cnt += 1
            lr = point + m
    
    if cnt <= k:
        r = m
    else:
        l = m + 1

print(l)
