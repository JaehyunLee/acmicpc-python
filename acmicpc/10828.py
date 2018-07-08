# 스택
# https://www.acmicpc.net/problem/10828

stack = []
n = int(input())
for _ in range(n):
    op = input().split()
    if len(op) == 2:
        stack.append(int(op[1]))
    else:
        if op[0] == 'pop':
            print('-1' if len(stack) == 0 else stack.pop())
        elif op[0] == 'size':
            print(len(stack))
        elif op[0] == 'empty':
            print('1' if len(stack) == 0 else '0')
        elif op[0] == 'top':
            print('-1' if len(stack) == 0 else stack[len(stack)-1])
