N = int(input())
pr = list(map(int, input().split()))
stack = []
ans = [-1 for i in range(N)]
ln = 0

for i, v in enumerate(pr):
    if ln > 0:
        for j in reversed(stack):
            if v < j[1]:
                x = stack.pop()
                ln -= 1
                ans[x[0]] = i
            else:
                break

        stack.append([i, v])
        ln += 1
    else:
        stack.append([i, v])
        ln += 1

print(*ans)