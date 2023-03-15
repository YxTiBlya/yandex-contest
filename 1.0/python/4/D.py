n = int(input())
keys = list(map(int, input().split()))
k = int(input())
presses = list(map(int, input().split()))
dt = {}

for i in range(1, n+1):
    dt[i] = keys[i-1]

for pressing in presses:
    dt[pressing] -= 1

for k, v in dt.items():
    if v < 0:
        print("YES")
    else:
        print("NO")