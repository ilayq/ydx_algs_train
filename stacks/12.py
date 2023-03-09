# def main():
#     s = input().strip()
#     st = []
#     b = 0
#     for i in s:
#         # print(i, st)
#         if b < 0:
#             return False
#         if i in ['(', '{', '[']:
#             st.append(i)
#             b += 1
#         elif i == ')':
#             if len(st) == 0:
#                 return False
#             else:
#                 if st[-1] == '(':
#                     st.pop()
#                     b -= 1
#                 else:
#                     b -= 1
#         elif i == ']':
#             if len(st) == 0:
#                 return False
#             else:
#                 if st[-1] == '[':
#                     st.pop()
#                     b -= 1
#                 else:
#                     b -= 1
#         elif i == '}':
#             if len(st) == 0:
#                 return False
#             else:
#                 if st[-1] == '{':
#                     st.pop()
#                     b -= 1
#                 else:
#                     b -= 1
#     return len(st) == 0 and b == 0


# if __name__ == '__main__':
#     print('yes') if main() else print('no')



import sys

flips = int(sys.stdin.readline().strip())
s = list(sys.stdin.readline().strip())
cntdict ={}
crntmax = 0
rhs = 0
while rhs < flips + crntmax:
    cntdict[s[rhs]] = cntdict.get(s[rhs], 0) + 1
    crntmax = max(crntmax, cntdict[s[rhs]])
    rhs += 1
win = crntmax + flips
while rhs < len(s):
    cntdict[s[rhs]] = cntdict.get(s[rhs], 0) + 1
    if cntdict[s[rhs]] > crntmax:
        win += 1
        crntmax += 1
    else:
        cntdict[s[rhs - win]] -= 1
    rhs += 1
sys.stdout.write(str(win))
    
