deq = []

while True:
    cmd = input()

    if "push" in cmd:
        cmd, n = cmd.split()
        if "front" in cmd:
            deq.insert(0, n)
        else:
            deq.append(n)
        print("ok")

    if "pop" in cmd:
        if len(deq) > 0:
            if "front" in cmd:
                print(deq.pop(0))
            else:
                print(deq.pop())
        else:
            print("error")

    if cmd == "front":
        if len(deq) > 0:
            print(deq[0])
        else:
            print("error")
    
    if cmd == "back":
        if len(deq) > 0:
            print(deq[-1])
        else:
            print("error")

    if cmd == "size":
        print(len(deq))
    
    if cmd == "clear":
        deq.clear()
        print("ok")

    if cmd == "exit":
        print("bye")
        break