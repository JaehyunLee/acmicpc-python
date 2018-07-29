# 지능형 기차
# https://www.acmicpc.net/problem/2455

result = 0
max_value = 0
for i in range(3):
    a, b = map(int, input().split())
    result = result - a + b
    if result > max_value:
        max_value = result
print(max_value)
