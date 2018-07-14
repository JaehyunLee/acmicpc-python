def std(num, data_list):
    from math import sqrt
    x_mean = sum(data_list) / num
    return sqrt(sum([(data_list[i] - x_mean) ** 2 for i in range(num)]) / num)


n = int(input())
x_set = list(map(int, input().split()))
print(round(std(n, x_set), 1))
