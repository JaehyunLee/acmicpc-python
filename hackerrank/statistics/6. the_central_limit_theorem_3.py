# Day 6: The Central Limit Theorem 3

from math import sqrt

n_value = int(input())
m = int(input())
s = int(input())
p = float(input())
z = float(input())  # Z score

error = z * s / sqrt(n_value)

print(round(m - error, 2))
print(round(m + error, 2))
