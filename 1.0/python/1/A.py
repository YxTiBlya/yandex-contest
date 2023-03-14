troom, tcond = map(int, input().split())
mode = input()

if mode == "heat":
    if troom < tcond:
        print(tcond)
    else:
        print(troom)

elif mode == "freeze":
    if troom > tcond:
        print(tcond)
    else:
        print(troom)

elif mode == "auto":
    print(tcond)

elif mode == "fan":
    print(troom)