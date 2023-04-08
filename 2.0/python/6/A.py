n = int(input())
nums = sorted(list(map(int, input().split())))

def l_bin_search(x):
    l, r = 0, n-1
    while l < r:
        m = (l + r) // 2
        if nums[m] >= x:
            r = m
        else:
            l = m + 1
        
    return l

def r_bin_search(x):
    l, r = 0, n-1
    while l < r:
        m = (l + r + 1) // 2
        if nums[m] <= x:
            l = m 
        else:
            r = m - 1
        
    return l

ans = []
for i in range(int(input())):
    s, e = map(int, input().split())

    if s == e and (s < nums[0] or s > nums[-1]):
        ans.append(0)
    else:
        ans.append(r_bin_search(e) - l_bin_search(s) + 1)

print(*ans)