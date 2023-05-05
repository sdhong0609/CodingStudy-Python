""" P.316 무지의 먹방 라이브 """

""" 내 풀이 (오답) """

# def solution(food_times, k):
#     answer = 0
#     time = 0
#     while time != k:
#         if food_times[answer] > 0:
#             food_times[answer] -= 1
#             time += 1
#             answer += 1
#             if answer == len(food_times):
#                 answer = 0
#         else:
#             answer += 1
#
#         if food_times.count(0) == len(food_times):
#             answer = -1
#             break
#
#     if answer != -1:
#         answer += 1
#     return answer


""" 내 풀이 2 """

from operator import itemgetter


def solution(food_times, k):
    foods = []
    n = len(food_times)
    for i in range(n):
        foods.append((food_times[i], i + 1))
    foods.sort()

    pretime = 0
    for i, food in enumerate(foods):
        diff = food[0] - pretime
        if diff != 0:
            spend = diff * n
            if k >= spend:
                k -= spend
                pretime = food[0]
            else:
                k %= n
                sublist = sorted(foods[i:], key=itemgetter(1))
                return sublist[k][1]
        n -= 1

    return -1


print(solution([3, 5, 1, 6, 5, 3], 20))
