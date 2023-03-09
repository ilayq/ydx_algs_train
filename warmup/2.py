from collections import deque


def main():
    k = int(input())
    s = input()
    chars = set(s)
    r = dict()

    max_ = 0
    # print(r)
    for char in chars:
        len_, end = 0, 0
        r[char] = []
        for i in range(len(s)):
            if s[i] == char:
                len_ += 1
                end = i
            else:
                if len_ or end:
                    r[char].append([end - len_ + 1, end])
                    end = 0
                    len_ = 0
        if len_ or end:
            r[char].append([end - len_ + 1, end])
        cur_k = k
        if len(r[char]) < 2:
            max_ = max(max_, r[char][0][1] - r[char][0][0] + 1 + k)
            continue
        st = deque()
        st.append(r[char][0])
        # st = [r[char][0]]
        k_st = deque()
        cur_l = 0
        for i in range(1, len(r[char])):
            if r[char][i][0] - st[-1][1] - 1 <= cur_k:
                cur_k -= (r[char][i][0] - st[-1][1] - 1)
                # print(r[char][i], st[-1])
                k_st.append(r[char][i][0] - st[-1][1] - 1)
                st.append(r[char][i])
                cur_l = st[-1][1] - st[0][0] + 1
                max_ = max(max_, cur_l + cur_k)
            else:
                while r[char][i][0] - st[-1][1] - 1 > cur_k:
                    st.popleft()
                    if not len(st):
                        break
                    if len(st) >= 1:
                        cur_k += k_st.popleft()
                if len(st):
                    cur_k -= (r[char][i][0] - st[-1][1] - 1)
                    k_st.append(r[char][i][0] - st[-1][1] - 1)
                    st.append(r[char][i])
                    cur_l = st[-1][1] - st[0][0] + 1
                    max_ = max(max_, cur_l + cur_k)
                else:
                    st.append(r[char][i])
                    cur_l = r[char][i][1] - r[char][i][0] + 1
                    max_ = max(max_, cur_l + cur_k)
            # if char == 'a':
                # print(r[char][i][0] - r[char][i - 1][1] - 1)
                # print(cur_k)
                # print(k_st)
                # print(st)
                # print(r[char][i])
    print(max_)
    # print(r)


if __name__ == '__main__':
    main()