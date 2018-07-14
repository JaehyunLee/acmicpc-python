# Day 8: Least Square Regression Line


def std(data_list):
    from math import sqrt
    num = len(data_list)
    x_mean = sum(data_list) / num
    return sqrt(sum([(data_list[i] - x_mean) ** 2 for i in range(num)]) / num)


def pcc(list1, list2):
    num = len(list1)
    x_mean = sum(list1) / num
    y_mean = sum(list2) / num
    return sum([(list1[i] - x_mean) * (list2[i] - y_mean) for i in range(int(num))]) / (num * std(list1) * std(list2))


def lsr(list1, list2, x):
    num = len(list1)
    x_mean = sum(list1) / num
    y_mean = sum(list2) / num
    b = pcc(list1, list2) * std(list2) / std(list1)
    a = y_mean - b * x_mean
    return a + b * x


x_list = []
y_list = []
for _ in range(5):
    x_data, y_data = map(int, input().split())
    x_list.append(x_data)
    y_list.append(y_data)

print(round(lsr(x_list, y_list, 80), 3))
