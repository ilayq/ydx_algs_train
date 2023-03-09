from collections import deque
import sys

q = deque()

n, m, s, t, q = map(int, input().split())
matr = [[-1 for _ in range(m)] for _ in range(n)]
b = []
matr[s-1][t-1] = 0
for i in range(q):
    b.append(list(map(int, input().split())))
q = deque()
q.append((s-1, t-1))
while q:
    i, j = q.popleft()
    if i - 2 > -1:
        if j + 1 < m and matr[i-2][j+1] < 0:
            matr[i-2][j+1] = matr[i][j] + 1
            q.append((i-2, j+1))
        if j - 1 > -1 and matr[i-2][j-1] < 0:
            matr[i-2][j-1] = matr[i][j] + 1
            q.append((i-2, j-1))
    if i + 2 < n:
        if j + 1 < m and matr[i+2][j+1] < 0:
            matr[i+2][j+1] = matr[i][j] + 1
            q.append((i+2, j+1))
        if j - 1 > -1 and matr[i+2][j-1] < 0:
            matr[i+2][j-1] = matr[i][j] + 1
            q.append((i+2, j-1))
    if j - 2 > - 1 :
        if i - 1 > -1 and matr[i-1][j-2] < 0:
            matr[i-1][j-2] = matr[i][j] + 1
            q.append((i-1, j-2))
        if i + 1 < n  and matr[i+1][j-2] < 0:
            matr[i+1][j-2] = matr[i][j] + 1
            q.append((i+1, j-2))
    if j +2 < m:
        if i - 1 > -1 and matr[i-1][j+2] < 0:
            matr[i-1][j+2] = matr[i][j] + 1
            q.append((i-1, j+2))
        if i + 1 < n and matr[i+1][j+2] < 0:
            matr[i+1][j+2] = matr[i][j] + 1
            q.append((i+1, j+2))
[print(i) for i in matr]
# print(matr)
f = True
s = 0
for i in b:
    if matr[i[0] - 1][i[1]-1] >= 0:
        s += matr[i[0] - 1][i[1]-1]
    else:
        print(-1)
        sys.exit()
print(s)
