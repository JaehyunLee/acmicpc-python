# 한수
# https://www.acmicpc.net/problem/1065

N = int(input())
result = 99
if N < 100:
    result = N
else:
    for i in range(100, N+1):
        a = int(str(i)[0])
        b = int(str(i)[1])
        c = int(str(i)[2])
        if a - b is b - c:
            result += 1
print(result)
