# X보다 작은 수
# https://www.acmicpc.net/problem/10871

N, X = map(int, input().split())
result = list(map(int, input().split()))
for i in range(1, N+1):
    if result[N-i] >= X:
        result.pop(N-i)
print(*result)
