from collections import deque


n = int(input())
m = int(input())
gr = [[] for _ in range(n+1)]
res = [[-1, -1] for _ in range(n+1)]
st = [set() for _ in range(n+1)]
for i in range(m):
    s = list(map(int, input().split()))
    s.pop(0)
    for j in range(len(s)):
        st[s[j]].add(i+1)
    for j in range(len(s)):
        for x in range(j+1, len(s)):
            gr[s[j]].append(s[x])
            gr[s[x]].append(s[j])
# print(st)
a, b = map(int, input().split())
# print(gr)
q = deque()
q.append(a)
res[a] = [0, -1]
c = 0
while q:
    v = q.popleft()
    for i in gr[v]:
        if res[i][0] == -1:
            res[i][0] = res[v][0] + 1
            q.append(i)
q.append(b)
res[b][1] = 0
while q:
    v = q.popleft()
    for i in gr[v]:
        if res[i][1] == -1:
            res[i][1] = res[v][1] + 1
            q.append(i)
if res[b][0] > 0:
    print(res[b][0] - 1)
else:
    print(-1)
# print(res)
# c = 0
# for i in range(n+1):
#     if i not in (a, b):
#         if sum(res[i]) == res[a][1]:
#             c += 1
# print(res)
# print(c)