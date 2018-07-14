# Day 6: The Central Limit Theorem 2

from math import sqrt


def normal_distributions(mean, std, x):
    from math import erf
    return 0.5 * (1 + erf((x - mean) / (std * (2 ** 0.5))))


max_ticket = int(input())
n_student = int(input())
m = float(input())
s = float(input())

result = normal_distributions(m * n_student, s * sqrt(n_student), max_ticket)
print(round(result, 4))
