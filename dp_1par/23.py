import sys


n = int(input())

if n == 1:
    print('0\n1')
    sys.exit()
elif n == 2:
    print('1\n1\n2')
    sys.exit()
elif n == 3:
    print('1\n1n3\n')
    sys.exit()
dp = [0 for i in range(n+1)]
dp[0] = dp[1] = dp[2] = 1
path = '1'
for i in range(3, n):
    min_dp = dp[i-1] + 1
    if (i + 1) % 2 == 0:
        min_dp = min(min_dp, dp[i//2] + 1)
    if (i + 1) % 3 == 0:
        min_dp = min(min_dp, dp[i//3] + 1)
    # if min_dp == dp[i//2] and (i+1) % 2 == 0:
    #     # path.append((i+1)//2)
    #     # path += ' '+str((i+1)//2)
    #     # print((i+1)//2, end=' ')
    # elif min_dp == dp[i//3] and (i+1) % 3 == 0:
    #     # path.append((i+1)//3)
    #     # path += ' '+str((i+1)//3)
    #     # print((i+1)//3, end=' ')
    # else:
    #     # path.append(i)
    #     # path += ' ' + str(i)
    #     # print(i, end=' ')
    dp[i] = min_dp
# path += ' ' + str(n)
print(dp[-1])
# print(path)
path = []
operations = []
i = n
while i > 1:
    if dp[i] == (dp[i-1]+1):
        operations.insert(0, 1)
        i -= 1
        continue
    if i%2 == 0 and dp[i] == dp[i//2]+1:
        operations.insert(0, 2)
        i //= 2
        continue
    operations.insert(0, 3)
    i //= 3
print(operations)
# path = [n]
# i = n
# while i > 1:
#     if i % 3 == 0:
#         path.append(i // 3)
#         i //= 3
#     elif i % 2 == 0:
#         path.append(i // 2)
#         i //= 2
#     else:
#         path.append(i-1)
#         i -= 1
print(' '.join(map(str, path[::-1])))
# print(path)
# print(' '.join(map(str, path)))