lst = []
cnt = 0
i = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        words = line.split()
        c = int(words[-1])
        pname = ' '.join(words[:-1])
        lst.append([pname, c, i])
        cnt += c
        i += 1

f = cnt / 450
free = 450
for i in range(len(lst)):
    party = lst[i]
    party.append(party[1] // f)
    free -= party[1] // f
    party.append(party[1] % f)

lst.sort(key=lambda x: x[4], reverse=True)
for i in range(int(free)):
    lst[i][3] += 1
    
lst.sort(key=lambda x: x[2])
for party in lst:
    print(party[0], int(party[3]))
