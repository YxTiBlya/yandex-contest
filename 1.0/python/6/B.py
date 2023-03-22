n, k = map(int, input().split())
nm = list(map(int, input().split()))
km = list(map(int, input().split()))

def bin_search(x):
    l = 0
    r = n - 1

    while r - l > 1:
        m = (l + r) // 2
        if nm[m] >= x:
            r = m
        else:
            l = m
    
    if x - nm[l] <= nm[r] - x:
        return nm[l]
    return nm[r]
    
for num in km:
    print(bin_search(num))