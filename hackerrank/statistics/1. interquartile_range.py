def get_mode(sample):
    n_sample = len(sample)
    if n_sample % 2 is 0:
        return (sample[n_sample // 2 - 1] + sample[n_sample // 2]) / 2
    else:
        return sample[n_sample // 2]


n = int(input())
x_set = list(map(int, input().split()))
f_set = list(map(int, input().split()))
data_set = []
for i in range(n):
    for j in range(f_set[i]):
        data_set.append(x_set[i])

sorted_data_set = sorted(data_set)
total_n = len(sorted_data_set)

first = get_mode(sorted_data_set[:total_n//2])
third = get_mode(sorted_data_set[round(total_n/2+0.1):])

print('{0:.1f}'.format(round(third - first)))