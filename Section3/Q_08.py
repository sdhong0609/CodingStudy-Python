# 곳감(모래시계)

# 내 풀이
# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# m = int(input())
#
# x, y, z = map(int, input().split())
# for i in range(n):
#     if y == 0:
#         j = i-z+n
#         if j == n:
#             j = 0
#         a[x-1][i] = a[x-1][j]
#         j += 1
#     else:
#         j = i+z
#         if j == n:
#             j = 0
#         a[x-1][i] = a[x-1][j]


# 강사 풀이
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

res = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)
