N = int(input())
graph = {i + 1: [] for i in range(N)}

for i in range(N): 
    row = list(map(int, input().split()))

    for j in range(N):
        if row[j]:
            graph[i+1].append(j+1)
start, end = map(int, input().split())

def bfs(graph, start, end):
    if start == end:
        return -1
    queue = [(start, [start])]
    visited = set()

    while queue:
        v, path = queue.pop(0)
        visited.add(v)
        for node in graph[v]:
            if node == end:
                return path + [end]
            else:
                if node not in visited:
                    visited.add(node)
                    queue.append((node, path + [node]))

ans = bfs(graph, start, end)
print(ans)
if ans:
    if ans == -1:
        print(0)
    else:
        print(len(ans)-1)
else:
    print(-1)