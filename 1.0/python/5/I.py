k = int(input())
operations = input()
prevLn = 0
ans = 0

for i in range(k, len(operations)):
    if operations[i] == operations[i-k]:
        prevLn += 1
        ans += prevLn
    else:
        prevLn = 0

print(ans)