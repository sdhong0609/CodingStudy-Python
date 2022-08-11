# 주사위 게임

# 내 풀이
# n = int(input())
# prize_max = 0
#
# for i in range(n):
#     a, b, c = map(int, input().split())
#
#     if a == b == c:
#         prize = 10000 + a * 1000
#     elif a == b or b == c or c == a:
#         if a == b:
#             prize = 1000 + a * 100
#         elif b == c:
#             prize = 1000 + b * 100
#         else:
#             prize = 1000 + c * 100
#     else:
#         if a > b and a > c:
#             prize = a * 100
#         elif b > a and b > c:
#             prize = b * 100
#         else:
#             prize = c * 100
#
#     if prize_max < prize:
#         prize_max = prize
#
# print(prize_max)


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
