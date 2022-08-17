# 뒤집은 소수

# 내 풀이
n = int(input())
arr = list(map(int, input().split()))

def reverse(x):
    res = 0
    while x > 0:
        res = res * 10 + x % 10
        x = x // 10
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True

for x in arr:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')


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
