n, m = map(int, input().split())
sections = []

START = -1
MIDDLE = 0
END = 1

for _ in range(n):
    a, b = map(int, input().split())
    sections.append([min(a, b), START])
    sections.append([max(a, b), END])

dt = {}
nums = list(map(int, input().split()))
for num in nums:
    dt[num] = 0
    sections.append([num, MIDDLE])
sections.sort()

open = 0
for section in sections:
    if section[1] == START:
        open += 1
    elif section[1] == END:
        open -= 1
    else:
        dt[section[0]] = open

for num in nums:
    print(dt[num], end=" ")