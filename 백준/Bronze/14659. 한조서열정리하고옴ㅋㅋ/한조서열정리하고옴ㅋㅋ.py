import sys

input = sys.stdin.readline

n = int(sys.stdin.readline().rstrip())
height = list(map(int, input().split()))
result = 0
for i in range(n):
    count = 0
    for j in range(i + 1, n):
        if height[i] > height[j]:
            count += 1
        else:
            break
    if count > result:
        result = count

print(result)
