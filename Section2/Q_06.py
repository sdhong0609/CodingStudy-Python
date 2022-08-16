# 자릿수의 합

# 내 풀이
def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum


n = int(input())
arr = list(map(int, input().split()))
max = 0
index = 0

for i, x in enumerate(arr):
    tmp = digit_sum(x)
    if max < tmp:
        max = tmp
        index = i

print(arr[index])


# 강사 풀이 1
n = int(input())
a = list(map(int, input().split()))


def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum


max = -2147000000

for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x

print(res)


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
