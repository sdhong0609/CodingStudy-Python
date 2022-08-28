# 주사위 게임

# 내 풀이
# n = int(input())
# max = 0
# for i in range(n):
#     a, b, c = map(int, input().split())
#     if a == b == c:
#         res = 10000 + a*1000
#         if max < res:
#             max = res
#     elif a == b or a == c:
#         res = 1000 + a*100
#     elif b == c:
#         res = 1000 + b*100
#     else:
#         if a > b and a > c:
#             res = a*100
#         elif b > c and b > a:
#             res = b*100
#         else:
#             res = c*100
#     if max < res:
#         max = res
#
# print(max)


# 강사 풀이
n = int(input())
res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a == b and b == c:
        money = 10000 + a * 1000
    elif a == b or a == c:
        money = 1000 + a * 100
    elif b == c:
        money = 1000 + b * 100
    else:
        money = c * 100
    if money > res:
        res = money
print(res)
