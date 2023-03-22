n, k = map(int, input().split())
colors = list(map(int, input().split()))
left = right = 0
aleft, aright = 0, n
numsInWindow = 0
dt = {}

while right < n:
    if dt.get(colors[right]) == None:
        dt[colors[right]] = 0
    dt[colors[right]] += 1
    
    if dt[colors[right]] == 1:
        numsInWindow += 1
    right += 1

    while numsInWindow == k:
        dt[colors[left]] -= 1
        if dt[colors[left]] == 0:
            numsInWindow -= 1
        left += 1
        
        if right - left < aright - aleft:
            aleft, aright = left, right

print(aleft, aright)