lst = []
ans = 0

for _ in range(int(input())):
    lst.append(int(input()))

for i in range(len(lst)-1):
    if lst[i] <= lst[i+1]:
        ans += lst[i]
    else:
        ans += lst[i+1]

print(ans)