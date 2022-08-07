# 뒤집은 소수

# 내 풀이
# n = int(input())
# arr = list(map(int, input().split()))
#
#
# def reverse(x):
#     cnt = len(str(x)) - 1
#     answer = 0
#     while x > 0:
#         answer += x % 10 * (10 ** cnt)
#         x = x // 10
#         cnt -= 1
#     return answer
#
#
# def isPrime(x):
#     if x == 1:
#         return False
#     isPrime = True
#     y = int(x ** (1 / 2))
#     for i in range(2, y + 1):
#         if x % i == 0:
#             isPrime = False
#             break
#     return isPrime
#
#
# for i in range(len(arr)):
#     arr[i] = reverse(arr[i])
#
# for i, x in enumerate(arr):
#     if isPrime(x):
#         print(x, end=' ')


# 강사 풀이
def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    else:
        return True


n = int(input())
a = list(map(int, input().split()))
for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
