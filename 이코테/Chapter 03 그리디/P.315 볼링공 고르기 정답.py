""" P.315 볼링공 고르기 정답 """

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i]  # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n  # B가 선택하는 경우의 수와 곱하기

print(result)

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
