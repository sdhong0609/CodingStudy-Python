# 소수(에라토스테네스 체)

# 내 풀이
# n = int(input())
# answer = 0
#
# for i in range(2, n):
#     isPrime = True
#     for j in range(2, i):
#         if i % j == 0:
#             isPrime = False
#             break
#     if isPrime:
#         answer += 1
#
# print(answer)

# 강사 풀이
n = int(input())
ch = [0] * (n + 1)
cnt = 0
for i in range(2, n + 1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n + 1, i):
            ch[j] = 1
print(cnt)
