# n, m, k = map(int, input().split())
# matr = []
# flat = []

# for i in range(n):
#     tmp = list(map(int, input().split()))
#     flat.extend(tmp)
#     matr.append(tmp)

# pref = [0 for _ in range(n*m+1)]
# for i in range(1, n*m+1):
#     pref[i] = pref[i-1] + flat[i-1]
# for _ in range(k):
#     x1, y1, x2, y2 = map(int, input().split())
#     x1 -= 1
#     x2 -= 1
#     y1 -= 1
#     y2 -= 1
#     left_flat_idx =  x1 * m + y1
#     right_flat_idx = x2 * m + y2
#     # print(x1, y1, x2, y2)
#     # print(left_flat_idx, right_flat_idx)
#     s = pref[right_flat_idx+1] - pref[left_flat_idx]
#     # print(pref[right_flat_idx+1] - pref[left_flat_idx])
#     # print(s)
#     for i in range(x1+1, min(x1 + (right_flat_idx - left_flat_idx) // 2, n)):
#         for j in range(y1):
#             # print(matr[i][j])
#             # if i > x1:
#             s -= matr[i][j]
#     for j in range(x1, min(x1 + (right_flat_idx - left_flat_idx) // 2 - 1, n)):
#         for j in range(y2 + 1, m):
#             s -= matr[i][j]
#     # for j in range(x1, )
#     print(s)

# # n, m, k = map(int, input().split())
# # matr = []
# # for i in range(n):
# # 	matr.append(list(map(int, input().split())))
# # for _ in range(k):
# #     x1, y1, x2, y2 = map(int, input().split())
# #     x1 -= 1
# #     y1 -= 1
# #     x2 -= 1
# #     y2 -= 1
# #     s = 0
# #     for i in range(x1, x2+1):
# #         for j in range(y1, y2+1):
# #             s += matr[i][j]
# #     print(s)

n, m, k = map(int, input().split())
pref = []
matr = []
for i in range(n):
    matr.append(list(map(int, input().split())))
pref = [[0 for _ in range(m)] for _ in range(n)]
pref[0][0] = matr[0][0]
for i in range(1, n):
    pref[i][0] = pref[i-1][0] + matr[i][0]
for i in range(1, m):
    pref[0][i] = pref[0][i-1] + matr[0][i]
for i in range(1, n):
    for j in range(1, m):
        pref[i][j] = pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1] + matr[i][j]

# for i in range(n):
#     for j in range(m+1):
#         if j == 0:
#             if i == 0:
#                 continue
#             else:
#                 pref[i][j] = pref[i-1][-1]
#         else:
#             pref[i][j] = pref[i][j-1] + matr[i][j-1]


def calc_pref(x, y):
    if x < 0 or y < 0:
        return 0
    return pref[x][y]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    # print(calc_pref(x2, y2), calc_pref(max(x1 - 1, 0), y2), calc_pref(x2, max(0, y1 - 1)),  calc_pref(max(0, x1-1), max(0, y1-1)))
    s = calc_pref(x2, y2) - calc_pref(x1 - 1, y2) - calc_pref(x2, y1 - 1) + calc_pref(x1-1, y1-1)
    print(s)

# print(pref)
        


# n, m, k = map(int, input().split())
# matr = []
# for i in range(n):
#     matr.append(list(map(int, input().split())))

# pref = [[0 for _ in range(m+1) for _ in range(n)]]

