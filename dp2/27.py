arr = []
n, m = map(int, input().split())

for i in range(n):
    arr.append(list(map(int, input().split())))
dp = [[[0, []] for i in range(m)] for j in range(n)]
dp[0][0][0] = arr[0][0]
for i in range(1, m):
    dp[0][i][0] = arr[0][i] + dp[0][i-1][0]
    dp[0][i][1] = dp[0][i-1][1] + ['R']
for j in range(1, n):
    dp[j][0][0] = arr[j][0] + dp[j-1][0][0]
    dp[j][0][1] = dp[j-1][0][1] + ['D']
path = []
# for i in dp:
#     print(i)
for i in range(1, n):
    for j in range(1, m):
        # dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + arr[i][j]
        if dp[i-1][j][0] > dp[i][j-1][0]:
            dp[i][j][1] = dp[i-1][j][1] + ['D']
            dp[i][j][0] = dp[i-1][j][0] + arr[i][j]
        else:
            dp[i][j][1] = dp[i][j-1][1] + ['R']
            dp[i][j][0] = dp[i][j-1][0] + arr[i][j]
print(dp[-1][-1][0])
# for i in dp:
#     print(i)
print(' '.join(dp[-1][-1][1]))
