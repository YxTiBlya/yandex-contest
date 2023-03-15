dt = {}
ans = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        for word in line.split():
            if dt.get(word) == None:
                dt[word] = 0
            else:
                dt[word] += 1
            ans.append(dt[word])

print(*ans)