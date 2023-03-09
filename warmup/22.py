from sys import stdin


k = int(input())
s = stdin.readline().strip()

chars = set(s)
max_ = 0
for char in chars:
    cur_k = k
    l, r = 0, 0
    while r < len(s):
        if s[r] != char:
            cur_k -= 1
        r += 1
        max_ = max(max_, r - l)
        while cur_k <= 0:
            l += 1
            if s[l] != char:
                cur_k += 1
        
print(max_)
