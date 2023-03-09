n, m = map(int, input().split())
gr = [[] for _ in range(n+1)]
for i in range(m):
    s, e = map(int, input().split())
    gr[s].append(e)
    gr[e].append(s)
visited = [0 for _ in range(n+1)]

def dfs(v, color):
    f = True
    visited[v] = color
    for i in gr[v]:
        if visited[i]:
            if visited[i] != 3 - color:
                return False
            else:
                continue
        else:
            f = f and dfs(i, 3-color)
    return f
f = True
color = 1
for i in range(1, n+1):
    if not visited[i]:
        f = f and dfs(i, color)
        color = 3 - color
print(visited)
print("YES") if f else print("NO")