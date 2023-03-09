from collections import deque


n = int(input())
arr = list(map(int, input().split()))
st = deque()
c = 1
pop_c = 0
for i in range(n):
    # print(arr, st, c)
    if arr[i-pop_c] == c:
        arr.pop(0)
        c += 1
    else:
        st.append(arr.pop(0))
    while len(st) > 0 and st[-1] == c:
        if st[-1] == c:
            st.pop()
            c += 1
    pop_c += 1
    # print(arr, st, c)
while len(st) > 0:
    if st[-1] == c:
        st.pop()
        c += 1
    else:
        break
print('YES') if len(st) == 0 else print('NO')