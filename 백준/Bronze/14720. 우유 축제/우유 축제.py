n = int(input())
milk = list(map(int, input().split()))

count = 0
target = 0
for i in range(n):
    if milk[i] == target:
        count += 1
        target += 1
        if target == 3:
            target = 0

print(count)