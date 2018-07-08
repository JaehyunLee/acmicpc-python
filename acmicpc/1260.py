# DFS와 BFS
# https://www.acmicpc.net/problem/1260


def init_table():
    for _ in range(N + 1):
        table.append([0] * (N + 1))

    for _ in range(M):
        a, b = map(int, input().split())
        table[a][b] = 1
        table[b][a] = 1


def dfs_travel(v):
    dfs_result.append(v)
    for j in range(1, N+1):
        if table[v][j] == 1 and dfs_result.count(j) == 0:
            dfs_travel(j)


def bfs_travel(v):
    queue = [v]
    while len(queue) != 0:
        tmp = queue.pop(0)
        bfs_result.append(tmp)
        for j in range(N+1):
            if table[tmp][j] == 1 and bfs_result.count(j) == 0 and queue.count(j) == 0:
                queue.append(j)


table = []
N, M, V = map(int, input().split())
init_table()

dfs_result = []
dfs_travel(V)
print(*dfs_result)

bfs_result = []
bfs_travel(V)
print(*bfs_result)
