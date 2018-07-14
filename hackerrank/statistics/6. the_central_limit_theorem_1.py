# Day 6: The Central Limit Theorem 1

from math import sqrt


def normal_distributions(mean, std, x):
    from math import erf
    return 0.5 * (1 + erf((x - mean) / (std * (2 ** 0.5))))


max_pound = int(input())
n_box = int(input())
m = int(input())
s = int(input())

result = normal_distributions(m * n_box, s * sqrt(n_box), max_pound)
print(round(result, 4))
