from sys import setrecursionlimit
setrecursionlimit(1000000)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
colors = [0 for _ in range(n+1)]
ans = []

for _ in range(m):
    v, e = map(int, input().split())
    graph[v].append(e)

def dfs(graph, colors, now):
    global flag
    colors[now] = 1

    for neig in graph[now]:
        if colors[neig] == 0:
            dfs(graph, colors, neig)
        elif colors[neig] == 1:
            flag = False
            break

    colors[now] = 2
    ans.append(now)

flag = True
for i in range(1, n+1):
    if colors[i] == 0:
        dfs(graph, colors, i)

if flag:
    print(*reversed(ans))
else:
    print(-1)