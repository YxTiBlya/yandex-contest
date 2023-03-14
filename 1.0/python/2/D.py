lst = list(map(int, input().split()))
ans = 0
if len(lst) >= 3:
    for i in range(1, len(lst)-1):
        if lst[i-1] < lst[i] > lst[i+1]:
            ans += 1
    print(ans)
else:
    print(0)