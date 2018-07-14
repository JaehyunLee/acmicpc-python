# RGB거리
# https://www.acmicpc.net/problem/1149

N = int(input())
table = [0, 0, 0]
tmp = [0, 0, 0]
for _ in range(N):
    n1, n2, n3 = map(int, input().split())
    tmp[0] = n1 + min(table[1], table[2])
    tmp[1] = n2 + min(table[0], table[2])
    tmp[2] = n3 + min(table[0], table[1])
    table = tmp[:]
print(min(table))
