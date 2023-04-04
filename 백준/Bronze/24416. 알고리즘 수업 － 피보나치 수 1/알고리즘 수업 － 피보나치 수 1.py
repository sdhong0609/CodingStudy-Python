def fib(n):
    arr = [1, 1]
    for i in range(2, n):
        arr.append(arr[-1] + arr[-2])
    return arr[-1]


n = int(input())
print(fib(n), n - 2)
