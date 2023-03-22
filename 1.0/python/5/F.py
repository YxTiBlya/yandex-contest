n = int(input())
capacities = sorted(list(map(int, input().split())))
conditioners = []

for _ in range(int(input())):
    power, cost = map(int, input().split())
    conditioners.append([cost, power])
conditioners.sort()

left = 0
ans = 0
for capacity in capacities:
    while conditioners[left][1] < capacity:
        left += 1
    
    ans  += conditioners[left][0]

print(ans)