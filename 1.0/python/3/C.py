N, M = map(int, input().split())
ann = set()
bor = set()

for _ in range(N):
    ann.add(int(input()))
for _ in range(M):
    bor.add(int(input()))

inter = sorted(list(ann.intersection(bor)))
print(len(inter))
print(*inter)
anndiff = sorted(list(ann.difference(bor)))
print(len(anndiff))
print(*anndiff)
bordiff = sorted(list(bor.difference(ann)))
print(len(bordiff))
print(*bordiff)