# 자릿수의 합

# 내 풀이
# n = int(input())
# arr = list(map(int, input().split()))
#
# max = -2147000000
# answer = 0
#
#
# def digit_sum(x):
#     a = b = x
#     sum = 0
#     while a > 10:
#         b = a % 10
#         a = a // 10
#         sum += b
#     sum += a
#     return sum
#
#
# for i in range(n):
#     if max < digit_sum(arr[i]):
#         max = digit_sum(arr[i])
#         answer = arr[i]
#
# print(answer)


# 강사 풀이 1
# n = int(input())
# a = list(map(int, input().split()))
#
#
# def digit_sum(x):
#     sum = 0
#     while x > 0:
#         sum += x % 10
#         x = x // 10
#     return sum
#
#
# max = -2147000000
#
# for x in a:
#     tot = digit_sum(x)
#     if tot > max:
#         max = tot
#         res = x
#
# print(res)


# 강사 풀이 2
n = int(input())
a = list(map(int, input().split()))


def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum


max = float('-inf')

for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x

print(res)
