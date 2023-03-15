n  = int(input())
droped = set()
for i in range(n):
    x, y = map(int, input().split())
    droped.add(x)
print(len(droped))