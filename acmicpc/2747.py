# 피보나치 수
# https://www.acmicpc.net/problem/2747

N = int(input())
fibo = [0, 1]
for i in range(1, N):
    fibo.append(fibo[i] + fibo[i - 1])
print(fibo[N])
