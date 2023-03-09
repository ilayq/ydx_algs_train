n, m = map(int, input().split())
dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = 1
# for i in dp:
#     print(i)
for i in range(n):
    for j in range(m):
        if i + 2 < n and j + 1 < m:
            dp[i + 2][j+1] += dp[i][j]
        if i + 1 < n and j + 2 < m:
            dp[i + 1][j+2] += dp[i][j]
print(dp[-1][-1])