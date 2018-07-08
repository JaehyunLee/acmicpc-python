# 덱
# https://www.acmicpc.net/problem/10866

deque = []
n = int(input())
for _ in range(n):
    op = input().split()
    if len(op) == 2:
        if op[0] == 'push_front':
            deque.append(int(op[1]))
        elif op[0] == 'push_back':
            deque.insert(0, int(op[1]))
    else:
        if op[0] == 'pop_front':
            print('-1' if len(deque) == 0 else deque.pop())
        elif op[0] == 'pop_back':
            print('-1' if len(deque) == 0 else deque.pop(0))
        elif op[0] == 'size':
            print(len(deque))
        elif op[0] == 'empty':
            print('1' if len(deque) == 0 else '0')
        elif op[0] == 'front':
            print('-1' if len(deque) == 0 else deque[len(deque) - 1])
        elif op[0] == 'back':
            print('-1' if len(deque) == 0 else deque[0])
