arr = []
n, m = map(int, input().split())

for i in range(n):
    arr.append(list(map(int, input().split())))
dp = [[0 for i in range(m)] for j in range(n)]
dp[0][0] = arr[0][0]
for i in range(1, m):
    dp[0][i] = arr[0][i] + dp[0][i-1]
for j in range(1, n):
    dp[j][0] = arr[j][0] + dp[j-1][0]
# for i in dp:
#     print(i)
for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + arr[i][j]
print(dp[-1][-1])
