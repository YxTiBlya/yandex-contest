dt = {}
with open("input.txt", "r") as f:
    for line in f.readlines():
        f, n = line.split()

        if f not in dt:
            dt[f] = 0
        dt[f] += int(n)

for item in sorted(list(dt.items())):
    print(*item)