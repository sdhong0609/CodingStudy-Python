# K번째 약수

# 내 풀이
n, k = map(int, input().split())
cnt = 0
res = 0
for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
        if cnt == k:
            res = i
            break
if cnt < k:
    res = -1
print(res)


# 강사 풀이
n, k = map(int, input().split())
cnt = 0
for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)

