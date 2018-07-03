# 평균은 넘겠지
# https://www.acmicpc.net/problem/4344

for _ in range(int(input())):
    raw = input().split()
    N = int(raw[0])
    data = list(map(int, raw[1:]))

    count = 0
    avg = sum(data) / N
    for _, d in enumerate(data):
        if d > avg:
            count += 1
    percent = round(count / N * 100, 3)
    print('{0:.3f}%'.format(percent))
