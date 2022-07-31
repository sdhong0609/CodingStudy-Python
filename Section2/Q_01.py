# K번째 약수

# 내 풀이
a, b = map(int, input().split())
count = 0
for i in range(1, a + 1):
    if a % i == 0:
        count = count + 1
    if count == b:
        print(i)
        break

if count < b:
    print(-1)


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

