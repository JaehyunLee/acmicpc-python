def get_mode(sample):
    n_sample = len(sample)
    if n_sample % 2 is 0:
        return (sample[n_sample // 2 - 1] + sample[n_sample // 2]) / 2
    else:
        return sample[n_sample // 2]


n = int(input())
x_set = sorted(list(map(int, input().split())))

first = get_mode(x_set[:n//2])
second = get_mode(x_set)
third = get_mode(x_set[round(n/2+0.1):])

print(('%d' if first == int(first) else '%s') % first)
print(('%d' if second == int(second) else '%s') % second)
print(('%d' if third == int(third) else '%s') % third)
