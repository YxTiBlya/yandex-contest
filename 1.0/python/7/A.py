n, m = map(int, input().split())
events = []

START = -1
END = 1

for _ in range(m):
    start, end = map(int, input().split())
    events.append((start, START))
    events.append((end + 1, END))
events.sort()

open = 0
last = 0
covered = 0
for coord, type in events:
    if open > 0:
        covered += coord - last

    if type == START: 
        open += 1
    else:
        open -= 1

    last = coord

print(n-covered)