# soltion without stack
c = 0
for i in input():
    if i == "(":
        c += 1
    else:
        c -= 1
        if c < 0: break

if c == 0:
    print("YES")
else:
    print("NO")