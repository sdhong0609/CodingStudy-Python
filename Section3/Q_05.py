# 수들의 합

# 내 풀이
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# cnt = 0
#
# for i in range(0, n):
#     if a[i] == m:
#         cnt += 1
#     for j in range(i+1, n):
#         sum = 0
#         for k in range(i, j+1):
#             sum += a[k]
#         if sum == m:
#             cnt += 1
#             break
#
# print(cnt)


# 강사 풀이
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0
while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)
