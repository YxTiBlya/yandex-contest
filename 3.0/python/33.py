n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)

def dfs(graph, visited, now, color):
    visited[now] = color
    color = 3 - color

    for neig in graph[now]:
        if visited[neig] == 0:
            dfs(graph, visited, neig, color)


color = 1
for i in range(1, n+1):
    if visited[i] == 0:
        dfs(graph, visited, i, color)
        color = 3 - color


flag = True
for i in range(1, n+1):
    for node in graph[i]:
        if visited[node] == visited[i]:
            flag = False
            break

if flag:
    print("YES")
else:
    print("NO")