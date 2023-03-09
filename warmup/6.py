# m = int(input())
# n = int(input())
# arr = [0 for _ in range(m)]
# c = 0
# for j in range(n):
#     # print(arr)
#     l, r = map(int, input().split())
#     l -= 1
#     r -= 1
#     if arr[l]:
#         for i in range(arr[l][0], arr[l][1] + 1):
#             arr[i] = 0
#         c -= 1
#     if arr[r]:
#         for i in range(arr[r][0], arr[r][1] + 1):
#             arr[i] = 0
#         c -= 1
#     for i in range(l, r+1):
#         arr[i] = (l, r)
#     c += 1
# # print(arr)
# print(c)

# n, k, row, column = int(input()), int(input()), int(input()), int(input())
# pos1 = (row - 1) * 2 + column - k
# pos2 = (row - 1) * 2 + column + k
# row1 = (pos1 + 1) // 2
# row2 = (pos2 + 1) // 2

# if pos1 > 0 and (pos2 > n or abs(row - row1) < abs(row - row2)):
# 	print(row1, 2 - pos1 % 2)
# elif pos2 <= n:
# 	print(row2, 2 - pos2 % 2)
# else:
# 	print(-1)


m, n = int(input()), int(input())
arr = []
for _ in range(n):
	l, r = map(int, input().split())
	pop_c = 0
	for i in range(len(arr)):
		if arr[i-pop_c][0] <= r <= arr[i-pop_c][1] or arr[i-pop_c][0] <= l <= arr[i-pop_c][1] or (arr[i-pop_c][0] > l and arr[i-pop_c][1] < r):
			arr.pop(i-pop_c)
			pop_c += 1
	arr.append((l, r))
print(len(arr))

