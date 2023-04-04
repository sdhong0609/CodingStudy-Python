num = int(input())
d = [0] * 45
count = 0
count2 = 0


# 피보나치 수 재귀호출
def fib(n):
    global count
    if n == 1 or n == 2:
        count += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 피보나치 수 다이나믹 프로그래밍
def fibonacci(n):
    global count2
    if n == 1 or n == 2:
        return 1
    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]
        count2 += 1
    return d[n]


fib(num)
fibonacci(num)

print(count, count2)