from sys import setrecursionlimit
setrecursionlimit(100000)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = {i: False for i in range(len(graph))}
components = {}

for _ in range(m):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)

def dfs(graph, visited, now, compc):
    visited[now] = True

    if components.get(compc) == None:
        components[compc] = set()
    
    if len(graph[now]) > 0:
        components[compc].update(graph[now])
    else:
        components[compc].add(now)

    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig, compc)

compc = 1
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, visited, i, compc)
        compc += 1
        
print(compc-1)
for k, v in components.items():
    print(len(v))
    print(*v)