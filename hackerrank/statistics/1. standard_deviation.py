import math

n = int(input())
x_set = list(map(int, input().split()))

x_mean = sum(x_set) / n

tmp = 0
for i in range(n):
    tmp += pow(x_set[i] - x_mean, 2)

x_std = math.sqrt(tmp / n)
print(round(x_std, 1))
