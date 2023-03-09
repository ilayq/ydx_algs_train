from collections import deque


n, m = map(int, input().split())
gr = [[] for _ in range(n+1)]
for i in range(m):
    s, e = map(int, input().split())
    gr[s].append(e)
    gr[e].append(s)
visited = [0 for _ in range(n+1)]
color = 1

def dfs(vertex, color):
    if visited[vertex]:
        return False
    st = deque()
    st.append(vertex)
    while len(st):
        vertex = st.pop()
        visited[vertex] = color
        for i in gr[vertex]:
            if not visited[i]:
                st.append(i)
    return True

for i in range(1, n+1):
    if not visited[i]:
        if dfs(i, color):
            color += 1
comps = [[] for _ in range(color)]
for i in range(1, len(visited)):
    comps[visited[i]].append(i)
comps.pop(0)
# print(visited)
print(len(comps))
for i in comps:
    print(len(i))
    print(' '.join(map(str, sorted(i))))