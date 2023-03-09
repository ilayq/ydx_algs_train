n, m = map(int, input().split())
gr = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for i in range(m):
    s, e = map(int, input().split())
    if s != e:
        gr[s].append(e)
        gr[e].append(s)
    else:
        gr[s].append(e)

v = []

def dfs(graph, visited, now):
    visited[now] = True
    for n in graph[now]:
        if not visited[n]:
            dfs(graph, visited, n)
dfs(gr, visited, 1)
res = []
for i in range(n+1):
    if visited[i]:
        res.append(i)
print(len(res))
print(' '.join(map(str, sorted(res))))