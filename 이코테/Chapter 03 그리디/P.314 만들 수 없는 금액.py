""" P.314 만들 수 없는 금액 """

""" 내 풀이 """

n = int(input())
data = list(map(int, input().split()))
data.sort()  # 오름차순으로 정렬

target = 1
for x in data:
    if target < x:
        break
    else:
        target += x

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
