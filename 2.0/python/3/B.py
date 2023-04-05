nums = list(map(int, input().split()))
dt = {}

for num in nums:
    if num not in dt:
        dt[num] = True
        print("NO")
    else:
        print("YES")