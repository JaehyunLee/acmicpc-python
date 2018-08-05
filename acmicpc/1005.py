# ACM Craft
# https://www.acmicpc.net/problem/1005

import sys
read = sys.stdin.readline
sys.setrecursionlimit(100000)


def get_cost(index):
    if memory[index] != -1:
        return memory[index]
    max_value = 0
    for i in required[index]:
        max_value = max(max_value, get_cost(i))
    memory[index] = max_value + cost_table[index]
    return memory[index]


T = int(read())
for _ in range(T):
    N, K = map(int, read().split())
    cost_table = list(map(int, read().split()))
    required = [[] for _ in range(N)]
    memory = [-1] * N
    for _ in range(K):
        x, y = map(int, read().split())
        required[y-1].append(x-1)
    print(get_cost(int(read())-1))
