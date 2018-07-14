# Day 4: Geometric Distribution 1
# 성공확률 p인 모수를 갖고, 처음으로 성공하는 시행횟수 x의 이산 확률분포

a, b = map(int, input().split())
n = int(input())
result = pow((b - a) / b, n - 1) * (a / b)
print(round(result, 3))
