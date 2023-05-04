""" P.314 만들 수 없는 금액 정답 """

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)

# 입력 1
# 5
# 3 2 1 1 9
# 출력 1
# 8

# 입력 2
# 3
# 3 5 7
# 출력 2
# 1
