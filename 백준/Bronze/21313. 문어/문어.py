n = int(input())
for _ in range(n // 2):
    print(1, 2, end=' ')
if n % 2 != 0:
    print(3)