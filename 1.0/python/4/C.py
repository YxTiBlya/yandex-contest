dt = {}
with open("input.txt", "r") as f:
    for line in f.readlines():
        for word in line.split():
            if dt.get(word) == None:
                dt[word] = 0
            dt[word] += 1

key = list(dt.keys())[0]
for k, v in dt.items():
    if v > dt[key] or k < key and v == dt[key]:
        key = k
print(key)