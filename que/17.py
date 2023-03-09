arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

c = 0
f = False
while c < 10 ** 6:
    c += 1
    card1 = arr1.pop(0)
    card2 = arr2.pop(0)
    if card1 == 9 and card2 == 0:
        arr2.append(card1)
        arr2.append(card2)
    elif card1 == 0 and card2 == 9:
        arr1.append(card1)
        arr1.append(card2)
    elif card1 > card2:
        arr1.append(card1)
        arr1.append(card2)
    else:
        arr2.append(card1)
        arr2.append(card2)
    if len(arr1) == 0:
        print(f'second {c}')
        f = True
        break
    elif len(arr2) == 0:
        print(f'first {c}')
        f = True
        break
if not f:
    print('botva')