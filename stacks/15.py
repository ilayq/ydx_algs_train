from collections import deque


n = int(input())
arr = list(map(int, input().split()))
st = deque()
res = [-1 for _ in range(n)]
for i in range(n):
    if len(st) == 0:
        st.append((i, arr[i]))
        continue
    elif len(st) > 0:
        while len(st) > 0 and st[-1][1] > arr[i]:
            res[st.pop()[0]] = i
        st.append((i, arr[i]))
# if len(st) > 0:
#     for i in range(len(st)):
#         res.append(-1)
print(' '.join(map(str, res)))