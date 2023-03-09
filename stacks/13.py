from collections import deque


s = input().split()
# s.append('')
st = deque()
#res = 0
# print(s)
for i in range(len(s)):
    # print(st, s[i])
    if s[i].isdigit():
        # tmp = s[i]
        # if s[i+1].isdigit():
        #     c = 0
        #     tmp = ''
        #     while not s[i + c].isdigit():
        #         tmp += s[i+c]
        #         c += 1
        st.append(s[i])
    else:
        #b = st[-2]
        #a = st[-1]
        # a = st.pop()
        # b = st.pop()
        a = st.pop()
        b = st.pop()
        # print((b + s[i] + a))
        if s[i] == '-':
            st.append(str(int(b) - int(a)))
        elif s[i] == '+':
            st.append(str(int(b) + int(a)))
        else:
            st.append(str(int(b) * int(a)))
print(st[-1])
