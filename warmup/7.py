s1, s2, s3 = input(), input(), input()


def sec(s: str) -> int:
    s = s.split(':')
    return int(s[0]) * 3600 + int(s[1]) * 60 + int(s[2])

delta = (sec(s3) - sec(s1)) / 2
if delta < 0:
    delta = (sec(s3) + (sec('24:00:00') - sec(s1)))/2
    # print(delta)
res = sec(s2) + delta
h, m, s = 0, 0, 0
while res > 0:
    if res >= 3600:
        h += 1
        res -= 3600
    elif res >= 60:
        m += 1
        res -= 60
    else:
        s = res
        res = 0
s = int(s + (0.5 if s > 0 else -0.5))
if s == 60:
    m += 1
    s = 0
if m == 60:
    h += 1
    m = 0
h %= 24

h, m, s = map(str, [h, m, s])
aaa = [h, m, s]
for i in range(3):
    if len(aaa[i]) == 1:
        # print('aaa', aaa[i])
        aaa[i] = '0' + aaa[i]
print(':'.join(aaa))
