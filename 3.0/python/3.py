n = int(input())
cards = list(set(map(int, input().split())))
k = int(input())
interests = list(list(map(int, input().split())))

cards.sort()
mx = cards[-1]
ln = len(cards)

def search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    if arr[mid] < x:
        return mid + 1
    return mid

for interest in interests:
    if interest > mx:
        print(ln)
    else:
        print(search(cards, interest))