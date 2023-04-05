dt = {}
with open("input.txt", "r") as f:
    for line in f.readlines():
        words = list(line.split())
        for word in words:
            if word not in dt:
                dt[word] = 0
            dt[word] += 1

for item in sorted(dt.items(), key=lambda x: (-x[1], x[0])):
    print(item[0])