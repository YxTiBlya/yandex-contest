from sys import setrecursionlimit
setrecursionlimit(10000)

N = int(input())

graph = [[] for _ in range(N+1)]
colors = [0 for _ in range(N+1)]
ans = []

for i in range(1, N+1):
    ln = list(map(int, input().split()))
    for j in range(i, len(ln)):
        if ln[j]:
            graph[i].append(j+1)
            graph[j+1].append(i)

flag = False
def dfs(graph, colors, now, prev):
    global flag
    colors[now] = 1

    for neig in graph[now]:
        if colors[neig] == 0:
            if not flag:
                dfs(graph, colors, neig, now)
        elif colors[neig] == 1 and neig != prev:
            flag = True
            break
    
    colors[now] = 2
    if flag:
        ans.append(now)

for i in range(1, N+1):
    if colors[i] == 0:
        if flag:
            break
        dfs(graph, colors, i, 0)

if len(ans) > 0:
    while ans[0] not in graph[ans[-1]]:
        ans.pop()
        
    print("YES")
    print(len(ans))
    print(*ans)
else:
    print("NO")