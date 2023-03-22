n, k = map(int, input().split())
nm = list(map(int, input().split()))
km = list(map(int, input().split()))

def bin_search(x):
    low = 0
    high = n-1

    while low <= high:
        mid = (low + high) // 2
        if nm[mid] < x:
            low = mid + 1
        elif nm[mid] > x:
            high = mid - 1
        else:
            return "YES"
    
    return "NO"


for num in km:
    print(bin_search(num))