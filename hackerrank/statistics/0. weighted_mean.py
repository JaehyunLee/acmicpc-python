# Day 0: Weighted Mean

N = int(input())
x_set = list(map(int, input().split()))
w_set = list(map(int, input().split()))

x_sum = 0
for i in range(N):
    x_sum += x_set[i] * w_set[i]

weight_mean = x_sum / sum(w_set)
print(round(weight_mean, 1))
