import sys

sys.setrecursionlimit(10 ** 5)

n = int(input())

matr = []
for i in range(n):
    matr.append(list(map(int, input().split())))
gr = [[] for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        if matr[i][j]:
            gr[i+1].append(j+1)
# print(gr)
visited = [0 for _ in range(n+1)]
cycle = []
def dfs(v, from_):
    if visited[v] == 1:
        cycle.append(v)
        return v
    visited[v] = 1
    for i in gr[v]:
        if i == from_:
            continue
        res = dfs(i, v)
        if res > 0:
            if res == v:
                print("YES")
                print(len(cycle))
                print(' '.join(map(str, cycle)))
                sys.exit()
            cycle.append(v)
            return res
    visited[v] = 2
    return -1

for i in range(1, n+1):
    if not visited[i]:
        dfs(i, 0)
print("NO")
            