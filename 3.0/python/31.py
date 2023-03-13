from sys import setrecursionlimit
setrecursionlimit(10000)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = {i: False for i in range(len(graph))}

for _ in range(M):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)

def dfs(graph, visited, now):
    visited[now] = True
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig)

dfs(graph, visited, 1)

ans = []
for k, v in visited.items():
    if v:
        ans.append(k)

print(len(ans))
print(*ans)