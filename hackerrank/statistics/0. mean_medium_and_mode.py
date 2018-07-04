# Day 0: Mean, Median, and Mode

N = int(input())
data_set = list(map(int, input().split()))
sorted_data_set = sorted(data_set)

mean = sum(sorted_data_set)/N
print(round(mean, 1))

if N % 2 is 1:
    median = sorted_data_set[int(N/2)]
    print(round(median, 1))
else:
    median = (sorted_data_set[int(N/2-1)] + sorted_data_set[int(N/2)]) / 2
    print(round(median, 1))

mode = sorted_data_set[0]
count = 1
for i in range(1, N):
    tmp = sorted_data_set.count(sorted_data_set[i])
    if count < tmp:
        mode = sorted_data_set[i]
        count = tmp
print(mode)
