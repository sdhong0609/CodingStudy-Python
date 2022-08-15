# 정다면체

n, m = map(int, input().split())
arr = [0]*(n+m+1)

for i in range(1, n+1):
    for j in range(1, m+1):
        arr[i+j] += 1

for i, x in enumerate(arr):
    if x == max(arr):
        print(i, end=' ')

