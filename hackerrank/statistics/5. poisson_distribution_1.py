# Day 5: Poisson Distribution 1 - 포아송 분포
# 특정 사건에 대한 기대값을 람다 l로 정의할때, 특정 사건이 k번 발생할 확률 분포

from math import exp


def factorial(n):
    return 1 if n == 1 else n * factorial(n-1)


def poisson(l, k):
    return (l ** k * exp(-l)) / factorial(k)


a = float(input())
b = float(input())

print(round(poisson(a, b), 3))
