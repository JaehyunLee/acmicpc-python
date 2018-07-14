# Day 7: Spearman's Rank Correlation Coefficient


def srcc(list1, list2):
    num = len(list1)
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    rank_list1 = [sorted_list1.index(list1[i]) + 1 for i in range(num)]
    rank_list2 = [sorted_list2.index(list2[i]) + 1 for i in range(num)]
    d2list = [(rank_list1[i] - rank_list2[i]) ** 2 for i in range(num)]
    return 1 - 6 * sum(d2list) / (num * (num ** 2 - 1))


n = int(input())
x_list = list(map(float, input().split()))
y_list = list(map(float, input().split()))
print(round(srcc(x_list, y_list), 3))
