l, k = map(int, input().split())
blocks = list(map(int, input().split()))
if l % 2 == 0:
    m = (l - 1) / 2
else:
    m = l // 2

for i in range(k):
    if blocks[i] == m:
        print(m)
        break
    elif blocks[i] > m:
        print(blocks[i-1], blocks[i])
        break
