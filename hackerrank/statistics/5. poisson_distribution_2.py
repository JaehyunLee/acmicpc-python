# Day 5: Poisson Distribution 2 - 포아송 분포
# 특정 사건에 대한 기대값을 람다 l로 정의할때, 특정 사건이 k번 발생할 확률 분포

a, b = map(float, input().split())

result1 = 160 + 40*(a + a**2)
result2 = 128 + 40*(b + b**2)

print(round(result1, 3))
print(round(result2, 3))
