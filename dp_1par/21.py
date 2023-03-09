n = int(input())
dp = [0 for _ in range(n + 3)]
dp[0] = 2
dp[1] = 4
dp[2] = 7
for i in range(3, n):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
print(dp[n-1]) 