lst = list(map(int, input().split()))

flag = True
for i in range(1, len(lst)):
    if lst[i] <= lst[i-1]:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")