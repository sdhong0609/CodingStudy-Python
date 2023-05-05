""" P.316 무지의 먹방 라이브 정답 """
""" P.316 무지의 먹방 라이브 그림.png 참고"""

from operator import itemgetter


def solution(food_times, k):
    foods = []  # 음식을 먹는 시간과 음식 번호를 함께 저장하고 정렬하기 위해 리스트 정의
    n = len(food_times)  # 음식의 개수
    for i in range(n):
        foods.append((food_times[i], i + 1))  # (음식을 먹는 시간, 음식 번호)

    foods.sort()  # 튜플을 sort할 때는 첫번째 값을 기준으로 정렬하기 때문에 음식을 먹는 시간을 기준으로 오름차순 정렬

    pretime = 0  # 이전 음식을 먹는데 필요한 시간
    for i, food in enumerate(foods):
        diff = food[0] - pretime  # diff는 그림의 그래프에서 세로 길이
        if diff != 0:
            spend = diff * n  # 이번 사이클에서 음식을 먹는데 필요한 시간
            if spend <= k:
                k -= spend
                pretime = food[0]
            else:
                k %= n
                sublist = sorted(foods[i:], key=itemgetter(1))
                return sublist[k][1]
        n -= 1  # 한 사이클에서 하나의 음식을 모두 먹은 것으로 생각하기 때문에 음식 총 개수에서 1을 빼준다

    return -1


print(solution([3, 5, 1, 6, 5, 3], 20))
