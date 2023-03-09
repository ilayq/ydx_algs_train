arr = []


def insert(val) -> None:
    arr.append(val)
    pos = len(arr) - 1
    while val > arr[(pos - 1) // 2] and (pos - 1) // 2 >= 0:
        arr[(pos - 1) // 2], arr[pos] = arr[pos], arr[(pos - 1) // 2]
        pos = (pos - 1) // 2
        if pos == 0:
            break

def extract() -> int:
    # if len(arr) == 1:
    #     return arr.pop()
    arr[0], arr[-1] = arr[-1], arr[0]
    res = arr.pop()
    pos = 0
    while (2 * pos + 1 < len(arr) and arr[pos] < arr[2 * pos + 1]) or (2 * pos + 2 < len(arr) and arr[pos] < arr[2 * pos + 2]):
        maxson = 2 * pos + 1
        if 2 * pos + 2 < len(arr):
            if arr[2 * pos + 1] < arr[2 * pos + 2]:
                maxson  = 2 * pos + 2
        arr[pos], arr[maxson] = arr[maxson], arr[pos]
        pos = maxson
    return res

n = int(input())
for i in range(n):
    s = input().split()
    if s[0] == '0':
        insert(int(s[1]))
    else:
        print(extract())
        # extract()
    # print(arr)
