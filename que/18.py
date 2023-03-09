from collections import deque


st = deque()
commands = [x.strip() for x in open('input.txt').readlines()]
for cmd in commands:
    if cmd.startswith('push_front'):
        st.appendleft(int(cmd.split()[1]))
        print('ok')
    elif cmd.startswith('push_back'):
        st.append(int(cmd.split()[1]))
        print('ok')
    elif cmd == 'pop_front':
        if len(st) == 0:
            print('error')
        else:
            print(st.popleft())
    elif cmd == 'pop_back':
        if len(st) == 0:
            print('error')
        else:
            print(st.pop())
    elif cmd == 'front':
        if len(st) == 0:
            print('error')
        else:
            print(st[0])
    elif cmd == 'back':
        if len(st) == 0:
            print('error')
        else:
            print(st[-1])
    elif cmd == 'size':
        print(len(st))
    elif cmd == 'clear':
        st = deque()
        print('ok')
    elif cmd == 'exit':
        print('bye')
        break
