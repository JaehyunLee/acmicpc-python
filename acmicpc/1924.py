# 2007년
# https://www.acmicpc.net/problem/1924

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

x, y = map(int, input().split())

date = y-1
for i in range(x-1):
    date += month[i]

print(day[date % 7])
