def main():
    n = int(input())
    d = sorted(list(set(list(map(int, input().split())))))
    k = int(input())
    a = list(map(int, input().split()))
    # print(min(a), min(d))
    # # c = 0
    # # for i in a:
    # #     if i > 
    # return
    for i in range(len(a)):
        a[i] = (i, a[i])
    a.sort(key=lambda x: x[1])
    pd = 0
    pa = 0
    res = [0 for _ in range(k)]
    # c = 0
    while pa < len(a) and pd < len(d):
        if d[pd] >= a[pa][1]:
            res[a[pa][0]] = pd
            pa += 1
        else:
            res[a[pa][0]] = pd
            pd += 1
    if pa == len(a) and pd == len(d):
        return res
    elif pa == len(a):
        return res
    elif pd == len(d):
        for i in range(pa, len(a)):
            res[a[pa][0]] = len(d)
        return res


if __name__ == '__main__':
    r = main()
    
    for i in r:
        print(i)
    print(len(r))