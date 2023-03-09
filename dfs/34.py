import sys

sys.setrecursionlimit(10 ** 5)


n, m = map(int, input().split())
gr = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for i in range(m):
    s, e = map(int, input().split())
    gr[s].append(e)
srt = []
def dfs(v):
    f = True
    visited[v] = 1
    for neigh in gr[v]:
        if visited[neigh] == 1:
            return False
        else:
            if visited[neigh] == 2:
                continue
            else:
                f = f and dfs(neigh)
    visited[v] = 2
    srt.append(v)
    return f
f = True
for i in range(1, n+1):
    if not visited[i]:
        f = f and dfs(i)
print(' '.join(map(str, srt[::-1]))) if f else print(-1)
# print(srt)