# 숫자카드
# https://www.acmicpc.net/problem/10815


def binary_search(target):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2
        if card[mid] == target:
            return 1
        elif card[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


N = int(input())
card = list(map(int, input().split()))
M = int(input())
test_case = list(map(int, input().split()))
card.sort()

for i, t in enumerate(test_case):
    print(binary_search(t), end=' ')
