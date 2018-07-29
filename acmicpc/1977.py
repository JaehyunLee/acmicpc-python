# 완전제곱수
# https://www.acmicpc.net/problem/1977

M = int(input())
N = int(input())

i = 1
result = []
while i ** 2 <= N:
    if M <= i ** 2:
        result.append(i ** 2)
    i += 1
if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))
