def main():
    n = int(input())
    d = sorted(list(set(list(map(int, input().split())))))
    k = int(input())
    a = list(map(int, input().split()))
    for col in a:
        s = rbinsearch(d, col)
        # print(a[s], col)
        if d[s] >= col:
            print(0)
        else:
            print(s+1)


def rbinsearch(arr, target):
    l = 0
    r = len(arr)-1
    while l < r:
        mid = (l + r + 1) // 2
        if arr[mid] < target:
            l = mid
        else:
            r = mid - 1
    return l
if __name__ == '__main__':
    main()
    # print(rbinsearch([1, 50, 100], 0))
    # print(rbinsearch([1, 50, 100], 75))
    # print(rbinsearch([1, 50, 100], 300))
    # print(rbinsearch([5], 4))