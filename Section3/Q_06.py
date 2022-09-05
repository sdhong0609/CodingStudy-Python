# 격자판 최대합

# 내 풀이
# n = int(input())
# a = []
# max = 0
# sum, sum2, sum3, sum4 = 0, 0, 0, 0
# for _ in range(n):
#     a.append(list(map(int, input().split())))
#
# for i in range(n):
#     sum = 0
#     sum2 = 0
#     for j in range(n):
#         sum += a[i][j]
#         sum2 += a[j][i]
#     if max < sum:
#         max = sum
#     if max < sum2:
#         max = sum2
#
# for i in range(n):
#     sum3 += a[i][i]
# if max < sum3:
#     max = sum3
#
# for i in range(n):
#     sum4 += a[i][n-i-1]
# if max < sum4:
#     max = sum4
#
# print(max)


# 강사 풀이
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2

print(largest)