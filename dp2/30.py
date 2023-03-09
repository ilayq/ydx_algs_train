n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
dp = [[0 for i in range(m)] for j in range(n)]
# print(dp)
for i in range(n):
    for j in range(m):
        if arr1[i] == arr2[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
                continue
            dp[i][j] = dp[max(0, i-1)][max(0, j-1)] + 1
        else:
            if i == 0 and j == 0:
                dp[i][j] = 0
                continue
            elif i > 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
            dp[i][j] = max(dp[max(i-1, 0)][j], dp[i][max(0, j-1)])
# print(dp)
i, j = n-1, m-1
c = dp[-1][-1]
path = []
while c > 0 and i > -1 and j > -1:
    if arr1[i] == arr2[j]:
        c -= 1
        path.append(arr1[i])
        i -= 1
        j -= 1
    else:
        if dp[i][j-1] == dp[i][j]:
            j -= 1
        else:
            i -= 1
if path:
    print(' '.join(map(str, path[::-1])))
