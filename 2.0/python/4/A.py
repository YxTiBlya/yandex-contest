dt = {}
for _ in range(int(input())):
    c, n = map(int, input().split())

    if c not in dt:
        dt[c] = 0
    dt[c] += n

for item in sorted(list(dt.items())):
    print(*item)