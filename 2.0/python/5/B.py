n = int(input())
lst = list(map(int, input().split()))

tmp = 0
mx = lst[0]
for i in lst:
    tmp += i
    mx = max(mx, tmp)
    if tmp < 0:
        tmp = 0

print(mx)