M = int(input())
N = int(input())
os = []

for _ in range(N):
    a, b = map(int, input().split())

    j = len(os)-1
    while j >= 0:
        if os[j][1] >= a and os[j][0] <= a or os[j][0] <= b and os[j][1] >= b or os[j][0] >= a and os[j][1] <= b:
            os.pop(j)
        j -= 1
        
    os.append([a, b])

print(len(os))
