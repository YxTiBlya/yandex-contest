houses = list(map(int, input().split()))
dist = [0 for _ in range(10)]

pos = -1
for i in range(10):
    if houses[i] == 2:
        pos = i
    elif houses[i] == 1 and pos != -1:
        dist[i] = i - pos

pos = -1
for i in range(9, -1, -1):
    if houses[i] == 2:
        pos = i
    elif houses[i] == 1 and pos != -1:
        if dist[i] != 0:
            dist[i] = min(pos - i, dist[i])
        else:
            dist[i] = pos - i

print(max(dist))