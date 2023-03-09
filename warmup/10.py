s = input()
l = len(s)
r = dict()
for char in s:
    r[char] = 0
for i in range(len(s)):
    r[s[i]] += (l - i) * (i + 1)
    # print(r[s[i]])
for key in sorted(r.keys()):
    print(f'{key}: {r[key]}')