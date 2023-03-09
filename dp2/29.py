# n = int(input())
# dp = [[0 for _ in range(n)] for _ in range(n)]
# days = []
# for i in range(n):
#     days.append(int(input()))
# # if days[0] > 100:
# #     for i in range(n):
# #         dp[0][i] = float('inf')
# #     dp[0][1] = days[0]
# # else:
# #     for i in range(1, n):
# #         dp[0][i] = float('inf')
# #     dp[0][0] = days[0]
# for i in range(n):
#     if i == 1:
#         continue
#     dp[0][i] = float('inf')
# for j in range(n):
#     dp[j][0] = float('inf')
# dp[0][1] = 0
# used = 0
# max_c = 0
# day_tu = []
# # print(dp)
# for i in range(n):
#     for j in range(1, n):
#         if days[i] > 100:
#             # dp[i][j] = min(dp[max(0, i-1)][min(n-1, j-1)] + days[i], dp[max(0, i-1)][min(n-1, j+1)])
#             dp[i][j] = min(dp[max(0, i-1)][j-1] + days[i], dp[max(0, i-1)][min(n-1, j+1)])
#         else:
#             dp[i][j] = min(dp[max(0, i-1)][j] + days[i], dp[max(0, i-1)][min(n-1, j+1)])

# min_ = dp[-1][0]
# min_k1 = 0
# for i in range(n):
#     if dp[-1][i] <= min_:
#         min_ = dp[-1][i]
#         min_k1 = i
#     # min_ = min(min_, dp[-1][i])
# print(min_)
# #TODO посчитать k2 и вывести дни в которые отдавался купон
# # print(dp)
# # print(max_c)
# # print(min_k1, max_c - min_k1)
# # for i in day_tu:
# #     print(i)
# path = []
# i, j = len(dp)-1, min_k1
# # print(dp)
# c = 0
# while i > 0:
#     min_j = 1 << 4334
#     min_ = 1 << 4343
#     for x in range(n):
#         if dp[i-1][x] < min_:
#             min_ = dp[i-1][x]
#             min_j = x
#         if dp[i-1][x] == dp[i][j]:
#             min_j = x
#             c += 1
#             path.append(i+1)
#             break
#     i -= 1
#     j = min_j
# print(min_k1, c)
# for i in sorted(path):
#     print(i)
# for i in dp:
#     print(' '.join(map(str, i)))
nm = 105
n = int(input())
a = [0 for _ in range(nm-1)]
for i in range(n):
    a[i] = int(input())
b = [[0 for _ in range(nm)] for _ in range(nm)]
p = [[0 for _ in range(nm)] for _ in range(nm-1)]
r = [0 for _ in range(nm-1)]
for i in range(n):
    for j in range(n):
        b[i][j] = - 1
b[0][0] = 0
for i in range(n-1):
    for j in range(n):
        if b[i][j] == -1:
            continue
        if j > 0:
            if (b[i+1][j-1]>b[i][j]) or (b[i+1][j-1]==-1):
                b[i+1][j-1] = b[i][j]
                p[i + 1][j-1] = j

        if a[i+1]>100:
            k = 1
        else:
            k = 0
        if (b[i+1][j+k]>b[i][j]+a[i+1]) or (b[i+1][j+k]==-1):
            b[i+1][j+k] = b[i][j] + a[i+1]
            p[i + 1][j+k] = j
    k1 = False
    res = float('inf')
    for i in range(n):
        if b[n-1][i] != -1 and b[n-1][i] <= res:
            res = b[n-1][i]
            k1 = i
    if k1:
        j = k1
        k2 = 0
        for i in range(n-1, 0, -1):
            if j + 1 == p[i][j]:
                k2 += 1
                r[k2] = i
            j = p[i][j]

print(res)
print(b[n-1])