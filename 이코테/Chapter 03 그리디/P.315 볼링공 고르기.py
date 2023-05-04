""" P.315 볼링공 고르기 """

""" 내 풀이 """

# n, m = map(int, input().split())
# balls = list(map(int, input().split()))
# count = 0
#
# for i in range(n):
#     for j in range(i + 1, n):
#         if balls[i] != balls[j]:
#             count += 1
#
# print(count)

""" 내 풀이 2 """
n, m = map(int, input().split())
balls = list(map(int, input().split()))
balls.sort()
array = [0] * 11

for x in balls:
    array[x] += 1

count = 0
for i in range(1, m+1):
    n -= array[i]
    count += array[i] * n

print(count)


# 입력 1
# 5 3
# 1 3 2 3 2
# 출력 1
# 8

# 입력 2
# 8 5
# 1 5 4 3 2 4 5 2
# 출력 2
# 25
