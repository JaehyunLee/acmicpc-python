# 트리 순회
# https://www.acmicpc.net/problem/1991

def preorder(i):
    mytable = table[:]
    print(mytable[i][0], end='')
    if mytable[i][1] != '.':
        preorder(ord(mytable[i][1])-ord('A'))
    if mytable[i][2] != '.':
        preorder(ord(mytable[i][2])-ord('A'))


def inorder(i):
    mytable = table[:]
    if mytable[i][1] != '.':
        inorder(ord(mytable[i][1])-ord('A'))
    print(mytable[i][0], end='')
    if mytable[i][2] != '.':
        inorder(ord(mytable[i][2])-ord('A'))


def postorder(i):
    mytable = table[:]
    if mytable[i][1] != '.':
        postorder(ord(mytable[i][1])-ord('A'))
    if mytable[i][2] != '.':
        postorder(ord(mytable[i][2])-ord('A'))
    print(mytable[i][0], end='')


N = int(input())
table = []
for i in range(N):
    table.append(input().split())

table.sort()
preorder(0)
print()
inorder(0)
print()
postorder(0)
