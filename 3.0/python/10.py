word = input()
dt = {}

for i in range(len(word)):
    if dt.get(word[i]) == None:
        dt[word[i]] = 0

    dt[word[i]] += len(word[:i+1]) * len(word[i:])

dt = dict(sorted(dt.items()))
for k, v in dt.items():
    print(f"{k}: {v}")