""" 알고리즘 노트 """

""" N x M 크기의 2차원 리스트 초기화 """
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)


""" 2차원 리스트 입력 받은 대로 초기화"""
n = int(input())  # 반복 횟수
a = [list(map(int, input().split())) for _ in range(n)]
print(a)


""" 입력 받은 문자열을 정수로 이루어진 리스트로 바꾸는 방법 """
a = list(map(int, input()))
print(a)

# 사용 예시
# 입력 : 12345
# 출력 : [1, 2, 3, 4, 5]


""" 거스름돈을 최소 동전 개수로 거슬러 주는 알고리즘 """
coin_types = [500, 100, 50, 10]
n = 1260  # 거슬러 주어야 할 돈
count = 0

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)


"""
n번째 피보나치 수를 쉽게 구하는 알고리즘 (시간복잡도와 공간복잡도가 대폭 낮아짐)
(재귀호출로 피보나치 수를 구현했을 떄 fib(1)과 fib(2)가 호출되는 총 횟수와 같다)
"""
def fib(n):
    arr = [1, 1]
    for i in range(2, n):
        arr.append(arr[-1] + arr[-2])
    return arr[-1]


n = 6  # 6번째 피보나치 수를 구하기 위해 n을 6으로 초기화
print(fib(n))


"""
리스트 내에서 특정 요소의 개수를 세는 방법
"""
s = ['0', '0', '1', '1', '0', '1']
print(s.count('0'))
# s.count(요소, start, end) : start와 end index값을 넣지 않으면 리스트 전체 탐색

# 출력 : 3
