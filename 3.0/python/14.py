N = int(input())
wagons = list(map(int, input().split()))
stack = []
stack2 = []

for i in wagons:
    if len(stack) > 0:
        for j in reversed(stack):
            if i > j:
                stack2.append(stack.pop())
            else:
                break
        stack.append(i)

    else:
        stack.append(i)

for i in reversed(stack):
    if len(stack2) > 0:
        if i < stack2[-1]: break
    stack2.append(i)
    stack.pop()

for i in range(1, len(stack2)):
    if stack2[i] < stack2[i-1]:
        stack2[0] = -1

if len(stack2) == N and stack2[0] == 1:
    print("YES")
else:
    print("NO")