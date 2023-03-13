stack = []
ln = 0

while True:
    cmd = input()

    if "push" in cmd:
        cmd, n = cmd.split()
        stack.append(n)
        ln += 1
        print("ok")

    if cmd == "pop":
        if ln == 0:
            print("error")
            continue
        print(stack.pop())
        ln -= 1

    if cmd == "back":
        if ln == 0:
            print("error")
            continue
        print(stack[-1])
    
    if cmd == "size":
        print(ln)
    
    if cmd == "clear":
        stack.clear()
        ln = 0
        print("ok")

    if cmd == "exit":
        print("bye")
        break