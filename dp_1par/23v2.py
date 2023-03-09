n = int(input())
dp = [0 for _ in range(n+1)]

dp[1] = 0
for n in range(2, n + 1):
    min_dp = dp[n - 1] + 1
    if n % 2 == 0:
        min_dp = min(min_dp, dp[n // 2] + 1)
    if n % 3 == 0:
        min_dp = min(min_dp, dp[n // 3] + 1)
    dp[n] = min_dp
print(dp[-1])

op = [n]
i = n
while i > 1:
    if dp[i] == (dp[i-1]+1):
        op.append(i - 1)
        i -= 1
        continue
    if i%2 == 0 and dp[i] == dp[i//2]+1:
        op.append(i // 2)
        i //= 2
        continue
    op.append(i // 3)
    i //= 3
print(' '.join(map(str, op[::-1])))