import sys

n, k = map(int, input().split())

dp = [0 for _ in range(n)]
dp[0] = 1
for i in range(1, n):
    s = 0
    for j in range(max(0, i-k), i):
        s += dp[j]
    dp[i] = s
print(dp[-1])