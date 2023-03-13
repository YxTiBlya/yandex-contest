minx, miny = 10000000000, 10000000000
maxx, maxy = 0, 0

for i in range(int(input())):
    x, y = map(int, input().split())
    if x < minx: minx = x
    if y < miny: miny = y
    if x > maxx: maxx = x
    if y > maxy: maxy = y

print(minx, miny, maxx, maxy)