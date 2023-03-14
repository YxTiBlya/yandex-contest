N = int(input())
lst = list(map(int, input().split()))
find = int(input())

diff = float("inf")
ans = 0
for num in lst:
    if abs(find - num) < diff:
        ans, diff = num, abs(find-num)
    
print(ans)