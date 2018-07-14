# 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609


def get_gcd():
    a = num1
    b = num2
    while b != 0:
        a, b = b, a % b
    return a


num1, num2 = map(int, input().split())
if num1 < num2:
    num1, num2 = num2, num1
gcd = get_gcd()
print(gcd)
lcm = num1 * num2 // gcd
print(lcm)
