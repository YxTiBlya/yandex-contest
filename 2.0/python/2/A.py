dt = {}
mx = 0

while True:
    num = int(input())
    if num == 0:
        break

    if dt.get(num) == None:
        dt[num] = 0

    dt[num] += 1
    mx = max(mx, num)

print(dt[mx])