N = int(input())
M = int(input())
lines = [[] for _ in range(N+1)]

for _ in range(M):
    line = list(map(int, input().split()))
    for i in line[1:]:
        for j in line[1:]:
            if i != j:
                lines[i].append(j)
start, end = map(int, input().split())
queue = [(start, [start])]
visited = set()

print(lines)

def bfs(lines, end):
    while queue:
        v, path = queue.pop(0)
        visited.add(v)
        for node in lines[v]:
            if node not in visited:
                if node == end:
                    return path + [end]
                queue.append((node, path + [node]))

ans = bfs(lines, end)
if ans:
    print(len(ans)-2)
else:
    print(-1)