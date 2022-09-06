# 사과나무(다이아몬드)

# 내 풀이
# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# sum = 0
# for i in range(n):
#     r1 = abs(n//2 - i)
#     r2 = n - r1
#     for j in range(r1, r2):
#         sum += a[i][j]
#
# print(sum)


# 강사 풀이
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
s = e = n//2
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)