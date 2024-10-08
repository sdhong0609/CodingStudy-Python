""" P.93 큰 수의 법칙 정답"""

""" 풀이 1 """
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
#
# data.sort()
# first = data[n - 1]  # 가장 큰 수
# second = data[n - 2]  # 두 번째로 큰 수
#
# result = 0
#
# while True:
#     for i in range(k):
#         if m == 0:  # m이 0이라면 반복문 탈출
#             break
#         result += first
#         m -= 1  # 더할 때마다 1씩 빼기
#     if m == 0:  # m이 0이라면 반복문 탈출
#         break
#     result += second  # 두 번째로 큰 수를 한 번 더하기
#     m -= 1  # 더할 때마다 1씩 빼기
#
# print(result)  # 최종 답안 출력


""" 풀이 2 """  # 반복되는 수열을 이용
# n: 배열의 크기, m: 숫자가 더해지는 횟수, k: 연속해서 k번을 초과하여 더해질 수 없음
n, m, k = map(int, input().split())
array = list(map(int, input().split()))
array.sort(reverse=True)

first = array[0]
second = array[1]

# 가장 큰 수가 더해지는 "횟수" 계산
# (k+1): 반복되는 수열의 길이
# (m // (k+1)): 수열이 반복되는 횟수
# (m // (k+1)) * k: 가장 큰 수가 더해지는 "횟수"
count = (m // (k + 1)) * k

# m이 (k+1)로 나누어 떨어지지 않는 경우도 추가로 더해준다
count += m % (k + 1)

result = 0
result += count * first  # 가장 큰 수 더하기
result += (m-count) * second  # 두 번째로 큰 수 더하기

print(result)
