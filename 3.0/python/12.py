stack = []
ln = 0

for i in input():
    if i in "([{":
        stack.append(i)
        ln += 1
    else:
        if ln == 0:
            ln = -1
            break
        else:
            if i == ")" and stack[-1] == "(":
                stack.pop()
                ln -= 1 
            elif i == "]" and stack[-1] == "[":
                stack.pop()
                ln -= 1 
            elif i == "}" and stack[-1] == "{":
                stack.pop()
                ln -= 1 
            else:
                ln = -1
                break

if ln == 0:
    print("yes")
else:
    print("no")
