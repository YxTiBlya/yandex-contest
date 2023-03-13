queue = []
i = 0
ln = 0

while True:
    cmd = input()

    if "push" in cmd:
        print("ok")
        cmd, n = cmd.split()
        queue.append(n)
        ln += 1

    if cmd == "pop":
        if ln-i > 0:
            print(queue[i])
            i += 1
        else:
            print("error")

    if cmd == "front":
        if ln-i > 0:
            print(queue[i])
        else:
            print("error")

    if cmd == "size":
        print(ln-i)

    if cmd == "clear":
        print("ok")
        queue.clear()
        ln, i = 0, 0

    if cmd == "exit":
        print("bye")
        break