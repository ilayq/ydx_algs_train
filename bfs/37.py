from collections import deque
import sys

n = int(input())
matr = []
for i in range(n):
    matr.append(list(map(int, input().split())))

gr = [[] for _ in range(n+1)]
q = deque()
for i in range(n):
    for j in range(n):
        if matr[i][j]:
            gr[i+1].append(j+1)
# print(gr)
s, e = map(int, input().split())
if s == e:
    print(0)
    sys.exit()
vert = [-1 for _ in range(n+1)]
vert[s] = 0
q.append(s)
while q:
    a = q.popleft()
    for i in gr[a]:
        if vert[i] == -1:
            vert[i] = vert[a] + 1
            q.append(i)
# print(gr)
if vert[e] >= 0:
    print(vert[e])
else:
    print(-1)
    sys.exit()
cv = e
path = [cv]
while cv != s:
    for i in gr[cv]:
        if vert[i] == vert[cv] - 1:
            path.append(i)
            cv = i
print(' '.join(map(str, path[::-1])))