n = int(input())
a, b, c = [1 << 43434 for _ in range(3)], [1 << 43434 for _ in range(3)], [1 << 43434 for _ in range(3)]
for i in range(n):
    r = list(map(int, input().split()))
    a.append(r[0])
    b.append(r[1])
    c.append(r[2])
# print(a)
dp = [0 for _ in range(n+3)]
for i in range(3, n+3):
    dp[i] = min([dp[i-1] + a[i], dp[i-2] + b[i-1], dp[i-3] + c[i-2]])
print(dp[-1])