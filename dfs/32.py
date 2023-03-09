import sys

#TODO TL
# sys.setrecursionlimit(10000)
# print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
gr = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for i in range(m):
    s, e = map(int, input().split())
    if s != e:
        gr[s].append(e)
        gr[e].append(s)
    else:
        gr[s].append(e)

comps = []
c = 1
def dfs(vertex):
    visited[vertex] = c
    for neigh in gr[vertex]:
        if not visited[neigh]:
            dfs(neigh)

for v in range(1, len(gr)):
    # print(visited[:10000])
    if not visited[v]:
        # print(v)
        dfs(v)
        c += 1
c = sorted(list(set(visited)))
c.remove(0)
def findall(lst, val):
    for i in range(len(lst)):
        if lst[i] == val:
            yield i
res = []
for i in c:
    r = findall(visited, i)
    t = []
    for i in r:
        t.append(i)
    res.append(t)
for i in res:
    print(len(i))
    print(' '.join(map(str, sorted(i))))