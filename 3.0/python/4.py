import sys

N = int(input())
K = int(input())
series = int(input())
place = int(input())
tmp = []

pplace = series * 2
if place == 1: pplace -= 1

pvar = pplace
if pplace > K: pvar %= K

tmp.append(pplace - K)
tmp.append(pplace + K)

for i in range(len(tmp)-1, -1, -1):
    if tmp[i] > N or tmp[i] < 1:
        tmp.pop(i)

if len(tmp) == 2:
    if abs(series - (tmp[0] + 1)//2) < abs(series - (tmp[1] + 1)//2):
        vseries = (tmp[0] + 1)//2
    else:
        vseries = (tmp[1] + 1)//2

    if vseries == (tmp[0] + 1)//2:
        vplace = tmp[0]
    else:
        vplace = tmp[1]
elif len(tmp) == 1:
    vseries = (tmp[0] + 1)//2
    vplace = tmp[0]
else:
    print(-1)
    sys.exit()

if vplace % 2 == 0:
    vn = 2
else:
    vn = 1

print(vseries, vn)