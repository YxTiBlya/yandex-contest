n = int(input())
lst = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

def l_bin_search(x):
    l, r = 0, n-1
    while l < r:
        m = (l + r) // 2
        if lst[m] >= x:
            r = m
        else:
            l = m + 1
        
    return l

def r_bin_search(x):
    l, r = 0, n-1
    while l < r:
        m = (l + r + 1) // 2
        if lst[m] <= x:
            l = m 
        else:
            r = m - 1
        
    return l

for num in nums:
    l = l_bin_search(num)
    r = r_bin_search(num)
    if lst[l] != num or lst[r] != num:
        print(0, 0)
    else:
        print(l+1, r+1)
