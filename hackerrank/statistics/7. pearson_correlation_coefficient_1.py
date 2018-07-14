# Day 7: Pearson Correlation Coefficient


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


n = int(input())
x_list = list(map(float, input().split()))
y_list = list(map(float, input().split()))
print(round(pcc(x_list, y_list), 3))
