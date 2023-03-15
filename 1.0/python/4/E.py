dt = {}
for _ in range(int(input())):
    h, w = map(int, input().split())
    dt[h] = max(dt.get(h, w), w)

print(sum(dt.values()))