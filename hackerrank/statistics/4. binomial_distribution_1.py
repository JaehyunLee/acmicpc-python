# Day 4: Binomial Distribution 1 - 이항 분포
# n번의 독립 시행에서 p의 확률을 가질때 확률 분포


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def binomial(n, k, p):
    return combination(n, k) * pow(p, k) * pow(1 - p, n - k)


boy, girl = map(float, input().split())

result = round(sum([binomial(6, i, boy / (boy + girl)) for i in range(3, 7)]), 3)
print(result)
