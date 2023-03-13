f = open("input.txt")
dict = {}
mx = 0

for line in f:
    b = line.split()
    line = "".join(b)
    for c in line:
        if c not in dict:
            dict[c] = 0
        dict[c] += 1
        mx = max(mx, dict[c])

s = ""
for i in dict:
    s += i
s = sorted(s)

for i in range(mx):
    str = ""
    for i in s:
        if dict[i] >= mx:
            str += "#"
        else:
            str += " "
    print(str)
    mx -= 1

print(*s, sep="")