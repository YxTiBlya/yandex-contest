N = int(input())
graph = {i + 1: [] for i in range(N)}
queue = []

for i in range(N): 
    row = list(map(int, input().split()))

    for j in range(N):
        if row[j]:
            graph[i+1].append(j+1)
start, end = map(int, input().split())

queue = [(start, [start])]
visited = set()

def bfs(graph, start, end):
    if start == end:
        return -1

    while queue:
        v, path = queue.pop(0)
        visited.add(v)
        for node in graph[v]:
            if node not in visited:
                if node == end:
                    return path + [end]
                queue.append((node, path + [node]))

ans = bfs(graph, start, end)
if ans:
    if ans == -1:
        print(0)
    else:
        print(len(ans)-1)
        print(*ans)
else:
    print(-1)