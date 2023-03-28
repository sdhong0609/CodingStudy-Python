""" P.97 숫자 카드 게임 """

""" 내 풀이 """
# n, m = map(int, input().split())
# cards = [list(map(int, input().split())) for _ in range(n)]
#
# max = 0
# for array in cards:
#     if min(array) > max:
#         max = min(array)
# print(max)


""" 내 풀이 2 """

n, m = map(int, input().split())
min_list = []
for _ in range(n):
    array = list(map(int, input().split()))
    min_list.append(min(array))

print(max(min_list))
