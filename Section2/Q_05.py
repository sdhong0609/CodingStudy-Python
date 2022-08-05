# 정다면체

# 내 풀이
# n, m = map(int, input().split())
# arr = []
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         arr.append(i + j)
#
# cnt = 0
# answer = [0]
# for i in range(2, n + m + 1):
#     if cnt < arr.count(i):
#         cnt = arr.count(i)
#         answer[0] = i
#     elif cnt == arr.count(i):
#         answer.append(i)
#
# print(*answer)


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
