# 정다면체

# 내 풀이
n, m = map(int, input().split())
arr = [0]*(n+m+1)

for i in range(1, n+1):
    for j in range(1, m+1):
        arr[i+j] += 1

for i, x in enumerate(arr):
    if x == max(arr):
        print(i, end=' ')


# 강사 풀이
n, m = map(int, input().split())
cnt = [0] * (n + m + 3)
max = -2147000000
for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i + j] += 1

for i in range(n + m + 1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(n + m + 1):
    if cnt[i] == max:
        print(i, end=' ')
