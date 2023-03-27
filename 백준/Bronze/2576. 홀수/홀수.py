array = []
for _ in range(7):
    n = int(input())
    if n % 2 != 0:
        array.append(n)

if len(array) == 0:
    print(-1)
else:
    print(sum(array))
    print(min(array))
