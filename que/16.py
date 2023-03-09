from collections import deque


st = deque()
commands = [x.strip() for x in open('input.txt').readlines()]
for cmd in commands:
    if cmd.startswith('push'):
        st.append(int(cmd.split()[1]))
        print('ok')
    elif cmd == 'pop':
        if len(st) == 0:
            print('error')
        else:
            print(st.popleft())
    elif cmd == 'front':
        if len(st) == 0:
            print('error')
        else:
            print(st[0])
    elif cmd == 'size':
        print(len(st))
    elif cmd == 'clear':
        st = deque()
        print('ok')
    elif cmd == 'exit':
        print('bye')
        break
