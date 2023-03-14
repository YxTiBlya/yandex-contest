a, b, c, d = map(int, input().split())
l = []
l.append(max(a, c) * (b + d))
l.append(max(a, d) * (b + c))
l.append(max(b, c) * (a + d))
l.append(max(b, d) * (a + c))

ansa, ansb = 0, 0

if min(l) == l[0]:
    ansa, ansb = max(a, c), b + d
elif min(l) == l[1]:
    ansa, ansb = max(a, d), b + c
elif min(l) == l[2]:
    ansa, ansb = max(b, c), a + d
else:
    ansa, ansb = max(b, d), a + c

with open("output.txt", "w") as f:
    f.write(f"{ansa} {ansb}\n")