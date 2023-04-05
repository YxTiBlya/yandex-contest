n = int(input())
dt = {}
topics = [" " for _ in range(n+1)]
for i in range(1, n+1):
    num = int(input())
    
    if num == 0:
        topic = input()
        msg = input()
        dt[topic] = 0
        topics[i] = topic
    else:
        msg = input()
        topic = topics[num]
        topics[i] = topic
        dt[topic] += 1

mx = max(dt.values())
for k, v in dt.items():
    if v == mx:
        print(k)
        break