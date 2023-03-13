stack = []

for i in list(input().split()):
    try:
        stack.append(int(i))
    except Exception:
        if i == "+":
            stack.append(stack.pop() + stack.pop())
        elif i == "*":
            stack.append(stack.pop() * stack.pop())
        elif i == "-":
            i2 = stack.pop()
            stack.append(stack.pop() - i2)

print(stack[0])