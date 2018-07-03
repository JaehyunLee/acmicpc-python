# 베르트랑 공준
# https://www.acmicpc.net/problem/4948

maxvalue = 123456
counter = [1] * (2 * maxvalue + 1)
counter[0] = 0
counter[1] = 0
i = 2

while i <= maxvalue:
    if counter[i] is 1:
        j = i
        while j + i <= 2 * maxvalue:
            j += i
            counter[j] = 0
    i += 1

while True:
    n = int(input())
    if n is 0:
        break
    print(counter[n + 1: 2 * n + 1].count(1))
