r = int(input())
i = int(input())
c = int(input())

if i == 0:
    if r != 0:
        ans = 3
    else:
        ans = c
elif i == 1:
    ans = c
elif i == 4:
    if r != 0:
        ans = 3
    else:
        ans = 4
elif i == 6:
    ans = 0
elif i == 7:
    ans = 1
else:
    ans = i

print(ans)