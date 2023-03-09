n = int(input())
arr = list(map(int, input().split()))
arr.sort()
dp = [0 for _ in range(n)]
dp[1] = arr[1] - arr[0]
if n > 2:
    dp[2] = arr[2] - arr[0]
for i in range(3, n):
    dp[i] = min(dp[i-1], dp[i-2]) + arr[i] - arr[i-1]
print(dp[-1])