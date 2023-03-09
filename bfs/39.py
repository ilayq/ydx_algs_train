from collections import deque
import sys


n = int(input())
# print(n)
gr = [[] for _ in range(n)]
for i in range(n):
    input()
    for _ in range(n):
        gr[i].append(list(input().strip()))
    # for j in range(n):
    #     for k in range(n):
    #         if gr[i][j][k] == 'S':
    #             s = (i, j, k)
    #             gr[i][j][k] = 0
# print(gr)
for i in range(n):
    for j in range(n):
        for k in range(n):
            if gr[i][j][k] == 'S':
                s = (i, j, k)
                gr[i][j][k] = 0
                break

# print(s)
# [print(_) for _ in gr]
if s[0] == 0:
    print(0)
    sys.exit()
q = deque()
q.append(s)
# while q:
#     i, j, k = q.popleft()
#     if i > 0:
#         if j > 0:
#             if k > 0:
#                 if gr[i-1][j-1][k-1] == '.':
#                     gr[i-1][j-1][k-1] = gr[i][j][k] + 1
#                     q.append((i-1, j-1, k-1))
#             if k < n - 1:
#                 if gr[i-1][j-1][k+1] == '.':
#                     gr[i-1][j-1][k+1] = gr[i][j][k] + 1
#                     q.append((i-1, j-1, k+1))
#         if j < n - 1:
#             if k > 0:
#                 if gr[i-1][j+1][k-1] == '.':
#                     gr[i-1][j+1][k-1] = gr[i][j][k] + 1
#                     q.append((i-1, j+1, k-1))
#             if k < n - 1:
#                 if gr[i-1][j+1][k+1] == '.':
#                     gr[i-1][j+1][k+1] = gr[i][j][k] + 1
#                     q.append((i-1, j+1, k+1))
#     if i < n - 1:
#         if j > 0:
#             if k > 0:
#                 if gr[i+1][j-1][k-1] == '.':
#                     gr[i+1][j-1][k-1] = gr[i][j][k] + 1
#                     q.append((i+1, j-1, k-1))
#             if k < n - 1:
#                 if gr[i+1][j-1][k+1] == '.':
#                     gr[i+1][j-1][k+1] = gr[i][j][k] + 1
#                     q.append((i+1, j-1, k+1))
#         if j < n - 1:
#             if k > 0:
#                 if gr[i+1][j+1][k-1] == '.':
#                     gr[i+1][j+1][k-1] = gr[i][j][k] + 1
#                     q.append((i+1, j+1, k-1))
#             if k < n - 1:
#                 if gr[i+1][j+1][k+1] == '.':
#                     gr[i+1][j+1][k+1] = gr[i][j][k] + 1
#                     q.append((i+1, j+1, k+1))
# while q:
#     i, j, k = q.popleft()
#     for d1 in (-1, 0, 1):
#         for d2 in (-1, 0, 1):
#             for d3 in (-1, 0, 1):
#                 if 0 <= i + d1 < n and 0 <= j + d2 < n and 0 <= k + d3 < n and gr[i+d1][j+d2][k+d3] == '.':
#                     gr[i+d1][j+d2][k+d3] = gr[i][j][k] + 1
#                     q.append((i+d1, j+d2, k+d3))
while q:
    i, j, k = q.popleft()
    if i - 1 > - 1:
        if gr[i-1][j][k] == '.':
            gr[i-1][j][k] = gr[i][j][k] + 1
            q.append((i-1, j, k))
    if i + 1 < n:
        if gr[i+1][j][k] == '.':
            gr[i+1][j][k] = gr[i][j][k] + 1
            q.append((i+1, j, k))
    if j - 1 > - 1:
        if gr[i][j-1][k] == '.':
            gr[i][j-1][k] = gr[i][j][k] + 1
            q.append((i, j-1, k))
    if j + 1 < n:
        if gr[i][j+1][k] == '.':
            gr[i][j+1][k] = gr[i][j][k] + 1
            q.append((i, j+1, k))
    if k - 1 > - 1:
        if gr[i][j][k-1] == '.':
            gr[i][j][k-1] = gr[i][j][k] + 1
            q.append((i, j, k-1))
    if k + 1 < n:
        if gr[i][j][k+1] == '.':
            gr[i][j][k+1] = gr[i][j][k] + 1
            q.append((i, j, k+1))
min_ = 1 << 34343434
for i in gr[0]:
    for j in i:
        if type(j) == int:
            min_ = min(min_, j)
print(min_)
for i in gr:
    for j in i:
        for k in j:
            print(k, end=' ')
        print()
    print()