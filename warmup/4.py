# def main():
#     n = int(input())
#     k = int(input())
#     petya_row = int(input())
#     petya_col = int(input())
#     petya_row -= 1
#     petya_col -= 1
#     if n < k:
#         print(-1)
#         return

#     #номер пети по порядку
#     num = petya_row * 2 + petya_col + 1
#     #вариант пети
#     petya_var = max(1, num % (k+1))
#     # print(petya_var)
#     var = 1
#     res = [1 << 3000, 1 << 3000]
#     c = 1
#     for i in range((n+1)//2):
#         for j in range(2):
#             if var == petya_var and i != petya_row:
#                 if abs(res[0] - petya_row) >= abs(i - petya_row):
#                     res = [i, j]
#             var += 1
#             c += 1
#             var = max(1, var % (k+1))
#             if c == n:
#                 break
#         if c == n:
#             break
#     if res != [1 << 3000, 1 << 3000]:
#         print(res[0] + 1, res[1] + 1)
#     else:
#         print(-1)
   
def main():
    n = int(input())
    k = int(input())
    petya_row = int(input())
    petya_col = int(input())
    petya_row -= 1
    petya_col -= 1
    if n < k:
        print(-1)
        return

    # matr = [[0, 0] for i in range((n+1) // 2)]
    var = 1
    # c = 0
    # print("place vars")
    # for i in range((n+1)//2):
    #     if c == n:
    #         break
    #     else:
    #         matr[i][0] = var
    #         var += 1
    #         var = max(1, var % (k+1))
    #         c += 1
    #         if c == n:
    #             break
    #         matr[i][1] = var
    #         var += 1
    #         var = max(1, var % (k+1))
    #         c += 1
    # for i in range(len(matr)):
    #     print(matr[i])
    # номер пети по порядку
    num = petya_row * 2 + petya_col + 1
    #вариант пети
    petya_var = num % k
    if petya_var == 0:
        petya_var = k
    #print(petya_var)
    ## print(pet_var)
    res = [1 << 300, 1 << 300]
    # print("find place")
    c = 0
    for i in range((n+1)//2):
        for j in range(2):
            c += 1
            if var == petya_var:
                # print(res[0], i, j)
                if (i, j) != (petya_row, petya_col):
                    if abs(res[0] - petya_row) >= (i - petya_row):
                        res = [i, j]
            var += 1
            var = max(1, var % (k+1))
            if c == n:
                break
        if c == n:
            break
    if res != [1 << 300, 1 << 300]:
        print(res[0] + 1, res[1] + 1)
    else:
        print(-1)


if __name__ == '__main__':
    main()