nums = list(map(int, input().split()))
dt = {}

for num in nums:
    if num not in dt:
        dt[num] = 0
    dt[num] += 1

for num in nums:
    if dt[num] == 1:
        print(num, end=" ")