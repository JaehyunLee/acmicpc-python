# 수 정렬하기
# https://www.acmicpc.net/problem/2750

data_list = []
for _ in range(int(input())):
    data_list.append(int(input()))
for _, data in enumerate(sorted(data_list)):
    print(data)
