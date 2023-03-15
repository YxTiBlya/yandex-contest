dt = {}

def create_acc(name: str):
    if dt.get(name) == None:
        dt[name] = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        cmd = line.split()
        if cmd[0] == "DEPOSIT":
            create_acc(cmd[1])
            dt[cmd[1]] += int(cmd[2])
        elif cmd[0] == "WITHDRAW":
            create_acc(cmd[1])
            dt[cmd[1]] -= int(cmd[2])
        elif cmd[0] == "TRANSFER":
            create_acc(cmd[1])
            create_acc(cmd[2])
            dt[cmd[1]] -= int(cmd[3])
            dt[cmd[2]] += int(cmd[3])
        elif cmd[0] == "INCOME":
            p = int(cmd[1])
            for name, value in dt.items():
                if value >= 0:
                    dt[name] += int(dt[name]/100 * p)

        elif cmd[0] == "BALANCE":
            if dt.get(cmd[1]) == None:
                print("ERROR")
            else:
                print(dt[cmd[1]])