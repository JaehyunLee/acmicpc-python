# 설탕배달
# https://www.acmicpc.net/problem/2839

n = int(input())
result = -1
for i in range(5):
    if (n - 3 * i) < 0:
        break
    if (n - 3 * i) % 5 is 0:
        result = (n - 3 * i) // 5 + i
print(result)
