
n = int(input())
a = [0 for i in range(n+1)]
for i in range(n):
    a[i] = int(input())
s = 0
for i in range(n-1):
    s += min(a[i], a[i+1])
print(s)
