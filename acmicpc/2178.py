# 미로 탐색
# https://www.acmicpc.net/problem/2178


def check_route(node):
    # Check Point: (1) 맵을 넘어서지는 않는지 (2) 갈수 있는 길인지 (3) 이미 방문한 곳은 아닌지
    if node[0] + 1 < N and table[node[0] + 1][node[1]] == 1 and not visit[node[0] + 1][node[1]]:
        queue.append([node[0]+1, node[1]])
        visit[node[0] + 1][node[1]] = True
    if node[1] + 1 < M and table[node[0]][node[1] + 1] == 1 and not visit[node[0]][node[1] + 1]:
        queue.append([node[0], node[1] + 1])
        visit[node[0]][node[1] + 1] = True
    if node[0] - 1 >= 0 and table[node[0] - 1][node[1]] == 1 and not visit[node[0] - 1][node[1]]:
        queue.append([node[0] - 1, node[1]])
        visit[node[0] - 1][node[1]] = True
    if node[1] - 1 >= 0 and table[node[0]][node[1] - 1] == 1 and not visit[node[0]][node[1] - 1]:
        queue.append([node[0], node[1] - 1])
        visit[node[0]][node[1] - 1] = True


N, M = map(int, input().split())
table = []
visit = []
for i in range(N):
    line_list = []
    line_str = input()
    for j in range(M):
        line_list.append(int(line_str[j]))
    table.append(line_list)
    visit.append([False] * M)

queue = [[0, 0]]  # Starting Point
result = 1  # BFS Depth Counter
while True:
    for _ in range(len(queue)):
        check_route(queue.pop(0))  # Q의 노드를 전부 리턴하고, 탐색이 가능한 새로운 노드를 다시 Q에 넣음
    result += 1  # Depth 카운트
    if queue.count([N-1, M-1]) != 0:  # Q에 도착지점을 발견하면 종료
        break
print(result)
