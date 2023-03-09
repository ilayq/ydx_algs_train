st = []
commands = [x.strip() for x in open('input.txt').readlines()]
for cmd in commands:
    if cmd.startswith('push'):
        c = cmd.split()
        st.append(int(c[1]))
        print('ok')
    elif cmd == 'pop':
        if len(st) > 0:
            print(st.pop())
        else:
            print('error')
    elif cmd == 'back':
        if len(st) > 0:
            print(st[-1])
        else:
            print('error')
    elif cmd == 'clear':
        st = []
        print('ok')
    elif cmd == 'exit':
        print('bye')
        break
    elif cmd == 'size':
        print(len(st))
    else:
        pass
    